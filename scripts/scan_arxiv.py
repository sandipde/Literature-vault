import json
import re
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

from scripts.literature import (
    canonicalize_url,
    load_registry,
    register_source,
    save_registry,
    utc_date,
    write_note,
)

CONFIG_FILE = Path("monitor_config.json")
SEEN_FILE = Path("seen_papers.json")
REGISTRY_FILE = Path("sources.json")
NOTES_DIR = Path("notes")
ATOM = "http://www.w3.org/2005/Atom"


def run_scan(config_file=CONFIG_FILE, seen_file=SEEN_FILE, registry_file=REGISTRY_FILE, notes_dir=NOTES_DIR):
    seen_file = Path(seen_file)
    notes_dir = Path(notes_dir)
    seen_ids = set(json.loads(seen_file.read_text(encoding="utf-8"))) if seen_file.exists() else set()
    original_seen = set(seen_ids)
    config_path = Path(config_file)
    config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {"queries": []}
    registry = load_registry(registry_file, notes_dir)
    notes_dir.mkdir(parents=True, exist_ok=True)

    for query_string in config.get("queries", []):
        response = requests.get(
            "https://export.arxiv.org/api/query",
            params={"search_query": query_string, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 10},
            timeout=30,
        )
        response.raise_for_status()
        root = ET.fromstring(response.text)
        for entry in root.findall(f"{{{ATOM}}}entry"):
            raw_id = (entry.findtext(f"{{{ATOM}}}id") or "").strip()
            arxiv_id = raw_id.split("/abs/")[-1].split("v")[0]
            if not arxiv_id:
                continue
            source_url = f"https://arxiv.org/abs/{arxiv_id}"
            _, canonical_url = canonicalize_url(source_url)
            if arxiv_id in seen_ids or canonical_url in registry["sources"]:
                seen_ids.add(arxiv_id)
                continue

            title = " ".join((entry.findtext(f"{{{ATOM}}}title") or "").split())
            summary = " ".join((entry.findtext(f"{{{ATOM}}}summary") or "").split())
            authors = [
                (author.findtext(f"{{{ATOM}}}name") or "").strip()
                for author in entry.findall(f"{{{ATOM}}}author")
            ]
            published = (entry.findtext(f"{{{ATOM}}}published") or "")[:10]
            categories = [item.get("term", "") for item in entry.findall(f"{{{ATOM}}}category")]
            metadata = {
                "type": "arxiv",
                "canonical_url": canonical_url,
                "title": title or f"arXiv:{arxiv_id}",
                "authors": authors,
                "published": published,
                "abstract": summary,
                "metadata_provider": "arXiv",
                "metadata_status": "complete",
                "provider_data": {"arxiv_id": arxiv_id, "categories": categories},
            }
            slug = re.sub(r"[^a-zA-Z0-9_-]", "_", metadata["title"])
            slug = re.sub(r"_+", "_", slug).strip("_")[:50] or "paper"
            target_path = notes_dir / f"arxiv_{arxiv_id}_{slug}.md"
            write_note(target_path, metadata, source_url, "auto-scanner", utc_date(), "auto")
            register_source(registry, metadata, target_path, source_url)
            seen_ids.add(arxiv_id)

    save_registry(registry, registry_file)
    if seen_ids != original_seen:
        seen_file.write_text(json.dumps(sorted(seen_ids), indent=2) + "\n", encoding="utf-8")
    return {"seen": seen_ids, "sources": registry["sources"]}


if __name__ == "__main__":
    run_scan()
