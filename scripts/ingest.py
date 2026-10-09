import os
import re
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
import requests

body = os.environ.get("ISSUE_BODY", "")
num = os.environ.get("ISSUE_NUM", "0")
author = os.environ.get("USER_LOGIN", "unknown")
raw_title = os.environ.get("ISSUE_TITLE", f"Paper-{num}")
abstract = "N/A"

title = " ".join(raw_title.split())

arxiv_match = re.search(r'(\d{4}\.\d{4,5})', body)
if arxiv_match:
    arxiv_id = arxiv_match.group(1)
    try:
        r = requests.get(f"https://export.arxiv.org/api/query?id_list={arxiv_id}", timeout=20)
        if r.ok:
            entry = ET.fromstring(r.text).find('{http://www.w3.org/2005/Atom}entry')
            if entry is not None:
                fetched_title = entry.find('{http://www.w3.org/2005/Atom}title')
                fetched_abstract = entry.find('{http://www.w3.org/2005/Atom}summary')
                if fetched_title is not None and fetched_title.text:
                    title = " ".join(fetched_title.text.split())
                if fetched_abstract is not None and fetched_abstract.text:
                    abstract = fetched_abstract.text.strip()
    except Exception as e:
        print(f"arXiv fetch error: {e}")

clean_slug = re.sub(r'[^a-zA-Z0-9_-]', '_', title)
clean_slug = re.sub(r'_+', '_', clean_slug).strip('_')[:40] or "paper"
filename = f"{num}_{clean_slug}.md"

out_dir = Path("notes")
out_dir.mkdir(parents=True, exist_ok=True)
target_path = out_dir / filename

safe_title = title.replace('"', '\\"')
note_content = (
    f"---\n"
    f"title: \"{safe_title}\"\n"
    f"source: \"{body.strip()}\"\n"
    f"captured_by: \"{author}\"\n"
    f"date: {date.today().isoformat()}\n"
    f"issue: {num}\n"
    f"---\n\n"
    f"# {title}\n\n"
    f"- **Captured by:** @{author}\n"
    f"- **Source:** {body.strip()}\n\n"
    f"## Abstract\n{abstract}\n"
)

target_path.write_text(note_content, encoding="utf-8")
print(f"Successfully generated note: {target_path}")
