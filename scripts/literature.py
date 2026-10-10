import html
import ipaddress
import json
import re
import socket
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path

import requests
import yaml

URL_PATTERN = re.compile(r"https?://[^\s<>\"'`]+", re.IGNORECASE)
DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/A-Z0-9]+", re.IGNORECASE)
TRACKING_PARAMETERS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
ATOM = "http://www.w3.org/2005/Atom"
ARXIV_ATOM = "http://arxiv.org/schemas/atom"


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        return " ".join(" ".join(self.parts).split())


class _CitationMetadataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = {}

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "meta":
            return
        attributes = dict(attrs)
        name = attributes.get("name") or attributes.get("property") or attributes.get("itemprop")
        content = attributes.get("content")
        if name and content:
            self.values.setdefault(name.lower(), []).append(html.unescape(content.strip()))


def clean_url(value):
    return value.strip().rstrip(".,;:!?) ]}>")


def extract_url(text):
    match = URL_PATTERN.search(text or "")
    if match:
        return clean_url(match.group(0))

    doi_match = DOI_PATTERN.search(text or "")
    if doi_match:
        return f"https://doi.org/{clean_url(doi_match.group(0))}"
    return ""


def _doi_from(value):
    match = DOI_PATTERN.search(urllib.parse.unquote(value or ""))
    return clean_url(match.group(0)) if match else ""


def classify_url(value):
    parsed = urllib.parse.urlsplit(value if "://" in value else f"https://{value}")
    host = (parsed.hostname or "").lower().removeprefix("www.")
    path = urllib.parse.unquote(parsed.path).strip("/")

    if host in {"doi.org", "dx.doi.org"} or _doi_from(path):
        return "paper"
    if host in {"arxiv.org", "export.arxiv.org"} and re.search(r"\d{4}\.\d{4,5}", path):
        return "arxiv"
    if host in {"github.com", "www.github.com"} and len(path.split("/")) >= 2:
        return "github"
    if host == "huggingface.co" and path:
        segments = path.split("/")
        if segments[0] in {"datasets", "spaces"}:
            return f"huggingface_{segments[0][:-1]}"
        if len(segments) >= 2:
            return "huggingface_model"
    if host in {"gitlab.com", "www.gitlab.com"} and path:
        return "gitlab"
    if host in {"chemrxiv.org", "www.chemrxiv.org"}:
        return "chemrxiv"
    return "web"


def canonicalize_url(value):
    parsed = urllib.parse.urlsplit(value if "://" in value else f"https://{value}")
    host = (parsed.hostname or "").lower().removeprefix("www.")
    path = urllib.parse.unquote(parsed.path).strip("/")
    kind = classify_url(value)

    if kind == "paper":
        doi = _doi_from(path)
        if not doi and host in {"doi.org", "dx.doi.org"}:
            doi = path
        if doi:
            return kind, f"https://doi.org/{doi.lower()}"
    elif kind == "arxiv":
        match = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?", path)
        if match:
            return kind, f"https://arxiv.org/abs/{match.group(1)}"
    elif kind == "github":
        segments = path.split("/")[:2]
        if len(segments) == 2:
            segments[1] = re.sub(r"\.git$", "", segments[1], flags=re.IGNORECASE)
            return kind, f"https://github.com/{'/'.join(segments).lower()}"
    elif kind.startswith("huggingface_"):
        segments = path.split("/")
        if segments[0] in {"datasets", "spaces"}:
            prefix, repo = segments[0], segments[1:3]
            return kind, f"https://huggingface.co/{prefix}/{'/'.join(repo).lower()}"
        return kind, f"https://huggingface.co/{'/'.join(segments[:2]).lower()}"
    elif kind == "gitlab":
        segments = []
        for segment in path.split("/"):
            if segment == "-":
                break
            segments.append(segment)
        if segments and segments[-1].endswith(".git"):
            segments[-1] = segments[-1][:-4]
        return kind, f"https://gitlab.com/{'/'.join(segments).lower()}"
    elif kind == "chemrxiv":
        return kind, f"https://chemrxiv.org/{path}"

    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(key, item) for key, item in query if key.lower() not in TRACKING_PARAMETERS and not key.lower().startswith("utm_")]
    normalized_path = f"/{path}" if path else ""
    normalized_query = urllib.parse.urlencode(query)
    suffix = f"?{normalized_query}" if normalized_query else ""
    return kind, f"https://{host}{normalized_path}{suffix}"


