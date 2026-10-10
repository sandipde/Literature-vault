import json
import os
import re
from pathlib import Path

from scripts.scan_config import validate_config

MARKER = "<!-- literature-vault:scan-settings:v1 -->"
JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
ALLOWED_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}
CONFIG_FILE = Path("monitor_config.json")


def parse_settings_request(body):
    if not isinstance(body, str) or MARKER not in body:
        raise ValueError("Missing scan-settings request marker")
    match = JSON_BLOCK.search(body.split(MARKER, 1)[1])
    if not match:
        raise ValueError("Missing JSON settings block")
    try:
        raw = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        raise ValueError("Settings payload is not valid JSON") from error
    serialized = json.dumps(raw, ensure_ascii=False, separators=(",", ":"))
    if len(serialized) > 50000:
        raise ValueError("Settings payload exceeds 50 KB")
    return validate_config(raw)


def apply_settings_request(body, author_association, config_path=CONFIG_FILE):
    if author_association not in ALLOWED_ASSOCIATIONS:
        return {"result": "rejected", "message": "Rejected: only repository owners, members, and collaborators can update scan settings."}
    try:
        config = parse_settings_request(body)
    except ValueError as error:
        return {"result": "rejected", "message": f"Rejected: {error}."}
    path = Path(config_path)
    path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"result": "applied", "message": f"Applied {len(config['profiles'])} validated scan profiles."}


def main():
    result = apply_settings_request(
        os.environ.get("ISSUE_BODY", ""),
        os.environ.get("ISSUE_AUTHOR_ASSOCIATION", "NONE"),
    )
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as output:
            output.write(f"result={result['result']}\n")
            output.write(f"message={result['message']}\n")
    print(f"{result['result']}: {result['message']}")
    return result


if __name__ == "__main__":
    main()
