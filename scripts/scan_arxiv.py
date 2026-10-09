import json, re, urllib.parse, requests
import xml.etree.ElementTree as ET
from pathlib import Path

CONFIG_FILE = Path("monitor_config.json")
SEEN_FILE = Path("seen_papers.json")
NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

seen_ids = set(json.loads(SEEN_FILE.read_text())) if SEEN_FILE.exists() else set()
config = json.loads(CONFIG_FILE.read_text()) if CONFIG_FILE.exists() else {"queries": []}
new_seen = set()

for query_str in config.get("queries", []):
    encoded_q = urllib.parse.quote(query_str)
    url = f"http://export.arxiv.org/api/query?search_query={encoded_q}&sortBy=submittedDate&sortOrder=descending&max_results=10"
    resp = requests.get(url, timeout=30)
    if not resp.ok: continue
    root = ET.fromstring(resp.text)
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        raw_id = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()
        arxiv_id = raw_id.split("/abs/")[-1]
        if arxiv_id in seen_ids: continue

        title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip().replace("\n", " ")
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip().replace("\n", " ")
        authors = [a.find("{http://www.w3.org/2005/Atom}name").text for a in entry.findall("{http://www.w3.org/2005/Atom}author")]
        published = entry.find("{http://www.w3.org/2005/Atom}published").text[:10]

        slug = re.sub(r"[^a-zA-Z0-9]", "_", title)[:40]
        filename = f"arxiv_{arxiv_id}_{slug}.md"
        content = f"""---
title: "{title}"
arxiv_id: "{arxiv_id}"
authors: {json.dumps(authors)}
published: "{published}"
source: "https://arxiv.org/abs/{arxiv_id}"
captured_by: "auto-scanner"
status: "to-read"
---

# {title}

- **Authors:** {', '.join(authors[:5])}
- **Published:** {published}
- **Link:** [arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})

## Abstract
{summary}
"""
        (NOTES_DIR / filename).write_text(content)
        seen_ids.add(arxiv_id)
        new_seen.add(arxiv_id)

if new_seen:
    SEEN_FILE.write_text(json.dumps(sorted(list(seen_ids)), indent=2))
