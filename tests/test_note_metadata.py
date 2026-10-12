import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from scripts.update_note_metadata import MARKER, apply_request, main

NOTE = """---
title: Sample paper
type: arxiv
source: https://arxiv.org/abs/2610.00001
status: to-read
abstract: A long abstract that
  continues on a second line.
provider_data:
  categories:
  - cond-mat.mtrl-sci
---

# Sample paper

## Summary
Useful summary.

## Provider details
- arXiv
"""

BASE = {"version": 1, "note": "notes/1_sample.md", "rating": 4, "priority": "high", "status": "reading",
        "tags": ["materials", "ML"], "comments": "Worth a close read."}


def request_body(payload):
    return f"{MARKER}\n\nSubmitted from Literature Vault.\n\n```json\n{json.dumps(payload, indent=2)}\n```\n"


def frontmatter(text):
    return yaml.safe_load(text.split("---\n", 2)[1])


class NoteMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "notes").mkdir()
        self.note = self.root / "notes" / "1_sample.md"
        self.note.write_text(NOTE, encoding="utf-8")

    def apply(self, payload=None, association="OWNER", **overrides):
        body = request_body({**BASE, **overrides} if payload is None else payload)
        return apply_request(body, association, self.root)

    def test_unauthorized_author_cannot_modify_a_note(self):
        for association in ("NONE", "CONTRIBUTOR", "FIRST_TIME_CONTRIBUTOR", ""):
            result = self.apply(association=association)
            self.assertEqual(result["result"], "rejected")
        self.assertEqual(self.note.read_text(encoding="utf-8"), NOTE)

    def test_collaborators_and_members_are_allowed(self):
        for association in ("OWNER", "MEMBER", "COLLABORATOR"):
            self.note.write_text(NOTE, encoding="utf-8")
            self.assertEqual(self.apply(association=association)["result"], "applied")

    def test_metadata_is_written_and_existing_frontmatter_is_preserved(self):
        result = self.apply()
        self.assertEqual(result["result"], "applied")
        self.assertEqual(result["note_path"], "notes/1_sample.md")
        updated = self.note.read_text(encoding="utf-8")
        data = frontmatter(updated)
        self.assertEqual(data["user_rating"], 4)
        self.assertEqual(data["user_priority"], "high")
        self.assertEqual(data["user_status"], "reading")
        self.assertEqual(data["user_tags"], ["materials", "ML"])
        self.assertEqual(data["user_comments"], "Worth a close read.")
        original = frontmatter(NOTE)
        self.assertEqual({key: data[key] for key in original}, original)
        self.assertIn("## Personal notes", updated)
        self.assertIn("- **Rating:** 4/5", updated)
        self.assertIn("## Summary\nUseful summary.", updated)

    def test_reapplying_replaces_the_personal_section_and_fields(self):
        self.apply()
        self.note.write_text(self.note.read_text(encoding="utf-8") + "\n## Later section\nKeep me.\n", encoding="utf-8")
        result = self.apply(rating=0, priority="low", status="read", tags=[], comments="")
        self.assertEqual(result["result"], "applied")
        updated = self.note.read_text(encoding="utf-8")
        self.assertEqual(updated.count("## Personal notes"), 1)
        self.assertEqual(updated.count("user_rating"), 1)
        self.assertIn("- **Rating:** Not rated", updated)
        self.assertIn("## Later section\nKeep me.", updated)
        data = frontmatter(updated)
        self.assertEqual((data["user_rating"], data["user_tags"], data["user_comments"]), (0, [], ""))

    def test_identical_request_reports_unchanged(self):
        self.apply()
        before = self.note.read_text(encoding="utf-8")
        self.assertEqual(self.apply()["result"], "unchanged")
        self.assertEqual(self.note.read_text(encoding="utf-8"), before)

    def test_yaml_special_characters_round_trip(self):
        comments = 'Line one: "quoted" \\ backslash\n\n  # not a comment\n- not a list\nEmoji \U0001F600 and   separator'
        tags = ["a: b", "#hash", "[bracket]", "- dash", "with 'quote'", "naïve"]
        result = self.apply(tags=tags, comments=comments)
        self.assertEqual(result["result"], "applied")
        data = frontmatter(self.note.read_text(encoding="utf-8"))
        self.assertEqual(data["user_tags"], tags)
        self.assertEqual(data["user_comments"], comments.strip())

    def test_tags_are_trimmed_and_deduplicated(self):
        self.apply(tags=["  ML ", "ML", "", "materials"])
        self.assertEqual(frontmatter(self.note.read_text(encoding="utf-8"))["user_tags"], ["ML", "materials"])

    def test_unsafe_note_paths_are_rejected(self):
        outside = self.root / "secret.md"
        outside.write_text(NOTE, encoding="utf-8")
        (self.root / "notes" / "link.md").symlink_to(outside)
        for path in ("../secret.md", "notes/../secret.md", "/etc/passwd", "secret.md", "notes/sub/1_sample.md",
                     "notes/1_sample.txt", "notes/.hidden.md", "notes/missing.md", "notes/link.md", "", None, 7):
            self.assertEqual(self.apply(note=path)["result"], "rejected", path)
        self.assertEqual(outside.read_text(encoding="utf-8"), NOTE)

    def test_invalid_values_are_rejected_without_changing_the_note(self):
        invalid = [
            {"rating": 6}, {"rating": -1}, {"rating": "4"}, {"rating": True}, {"rating": 3.5},
            {"priority": "critical"}, {"status": "done"},
            {"tags": "materials"}, {"tags": [1]}, {"tags": ["x" * 41]}, {"tags": [f"t{i}" for i in range(21)]},
            {"tags": ["bad\nnewline"]}, {"tags": ["bad\x00nul"]},
            {"comments": 5}, {"comments": "x" * 5001}, {"comments": "bad\x00nul"}, {"comments": "bad\x85nel"},
            {"version": 2},
        ]
        for overrides in invalid:
            self.assertEqual(self.apply(**overrides)["result"], "rejected", overrides)
        self.assertEqual(self.note.read_text(encoding="utf-8"), NOTE)

    def test_malformed_requests_are_rejected(self):
        bodies = [
            "no marker here", MARKER, f"{MARKER}\n\n```json\n{{not json}}\n```", f"{MARKER}\n\n```json\n[1, 2]\n```",
            f"{MARKER}\n```json\n{json.dumps({**BASE, 'comments': 'x' * 21000})}\n```",
            None,
        ]
        for body in bodies:
            self.assertEqual(apply_request(body, "OWNER", self.root)["result"], "rejected", str(body)[:40])
        self.assertEqual(self.note.read_text(encoding="utf-8"), NOTE)

    def test_note_without_valid_frontmatter_is_left_alone(self):
        for text in ("# No frontmatter\n", "---\ntitle: [unclosed\n---\nBody\n"):
            self.note.write_text(text, encoding="utf-8")
            self.assertEqual(self.apply()["result"], "rejected")
            self.assertEqual(self.note.read_text(encoding="utf-8"), text)

    def test_main_writes_single_line_workflow_outputs(self):
        output = self.root / "github_output"
        environment = {"ISSUE_BODY": request_body(BASE), "ISSUE_AUTHOR_ASSOCIATION": "OWNER", "GITHUB_OUTPUT": str(output)}
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            with patch.dict(os.environ, environment):
                main()
        finally:
            os.chdir(previous)
        lines = output.read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines[0], "result=applied")
        self.assertTrue(lines[1].startswith("message=Updated personal notes in notes/1_sample.md"))
        self.assertEqual(lines[2], "note_path=notes/1_sample.md")


if __name__ == "__main__":
    unittest.main()
