import re
import calendar
from datetime import datetime, timedelta, timezone

CONFIG_VERSION = 1
PROVIDERS = {
    "arxiv",
    "crossref",
    "chemrxiv",
    "github",
    "gitlab",
    "huggingface_model",
    "huggingface_dataset",
    "huggingface_space",
}
INTERVALS = {"twice_daily", "daily", "weekly", "monthly"}
PROFILE_ID = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
MLIP_COMMON_QUERIES = [
    "machine-learned interatomic potential",
    "machine learning interatomic potential MLIP",
    "MACE NequIP Allegro ACE GAP MTP SNAP CHGNet M3GNet SevenNet MatterSim",
    "equivariant neural network atomistic interatomic potential",
    "foundation model universal interatomic potential materials",
    "active learning on-the-fly learning atomistic simulation",
    "long-range electrostatics charge equilibration reactive potential",
    "heterogeneous catalysis surfaces interfaces defects materials modelling",
]
MLIP_ARXIV_QUERIES = [
    'all:"machine-learned interatomic potential" OR all:"machine learning interatomic potential" OR all:MLIP',
    "all:MACE OR all:NequIP OR all:Allegro OR all:ACE OR all:GAP OR all:MTP OR all:SNAP OR all:CHGNet OR all:M3GNet OR all:SevenNet OR all:MatterSim",
    'all:"equivariant neural network" AND (all:interatomic OR all:atomistic)',
    'all:"foundation model" AND (all:materials OR all:atomistic) AND (all:potential OR all:simulation)',
    'all:"active learning" AND (all:"interatomic potential" OR all:"atomistic simulation")',
    'all:"on-the-fly learning" AND (all:atomistic OR all:materials)',
    'all:"long-range electrostatics" AND (all:interatomic OR all:potential)',
    'all:"heterogeneous catalysis" AND (all:atomistic OR all:MLIP OR all:"machine learning potential")',
]


def default_profiles():
    profiles = [
        {
            "id": "arxiv-mlips",
            "name": "ML interatomic potentials",
            "provider": "arxiv",
            "enabled": True,
            "queries": ['all:"machine-learned interatomic potential" OR all:MLIP'],
            "max_results": 20,
            "interval": "daily",
        },
        {
            "id": "arxiv-ml-atomistic",
            "name": "ML for atomistic materials modelling",
            "provider": "arxiv",
            "enabled": True,
            "queries": ['cat:cond-mat.mtrl-sci AND (all:"machine learning" OR all:"machine learning potential")'],
            "max_results": 20,
            "interval": "daily",
        },
        {
            "id": "arxiv-atomic-scale",
            "name": "Atomic-scale modelling technology",
            "provider": "arxiv",
            "enabled": True,
            "queries": ['cat:cond-mat.mtrl-sci AND (all:"atomic scale modeling" OR all:"atomistic modeling")'],
            "max_results": 20,
            "interval": "daily",
        },
        {
            "id": "arxiv-heterogeneous-catalysis",
            "name": "Heterogeneous catalysis and atomistic ML",
            "provider": "arxiv",
            "enabled": True,
            "queries": ['all:"heterogeneous catalysis" AND (all:atomistic OR all:"machine learning")'],
            "max_results": 20,
            "interval": "daily",
        },
        {
            "id": "crossref-materials-ml",
            "name": "Materials science and ML papers",
            "provider": "crossref",
            "enabled": False,
            "queries": ["machine learning materials science", "interatomic potentials"],
            "max_results": 20,
            "interval": "weekly",
        },
        {
            "id": "chemrxiv-materials",
            "name": "ChemRxiv materials research",
            "provider": "chemrxiv",
            "enabled": False,
            "queries": ["materials science machine learning", "catalysis atomistic"],
            "max_results": 20,
            "interval": "weekly",
        },
        {
            "id": "github-materials-tools",
            "name": "Materials modelling repositories",
            "provider": "github",
            "enabled": False,
            "queries": ["atomistic materials machine learning", "interatomic potentials"],
            "max_results": 10,
            "interval": "weekly",
        },
        {
            "id": "gitlab-materials-tools",
            "name": "Materials modelling GitLab projects",
            "provider": "gitlab",
            "enabled": False,
            "queries": ["atomistic materials machine learning", "interatomic potentials"],
            "max_results": 10,
            "interval": "weekly",
        },
        {
            "id": "hf-materials-models",
            "name": "Materials-science Hugging Face models",
            "provider": "huggingface_model",
            "enabled": False,
            "queries": ["materials science atomistic", "interatomic potential"],
            "max_results": 10,
            "interval": "weekly",
        },
        {
            "id": "hf-materials-datasets",
            "name": "Materials-science Hugging Face datasets",
            "provider": "huggingface_dataset",
            "enabled": False,
            "queries": ["materials science atomistic", "molecular dynamics"],
            "max_results": 10,
            "interval": "weekly",
        },
        {
            "id": "hf-materials-spaces",
            "name": "Materials-science Hugging Face Spaces",
            "provider": "huggingface_space",
            "enabled": False,
            "queries": ["materials science", "molecular dynamics"],
            "max_results": 10,
            "interval": "weekly",
        },
    ]
    template_ids = {
        "crossref-materials-ml", "chemrxiv-materials", "github-materials-tools",
        "gitlab-materials-tools", "hf-materials-models", "hf-materials-datasets", "hf-materials-spaces",
    }
    profiles = [profile for profile in profiles if profile["id"] not in template_ids]
    profiles.extend(mlip_development_profiles())
    return profiles


