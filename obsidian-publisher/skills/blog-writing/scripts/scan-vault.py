#!/usr/bin/env python3
"""Scan an Obsidian vault and index research notes by tag and topic.

Usage:
    python scan-vault.py <vault-path> [--tags] [--topics] [--json]

Arguments:
    vault-path    Path to Obsidian vault or research subdirectory

Options:
    --tags        Group notes by frontmatter tags (default if no option given)
    --topics      Group notes by wikilink topics mentioned
    --json        Output as JSON instead of plain text
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    frontmatter = content[3:end].strip()
    result = {}
    for line in frontmatter.split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value.startswith("[") and value.endswith("]"):
                result[key] = [
                    v.strip().strip("'\"")
                    for v in value[1:-1].split(",")
                    if v.strip()
                ]
            elif value.startswith("- "):
                result[key] = [value[2:].strip()]
            else:
                result[key] = value.strip("'\"")
    # Handle multi-line tag arrays
    if "tags" not in result:
        tag_match = re.search(
            r"tags:\s*\n((?:\s+-\s+.+\n?)+)", frontmatter
        )
        if tag_match:
            result["tags"] = [
                line.strip().lstrip("- ").strip("'\"")
                for line in tag_match.group(1).strip().split("\n")
                if line.strip().startswith("-")
            ]
    return result


def extract_wikilinks(content: str) -> list[str]:
    """Extract all [[wikilinks]] from markdown content."""
    # Match [[target]] and [[target|display]]
    pattern = r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]"
    return list(set(re.findall(pattern, content)))


def scan_vault(vault_path: Path) -> list[dict]:
    """Scan vault directory for markdown files and extract metadata."""
    notes = []
    for md_file in sorted(vault_path.rglob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        frontmatter = parse_frontmatter(content)
        wikilinks = extract_wikilinks(content)
        rel_path = md_file.relative_to(vault_path)

        # Extract title from first heading or filename
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1) if title_match else md_file.stem

        notes.append(
            {
                "path": str(rel_path),
                "title": title,
                "tags": frontmatter.get("tags", []),
                "wikilinks": wikilinks,
                "type": frontmatter.get("type", ""),
                "word_count": len(content.split()),
            }
        )
    return notes


def group_by_tags(notes: list[dict]) -> dict[str, list[dict]]:
    """Group notes by their frontmatter tags."""
    groups: dict[str, list[dict]] = {}
    for note in notes:
        tags = note.get("tags", [])
        if not tags:
            groups.setdefault("untagged", []).append(note)
        else:
            for tag in tags:
                groups.setdefault(tag, []).append(note)
    return dict(sorted(groups.items()))


def group_by_topics(notes: list[dict]) -> dict[str, list[dict]]:
    """Group notes by wikilink topics they mention."""
    groups: dict[str, list[dict]] = {}
    for note in notes:
        for link in note.get("wikilinks", []):
            groups.setdefault(link, []).append(note)
    # Sort by number of mentions (most referenced topics first)
    return dict(
        sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
    )


def print_text(groups: dict[str, list[dict]], label: str) -> None:
    """Print groups in readable text format."""
    print(f"\n{'=' * 60}")
    print(f"  Notes grouped by {label}")
    print(f"{'=' * 60}\n")
    for group_name, group_notes in groups.items():
        print(f"## {group_name} ({len(group_notes)} notes)")
        for note in sorted(group_notes, key=lambda n: n["path"]):
            words = note["word_count"]
            print(f"  - {note['title']} ({words} words)")
            print(f"    {note['path']}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Scan Obsidian vault and index research notes"
    )
    parser.add_argument("vault_path", help="Path to vault or research directory")
    parser.add_argument(
        "--tags", action="store_true", help="Group by frontmatter tags"
    )
    parser.add_argument(
        "--topics", action="store_true", help="Group by wikilink topics"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output as JSON"
    )
    args = parser.parse_args()

    vault_path = Path(args.vault_path).resolve()
    if not vault_path.is_dir():
        print(f"Error: {vault_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    notes = scan_vault(vault_path)
    print(f"Found {len(notes)} notes in {vault_path}", file=sys.stderr)

    # Default to tags if no option specified
    if not args.tags and not args.topics:
        args.tags = True

    if args.tags:
        groups = group_by_tags(notes)
        if args.json:
            print(json.dumps(groups, indent=2, default=str))
        else:
            print_text(groups, "tags")

    if args.topics:
        groups = group_by_topics(notes)
        if args.json:
            print(json.dumps(groups, indent=2, default=str))
        else:
            print_text(groups, "wikilink topics")


if __name__ == "__main__":
    main()
