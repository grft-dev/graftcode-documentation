#!/usr/bin/env python3
"""Align frontmatter title, first markdown H1, and README navigation titles."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
README = DOCS / "README.md"

TITLE_PATTERN = re.compile(r'^title:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
NAV_TITLE_PATTERN = re.compile(
    r'(title:\s*")([^"]+)("\s*\n\s*path:\s*")([^"]+\.md)(")'
)
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+\.md)\)')


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def frontmatter_title(frontmatter: str) -> str | None:
    match = TITLE_PATTERN.search(frontmatter)
    if not match:
        return None
    return match.group(1).strip("\"'")


def find_first_h1_line(body: str) -> int | None:
    lines = body.splitlines()
    h2_index = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    for index in range(h2_index):
        line = lines[index]
        if line.startswith("# ") and not line.startswith("## "):
            return index
    return None


def document_h1(body: str) -> str | None:
    line_index = find_first_h1_line(body)
    if line_index is None:
        return None
    return body.splitlines()[line_index][2:].strip()


def set_body_h1(body: str, title: str) -> str:
    h1_line = f"# {title}"
    lines = body.splitlines(keepends=True)
    h2_index = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    preamble = lines[:h2_index]
    rest = lines[h2_index:]

    preamble = [
        line
        for line in preamble
        if not (line.startswith("# ") and not line.startswith("## "))
    ]
    while preamble and not preamble[0].strip():
        preamble.pop(0)
    while preamble and not preamble[-1].strip():
        preamble.pop()

    h1_block = f"{h1_line}\n\n"
    if preamble:
        preamble_text = "".join(preamble)
        if not preamble_text.endswith("\n"):
            preamble_text += "\n"
        return f"\n{h1_block}{preamble_text}{''.join(rest)}"
    return f"\n{h1_block}{''.join(rest)}"


def update_markdown_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        return False

    title = frontmatter_title(frontmatter)
    if not title:
        return False

    new_body = set_body_h1(body, title)
    if new_body == body:
        return False

    path.write_text(f"---{frontmatter}---{new_body}", encoding="utf-8")
    return True


def collect_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    for path in sorted(DOCS.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        frontmatter, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        if frontmatter is None:
            continue
        title = frontmatter_title(frontmatter)
        if title:
            titles[path.relative_to(DOCS).as_posix()] = title
    return titles


def update_readme_nav(titles: dict[str, str]) -> bool:
    text = README.read_text(encoding="utf-8")
    original = text

    def replace_nav(match: re.Match[str]) -> str:
        prefix, _old, middle, path, suffix = match.groups()
        new_title = titles.get(path)
        if not new_title:
            return match.group(0)
        return f"{prefix}{new_title}{middle}{path}{suffix}"

    text = NAV_TITLE_PATTERN.sub(replace_nav, text)

def replace_link(match: re.Match[str]) -> str:
        link_text, target = match.group(1), match.group(2)
        rel = target.split("#", 1)[0]
        if rel.startswith("http"):
            return match.group(0)
        resolved = (DOCS / rel).resolve()
        if not resolved.exists():
            return match.group(0)
        title = titles.get(Path(rel).as_posix())
        if not title:
            return match.group(0)
        return f"[{title}]({target})"

    text = LINK_PATTERN.sub(replace_link, text)
    if text != original:
        README.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed_files = 0
    for path in sorted(DOCS.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        if update_markdown_file(path):
            changed_files += 1
            print(f"updated H1: {path.relative_to(ROOT)}")

    titles = collect_titles()
    if update_readme_nav(titles):
        print("updated docs/README.md navigation titles")

    print(f"Done. Updated {changed_files} markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
