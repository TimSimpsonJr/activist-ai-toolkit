#!/usr/bin/env python3
"""Validate blog post frontmatter against framework schemas.

Usage:
    python validate-frontmatter.py <post-path> --framework <astro|hugo|generic>

Arguments:
    post-path     Path to the markdown blog post file

Options:
    --framework   Target framework: astro, hugo, or generic (default: generic)
"""

import argparse
import re
import sys
from pathlib import Path

SCHEMAS = {
    "astro": {
        "required": ["title", "date", "summary"],
        "optional": ["tags", "draft", "image", "author"],
        "date_format": "iso8601",  # 2026-03-05T00:00:00.000Z
    },
    "hugo": {
        "required": ["title", "date"],
        "optional": ["description", "tags", "draft", "categories", "author"],
        "date_format": "date",  # 2026-03-05
    },
    "generic": {
        "required": ["title", "date"],
        "optional": ["summary", "description", "tags", "draft"],
        "date_format": "date",
    },
}


def parse_frontmatter(content: str) -> tuple[dict, list[str]]:
    """Extract frontmatter fields and return (fields_dict, raw_lines)."""
    if not content.startswith("---"):
        return {}, []

    end = content.find("---", 3)
    if end == -1:
        return {}, []

    raw = content[3:end].strip()
    lines = raw.split("\n")
    fields = {}
    current_key = None
    current_list = []

    for line in lines:
        # New key-value pair
        if re.match(r"^[a-zA-Z_-]+:", line):
            # Save previous list if any
            if current_key and current_list:
                fields[current_key] = current_list
                current_list = []

            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value.startswith("[") and value.endswith("]"):
                # Inline array
                fields[key] = [
                    v.strip().strip("'\"")
                    for v in value[1:-1].split(",")
                    if v.strip()
                ]
                current_key = None
            elif value == "":
                # Possibly start of a list
                current_key = key
            else:
                fields[key] = value.strip("'\"")
                current_key = None
        elif line.strip().startswith("- ") and current_key:
            current_list.append(line.strip()[2:].strip().strip("'\""))

    # Save final list
    if current_key and current_list:
        fields[current_key] = current_list

    return fields, lines


def validate_date(value: str, fmt: str) -> tuple[bool, str]:
    """Validate date string against expected format."""
    if fmt == "iso8601":
        # Accept ISO 8601 with or without timezone
        patterns = [
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z",
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",
            r"\d{4}-\d{2}-\d{2}",
        ]
        for p in patterns:
            if re.fullmatch(p, value):
                return True, ""
        return False, f"Expected ISO 8601 date, got: {value}"
    elif fmt == "date":
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return True, ""
        return False, f"Expected YYYY-MM-DD date, got: {value}"
    return True, ""


def validate(post_path: Path, framework: str) -> list[dict]:
    """Validate frontmatter and return list of issues."""
    issues = []
    schema = SCHEMAS[framework]

    try:
        content = post_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [{"level": "error", "message": f"File not found: {post_path}"}]

    if not content.startswith("---"):
        return [{"level": "error", "message": "No frontmatter found (file must start with ---)"}]

    fields, _ = parse_frontmatter(content)

    if not fields:
        return [{"level": "error", "message": "Frontmatter is empty or malformed"}]

    # Check required fields
    for field in schema["required"]:
        if field not in fields:
            issues.append(
                {"level": "error", "message": f"Missing required field: {field}"}
            )

    # Validate date format
    if "date" in fields:
        ok, msg = validate_date(str(fields["date"]), schema["date_format"])
        if not ok:
            issues.append({"level": "error", "message": msg})

    # Check for unknown fields
    known = set(schema["required"]) | set(schema["optional"])
    for field in fields:
        if field not in known:
            issues.append(
                {"level": "warning", "message": f"Unknown field for {framework}: {field}"}
            )

    # Validate tags is a list
    if "tags" in fields and not isinstance(fields["tags"], list):
        issues.append(
            {"level": "warning", "message": "tags should be a list/array"}
        )

    # Validate title is not empty
    if "title" in fields and not fields["title"]:
        issues.append({"level": "error", "message": "title is empty"})

    # Check title length
    if "title" in fields and len(str(fields["title"])) > 100:
        issues.append(
            {"level": "warning", "message": f"title is long ({len(fields['title'])} chars), consider shortening"}
        )

    # Check summary/description length
    for field in ["summary", "description"]:
        if field in fields and len(str(fields[field])) > 160:
            issues.append(
                {
                    "level": "warning",
                    "message": f"{field} is {len(fields[field])} chars (>160), may be truncated in meta tags",
                }
            )

    if not issues:
        issues.append(
            {"level": "ok", "message": f"Frontmatter valid for {framework}"}
        )

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Validate blog post frontmatter"
    )
    parser.add_argument("post_path", help="Path to markdown blog post")
    parser.add_argument(
        "--framework",
        choices=["astro", "hugo", "generic"],
        default="generic",
        help="Target framework (default: generic)",
    )
    args = parser.parse_args()

    issues = validate(Path(args.post_path).resolve(), args.framework)

    has_errors = False
    for issue in issues:
        level = issue["level"].upper()
        symbol = {"ERROR": "X", "WARNING": "!", "OK": "v"}.get(level, "?")
        print(f"  [{symbol}] {level}: {issue['message']}")
        if level == "ERROR":
            has_errors = True

    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
