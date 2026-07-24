#!/usr/bin/env python3
"""Rename documentation markdown files to slugified frontmatter titles."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TITLE_PATTERN = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
LINK_PATTERN = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
PATH_IN_YAML_PATTERN = re.compile(r'(path:\s*")([^"]+\.md)(")')


def slugify(title: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return value.strip("-")


def frontmatter_title(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    match = TITLE_PATTERN.search(parts[1])
    if not match:
        return ""
    return match.group(1).strip("\"'")


def build_rename_map() -> dict[str, str]:
    entries: list[tuple[str, str, str]] = []
    for path in sorted(DOCS.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        rel = path.relative_to(DOCS).as_posix()
        title = frontmatter_title(path.read_text(encoding="utf-8")) or path.stem
        parent = path.parent.relative_to(DOCS).as_posix()
        base = slugify(title)
        candidate = f"{parent}/{base}.md" if parent != "." else f"{base}.md"
        entries.append((rel, candidate, title))

    rename_map: dict[str, str] = {}
    used_targets: dict[str, str] = {}
    for rel, candidate, title in entries:
        if candidate in used_targets and used_targets[candidate] != rel:
            stem = Path(rel).stem
            parent = str(Path(rel).parent).replace("\\", "/")
            if parent == ".":
                candidate = f"{slugify(title)}-{stem}.md"
            else:
                candidate = f"{parent}/{slugify(title)}-{stem}.md"
        used_targets[candidate] = rel
        if candidate != rel:
            rename_map[rel] = candidate
    return rename_map


def resolve_link(path: Path, target: str, rename_map: dict[str, str]) -> str:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target

    fragment = ""
    query = ""
    base = target
    if "#" in base:
        base, fragment = base.split("#", 1)
        fragment = f"#{fragment}"
    if "?" in base:
        base, query = base.split("?", 1)
        query = f"?{query}"
    if not base.endswith(".md"):
        return target

    resolved = (path.parent / base).resolve()
    try:
        rel = resolved.relative_to(DOCS.resolve()).as_posix()
    except ValueError:
        return target

    new_rel = rename_map.get(rel, rel)
    new_abs = (DOCS / new_rel).resolve()
    new_link = os.path.relpath(new_abs, path.parent.resolve()).replace("\\", "/")
    return f"{new_link}{query}{fragment}"


def update_links(text: str, path: Path, rename_map: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, target, suffix = match.groups()
        updated = resolve_link(path, target, rename_map)
        return f"{prefix}{updated}{suffix}"

    updated = LINK_PATTERN.sub(replace, text)
    if path.name.lower() == "readme.md":
        def replace_yaml(match: re.Match[str]) -> str:
            prefix, nav_path, suffix = match.groups()
            return f"{prefix}{rename_map.get(nav_path, nav_path)}{suffix}"

        updated = PATH_IN_YAML_PATTERN.sub(replace_yaml, updated)
    for old, new in sorted(rename_map.items(), key=lambda item: len(item[0]), reverse=True):
        updated = updated.replace(old, new)
    return updated


def apply_renames(rename_map: dict[str, str], dry_run: bool) -> None:
    if not rename_map:
        print("No files to rename.")
        return

    # Two-phase rename via temporary names to avoid target collisions.
    temp_map: dict[str, str] = {}
    for index, old in enumerate(rename_map):
        temp_map[old] = f"__rename_tmp_{index:03d}.md"

    phase1: list[tuple[Path, Path]] = []
    phase2: list[tuple[Path, Path]] = []
    for old, new in rename_map.items():
        old_path = DOCS / old
        temp_path = old_path.parent / temp_map[old]
        new_path = DOCS / new
        phase1.append((old_path, temp_path))
        phase2.append((temp_path, new_path))

    if dry_run:
        print(f"Would rename {len(rename_map)} files:")
        for old, new in sorted(rename_map.items()):
            print(f"  {old} -> {new}")
        return

    for old_path, temp_path in phase1:
        temp_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.rename(temp_path)

    for temp_path, new_path in phase2:
        new_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path.rename(new_path)

    targets = list(DOCS.rglob("*.md")) + list((ROOT / "scripts").glob("*.py"))
    style_guide = ROOT.parent.parent / ".cursor" / "rules" / "DOCS_STYLE_GUIDE.md"
    if style_guide.exists():
        targets.append(style_guide)

    for file_path in targets:
        if not file_path.exists():
            continue
        original = file_path.read_text(encoding="utf-8")
        if file_path.suffix == ".md":
            updated = update_links(original, file_path, rename_map)
        else:
            updated = original
            for old, new in sorted(rename_map.items(), key=lambda item: len(item[0]), reverse=True):
                updated = updated.replace(old, new)
        if updated != original:
            file_path.write_text(updated, encoding="utf-8")

    print(f"Renamed {len(rename_map)} files and updated links.")


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    rename_map = build_rename_map()
    apply_renames(rename_map, dry_run=dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
