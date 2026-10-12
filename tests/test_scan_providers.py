import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, call, patch

import requests

from scripts import scan_providers as providers
from scripts.scan_providers import search_profile

NOW = datetime(2026, 10, 10, 12, tzinfo=timezone.utc)


class ScanProviderTests(unittest.TestCase):
    def test_arxiv_search_normalizes_atom_results(self):
        feed = '''<feed xmlns="http://www.w3.org/2005/Atom">
          <entry><id>https://arxiv.org/abs/2610.04224v2</id><title>MLIP paper</title>
            <summary>Useful atomistic abstract.</summary><published>2026-10-10T11:00:00Z</published>
            <author><name>Ada Lovelace</name></author><category term="cond-mat.mtrl-sci" />
          </entry></feed>'''
        profile = {"provider": "arxiv", "queries": ["all:MLIP"], "max_results": 5}
        with patch("scripts.scan_providers._get_text", return_value=feed) as request:
            results = search_profile(profile, now=NOW)
        self.assertIn("submittedDate:[202610091200 TO 202610101200]", request.call_args.args[1]["search_query"])
        self.assertEqual(results[0]["canonical_url"], "https://arxiv.org/abs/2610.04224")
        self.assertEqual(results[0]["authors"], ["Ada Lovelace"])
        self.assertEqual(results[0]["provider_data"]["categories"], ["cond-mat.mtrl-sci"])

    def test_crossref_and_chemrxiv_queries_normalize_doi_records(self):
        payload = {"message": {"items": [{
            "DOI": "10.26434/chemrxiv-2026-test",
            "URL": "https://doi.org/10.26434/chemrxiv-2026-test",
            "title": ["Catalysis preprint"],
            "abstract": "<jats:p>Open preprint abstract.</jats:p>",
            "author": [{"given": "Ada", "family": "Lovelace"}],
            "published": {"date-parts": [[2026, 10, 1]]},
            "publisher": "ChemRxiv",
            "subject": ["Catalysis"],
            "created": {"date-time": "2026-10-10T11:30:00Z"},
        }]}}
        profile = {"provider": "crossref", "queries": ["heterogeneous catalysis"], "max_results": 3}
        with patch("scripts.scan_providers._get_json", return_value=payload) as request:
            results = search_profile(profile, now=NOW)
        self.assertEqual(request.call_args.args[0], "https://api.crossref.org/works")
        self.assertEqual(request.call_args.args[1]["filter"], "from-created-date:2026-10-09")
        self.assertEqual(results[0]["type"], "chemrxiv")
        self.assertEqual(results[0]["abstract"], "Open preprint abstract.")
        self.assertEqual(results[0]["authors"], ["Ada Lovelace"])

    def test_repository_and_huggingface_adapters(self):
        github = {"items": [{"html_url": "https://github.com/org/model", "full_name": "org/model",
                             "description": "Atomistic model", "topics": ["materials"], "stargazers_count": 12,
                             "pushed_at": "2026-10-10T11:30:00Z"}]}
        gitlab = [{"web_url": "https://gitlab.com/group/simulator", "path_with_namespace": "group/simulator",
                   "description": "Simulator", "topics": ["materials"], "star_count": 4,
                   "last_activity_at": "2026-10-10T11:30:00Z"}]
        hf = [{"id": "org/material-model", "cardData": {"description": "Model card", "license": "mit"},
               "pipeline_tag": "feature-extraction", "tags": ["materials"], "downloads": 42, "likes": 3,
               "lastModified": "2026-10-10T11:30:00Z"}]
        with patch("scripts.scan_providers._get_json", side_effect=[github, gitlab, hf]) as request:
            github_results = search_profile({"provider": "github", "queries": ["atomistic model"], "max_results": 5}, now=NOW)
            gitlab_results = search_profile({"provider": "gitlab", "queries": ["simulator"], "max_results": 5}, now=NOW)
            hf_results = search_profile({"provider": "huggingface_model", "queries": ["materials"], "max_results": 5}, now=NOW)
        self.assertEqual(github_results[0]["provider_data"]["stars"], 12)
        self.assertEqual(gitlab_results[0]["provider_data"]["topics"], ["materials"])
        self.assertEqual(hf_results[0]["provider_data"]["downloads"], 42)
        self.assertIn("pushed:>=2026-10-09T12:00:00Z", request.call_args_list[0].args[1]["q"])
        self.assertEqual(request.call_args_list[1].args[1]["last_activity_after"], "2026-10-09T12:00:00Z")
        self.assertEqual(request.call_args_list[2].args[1]["sort"], "lastModified")

    def test_huggingface_dataset_and_space_adapters(self):
        dataset = [{"id": "org/material-data", "cardData": {"description": "Dataset card", "license": "cc-by-4.0"},
                                        "tags": ["materials"], "downloads": 18, "lastModified": "2026-10-10T11:30:00Z"}]
        space = [{"id": "org/material-demo", "cardData": {"description": "Demo", "license": "mit"},
                                    "sdk": "gradio", "tags": ["materials"], "likes": 5, "lastModified": "2026-10-10T11:30:00Z"}]
        with patch("scripts.scan_providers._get_json", side_effect=[dataset, space]) as request:
                        dataset_results = search_profile({"provider": "huggingface_dataset", "queries": ["materials"], "max_results": 5}, now=NOW)
                        space_results = search_profile({"provider": "huggingface_space", "queries": ["materials"], "max_results": 5}, now=NOW)
        self.assertEqual(request.call_args_list[0].args[0], "https://huggingface.co/api/datasets")
        self.assertEqual(request.call_args_list[1].args[0], "https://huggingface.co/api/spaces")
        self.assertEqual(request.call_args_list[0].args[1]["sort"], "lastModified")
        self.assertEqual(dataset_results[0]["type"], "huggingface_dataset")
        self.assertEqual(space_results[0]["type"], "huggingface_space")

    def test_result_cap_and_query_overlap_are_applied(self):
        item = {"html_url": "https://github.com/org/repo", "full_name": "org/repo", "description": "Project",
                "pushed_at": "2026-10-10T11:30:00Z"}
        profile = {"provider": "github", "queries": ["query one", "query two"], "max_results": 1}
        with patch("scripts.scan_providers._get_json", return_value={"items": [item]}) as request:
            results = search_profile(profile, now=NOW)
        self.assertEqual(len(results), 1)
        self.assertEqual(request.call_count, 1)

    def test_result_budget_is_shared_across_queries(self):
        profile = {"provider": "github", "queries": ["one", "two"], "max_results": 4}
        responses = [
            {"items": [{"html_url": f"https://github.com/org/one-{index}", "full_name": f"org/one-{index}", "pushed_at": "2026-10-10T11:30:00Z"} for index in range(3)]},
            {"items": [{"html_url": f"https://github.com/org/two-{index}", "full_name": f"org/two-{index}", "pushed_at": "2026-10-10T11:30:00Z"} for index in range(3)]},
        ]
        with patch("scripts.scan_providers._get_json", side_effect=responses) as request:
            results = search_profile(profile, now=NOW)
        self.assertEqual(request.call_count, 2)
        self.assertEqual(len(results), 4)
        self.assertTrue(any("two-" in item["canonical_url"] for item in results))

    def test_only_results_inside_rolling_window_are_returned(self):
        items = {"items": [
            {"html_url": "https://github.com/org/inside", "full_name": "org/inside", "pushed_at": "2026-10-09T12:00:00Z"},
            {"html_url": "https://github.com/org/old", "full_name": "org/old", "pushed_at": "2026-10-09T11:59:59Z"},
            {"html_url": "https://github.com/org/future", "full_name": "org/future", "pushed_at": "2026-10-10T12:00:01Z"},
        ]}
        profile = {"provider": "github", "queries": ["atomistic"], "max_results": 5, "lookback_hours": 24}
        with patch("scripts.scan_providers._get_json", return_value=items) as request:
            results = search_profile(profile, now=NOW)
        self.assertEqual([item["canonical_url"] for item in results], ["https://github.com/org/inside"])
        self.assertIn("pushed:>=2026-10-09T12:00:00Z", request.call_args.args[1]["q"])