def mlip_development_profiles():
    providers = [
        ("arxiv", "mlip-development-arxiv"),
        ("crossref", "mlip-development-crossref"),
        ("chemrxiv", "mlip-development-chemrxiv"),
        ("github", "mlip-development-github"),
        ("gitlab", "mlip-development-gitlab"),
        ("huggingface_model", "mlip-development-hf-model"),
        ("huggingface_dataset", "mlip-development-hf-dataset"),
        ("huggingface_space", "mlip-development-hf-space"),
    ]
    return [
        {
            "id": profile_id,
            "name": "MLIP developments scan",
            "provider": provider,
            "enabled": True,
            "queries": MLIP_ARXIV_QUERIES if provider == "arxiv" else MLIP_COMMON_QUERIES,
            "max_results": 20,
            "lookback_hours": 24,
            "interval": "twice_daily",
        }
        for provider, profile_id in providers
    ]


def migrate_config(config):
    if isinstance(config, dict) and config.get("version") == CONFIG_VERSION and isinstance(config.get("profiles"), list):
        return validate_config(config)

    profiles = default_profiles()
    legacy_queries = config.get("queries", []) if isinstance(config, dict) else []
    for index, query in enumerate(legacy_queries, start=1):
        profiles.append({
            "id": f"arxiv-legacy-{index}",
            "name": f"Existing arXiv query {index}",
            "provider": "arxiv",
            "enabled": True,
            "queries": [query],
            "max_results": 10,
            "interval": "daily",
        })
    return validate_config({"version": CONFIG_VERSION, "profiles": profiles})


def validate_config(config):
    if not isinstance(config, dict) or config.get("version") != CONFIG_VERSION:
        raise ValueError("Unsupported scan settings version")
    profiles = config.get("profiles")
    if not isinstance(profiles, list) or len(profiles) > 50:
        raise ValueError("Profiles must be a list with at most 50 entries")

    seen_ids = set()
    normalized = []
    for profile in profiles:
        if not isinstance(profile, dict):
            raise ValueError("Each profile must be an object")
        profile_id = profile.get("id")
        if not isinstance(profile_id, str) or not PROFILE_ID.fullmatch(profile_id) or profile_id in seen_ids:
            raise ValueError(f"Invalid or duplicate profile id: {profile_id!r}")
        seen_ids.add(profile_id)
        provider = profile.get("provider")
        if provider not in PROVIDERS:
            raise ValueError(f"Unsupported provider in profile {profile_id}")
        if not isinstance(profile.get("name"), str) or not profile["name"].strip() or len(profile["name"]) > 100:
            raise ValueError(f"Invalid name in profile {profile_id}")
        if not isinstance(profile.get("enabled"), bool):
            raise ValueError(f"Enabled must be boolean in profile {profile_id}")
        queries = profile.get("queries")
        if not isinstance(queries, list) or not 1 <= len(queries) <= 20:
            raise ValueError(f"Profile {profile_id} must have 1 to 20 queries")
        if any(not isinstance(query, str) or not query.strip() or len(query) > 500 for query in queries):
            raise ValueError(f"Invalid query in profile {profile_id}")
        limit = profile.get("max_results")
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100:
            raise ValueError(f"max_results must be from 1 to 100 in profile {profile_id}")
        lookback_hours = profile.get("lookback_hours", 24)
        if isinstance(lookback_hours, bool) or not isinstance(lookback_hours, int) or not 1 <= lookback_hours <= 720:
            raise ValueError(f"lookback_hours must be from 1 to 720 in profile {profile_id}")
        interval = profile.get("interval")
        if interval not in INTERVALS:
            raise ValueError(f"Unsupported interval in profile {profile_id}")
        normalized.append({
            "id": profile_id,
            "name": profile["name"].strip(),
            "provider": provider,
            "enabled": profile["enabled"],
            "queries": [query.strip() for query in queries],
            "max_results": limit,
            "lookback_hours": lookback_hours,
            "interval": interval,
        })
    return {"version": CONFIG_VERSION, "profiles": normalized}


def is_due(profile, last_successful_at, now=None):
    if not last_successful_at:
        return True
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    previous = datetime.fromisoformat(last_successful_at.replace("Z", "+00:00"))
    if previous.tzinfo is None:
        previous = previous.replace(tzinfo=timezone.utc)
    interval = profile["interval"]
    if interval == "twice_daily":
        previous = previous.astimezone(timezone.utc)
        now = now.astimezone(timezone.utc)

        def slot(moment):
            if moment.hour >= 17:
                return moment.replace(hour=17, minute=0, second=0, microsecond=0)
            if moment.hour >= 5:
                return moment.replace(hour=5, minute=0, second=0, microsecond=0)
            prior_day = moment.date() - timedelta(days=1)
            return datetime(prior_day.year, prior_day.month, prior_day.day, 17, tzinfo=timezone.utc)

        return slot(now) > slot(previous)
    if interval == "daily":
        return now >= previous + timedelta(days=1)
    if interval == "weekly":
        return now >= previous + timedelta(days=7)
    year = previous.year + (1 if previous.month == 12 else 0)
    month = 1 if previous.month == 12 else previous.month + 1
    day = min(previous.day, calendar.monthrange(year, month)[1])
    next_month = previous.replace(year=year, month=month, day=day)
    return now >= next_month
