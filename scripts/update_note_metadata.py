"""Apply a personal-metadata request (rating, priority, status, tags, comments) to a note.

The capture page cannot write repository files directly: its token only has Issues write
access. It submits a marked Issue instead, and this script, run by Actions, validates the
request and edits the note.
"""
import json
import os
import re
from pathlib import Path

import yaml

MARKER = "<!-- literature-vault:note-metadata:v1 -->"
JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
ALLOWED_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}

NOTE_PATH = re.compile(r"^notes/[A-Za-z0-9][A-Za-z0-9._-]*\.md$")
PRIORITIES = ("low", "normal", "high", "urgent")
STATUSES = ("to-read", "reading", "read", "archived")
USER_FIELDS = ("user_rating", "user_priority", "user_status", "user_tags", "user_comments")

MAX_PAYLOAD_CHARS = 20000
MAX_TAGS = 20
MAX_TAG_CHARS = 40
MAX_COMMENT_CHARS = 5000

# Control characters (tab and newline are allowed in comments only) and C1 controls.
UNSAFE_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
TOP_LEVEL_KEY = re.compile(r"^([A-Za-z_][\w.-]*):(?:\s|$)")
PERSONAL_SECTION = re.compile(r"^## Personal notes[ \t]*\r?\n.*?(?=^## |\Z)", re.DOTALL | re.MULTILINE)


class RequestError(ValueError):
    """A request that must be rejected; the message is safe to show to the requester."""


def _reject_unsafe(value, label, multiline=False):
    # Tags are single-line; comments may contain newlines and tabs.
    if UNSAFE_CHARS.search(value) or (not multiline and re.search(r"[\t\n\r]", value)):
        raise RequestError(f"{label} contains unsupported control characters")


def parse_request(body):
    if not isinstance(body, str) or MARKER not in body:
        raise RequestError("Missing note-metadata request marker")
    match = JSON_BLOCK.search(body.split(MARKER, 1)[1])
    if not match:
        raise RequestError("Missing JSON metadata block")
    if len(match.group(1)) > MAX_PAYLOAD_CHARS:
        raise RequestError("Metadata payload exceeds 20 KB")
    try:
        raw = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        raise RequestError("Metadata payload is not valid JSON") from error
    if not isinstance(raw, dict) or raw.get("version") != 1:
        raise RequestError("Unsupported metadata payload version")

    note = raw.get("note")
    if not isinstance(note, str) or not NOTE_PATH.match(note):
        raise RequestError("Note path must look like notes/<file>.md")

    rating = raw.get("rating", 0)
    if isinstance(rating, bool) or not isinstance(rating, int) or not 0 <= rating <= 5:
        raise RequestError("Rating must be a whole number from 0 to 5")

    priority = raw.get("priority", "normal")
    if priority not in PRIORITIES:
        raise RequestError(f"Priority must be one of: {', '.join(PRIORITIES)}")
    status = raw.get("status", "to-read")
    if status not in STATUSES:
        raise RequestError(f"Status must be one of: {', '.join(STATUSES)}")

    raw_tags = raw.get("tags", [])
    if not isinstance(raw_tags, list) or not all(isinstance(tag, str) for tag in raw_tags):
        raise RequestError("Tags must be a list of text values")
    tags = []
    for tag in raw_tags:
        tag = tag.strip()
        if not tag or tag in tags:
            continue
        if len(tag) > MAX_TAG_CHARS:
            raise RequestError(f"Each tag must be at most {MAX_TAG_CHARS} characters")
        _reject_unsafe(tag, "Tags")
        tags.append(tag)
    if len(tags) > MAX_TAGS:
        raise RequestError(f"At most {MAX_TAGS} tags are allowed")

    comments = raw.get("comments", "")
    if not isinstance(comments, str):
        raise RequestError("Comments must be text")
    comments = comments.replace("\r\n", "\n").replace("\r", "\n").strip()
    if len(comments) > MAX_COMMENT_CHARS:
        raise RequestError(f"Comments must be at most {MAX_COMMENT_CHARS} characters")
    _reject_unsafe(comments, "Comments", multiline=True)

    return {"note": note, "rating": rating, "priority": priority, "status": status, "tags": tags, "comments": comments}


def _yaml_json(value):
    # JSON is valid YAML. Escape the Unicode line separators YAML would otherwise fold.
    text = json.dumps(value, ensure_ascii=False)
    return text.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def _user_field_lines(meta):
    return [
        f"user_rating: {meta['rating']}",
        f"user_priority: {meta['priority']}",
        f"user_status: {meta['status']}",
        f"user_tags: {_yaml_json(meta['tags'])}",
        f"user_comments: {_yaml_json(meta['comments'])}",
    ]


