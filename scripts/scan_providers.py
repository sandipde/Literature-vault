import math
import os
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import requests

from scripts import literature

ATOM = "http://www.w3.org/2005/Atom"
USER_AGENT = "LiteratureVault/1.0 (public metadata scan)"

# Minimum seconds between requests to the same host. arXiv's API terms ask for at
# most one request every three seconds; Crossref's shared pool throttles bursts.
MIN_REQUEST_INTERVAL = {"export.arxiv.org": 3.0, "api.crossref.org": 1.0, "api.github.com": 2.0}
RETRY_STATUSES = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 3
MAX_WAIT_SECONDS = 60
_last_request_at = {}


def _throttle(url):
    host = urllib.parse.urlsplit(url).netloc
    gap = MIN_REQUEST_INTERVAL.get(host, 0)
    wait = _last_request_at.get(host, float("-inf")) + gap - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_request_at[host] = time.monotonic()


def _is_rate_limited(response):
    if response.status_code in RETRY_STATUSES:
        return True
    # GitHub reports an exhausted search quota as 403 with no remaining requests.
    return response.status_code == 403 and (
        response.headers.get("Retry-After") or response.headers.get("X-RateLimit-Remaining") == "0"
    )


def _retry_delay(response, attempt):
    try:
        delay = float(response.headers.get("Retry-After", ""))
    except ValueError:
        delay = 5.0 * 2 ** (attempt - 1)
    return max(1.0, min(delay, MAX_WAIT_SECONDS))


def _request(url, params, headers):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        _throttle(url)
        try:
            response = requests.get(url, params=params, timeout=30, headers=headers)
        except (requests.ConnectionError, requests.Timeout):
            if attempt == MAX_ATTEMPTS:
                raise
            time.sleep(5.0 * 2 ** (attempt - 1))
            continue
        if attempt < MAX_ATTEMPTS and _is_rate_limited(response):
            time.sleep(_retry_delay(response, attempt))
            continue
        response.raise_for_status()
        return response


def _auth_headers(url):
    # An optional token raises GitHub's search limit from 10 to 30 requests a minute.
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and urllib.parse.urlsplit(url).netloc == "api.github.com":
        return {"Authorization": f"Bearer {token}"}
    return {}


def _get_json(url, params):
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json", **_auth_headers(url)}
    return _request(url, params, headers).json()


def _get_text(url, params):
    return _request(url, params, {"User-Agent": USER_AGENT}).text


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


# Crossref keeps a hit when roughly one in five query words appears anywhere in the
# record, then ranks those hits. Common words such as "potential" or "learning"
# therefore outrank an actual subject match inside a one-day window.
_GENERIC_CROSSREF_WORDS = {
    "a", "an", "and", "or", "the", "of", "for", "with", "from", "in", "on", "to",
    "machine", "learn", "potential", "model", "material", "simulation", "network",
    "neural", "active", "universal", "foundation", "energy", "charge", "surface",
    "interface", "defect", "method", "using", "based", "long", "range", "molecular",
    "atomic",
}
_AMBIGUOUS_MODEL_NAMES = {"ace", "gap", "mtp", "snap"}


def _normalize_crossref_word(word):
    word = word.lower()
    if word.startswith("learn"):
        return "learn"
    if word in {"modelling", "modeling", "model", "models"}:
        return "model"
    if word in {"material", "materials"}:
        return "material"
    if word in {"simulation", "simulations"}:
        return "simulation"
    if word in {"potential", "potentials"}:
        return "potential"
    if word in {"network", "networks"}:
        return "network"
    if word in {"surface", "surfaces"}:
        return "surface"
    if word in {"interface", "interfaces"}:
        return "interface"
    if word in {"defect", "defects"}:
        return "defect"
    if word in {"method", "methods"}:
        return "method"
    return word


def _crossref_words(text):
    return {_normalize_crossref_word(word) for word in re.findall(r"[A-Za-z0-9]+", text or "")}