def _request_json(url, params=None):
    response = requests.get(url, params=params, timeout=20, headers={"User-Agent": "LiteratureVault/1.0 (open metadata lookup)"})
    response.raise_for_status()
    return response.json()


def _request_text(url, params=None):
    response = requests.get(url, params=params, timeout=20, headers={"User-Agent": "LiteratureVault/1.0 (open metadata lookup)"})
    response.raise_for_status()
    return response.text


def _request_public_html(url):
    current_url = url
    for _ in range(5):
        parsed = urllib.parse.urlsplit(current_url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError("Publisher metadata URL must be a public HTTP(S) URL.")
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        if port != (443 if parsed.scheme == "https" else 80):
            raise ValueError("Publisher metadata URL uses an unsupported port.")
        try:
            addresses = socket.getaddrinfo(parsed.hostname, port, type=socket.SOCK_STREAM)
        except OSError as error:
            raise requests.ConnectionError(f"Could not resolve publisher host: {error}") from error
        if not addresses or any(not ipaddress.ip_address(address[4][0]).is_global for address in addresses):
            raise ValueError("Publisher metadata URL must resolve only to public addresses.")

        response = requests.get(
            current_url,
            timeout=20,
            headers={"User-Agent": "LiteratureVault/1.0 (open metadata lookup)", "Accept": "text/html"},
            allow_redirects=False,
            stream=True,
        )
        try:
            if 300 <= response.status_code < 400:
                location = response.headers.get("Location")
                if not location:
                    response.raise_for_status()
                current_url = urllib.parse.urljoin(current_url, location)
                continue
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "text/html").lower()
            if "html" not in content_type:
                return ""
            body = bytearray()
            for chunk in response.iter_content(65536):
                body.extend(chunk)
                if len(body) > 2 * 1024 * 1024:
                    raise requests.RequestException("Publisher page exceeds the metadata size limit.")
            return bytes(body).decode(response.encoding or "utf-8", errors="replace")
        finally:
            response.close()
    raise requests.TooManyRedirects("Publisher page has too many redirects.")


def _plain_text(value):
    parser = _TextExtractor()
    parser.feed(value or "")
    return html.unescape(parser.text())


def _date_parts(value):
    if isinstance(value, dict):
        value = value.get("date-parts", [[]])
    try:
        parts = value[0]
        return "-".join(str(part).zfill(2) if index else str(part) for index, part in enumerate(parts[:3]))
    except (IndexError, TypeError):
        return ""


def _crossref(doi):
    data = _request_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")["message"]
    authors = [" ".join(part for part in (item.get("given"), item.get("family")) if part) for item in data.get("author", [])]
    return {
        "title": (data.get("title") or [""])[0],
        "authors": authors,
        "published": _date_parts(data.get("published-print") or data.get("published-online") or data.get("created")),
        "abstract": _plain_text(data.get("abstract", "")),
        "provider_data": {
            "doi": data.get("DOI", doi),
            "journal": (data.get("container-title") or [""])[0],
            "publisher": data.get("publisher", ""),
            "volume": data.get("volume", ""),
            "issue": data.get("issue", ""),
            "page": data.get("page", ""),
            "type": data.get("type", ""),
            "subjects": data.get("subject", []),
            "license": data.get("license", []),
        },
    }


def _openalex(canonical_url):
    data = _request_json(
        "https://api.openalex.org/works",
        params={"filter": f"locations.landing_page_url:{canonical_url}", "per-page": 1},
    )
    results = data.get("results", [])
    return _openalex_work(results[0]) if results else {}


