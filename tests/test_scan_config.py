import unittest
from datetime import datetime, timezone

from scripts.scan_config import default_profiles, is_due, migrate_config, mlip_development_profiles, validate_config


class ScanConfigTests(unittest.TestCase):
    def test_migration_preserves_existing_queries_and_adds_editable_profiles(self):
        old = {
            "queries": [
                "cat:physics.chem-ph AND abs:catalysis",
                'cat:cond-mat.mtrl-sci AND abs:"machine learning"',
            ]
        }
        migrated = migrate_config(old)
        legacy = [profile for profile in migrated["profiles"] if profile["id"].startswith("arxiv-legacy-")]
        self.assertEqual([profile["queries"][0] for profile in legacy], old["queries"])
        self.assertTrue(all(profile["enabled"] for profile in legacy))
        self.assertTrue({"arxiv", "crossref", "chemrxiv", "github", "gitlab", "huggingface_model", "huggingface_dataset", "huggingface_space"}.issubset(
            {profile["provider"] for profile in migrated["profiles"]}
        ))

    def test_validation_rejects_duplicate_ids_and_unsafe_limits(self):
        duplicate = {"version": 1, "profiles": [default_profiles()[0], default_profiles()[0]]}
        with self.assertRaisesRegex(ValueError, "Invalid or duplicate profile id"):
            validate_config(duplicate)
        unsafe = default_profiles()[0] | {"max_results": 1000}
        with self.assertRaisesRegex(ValueError, "max_results"):
            validate_config({"version": 1, "profiles": [unsafe]})

    def test_mlip_template_covers_all_scan_providers_twice_daily(self):
        profiles = mlip_development_profiles()
        self.assertEqual({profile["provider"] for profile in profiles}, {
            "arxiv", "crossref", "chemrxiv", "github", "gitlab",
            "huggingface_model", "huggingface_dataset", "huggingface_space",
        })
        self.assertTrue(all(profile["name"] == "MLIP developments scan" for profile in profiles))
        self.assertTrue(all(profile["enabled"] and profile["interval"] == "twice_daily" for profile in profiles))
        arxiv_queries = " ".join(next(profile for profile in profiles if profile["provider"] == "arxiv")["queries"])
        self.assertTrue(all(term in arxiv_queries for term in ("MACE", "NequIP", "active learning", "heterogeneous catalysis")))
        self.assertTrue(all(profile["lookback_hours"] == 24 for profile in profiles))

    def test_lookback_defaults_to_24_hours_and_rejects_invalid_values(self):
        profile = default_profiles()[0]
        normalized = validate_config({"version": 1, "profiles": [profile]})
        self.assertEqual(normalized["profiles"][0]["lookback_hours"], 24)
        invalid = profile | {"lookback_hours": 0}
        with self.assertRaisesRegex(ValueError, "lookback_hours"):
            validate_config({"version": 1, "profiles": [invalid]})

    def test_interval_schedule_and_month_end_clamping(self):
        now = datetime(2026, 2, 28, 12, tzinfo=timezone.utc)
        self.assertTrue(is_due({"interval": "monthly"}, "2026-01-31T12:00:00+00:00", now))
        self.assertTrue(is_due({"interval": "twice_daily"}, "2026-02-28T00:00:00+00:00", now))
        self.assertFalse(is_due({"interval": "twice_daily"}, "2026-02-28T05:00:00+00:00", now))
        self.assertTrue(is_due({"interval": "twice_daily"}, "2026-02-27T20:00:00+00:00", datetime(2026, 2, 28, 5, tzinfo=timezone.utc)))
        self.assertFalse(is_due({"interval": "twice_daily"}, "2026-02-28T20:00:00+00:00", datetime(2026, 2, 28, 22, tzinfo=timezone.utc)))
        self.assertFalse(is_due({"interval": "weekly"}, "2026-02-23T12:00:00+00:00", now))
        self.assertTrue(is_due({"interval": "weekly"}, "2026-02-21T12:00:00+00:00", now))
        self.assertTrue(is_due({"interval": "daily"}, None, now))


if __name__ == "__main__":
    unittest.main()
