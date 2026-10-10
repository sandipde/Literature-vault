import os
import re
from pathlib import Path

from scripts.literature import (
    extract_url,
    load_registry,
    register_source,
    resolve_metadata,
    save_registry,
    utc_date,
    write_note,
)

NOTES_DIR = Path("notes")
REGISTRY_FILE = Path("sources.json")


def main():
    issue_number = os.environ.get("ISSUE_NUM", "0")
    author = os.environ.get("USER_LOGIN", "unknown")
    raw_title = os.environ.get("ISSUE_TITLE", f"Paper-{issue_number}")
    body = os.environ.get("ISSUE_BODY", "")
    source_url = extract_url(body)
    if not source_url:
        raise ValueError("Issue body must contain a URL or DOI")

    metadata = resolve_metadata(source_url, fallback_title=raw_title)
    registry = load_registry(REGISTRY_FILE, NOTES_DIR)
    existing = registry["sources"].get(metadata["canonical_url"])
    if existing:
        save_registry(registry, REGISTRY_FILE)
        note_path = existing.get("notes", [""])[0]
        result = {"result": "duplicate", "note_path": note_path, "canonical_url": metadata["canonical_url"]}
    else:
        title_slug = re.sub(r"[^a-zA-Z0-9_-]", "_", metadata["title"])
        title_slug = re.sub(r"_+", "_", title_slug).strip("_")[:50] or "reference"
        filename = f"{issue_number}_{title_slug}.md"
        NOTES_DIR.mkdir(parents=True, exist_ok=True)
        target_path = NOTES_DIR / filename
        write_note(target_path, metadata, source_url, author, utc_date(), issue_number)
        register_source(registry, metadata, target_path, source_url)
        save_registry(registry, REGISTRY_FILE)
        result = {"result": "created", "note_path": str(target_path), "canonical_url": metadata["canonical_url"]}

    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as output:
            for key, value in result.items():
                output.write(f"{key}={value}\n")
    print(f"{result['result']}: {result['note_path']}")
    return result


if __name__ == "__main__":
    main()