def _openalex_work(work):
    inverted = work.get("abstract_inverted_index") or {}
    words = []
    for word, positions in inverted.items():
        words.extend((position, word) for position in positions)
    abstract = " ".join(word for _, word in sorted(words))
    authors = [item.get("author", {}).get("display_name", "") for item in work.get("authorships", [])]
    primary_source = ((work.get("primary_location") or {}).get("source") or {})
    return {
        "title": work.get("title", ""),
        "authors": authors,
        "published": work.get("publication_date", ""),
        "abstract": abstract,
        "provider_data": {
            "doi": work.get("doi", ""),
            "journal": primary_source.get("display_name", ""),
            "type": work.get("type", ""),
            "topics": [topic.get("display_name", "") for topic in work.get("topics", [])],
            "open_access": work.get("open_access", {}),
            "cited_by_count": work.get("cited_by_count"),
        },
    }


def _openalex_by_doi(doi):
    encoded_doi = urllib.parse.quote(doi, safe="/")
    work = _request_json(f"https://api.openalex.org/works/https://doi.org/{encoded_doi}")
    return _openalex_work(work)


def _title_for_lookup(value):
    title = (value or "").split(" | ", 1)[0]
    return " ".join(re.findall(r"\w+", title.casefold()))


def _openalex_by_title(title):
    normalized_title = _title_for_lookup(title)
    if len(normalized_title) < 20 or normalized_title in {"new reference", "paper"}:
        return {}
    results = _request_json(
        "https://api.openalex.org/works",
        params={"search": title.split(" | ", 1)[0], "per-page": 5},
    ).get("results", [])
    if not results:
        return {}
    best_match = max(
        results,
        key=lambda work: SequenceMatcher(None, normalized_title, _title_for_lookup(work.get("title", ""))).ratio(),
    )
    similarity = SequenceMatcher(None, normalized_title, _title_for_lookup(best_match.get("title", ""))).ratio()
    return _openalex_work(best_match) if similarity >= 0.9 else {}


def _metadata_values(values, *keys):
    return [value for key in keys for value in values.get(key, []) if value]


def _fetch_web_metadata(canonical_url, fallback_title=""):
    values = {}
    try:
        parser = _CitationMetadataParser()
        parser.feed(_request_public_html(canonical_url))
        values = parser.values
    except (requests.RequestException, ValueError):
        pass

    page_titles = _metadata_values(values, "citation_title", "dc.title", "dcterms.title", "og:title")
    page_authors = _metadata_values(values, "citation_author")
    if not page_authors:
        page_authors = _metadata_values(values, "dc.creator", "author")
    page_abstracts = _metadata_values(values, "citation_abstract", "description", "og:description")
    page_dates = _metadata_values(values, "citation_publication_date", "citation_online_date", "citation_date", "dc.date")
    page_dois = _metadata_values(values, "citation_doi", "prism.doi", "dc.identifier")
    doi = _doi_from(page_dois[0]) if page_dois else ""
    title = page_titles[0] if page_titles else fallback_title

    crossref = {}
    if doi:
        try:
            crossref = _crossref(doi)
        except requests.RequestException:
            pass

    openalex = {}
    if doi and (not crossref.get("abstract") or not crossref.get("authors")):
        try:
            openalex = _openalex_by_doi(doi)
        except requests.RequestException:
            pass
    elif title:
        try:
            openalex = _openalex_by_title(title)
        except requests.RequestException:
            pass
    if not crossref and openalex:
        doi = _doi_from(openalex.get("provider_data", {}).get("doi", ""))
        if doi:
            try:
                crossref = _crossref(doi)
            except requests.RequestException:
                pass

    details = {
        "title": page_titles[0] if page_titles else crossref.get("title") or openalex.get("title", ""),
        "authors": page_authors or crossref.get("authors") or openalex.get("authors", []),
        "published": crossref.get("published") or openalex.get("published") or (page_dates[0] if page_dates else ""),
        "abstract": page_abstracts[0] if page_abstracts else crossref.get("abstract") or openalex.get("abstract", ""),
        "provider_data": {},
    }
    details["provider_data"].update(crossref.get("provider_data", {}))
    for key, value in openalex.get("provider_data", {}).items():
        details["provider_data"].setdefault(key, value)
    if doi:
        details["provider_data"].setdefault("doi", doi)
    journal_titles = _metadata_values(values, "citation_journal_title", "prism.publicationname")
    if journal_titles:
        details["provider_data"].setdefault("journal", journal_titles[0])

    if not any((details["title"], details["authors"], details["published"], details["abstract"])):
        return "Publisher metadata", {}
    provider = "Crossref" if crossref else "OpenAlex" if openalex else "Publisher metadata"
    return provider, details


