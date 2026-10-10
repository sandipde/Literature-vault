import json
import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import requests
import yaml

from scripts import ingest, literature, scan_profiles


class LiteratureTests(unittest.TestCase):
    def test_url_extraction_and_canonical_aliases(self):
        self.assertEqual(
            literature.extract_url("Reference: https://arxiv.org/pdf/2610.04224v2)."),
            "https://arxiv.org/pdf/2610.04224v2",
        )
        self.assertEqual(
            literature.extract_url("10.5555/example.123"),
            "https://doi.org/10.5555/example.123",
        )
        self.assertEqual(
            literature.canonicalize_url("https://arxiv.org/pdf/2610.04224v2")[1],
            literature.canonicalize_url("https://arxiv.org/abs/2610.04224")[1],
        )
        self.assertEqual(
            literature.canonicalize_url("https://dx.doi.org/10.5555/EXAMPLE.123")[1],
            literature.canonicalize_url("https://doi.org/10.5555/example.123")[1],
        )

    def test_repository_types_and_distinct_repositories(self):
        self.assertEqual(literature.classify_url("https://github.com/Org/Repo/tree/main"), "github")
        self.assertEqual(literature.canonicalize_url("https://github.com/Org/Repo/tree/main")[1], "https://github.com/org/repo")
        self.assertNotEqual(
            literature.canonicalize_url("https://github.com/org/repo")[1],
            literature.canonicalize_url("https://github.com/org/other")[1],
        )
        self.assertEqual(literature.classify_url("https://huggingface.co/datasets/org/data"), "huggingface_dataset")
        self.assertEqual(literature.classify_url("https://huggingface.co/spaces/org/app"), "huggingface_space")
        self.assertEqual(literature.classify_url("https://huggingface.co/org/model"), "huggingface_model")
        self.assertEqual(literature.classify_url("https://gitlab.com/group/subgroup/project"), "gitlab")
        self.assertEqual(literature.classify_url("https://chemrxiv.org/engage/chemrxiv/article-details/abc"), "chemrxiv")

    def test_crossref_metadata_parser(self):
        with patch.object(literature, "_request_json", return_value={"message": {
            "title": ["A sample paper"],
            "author": [{"given": "Ada", "family": "Lovelace"}],
            "published-print": {"date-parts": [[2025, 3, 8]]},
            "abstract": "<jats:p>Useful open abstract.</jats:p>",
            "DOI": "10.5555/example.123",
            "container-title": ["Journal of Tests"],
            "subject": ["materials science"],
        }}):
            parsed = literature._crossref("10.5555/example.123")
        self.assertEqual(parsed["title"], "A sample paper")
        self.assertEqual(parsed["authors"], ["Ada Lovelace"])
        self.assertEqual(parsed["published"], "2025-03-08")
        self.assertEqual(parsed["abstract"], "Useful open abstract.")
        self.assertEqual(parsed["provider_data"]["journal"], "Journal of Tests")

    def test_openalex_metadata_parser_for_chemrxiv(self):
        work = {
            "title": "A ChemRxiv preprint",
            "publication_date": "2026-05-12",
            "authorships": [{"author": {"display_name": "Ada Lovelace"}}],
            "abstract_inverted_index": {"Open": [0], "metadata.": [1], "Structured": [2]},
            "primary_location": {"source": None},
            "topics": [{"display_name": "Chemistry"}],
            "open_access": {"is_oa": True},
            "cited_by_count": 0,
            "type": "preprint",
        }
        with patch.object(literature, "_request_json", return_value={"results": [work]}):
            parsed = literature._openalex("https://chemrxiv.org/engage/chemrxiv/article-details/abc")
        self.assertEqual(parsed["title"], "A ChemRxiv preprint")
        self.assertEqual(parsed["abstract"], "Open metadata. Structured")
        self.assertEqual(parsed["provider_data"]["topics"], ["Chemistry"])

    def test_repository_metadata_parsers(self):
        github = {
            "full_name": "org/repo", "description": "A useful project", "language": "Python",
            "topics": ["science"], "license": {"spdx_id": "MIT"}, "stargazers_count": 42,
            "forks_count": 3, "open_issues_count": 2, "created_at": "2024-01-01", "pushed_at": "2026-01-01",
            "default_branch": "main",
        }
        huggingface = {
            "id": "org/model", "cardData": {"description": "A model card", "license": "apache-2.0"},
            "pipeline_tag": "text-generation", "tags": ["research"], "downloads": 100, "likes": 8,
            "siblings": [{"rfilename": "README.md"}],
        }
        gitlab = {
            "path_with_namespace": "group/project", "description": "A project", "topics": ["tools"],
            "license": {"key": "mit"}, "star_count": 9, "forks_count": 1, "visibility": "public",
            "created_at": "2024-01-01", "last_activity_at": "2026-01-01", "default_branch": "main",
        }
        with patch.object(literature, "_request_json", side_effect=[github, huggingface, gitlab]):
            github_data = literature._fetch_github("https://github.com/org/repo")
            hf_data = literature._fetch_huggingface("huggingface_model", "https://huggingface.co/org/model")
            gitlab_data = literature._fetch_gitlab("https://gitlab.com/group/project")
        self.assertEqual(github_data["provider_data"]["stars"], 42)
        self.assertEqual(github_data["provider_data"]["license"], "MIT")
        self.assertEqual(hf_data["provider_data"]["task"], "text-generation")
        self.assertEqual(hf_data["provider_data"]["downloads"], 100)
        self.assertEqual(gitlab_data["provider_data"]["visibility"], "public")
        self.assertEqual(gitlab_data["provider_data"]["topics"], ["tools"])

    def test_arxiv_parser_keeps_primary_category(self):
        content = '''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry><id>https://arxiv.org/abs/2610.04224</id><title>Paper</title>
            <summary>Summary.</summary><author><name>Ada</name></author>
            <published>2026-10-10T00:00:00Z</published>
            <arxiv:primary_category term="cs.LG" />
          </entry></feed>'''
        with patch.object(literature, "_request_text", return_value=content):
            parsed = literature._fetch_arxiv("https://arxiv.org/abs/2610.04224")
        self.assertEqual(parsed["provider_data"]["primary_category"], "cs.LG")

    def test_resolver_preserves_source_when_provider_is_unavailable(self):
        with patch.object(literature, "_fetch_github", side_effect=requests.Timeout("offline")):
            result = literature.resolve_metadata("https://github.com/org/repo", "Fallback title")
        self.assertEqual(result["title"], "Fallback title")
        self.assertEqual(result["metadata_status"], "unavailable")
        self.assertEqual(result["canonical_url"], "https://github.com/org/repo")

    def test_registry_bootstraps_and_groups_legacy_duplicates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes = Path(temp_dir) / "notes"
            notes.mkdir()
            for filename in ("3_old.md", "4_duplicate.md"):
                (notes / filename).write_text(
                    '---\ntitle: Legacy\nsource: "https://arxiv.org/pdf/2610.04224v1"\n---\n',
                    encoding="utf-8",
                )
            registry = literature.load_registry(Path(temp_dir) / "sources.json", notes)
        record = registry["sources"]["https://arxiv.org/abs/2610.04224"]
        self.assertEqual(set(record["notes"]), {"notes/3_old.md", "notes/4_duplicate.md"})


