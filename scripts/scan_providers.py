import math
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import requests

from scripts import literature

ATOM = "http://www.w3.org/2005/Atom"
USER_AGENT = "LiteratureVault/1.0 (public metadata scan)"


def _get_json(url, params):
    response = requests.get(url, params=params, timeout=30, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    response.raise_for_status()
    return response.json()


def _get_text(url, params):
    response = requests.get(url, params=params, timeout=30, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    return response.text


def _parse_timestamp(value):
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _crossref_created_at(item):
    created = item.get("created") or {}
    timestamp = created.get("date-time")
    if timestamp:
        return timestamp
    milliseconds = created.get("timestamp")
    if milliseconds:
        return datetime.fromtimestamp(milliseconds / 1000, timezone.utc).isoformat()
    return ""


def _metadata(profile, source_url, title, abstract="", authors=None, published="", provider_data=None, metadata_provider=None, observed_at=""):
    detected_type, canonical_url = literature.canonicalize_url(source_url)
    doi_path = urllib.parse.urlsplit(canonical_url).path.lower()
    if detected_type == "paper" and (profile["provider"] == "chemrxiv" or doi_path.startswith("/10.26434/")):
        detected_type = "chemrxiv"
    return {
        "type": detected_type,
        "canonical_url": canonical_url,
        "title": " ".join((title or source_url).split()),
        "authors": authors or [],
        "published": published or "",
        "abstract": literature._plain_text(abstract or ""),
        "metadata_provider": metadata_provider or profile["provider"],
        "metadata_status": "complete" if title else "partial",
        "provider_data": provider_data or {},
        "source_url": source_url,
        "_observed_at": observed_at,
    }


def _arxiv(profile, query):
    cutoff = profile["_cutoff"]
    now = profile["_now"]
    date_range = f"submittedDate:[{cutoff.strftime('%Y%m%d%H%M')} TO {now.strftime('%Y%m%d%H%M')}]"
    content = _get_text(
        "https://export.arxiv.org/api/query",
        {"search_query": f"({query}) AND {date_range}", "sortBy": "submittedDate", "sortOrder": "descending", "max_results": profile["max_results"]},
    )
    root = ET.fromstring(content)
    results = []
    for entry in root.findall(f"{{{ATOM}}}entry"):
        raw_url = (entry.findtext(f"{{{ATOM}}}id") or "").strip()
        arxiv_id = raw_url.split("/abs/")[-1].split("v")[0]
        if not arxiv_id:
            continue
        source_url = f"https://arxiv.org/abs/{arxiv_id}"
        authors = [(item.findtext(f"{{{ATOM}}}name") or "").strip() for item in entry.findall(f"{{{ATOM}}}author")]
        categories = [item.get("term", "") for item in entry.findall(f"{{{ATOM}}}category")]
        published_at = (entry.findtext(f"{{{ATOM}}}published", default="") or "").strip()
        metadata = _metadata(
            profile,
            source_url,
            entry.findtext(f"{{{ATOM}}}title", default=""),
            entry.findtext(f"{{{ATOM}}}summary", default=""),
            authors,
            published_at[:10],
            {"arxiv_id": arxiv_id, "categories": categories},
            "arXiv",
            published_at,
        )
        results.append(metadata)
    return results


def _crossref(profile, query):
    params = {
        "query": query,
        "rows": profile["max_results"],
        "filter": f"from-created-date:{profile['_cutoff'].date().isoformat()}",
    }
    if profile["provider"] == "chemrxiv":
        params["filter"] = f"prefix:10.26434,{params['filter']}"
    data = _get_json("https://api.crossref.org/works", params).get("message", {}).get("items", [])
    results = []
    for item in data:
        doi = item.get("DOI", "")
        if not doi:
            continue
        source_url = item.get("URL") or f"https://doi.org/{doi}"
        author_names = [
            " ".join(part for part in (author.get("given"), author.get("family")) if part)
            for author in item.get("author", [])
        ]
        published = literature._date_parts(item.get("published-print") or item.get("published-online") or item.get("created"))
        provider_data = {
            "doi": doi,
            "journal": (item.get("container-title") or [""])[0],
            "publisher": item.get("publisher", ""),
            "type": item.get("type", ""),
            "subjects": item.get("subject", []),
        }
        results.append(_metadata(
            profile,
            source_url,
            (item.get("title") or [""])[0],
            item.get("abstract", ""),
            author_names,
            published,
            provider_data,
            "Crossref",
            _crossref_created_at(item),
        ))
    return results


def _github(profile, query):
    pushed_after = profile["_cutoff"].strftime("%Y-%m-%dT%H:%M:%SZ")
    data = _get_json(
        "https://api.github.com/search/repositories",
        {"q": f"{query} pushed:>={pushed_after}", "sort": "updated", "order": "desc", "per_page": profile["max_results"]},
    )
    results = []
    for item in data.get("items", []):
        source_url = item.get("html_url", "")
        if not source_url:
            continue
        provider_data = {
            "description": item.get("description", ""),
            "language": item.get("language", ""),
            "topics": item.get("topics", []),
            "license": (item.get("license") or {}).get("spdx_id", ""),
            "stars": item.get("stargazers_count"),
            "forks": item.get("forks_count"),
            "open_issues": item.get("open_issues_count"),
            "pushed_at": item.get("pushed_at", ""),
        }
        results.append(_metadata(profile, source_url, item.get("full_name", ""), item.get("description", ""), provider_data=provider_data, metadata_provider="GitHub", observed_at=item.get("pushed_at", "")))
    return results


def _gitlab(profile, query):
    last_activity_after = profile["_cutoff"].isoformat().replace("+00:00", "Z")
    data = _get_json(
        "https://gitlab.com/api/v4/projects",
        {"search": query, "order_by": "last_activity_at", "sort": "desc", "per_page": profile["max_results"], "last_activity_after": last_activity_after},
    )
    results = []
    for item in data:
        source_url = item.get("web_url", "")
        if not source_url:
            continue
        provider_data = {
            "description": item.get("description", ""),
            "topics": item.get("topics", []),
            "license": (item.get("license") or {}).get("key", ""),
            "stars": item.get("star_count"),
            "forks": item.get("forks_count"),
            "visibility": item.get("visibility", ""),
            "last_activity_at": item.get("last_activity_at", ""),
        }
        results.append(_metadata(profile, source_url, item.get("path_with_namespace", ""), item.get("description", ""), provider_data=provider_data, metadata_provider="GitLab", observed_at=item.get("last_activity_at", "")))
    return results


def _huggingface(profile, query):
    endpoint = profile["provider"].removeprefix("huggingface_")
    kind = {"model": "models", "dataset": "datasets", "space": "spaces"}[endpoint]
    data = _get_json(
        f"https://huggingface.co/api/{kind}",
        {"search": query, "limit": profile["max_results"], "full": "true", "sort": "lastModified", "direction": "-1"},
    )
    results = []
    for item in data:
        source_url = f"https://huggingface.co/{kind}/{item['id']}" if kind != "models" else f"https://huggingface.co/{item['id']}"
        card = item.get("cardData") or {}
        provider_data = {
            "task": item.get("pipeline_tag", ""),
            "sdk": item.get("sdk", ""),
            "tags": item.get("tags", []),
            "license": card.get("license", ""),
            "downloads": item.get("downloads"),
            "likes": item.get("likes"),
            "last_modified": item.get("lastModified", ""),
        }
        results.append(_metadata(profile, source_url, item.get("id", ""), card.get("description", ""), provider_data=provider_data, metadata_provider="Hugging Face", observed_at=item.get("lastModified", "")))
    return results


SEARCHERS = {
    "arxiv": _arxiv,
    "crossref": _crossref,
    "chemrxiv": _crossref,
    "github": _github,
    "gitlab": _gitlab,
    "huggingface_model": _huggingface,
    "huggingface_dataset": _huggingface,
    "huggingface_space": _huggingface,
}


def search_profile(profile, now=None):
    searcher = SEARCHERS[profile["provider"]]
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now = now.astimezone(timezone.utc)
    cutoff = now - timedelta(hours=profile.get("lookback_hours", 24))
    results = []
    found = set()
    per_query_limit = max(1, math.ceil(profile["max_results"] / len(profile["queries"])))
    query_profile = {**profile, "max_results": per_query_limit, "_cutoff": cutoff, "_now": now}
    for query in profile["queries"]:
        for item in searcher(query_profile, query)[:per_query_limit]:
            observed_at = _parse_timestamp(item.get("_observed_at"))
            if observed_at is None or observed_at < cutoff or observed_at > now:
                continue
            canonical_url = item["canonical_url"]
            if canonical_url not in found:
                found.add(canonical_url)
                results.append(item)
            if len(results) >= profile["max_results"]:
                return results
    return results