def _query_tokens(query):
    return re.findall(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", query or "")


def _is_distinctive_model_name(token):
    key = re.sub(r"[^A-Za-z0-9]", "", token or "").lower()
    if len(key) < 4 or key in _AMBIGUOUS_MODEL_NAMES:
        return False
    return any(character.isupper() for character in token) or any(character.isdigit() for character in token)


def _is_alternative_name_list(query):
    tokens = _query_tokens(query)
    if len(tokens) < 4:
        return False
    cased = sum(1 for token in tokens if any(character.isupper() for character in token))
    return cased * 2 >= len(tokens)


def _distinctive_model_names(query):
    names = []
    for token in _query_tokens(query):
        if _is_distinctive_model_name(token) and token not in names:
            names.append(token)
    return names


def _crossref_matches_query(query, title, abstract="", subjects=None):
    tokens = _query_tokens(query)
    if not tokens:
        return False
    haystack = _crossref_words(" ".join([title or "", abstract or "", " ".join(subjects or [])]))
    required_names = [token for token in tokens if _is_distinctive_model_name(token)]
    if required_names and not all(_normalize_crossref_word(token) in haystack for token in required_names):
        return False
    cased = sum(1 for token in tokens if any(character.isupper() for character in token))
    # Model-family queries are alternative names ("MACE NequIP ..."), not phrases.
    if len(tokens) >= 4 and cased * 2 >= len(tokens):
        for token in tokens:
            key = re.sub(r"[^A-Za-z0-9]", "", token).lower()
            if len(key) < 4 or key in _AMBIGUOUS_MODEL_NAMES:
                continue
            if _normalize_crossref_word(key) in haystack:
                return True
        return False

    matched = []
    specific = []
    for token in tokens:
        parts = [_normalize_crossref_word(part) for part in re.findall(r"[A-Za-z0-9]+", token)]
        if parts and all(part in haystack for part in parts):
            matched.append(token)
        if any(part not in _GENERIC_CROSSREF_WORDS for part in parts):
            specific.append(token)
    if specific and not any(token in matched for token in specific):
        return False
    needed = 1 if len(tokens) == 1 else max(2, math.ceil(len(tokens) * 0.5))
    return len(matched) >= needed


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
        # arXiv reports query errors as a feed entry whose id is an /api/errors URL.
        if "/abs/" not in raw_url:
            continue
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
        # Ask for more than the profile keeps. The highest-scored rows are often
        # partial word matches, and the relevant record may sit further down.
        "rows": min(30, max(profile["max_results"], 15)),
        "filter": f"from-created-date:{profile['_cutoff'].date().isoformat()}",
    }
    if profile["provider"] == "chemrxiv":
        params["filter"] = f"prefix:10.26434,{params['filter']}"
    mailto = os.environ.get("CROSSREF_MAILTO", "").strip()
    if mailto:
        params["mailto"] = mailto  # Crossref's "polite pool" has much more generous rate limits.
    data = _get_json("https://api.crossref.org/works", params).get("message", {}).get("items", [])
    results = []
    for item in data:
        doi = item.get("DOI", "")
        if not doi:
            continue
        source_url = item.get("URL") or f"https://doi.org/{doi}"
        title = (item.get("title") or [""])[0]
        abstract = literature._plain_text(item.get("abstract", "") or "")
        subjects = [subject for subject in item.get("subject", []) if isinstance(subject, str)]
        if not _crossref_matches_query(query, title, abstract, subjects):
            continue
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
            title,
            abstract,
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


_PROVIDER_SYNTAX = re.compile(r"\b(?:AND|OR|ANDNOT)\b|(?:^|\s)(?:all|cat|ti|abs|au):")
_BROAD_MODEL_NAMES = {"mace", "allegro"}
_DOMAIN_WORDS = {"interatomic", "atomistic", "potential", "mlip", "material", "molecular", "chemistry", "catalyst", "catalysis"}
_FOCUSED_PHRASE_WORDS = {"learning", "model", "models", "materials", "material", "simulation", "potential", "potentials", "network", "networks", "using", "based"}


def _uses_provider_syntax(query):
    return bool(_PROVIDER_SYNTAX.search(query or ""))


def _unique(items):
    seen = []
    for item in items:
        if item and item not in seen:
            seen.append(item)
    return seen


