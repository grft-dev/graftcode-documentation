#!/usr/bin/env python3
"""Validate the Markdown documentation without external dependencies."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
README = DOCS / "README.md"
MARKETING_PHRASES = (
    "seamless",
    "effortless",
    "revolutionary",
    "zero overhead",
    "always up to date",
    "works with everything",
    "production ready",
    "production-ready",
    "production-capable",
)
LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
NAV_PATH_PATTERN = re.compile(r'\bpath:\s*"([^"]+\.md)"')
NAV_TITLE_PATTERN = re.compile(
    r'title:\s*"([^"]+)"\s*\n\s*path:\s*"([^"]+\.md)"'
)
TITLE_PATTERN = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
FENCE_PATTERN = re.compile(r"^```(.*)$", re.MULTILINE)


def markdown_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def validate_frontmatter(path: Path, text: str, errors: list[str]) -> str | None:
    if path == README:
        return None
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return None
    match = TITLE_PATTERN.search(text)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: frontmatter has no title")
        return None
    return match.group(1).strip("\"'")


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        relative_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        resolved = (path.parent / relative_target).resolve()
        if not resolved.exists():
            errors.append(
                f"{path.relative_to(ROOT)}: broken link {raw_target!r}"
            )


def validate_fences(path: Path, text: str, warnings: list[str]) -> None:
    fences = FENCE_PATTERN.findall(text)
    if len(fences) % 2:
        warnings.append(f"{path.relative_to(ROOT)}: unmatched fenced code block")
        return
    for index in range(0, len(fences), 2):
        if not fences[index].strip():
            warnings.append(
                f"{path.relative_to(ROOT)}: code fence has no language at fence {index // 2 + 1}"
            )


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def document_h1(body: str) -> str | None:
    lines = body.splitlines()
    h2_index = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    for index in range(h2_index):
        line = lines[index]
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return None


def validate_titles(files: list[Path], errors: list[str]) -> None:
    readme = README.read_text(encoding="utf-8")
    nav_titles = {
        path: title for title, path in NAV_TITLE_PATTERN.findall(readme)
    }

    for path in files:
        if path == README:
            continue
        text = path.read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(text)
        if frontmatter is None:
            continue
        match = TITLE_PATTERN.search(frontmatter)
        if not match:
            continue
        title = match.group(1).strip("\"'")
        rel = path.relative_to(DOCS).as_posix()
        h1 = document_h1(body)
        if h1 is None:
            errors.append(f"{path.relative_to(ROOT)}: missing H1 before first section heading")
        elif h1 != title:
            errors.append(
                f"{path.relative_to(ROOT)}: H1 {h1!r} does not match frontmatter title {title!r}"
            )
        nav_title = nav_titles.get(rel)
        if nav_title and nav_title != title:
            errors.append(
                f"docs/README.md: nav title {nav_title!r} does not match "
                f"{rel} frontmatter title {title!r}"
            )


def validate_navigation(files: list[Path], errors: list[str]) -> None:
    text = README.read_text(encoding="utf-8")
    listed = set(NAV_PATH_PATTERN.findall(text))
    expected = {
        path.relative_to(DOCS).as_posix()
        for path in files
        if path != README
    }
    for missing in sorted(expected - listed):
        errors.append(f"docs/README.md: page absent from YAML navigation: {missing}")
    for stale in sorted(listed - expected):
        errors.append(f"docs/README.md: YAML navigation target does not exist: {stale}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    files = markdown_files()

    for path in files:
        text = path.read_text(encoding="utf-8")
        title = validate_frontmatter(path, text, errors)
        if title:
            titles[title.casefold()].append(path)
        validate_links(path, text, errors)
        validate_fences(path, text, warnings)

        lowered = text.casefold()
        for phrase in MARKETING_PHRASES:
            if phrase in lowered:
                errors.append(
                    f"{path.relative_to(ROOT)}: forbidden marketing phrase {phrase!r}"
                )

    validate_navigation(files, errors)
    validate_titles(files, errors)

    for paths in titles.values():
        if len(paths) > 1:
            warnings.append(
                "duplicate title: " + ", ".join(str(path.relative_to(ROOT)) for path in paths)
            )

    print(f"Validated {len(files)} Markdown files.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
