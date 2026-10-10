import hashlib
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from scripts.literature import load_registry, register_source, save_registry, utc_date, write_note
from scripts.scan_config import is_due, migrate_config
from scripts.scan_providers import search_profile

CONFIG_FILE = Path("monitor_config.json")
STATE_FILE = Path("scan_state.json")
HISTORY_FILE = Path("scan_history.json")
SEEN_FILE = Path("seen_papers.json")
REGISTRY_FILE = Path("sources.json")
NOTES_DIR = Path("notes")


def _load_state(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("version") == 1 and isinstance(data.get("profiles"), dict):
            return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"version": 1, "profiles": {}}


def _load_history(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("version") == 1 and isinstance(data.get("runs"), list):
            return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"version": 1, "runs": []}


def _filename(profile, metadata):
    slug = re.sub(r"[^a-zA-Z0-9_-]", "_", metadata["title"])
    slug = re.sub(r"_+", "_", slug).strip("_")[:45] or "reference"
    digest = hashlib.sha1(metadata["canonical_url"].encode("utf-8")).hexdigest()[:10]
    arxiv_id = metadata.get("provider_data", {}).get("arxiv_id")
    prefix = f"arxiv_{arxiv_id}" if arxiv_id else profile["provider"]
    return f"{prefix}_{slug}_{digest}.md"


def run_scan(config_file=CONFIG_FILE, seen_file=SEEN_FILE, registry_file=REGISTRY_FILE, notes_dir=NOTES_DIR, state_file=None, now=None, profile_names=None, max_results_override=None, history_file=None, force=False):
    config_path = Path(config_file)
    seen_path = Path(seen_file)
    registry_path = Path(registry_file)
    notes_path = Path(notes_dir)
    state_path = Path(state_file) if state_file else config_path.parent / "scan_state.json"
    history_path = Path(history_file) if history_file else config_path.parent / "scan_history.json"
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    raw_config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {"queries": []}
    config = migrate_config(raw_config)
    state = _load_state(state_path)
    seen_ids = set(json.loads(seen_path.read_text(encoding="utf-8"))) if seen_path.exists() else set()
    initial_seen = set(seen_ids)
    registry = load_registry(registry_path, notes_path)
    notes_path.mkdir(parents=True, exist_ok=True)
    completed = []
    failed = {}
    added_notes = []
    profile_runs = []
    selected_names = set(profile_names) if profile_names is not None else None

    for profile in config["profiles"]:
        if selected_names is not None and profile["name"] not in selected_names:
            continue
        if not profile["enabled"]:
            profile_runs.append({"id": profile["id"], "name": profile["name"], "provider": profile["provider"], "lookback_hours": profile["lookback_hours"], "status": "disabled"})
            continue
        previous = state["profiles"].get(profile["id"])
        if not force and not is_due(profile, previous, now):
            profile_runs.append({"id": profile["id"], "name": profile["name"], "provider": profile["provider"], "lookback_hours": profile["lookback_hours"], "status": "not_due"})
            continue
        try:
            active_profile = dict(profile)
            if max_results_override is not None:
                active_profile["max_results"] = min(profile["max_results"], max_results_override)
            results = search_profile(active_profile, now=now)
            before_count = len(added_notes)
            for metadata in results:
                canonical_url = metadata["canonical_url"]
                arxiv_id = metadata.get("provider_data", {}).get("arxiv_id")
                if canonical_url in registry["sources"] or (arxiv_id and arxiv_id in seen_ids):
                    if arxiv_id:
                        seen_ids.add(arxiv_id)
                    continue
                target_path = notes_path / _filename(profile, metadata)
                write_note(target_path, metadata, metadata.get("source_url", canonical_url), "auto-scanner", utc_date(), f"scan:{profile['id']}")
                register_source(registry, metadata, target_path, metadata.get("source_url", canonical_url))
                added_notes.append(str(target_path))
                if arxiv_id:
                    seen_ids.add(arxiv_id)
            state["profiles"][profile["id"]] = now.astimezone(timezone.utc).isoformat()
            completed.append(profile["id"])
            profile_runs.append({
                "id": profile["id"], "name": profile["name"], "provider": profile["provider"],
                "lookback_hours": profile["lookback_hours"], "status": "success",
                "results": len(results), "notes_added": len(added_notes) - before_count,
            })
        except Exception as error:
            failed[profile["id"]] = str(error)[:300]
            profile_runs.append({
                "id": profile["id"], "name": profile["name"], "provider": profile["provider"],
                "lookback_hours": profile["lookback_hours"], "status": "failed", "error": str(error)[:300],
            })
            print(f"Profile {profile['id']} failed: {error}")

    save_registry(registry, registry_path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if seen_ids != initial_seen:
        seen_path.write_text(json.dumps(sorted(seen_ids), indent=2) + "\n", encoding="utf-8")
    history = _load_history(history_path)
    history["runs"].append({
        "started_at": now.astimezone(timezone.utc).isoformat(),
        "profiles": profile_runs,
        "notes_added": len(added_notes),
    })
    history["runs"] = history["runs"][-100:]
    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "completed": completed,
        "failed": failed,
        "added_notes": added_notes,
        "seen": seen_ids,
        "sources": registry["sources"],
        "state": state,
        "profile_runs": profile_runs,
    }


def main():
    parser = argparse.ArgumentParser(description="Run due literature scan profiles")
    parser.add_argument("--profile-name", action="append", help="Run only profiles with this name; may be repeated")
    parser.add_argument("--max-results", type=int, help="Temporarily cap results per profile for a test run")
    parser.add_argument("--force", action="store_true", help="Ignore profile cadence while preserving lookback and deduplication")
    arguments = parser.parse_args()
    if arguments.max_results is not None and not 1 <= arguments.max_results <= 100:
        parser.error("--max-results must be between 1 and 100")
    result = run_scan(profile_names=arguments.profile_name, max_results_override=arguments.max_results, force=arguments.force)
    print(f"Completed profiles: {len(result['completed'])}; notes added: {len(result['added_notes'])}; profile failures: {len(result['failed'])}")
    for profile in result["profile_runs"]:
        print(f"{profile['provider']} / {profile['name']}: {profile['status']} ({profile.get('notes_added', 0)} notes)")
    return result


if __name__ == "__main__":
    main()