def _fetch_arxiv(canonical_url):
    arxiv_id = canonical_url.rsplit("/", 1)[-1]
    content = _request_text("https://export.arxiv.org/api/query", params={"id_list": arxiv_id})
    entry = ET.fromstring(content).find(f"{{{ATOM}}}entry")
    if entry is None:
        return {}
    get_text = lambda name: (entry.findtext(f"{{{ATOM}}}{name}") or "").strip()
    primary_category = entry.find(f"{{{ARXIV_ATOM}}}primary_category")
    return {
        "title": " ".join(get_text("title").split()),
        "authors": [item.findtext(f"{{{ATOM}}}name", default="").strip() for item in entry.findall(f"{{{ATOM}}}author")],
        "published": get_text("published")[:10],
        "abstract": " ".join(get_text("summary").split()),
        "provider_data": {
            "arxiv_id": arxiv_id,
            "categories": [item.get("term", "") for item in entry.findall(f"{{{ATOM}}}category")],
            "primary_category": primary_category.get("term", "") if primary_category is not None else "",
            "updated": get_text("updated"),
            "doi": get_text("doi"),
        },
    }


def _fetch_github(canonical_url):
    owner, repo = urllib.parse.urlsplit(canonical_url).path.strip("/").split("/", 1)
    data = _request_json(f"https://api.github.com/repos/{owner}/{repo}")
    return {
        "title": data.get("full_name", ""),
        "abstract": data.get("description", "") or "",
        "provider_data": {
            "description": data.get("description", ""),
            "language": data.get("language", ""),
            "topics": data.get("topics", []),
            "license": (data.get("license") or {}).get("spdx_id", ""),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "open_issues": data.get("open_issues_count"),
            "created_at": data.get("created_at", ""),
            "pushed_at": data.get("pushed_at", ""),
            "default_branch": data.get("default_branch", ""),
        },
    }


def _fetch_huggingface(kind, canonical_url):
    path = urllib.parse.urlsplit(canonical_url).path.strip("/")
    if kind == "huggingface_dataset":
        _, owner, repo = path.split("/", 2)
        endpoint = f"datasets/{owner}/{repo}"
    elif kind == "huggingface_space":
        _, owner, repo = path.split("/", 2)
        endpoint = f"spaces/{owner}/{repo}"
    else:
        owner, repo = path.split("/", 1)
        endpoint = f"models/{owner}/{repo}"
    data = _request_json(f"https://huggingface.co/api/{endpoint}", params={"full": "true"})
    card = data.get("cardData") or {}
    siblings = data.get("siblings", [])
    return {
        "title": data.get("id", f"{owner}/{repo}"),
        "abstract": card.get("description", "") or "",
        "provider_data": {
            "task": data.get("pipeline_tag", ""),
            "sdk": data.get("sdk", ""),
            "tags": data.get("tags", []),
            "license": card.get("license", ""),
            "downloads": data.get("downloads"),
            "likes": data.get("likes"),
            "last_modified": data.get("lastModified", ""),
            "files": [item.get("rfilename", "") for item in siblings[:30]],
        },
    }