def _response(status=200, headers=None, text="", payload=None):
    response = Mock(status_code=status, headers=headers or {}, text=text)
    response.json.return_value = payload if payload is not None else {}
    response.raise_for_status.side_effect = None if status < 400 else requests.HTTPError(f"{status} error")
    return response


class RequestResilienceTests(unittest.TestCase):
    def setUp(self):
        providers._last_request_at.clear()

    def test_rate_limited_request_is_retried_after_retry_after_delay(self):
        responses = [_response(429, {"Retry-After": "7"}), _response(200, payload={"ok": True})]
        with patch("scripts.scan_providers.requests.get", side_effect=responses) as get, \
                patch("scripts.scan_providers.time.sleep") as sleep:
            result = providers._get_json("https://api.crossref.org/works", {})
        self.assertEqual(result, {"ok": True})
        self.assertEqual(get.call_count, 2)
        self.assertIn(call(7.0), sleep.call_args_list)

    def test_persistent_rate_limit_eventually_raises(self):
        responses = [_response(429, {"Retry-After": "1"}) for _ in range(providers.MAX_ATTEMPTS)]
        with patch("scripts.scan_providers.requests.get", side_effect=responses) as get, \
                patch("scripts.scan_providers.time.sleep"):
            with self.assertRaises(requests.HTTPError):
                providers._get_json("https://api.crossref.org/works", {})
        self.assertEqual(get.call_count, providers.MAX_ATTEMPTS)

    def test_github_quota_403_is_retried_but_plain_403_is_not(self):
        quota = _response(403, {"X-RateLimit-Remaining": "0"})
        with patch("scripts.scan_providers.requests.get", side_effect=[quota, _response(200, payload={})]) as get, \
                patch("scripts.scan_providers.time.sleep"):
            providers._get_json("https://api.github.com/search/repositories", {})
        self.assertEqual(get.call_count, 2)
        with patch("scripts.scan_providers.requests.get", return_value=_response(403)) as get, \
                patch("scripts.scan_providers.time.sleep"):
            with self.assertRaises(requests.HTTPError):
                providers._get_json("https://api.github.com/search/repositories", {})
        self.assertEqual(get.call_count, 1)

    def test_consecutive_arxiv_requests_are_spaced_at_least_three_seconds_apart(self):
        clock = {"now": 100.0}
        slept = []

        def fake_sleep(seconds):
            slept.append(seconds)
            clock["now"] += seconds

        with patch("scripts.scan_providers.requests.get", return_value=_response(200, text="<feed/>")), \
                patch("scripts.scan_providers.time.monotonic", side_effect=lambda: clock["now"]), \
                patch("scripts.scan_providers.time.sleep", side_effect=fake_sleep):
            providers._get_text("https://export.arxiv.org/api/query", {})
            providers._get_text("https://export.arxiv.org/api/query", {})
        self.assertEqual(len(slept), 1)
        self.assertGreaterEqual(slept[0], 3.0)

    def test_github_token_is_sent_only_to_github(self):
        with patch.dict("os.environ", {"GITHUB_TOKEN": "secret-token"}), \
                patch("scripts.scan_providers.requests.get", return_value=_response(200, payload={})) as get, \
                patch("scripts.scan_providers.time.sleep"):
            providers._get_json("https://api.github.com/search/repositories", {})
            providers._get_json("https://gitlab.com/api/v4/projects", {})
        self.assertEqual(get.call_args_list[0].kwargs["headers"]["Authorization"], "Bearer secret-token")
        self.assertNotIn("Authorization", get.call_args_list[1].kwargs["headers"])

    def test_crossref_mailto_is_added_only_when_configured(self):
        profile = {"provider": "crossref", "queries": ["catalysis"], "max_results": 3}
        with patch("scripts.scan_providers._get_json", return_value={"message": {"items": []}}) as request:
            with patch.dict("os.environ", {"CROSSREF_MAILTO": "owner@example.org"}):
                search_profile(profile, now=NOW)
            with patch.dict("os.environ", {}, clear=True):
                search_profile(profile, now=NOW)
        self.assertEqual(request.call_args_list[0].args[1]["mailto"], "owner@example.org")
        self.assertNotIn("mailto", request.call_args_list[1].args[1])

    def test_arxiv_error_entries_are_not_treated_as_papers(self):
        feed = '''<feed xmlns="http://www.w3.org/2005/Atom"><entry>
          <id>http://arxiv.org/api/errors#incorrect_id_format_for_1234</id><title>Error</title>
          <summary>incorrect id format</summary><published>2026-10-10T11:00:00Z</published></entry></feed>'''
        profile = {"provider": "arxiv", "queries": ["all:MLIP"], "max_results": 5}
        with patch("scripts.scan_providers._get_text", return_value=feed):
            self.assertEqual(search_profile(profile, now=NOW), [])


if __name__ == "__main__":
    unittest.main()