class IngestTests(unittest.TestCase):
    def metadata(self):
        return {
            "type": "arxiv",
            "canonical_url": "https://arxiv.org/abs/2610.04224",
            "title": "A sample paper",
            "authors": ["Ada Lovelace"],
            "published": "2026-10-10",
            "abstract": "A useful abstract.",
            "metadata_provider": "arXiv",
            "metadata_status": "complete",
            "provider_data": {"categories": ["cs.LG"]},
        }

    def test_issue_ingest_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            notes = Path(temp_dir) / "notes"
            registry_path = Path(temp_dir) / "sources.json"
            env = {
                "ISSUE_NUM": "12",
                "USER_LOGIN": "reader",
                "ISSUE_TITLE": "Captured title",
                "ISSUE_BODY": "https://arxiv.org/pdf/2610.04224v3",
            }
            with patch.object(ingest, "NOTES_DIR", notes), patch.object(ingest, "REGISTRY_FILE", registry_path), patch.object(
                ingest, "resolve_metadata", return_value=self.metadata()
            ), patch.dict(os.environ, env, clear=True):
                first = ingest.main()
                os.environ["ISSUE_NUM"] = "13"
                os.environ["ISSUE_BODY"] = "https://arxiv.org/abs/2610.04224"
                second = ingest.main()

            self.assertEqual(first["result"], "created")
            self.assertEqual(second["result"], "duplicate")
            self.assertEqual(len(list(notes.glob("*.md"))), 1)
            note_text = Path(first["note_path"]).read_text(encoding="utf-8")
            note_end = note_text.find("\n---", 4)
            note = yaml.safe_load(note_text[4:note_end])
            self.assertEqual(note["type"], "arxiv")
            self.assertEqual(note["provider_data"]["categories"], ["cs.LG"])