def _fetch_gitlab(canonical_url):
    project_path = urllib.parse.urlsplit(canonical_url).path.strip("/")
    project_id = urllib.parse.quote(project_path, safe="")
    data = _request_json(f"https://gitlab.com/api/v4/projects/{project_id}")
    return {
        "title": data.get("path_with_namespace", ""),
        "abstract": data.get("description", "") or "",
        "provider_data": {
            "description": data.get("description", ""),
            "topics": data.get("topics", []),
            "license": (data.get("license") or {}).get("key", ""),
            "stars": data.get("star_count"),
            "forks": data.get("forks_count"),
            "visibility": data.get("visibility", ""),
            "created_at": data.get("created_at", ""),
            "last_activity_at": data.get("last_activity_at", ""),
            "default_branch": data.get("default_branch", ""),
        },
    }


def resolve_metadata(value, fallback_title=""):
    kind, canonical_url = canonicalize_url(value)
    result = {
        "type": kind,
        "canonical_url": canonical_url,
        "title": " ".join((fallback_title or "").split()) or canonical_url,
        "authors": [],
        "published": "",
        "abstract": "",
        "metadata_provider": "",
        "metadata_status": "unavailable",
        "provider_data": {},
    }
    try:
        if kind == "arxiv":
            provider, details = "arXiv", _fetch_arxiv(canonical_url)
        elif kind == "github":
            provider, details = "GitHub", _fetch_github(canonical_url)
        elif kind.startswith("huggingface_"):
            provider, details = "Hugging Face", _fetch_huggingface(kind, canonical_url)
        elif kind == "gitlab":
            provider, details = "GitLab", _fetch_gitlab(canonical_url)
        elif kind == "paper":
            doi = _doi_from(urllib.parse.urlsplit(canonical_url).path)
            provider = "Crossref"
            details = _crossref(doi) if doi else {}
        elif kind == "chemrxiv":
            provider, details = "OpenAlex", _openalex(canonical_url)
        elif kind == "web":
            provider, details = _fetch_web_metadata(canonical_url, fallback_title)
        else:
            provider, details = "", {}
        if details:
            for key in ("title", "authors", "published", "abstract", "provider_data"):
                if details.get(key):
                    result[key] = details[key]
            result["metadata_provider"] = provider
            result["metadata_status"] = "complete" if result["title"] and (result["abstract"] or result["provider_data"]) else "partial"
    except (requests.RequestException, ValueError, KeyError, TypeError, ET.ParseError) as error:
        result["metadata_status"] = "unavailable"
        result["metadata_error"] = str(error)[:300]
    return result


def _load_frontmatter(path):
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            return {}
        end = text.find("\n---", 4)
        if end < 0:
            return {}
        value = yaml.safe_load(text[4:end])
        return value if isinstance(value, dict) else {}
    except (OSError, yaml.YAMLError):
        return {}


def _timestamp_order(value):
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.timestamp()
    except (OverflowError, TypeError, ValueError):
        return float("-inf")


def _provider_updated_at(provider_data):
    if not isinstance(provider_data, dict):
        return ""
    for key in ("pushed_at", "last_activity_at", "last_modified", "updated", "updated_at"):
        value = provider_data.get(key)
        if value:
            return str(value)
    return ""