def plan_searches(provider, query):
    """Turn one stored query into the searches that provider can actually run.

    arXiv queries already use boolean syntax and are sent through unchanged.
    A list of model names is OR on GitHub, one name per request on GitLab and
    Hugging Face, and one "<name> interatomic potential" query on Crossref.
    A plain phrase is quoted or reduced to its distinctive words instead of
    requiring every word to occur together.
    """
    text = (query or "").strip()
    if not text:
        return []
    if provider == "arxiv" or _uses_provider_syntax(text):
        return [text]
    if _is_alternative_name_list(text):
        names = _distinctive_model_names(text)
        if not names:
            return [text]
        if provider == "github":
            qualifier = "(interatomic OR atomistic OR MLIP OR potential)"
            groups = []
            for start in range(0, len(names), 4):
                alternatives = " OR ".join(names[start:start + 4])
                groups.append(f"({alternatives}) {qualifier}")
            return groups
        if provider in {"gitlab", "huggingface_model", "huggingface_dataset", "huggingface_space"}:
            return names
        if provider in {"crossref", "chemrxiv"}:
            return [f"{name} interatomic potential" for name in names]
        return names
    if provider == "github":
        return [_github_phrase(text)]
    if provider in {"gitlab", "huggingface_model", "huggingface_dataset", "huggingface_space"}:
        return _focused_terms(text) or [text]
    return [text]


def _github_phrase(query):
    hyphenated = [f'"{term}"' for term in re.findall(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+", query)]
    pieces = list(hyphenated)
    lowered = query.lower()
    if "interatomic" in lowered and "potential" in lowered:
        pieces.append('"interatomic potential"')
    if re.search(r"\bMLIP\b", query):
        pieces.append("MLIP")
    pieces = _unique(pieces)
    if not pieces:
        words = _query_tokens(query)
        if len(words) <= 4:
            return f'"{query.strip()}"'
        return f'"{" ".join(words[:3])}"'
    extras = [
        token for token in _query_tokens(query)
        if token.lower() not in _FOCUSED_PHRASE_WORDS
        and token.lower() not in {"interatomic", "potential", "mlip", "machine", "active"}
        and "-" not in token
    ]
    if len(_query_tokens(query)) > 4 and extras:
        return f'({" OR ".join(pieces)}) {extras[0]}'
    return " OR ".join(pieces)


def _focused_terms(query):
    hyphenated = re.findall(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+", query)
    if hyphenated:
        terms = list(hyphenated[:1])
        if re.search(r"\binteratomic\b", query, re.IGNORECASE):
            terms.append("interatomic")
        return _unique(terms)
    for token in _query_tokens(query):
        if token.lower() in {"mlip", "interatomic", "equivariant", "chemrxiv"}:
            return [token]
    content = [token for token in _query_tokens(query) if token.lower() not in _FOCUSED_PHRASE_WORDS and len(token) >= 5]
    return content[:1]


def _item_words(item):
    provider_data = item.get("provider_data") or {}
    topics = provider_data.get("topics") or []
    tags = provider_data.get("tags") or []
    description = provider_data.get("description") or ""
    return _crossref_words(" ".join([
        item.get("title") or "",
        item.get("abstract") or "",
        description,
        " ".join(topic for topic in topics if isinstance(topic, str)),
        " ".join(tag for tag in tags if isinstance(tag, str)),
    ]))


def _planned_hit_is_relevant(planned_query, item):
    tokens = _query_tokens(planned_query)
    if len(tokens) != 1 or not _is_distinctive_model_name(tokens[0]):
        return True
    words = _item_words(item)
    if _normalize_crossref_word(tokens[0]) not in words:
        return False
    if tokens[0].lower() in _BROAD_MODEL_NAMES and not (words & _DOMAIN_WORDS):
        return False
    return True


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
        planned = plan_searches(profile["provider"], query)
        if not planned:
            continue
        share = max(1, math.ceil(per_query_limit / len(planned)))
        for planned_query in planned:
            # A name search can put an unrelated partial match first. Ask for a
            # few extra rows and keep only hits that actually contain the name.
            fetch_limit = share * 5 if len(_query_tokens(planned_query)) == 1 else share
            narrowed = {**query_profile, "max_results": fetch_limit}
            accepted = 0
            for item in searcher(narrowed, planned_query):
                if not _planned_hit_is_relevant(planned_query, item):
                    continue
                observed_at = _parse_timestamp(item.get("_observed_at"))
                if observed_at is None or observed_at < cutoff or observed_at > now:
                    continue
                canonical_url = item["canonical_url"]
                if canonical_url not in found:
                    found.add(canonical_url)
                    results.append(item)
                    accepted += 1
                if accepted >= share or len(results) >= profile["max_results"]:
                    break
            if len(results) >= profile["max_results"]:
                return results
    return results
