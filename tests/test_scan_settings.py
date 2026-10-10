import json
import tempfile
import unittest
from pathlib import Path

from scripts.scan_config import default_profiles, validate_config
from scripts.update_scan_settings import MARKER, apply_settings_request


def issue_body(config):
    return f"{MARKER}\n\n```json\n{json.dumps(config)}\n```"


class ScanSettingsTests(unittest.TestCase):
    def test_unauthorized_request_does_not_modify_config(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "monitor_config.json"
            path.write_text('{"version": 1, "profiles": []}\n', encoding="utf-8")
            original = path.read_text(encoding="utf-8")
            result = apply_settings_request(issue_body({"version": 1, "profiles": []}), "NONE", path)
            self.assertEqual(result["result"], "rejected")
            self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_authorized_request_updates_config(self):
        config = {"version": 1, "profiles": [default_profiles()[0]]}
        expected = validate_config(config)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "monitor_config.json"
            result = apply_settings_request(issue_body(config), "COLLABORATOR", path)
            self.assertEqual(result["result"], "applied")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), expected)

    def test_invalid_payload_does_not_modify_config(self):
        config = {"version": 1, "profiles": [default_profiles()[0] | {"max_results": 1000}]}
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "monitor_config.json"
            result = apply_settings_request(issue_body(config), "OWNER", path)
            self.assertEqual(result["result"], "rejected")
            self.assertFalse(path.exists())

    def test_unmarked_issue_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "monitor_config.json"
            result = apply_settings_request("not a settings issue", "OWNER", path)
            self.assertEqual(result["result"], "rejected")
            self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