def load_registry(registry_path, notes_dir):
    try:
        registry = json.loads(Path(registry_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        registry = {"schema_version": 1, "sources": {}}
    registry.setdefault("schema_version", 1)
    registry.setdefault("sources", {})

    for note_path in sorted(Path(notes_dir).glob("*.md")):
        frontmatter = _load_frontmatter(note_path)
        source = frontmatter.get("canonical_url") or frontmatter.get("source")
        if not isinstance(source, str) or not source.startswith(("http://", "https://")):
            continue
        kind, canonical_url = canonicalize_url(source)
        record = registry["sources"].setdefault(canonical_url, {
            "type": frontmatter.get("type", kind),
            "canonical_url": canonical_url,
            "original_url": source,
            "title": frontmatter.get("title", ""),
            "notes": [],
        })
        note_added_at = frontmatter.get("captured_at") or frontmatter.get("date")
        if note_added_at:
            note_added_at = str(note_added_at)
            current_added_at = record.get("added_at", "")
            if not current_added_at or _timestamp_order(note_added_at) < _timestamp_order(current_added_at):
                record["added_at"] = note_added_at
        published_at = frontmatter.get("published")
        if published_at and not record.get("published_at"):
            record["published_at"] = str(published_at)
        updated_at = _provider_updated_at(frontmatter.get("provider_data"))
        current_updated_at = record.get("updated_at", "")
        if updated_at and (not current_updated_at or _timestamp_order(updated_at) > _timestamp_order(current_updated_at)):
            record["updated_at"] = updated_at
        try:
            note_name = note_path.resolve().relative_to(Path(notes_dir).resolve().parent).as_posix()
        except ValueError:
            note_name = note_path.as_posix()
        if note_name not in record.setdefault("notes", []):
            record["notes"].append(note_name)
    return registry


def save_registry(registry, registry_path):
    Path(registry_path).write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def register_source(registry, metadata, note_path, original_url, added_at=None):
    key = metadata["canonical_url"]
    provider_data = metadata.get("provider_data", {})
    registry["sources"][key] = {
        "type": metadata["type"],
        "canonical_url": key,
        "original_url": original_url,
        "title": metadata["title"],
        "notes": [str(note_path).replace("\\", "/")],
        "added_at": added_at or utc_timestamp(),
        "published_at": str(metadata.get("published") or ""),
        "updated_at": _provider_updated_at(provider_data),
    }


def write_note(path, metadata, original_url, author, captured_date, issue_number, captured_at=None):
    frontmatter = {
        "title": metadata["title"],
        "type": metadata["type"],
        "source": original_url,
        "canonical_url": metadata["canonical_url"],
        "captured_by": author,
        "date": captured_date,
        "captured_at": captured_at or utc_timestamp(),
        "issue": str(issue_number),
        "status": "to-read",
        "authors": metadata.get("authors", []),
        "published": metadata.get("published", ""),
        "abstract": metadata.get("abstract", ""),
        "metadata_provider": metadata.get("metadata_provider", ""),
        "metadata_status": metadata.get("metadata_status", "unavailable"),
        "provider_data": metadata.get("provider_data", {}),
    }
    if metadata.get("metadata_error"):
        frontmatter["metadata_error"] = metadata["metadata_error"]
    yaml_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False).rstrip()

    lines = [
        f"# {metadata['title']}",
        "",
        f"- **Type:** {metadata['type']}",
        f"- **Source:** {original_url}",
        f"- **Captured by:** @{author}",
        f"- **Metadata:** {metadata.get('metadata_status', 'unavailable')} ({metadata.get('metadata_provider') or 'no provider data'})",
    ]
    if metadata.get("authors"):
        lines.append(f"- **Authors:** {', '.join(metadata['authors'])}")
    if metadata.get("published"):
        lines.append(f"- **Published:** {metadata['published']}")
    if metadata.get("abstract"):
        lines.extend(["", "## Summary", metadata["abstract"]])
    provider_data = metadata.get("provider_data", {})
    if provider_data:
        lines.extend(["", "## Provider details"])
        for key, value in provider_data.items():
            if value not in (None, "", [], {}):
                rendered = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
                lines.append(f"- **{key.replace('_', ' ').title()}:** {rendered}")
    if not metadata.get("abstract") and not provider_data:
        lines.extend(["", "Metadata lookup did not return additional public information."])
    path.write_text(f"---\n{yaml_text}\n---\n\n" + "\n".join(lines) + "\n", encoding="utf-8")


def utc_date():
    return datetime.now(timezone.utc).date().isoformat()


def utc_timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