class ScannerTests(unittest.TestCase):
    def test_scanner_does_not_duplicate_second_pass(self):
        profile = {"id": "test-arxiv", "name": "Test arXiv", "provider": "arxiv", "enabled": True,
                   "queries": ["cat:cs.LG"], "max_results": 10, "interval": "daily"}
        metadata = {"type": "arxiv", "canonical_url": "https://arxiv.org/abs/2610.04224",
                    "title": "A sample paper", "authors": ["Ada Lovelace"], "published": "2026-10-10",
                    "abstract": "A sample abstract.", "metadata_provider": "arXiv", "metadata_status": "complete",
                    "provider_data": {"arxiv_id": "2610.04224", "categories": ["cs.LG"]},
                    "source_url": "https://arxiv.org/abs/2610.04224"}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config_file = root / "monitor_config.json"
            config_file.write_text(json.dumps({"version": 1, "profiles": [profile]}), encoding="utf-8")
            notes = root / "notes"
            with patch.object(scan_profiles, "search_profile", return_value=[metadata]) as search:
                first = scan_profiles.run_scan(config_file, root / "seen_papers.json", root / "sources.json", notes,
                                               root / "scan_state.json", datetime(2026, 10, 10, tzinfo=timezone.utc))
                second = scan_profiles.run_scan(config_file, root / "seen_papers.json", root / "sources.json", notes,
                                                root / "scan_state.json", datetime(2026, 10, 10, 1, tzinfo=timezone.utc))
            self.assertEqual(len(list(notes.glob("*.md"))), 1)
            self.assertEqual(len(first["added_notes"]), 1)
            self.assertEqual(second["added_notes"], [])
            self.assertEqual(search.call_count, 1)
            self.assertEqual(json.loads((root / "seen_papers.json").read_text(encoding="utf-8")), ["2610.04224"])
            history = json.loads((root / "scan_history.json").read_text(encoding="utf-8"))
            self.assertEqual(history["runs"][0]["profiles"][0]["status"], "success")
            self.assertEqual(history["runs"][0]["notes_added"], 1)

    def test_disabled_and_not_due_profiles_are_not_searched(self):
        profiles = [
            {"id": "disabled", "name": "Disabled", "provider": "arxiv", "enabled": False,
             "queries": ["query"], "max_results": 10, "interval": "daily"},
            {"id": "weekly", "name": "Weekly", "provider": "arxiv", "enabled": True,
             "queries": ["query"], "max_results": 10, "interval": "weekly"},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config = root / "monitor_config.json"
            config.write_text(json.dumps({"version": 1, "profiles": profiles}), encoding="utf-8")
            state = root / "scan_state.json"
            state.write_text(json.dumps({"version": 1, "profiles": {"weekly": "2026-10-07T05:00:00+00:00"}}), encoding="utf-8")
            with patch.object(scan_profiles, "search_profile") as search:
                result = scan_profiles.run_scan(config, root / "seen.json", root / "sources.json", root / "notes",
                                                state, datetime(2026, 10, 10, 5, tzinfo=timezone.utc))
            search.assert_not_called()
            self.assertEqual(result["completed"], [])

    def test_failed_profile_does_not_advance_state(self):
        profile = {"id": "retry-me", "name": "Retry", "provider": "arxiv", "enabled": True,
                   "queries": ["query"], "max_results": 10, "interval": "daily"}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config = root / "monitor_config.json"
            config.write_text(json.dumps({"version": 1, "profiles": [profile]}), encoding="utf-8")
            state = root / "scan_state.json"
            with patch.object(scan_profiles, "search_profile", side_effect=requests.Timeout("offline")):
                result = scan_profiles.run_scan(config, root / "seen.json", root / "sources.json", root / "notes",
                                                state, datetime(2026, 10, 10, 5, tzinfo=timezone.utc))
            self.assertIn("retry-me", result["failed"])
            self.assertNotIn("retry-me", result["state"]["profiles"])

    def test_profile_name_filter_runs_only_the_requested_group(self):
        profiles = [
            {"id": "mlip-arxiv", "name": "MLIP developments scan", "provider": "arxiv", "enabled": True,
             "queries": ["query"], "max_results": 10, "interval": "twice_daily"},
            {"id": "other", "name": "Other scan", "provider": "crossref", "enabled": True,
             "queries": ["query"], "max_results": 10, "interval": "daily"},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config = root / "monitor_config.json"
            config.write_text(json.dumps({"version": 1, "profiles": profiles}), encoding="utf-8")
            with patch.object(scan_profiles, "search_profile", return_value=[]) as search:
                result = scan_profiles.run_scan(config, root / "seen.json", root / "sources.json", root / "notes",
                                                root / "state.json", profile_names=["MLIP developments scan"])
            self.assertEqual(search.call_count, 1)
            self.assertEqual(result["completed"], ["mlip-arxiv"])
            self.assertNotIn("other", result["state"]["profiles"])

    def test_duplicate_source_across_profiles_creates_one_note(self):
        profiles = [
            {"id": f"profile-{index}", "name": f"Profile {index}", "provider": "arxiv", "enabled": True,
             "queries": [f"query {index}"], "max_results": 10, "interval": "daily"}
            for index in (1, 2)
        ]
        metadata = {"type": "arxiv", "canonical_url": "https://arxiv.org/abs/2610.04224",
                    "title": "A sample paper", "authors": [], "published": "", "abstract": "Summary",
                    "metadata_provider": "arXiv", "metadata_status": "complete",
                    "provider_data": {"arxiv_id": "2610.04224"}, "source_url": "https://arxiv.org/abs/2610.04224"}
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config_file = root / "monitor_config.json"
            config_file.write_text(json.dumps({"version": 1, "profiles": profiles}), encoding="utf-8")
            with patch.object(scan_profiles, "search_profile", return_value=[metadata]):
                result = scan_profiles.run_scan(config_file, root / "seen.json", root / "sources.json",
                                                root / "notes", root / "state.json")
            self.assertEqual(len(result["added_notes"]), 1)
            self.assertEqual(result["completed"], ["profile-1", "profile-2"])


if __name__ == "__main__":
    unittest.main()