def _strip_user_fields(frontmatter):
    kept = []
    skipping = False
    for line in frontmatter.split("\n"):
        key = TOP_LEVEL_KEY.match(line)
        if key:
            skipping = key.group(1) in USER_FIELDS
            if skipping:
                continue
        elif skipping and (not line.strip() or line[0] in " \t-"):
            continue
        else:
            skipping = False
        kept.append(line)
    return "\n".join(kept).rstrip()


def _personal_section(meta):
    comment_lines = meta["comments"].split("\n") if meta["comments"] else []
    lines = [
        "## Personal notes",
        "",
        f"- **Rating:** {str(meta['rating']) + '/5' if meta['rating'] else 'Not rated'}",
        f"- **Priority:** {meta['priority']}",
        f"- **Status:** {meta['status']}",
        f"- **Tags:** {', '.join(meta['tags']) if meta['tags'] else 'None'}",
    ]
    if comment_lines:
        lines.append(f"- **Comments:** {comment_lines[0]}")
        lines.extend(f"  {line}" if line.strip() else "" for line in comment_lines[1:])
    else:
        lines.append("- **Comments:** None")
    return "\n".join(lines) + "\n"


def render_note(text, meta):
    """Return the note text with the personal metadata applied, or raise RequestError."""
    match = FRONTMATTER.match(text)
    if not match:
        raise RequestError("Note has no frontmatter block")
    try:
        original = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as error:
        raise RequestError("Note frontmatter is not valid YAML") from error
    if not isinstance(original, dict):
        raise RequestError("Note frontmatter is not a mapping")

    frontmatter = _strip_user_fields(match.group(1))
    frontmatter = f"{frontmatter}\n" + "\n".join(_user_field_lines(meta))

    try:
        updated = yaml.safe_load(frontmatter)
    except yaml.YAMLError as error:
        raise RequestError("Updated frontmatter would not be valid YAML") from error
    expected = {
        "user_rating": meta["rating"],
        "user_priority": meta["priority"],
        "user_status": meta["status"],
        "user_tags": meta["tags"],
        "user_comments": meta["comments"],
    }
    untouched = {key: value for key, value in original.items() if key not in USER_FIELDS}
    if not isinstance(updated, dict) or any(updated.get(key) != value for key, value in expected.items()) \
            or {key: value for key, value in updated.items() if key not in USER_FIELDS} != untouched:
        raise RequestError("Updated frontmatter failed the round-trip check")

    body = text[match.end():]
    section = _personal_section(meta)
    if PERSONAL_SECTION.search(body):
        body = PERSONAL_SECTION.sub(lambda _: section + "\n", body, count=1)
    else:
        body = body.rstrip() + "\n\n" + section
    return f"---\n{frontmatter}\n---\n{body.rstrip()}\n"


def _resolve_note(root, note):
    notes_dir = (root / "notes").resolve()
    candidate = root / note
    if candidate.is_symlink() or not candidate.is_file() or candidate.resolve().parent != notes_dir:
        raise RequestError("The requested note does not exist")
    return candidate


def apply_request(body, author_association, root="."):
    if author_association not in ALLOWED_ASSOCIATIONS:
        return {"result": "rejected", "message": "Rejected: only repository owners, members, and collaborators can update notes.", "note_path": ""}
    root = Path(root)
    try:
        meta = parse_request(body)
        path = _resolve_note(root, meta["note"])
        original = path.read_text(encoding="utf-8")
        updated = render_note(original, meta)
    except RequestError as error:
        return {"result": "rejected", "message": f"Rejected: {error}.", "note_path": ""}
    except (OSError, UnicodeDecodeError):
        return {"result": "rejected", "message": "Rejected: the note could not be read.", "note_path": ""}
    if updated == original:
        return {"result": "unchanged", "message": f"No changes: {meta['note']} already has these personal notes.", "note_path": meta["note"]}
    path.write_text(updated, encoding="utf-8")
    return {"result": "applied", "message": f"Updated personal notes in {meta['note']}.", "note_path": meta["note"]}


def main():
    result = apply_request(
        os.environ.get("ISSUE_BODY", ""),
        os.environ.get("ISSUE_AUTHOR_ASSOCIATION", "NONE"),
    )
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as output:
            for key in ("result", "message", "note_path"):
                output.write(f"{key}={result[key]}\n")
    print(f"{result['result']}: {result['message']}")
    return result


if __name__ == "__main__":
    main()
