#!/usr/bin/env python3
"""Simplify gg examples: drop redundant --runtime/--modules; remove pinned Gateway versions."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# gg --projectKey "x" --runtime netcore --modules ./path [--flags]
PROJECT_RUNTIME_MODULES = re.compile(
    r"gg (--projectKey [^\n]+?) --runtime \S+ --modules (\S+)"
)

# gg --runtime X --modules PATH (optional trailing flags on same line)
RUNTIME_MODULES = re.compile(
    r"gg --runtime \S+ --modules (\S+)"
)

# gg --graftOnly --runtime <runtime> --modules <module>
GRAFT_ONLY = re.compile(
    r"gg --graftOnly --runtime <runtime> --modules <module>"
)

# gg --modules <module> --corsConfig
MODULES_ONLY = re.compile(
    r"gg --modules (\S+)"
)

# CMD ["gg", "--runtime", "netcore", "--modules", "BillingService.dll"]
CMD_RUNTIME_MODULES = re.compile(
    r'\["gg", "--runtime", "[^"]+", "--modules", "([^"]+)"\]'
)

# CMD ["gg", "--modules", "Provider.dll"]
CMD_MODULES_ONLY = re.compile(
    r'\["gg", "--modules", "([^"]+)"\]'
)

# Gateway 1.3.6 / Docker-hosted Gateway 1.3.6 / live Gateway 1.3.6
GATEWAY_VERSION = re.compile(
    r"(?:Docker-hosted |live )?Gateway 1\.3\.6",
    re.IGNORECASE,
)

PROSE_REPLACEMENTS = [
    (
        "Prefer explicit `--runtime` and `--modules` over auto-scan in crowded directories.",
        "Pass the built module path explicitly when auto-scan would pick the wrong artifact.",
    ),
    (
        "pass explicit `--runtime` and `--modules`",
        "pass the built module path explicitly",
    ),
    (
        "Pass explicit `--runtime`/`--modules`",
        "Pass the module path explicitly",
    ),
    (
        "`--runtime netcore`, and `--modules BillingService.dll` resolves from `/usr/app/publish`.",
        "`gg BillingService.dll` resolves from `/usr/app/publish`.",
    ),
    (
        "Run Gateway with `--runtime ruby` and wait for publication.",
        "Run Gateway against the provider module and wait for publication.",
    ),
    (
        "Explicit `--runtime ruby` is safer than relying on auto-detection.",
        "Pass the module path explicitly when auto-detection is ambiguous.",
    ),
    (
        "Run Gateway with `--runtime php` against the provider and wait for successful publication.",
        "Run Gateway against the provider module and wait for successful publication.",
    ),
    (
        "Explicit `--runtime php` is safer than relying on auto-detection.",
        "Pass the module path explicitly when auto-detection is ambiguous.",
    ),
    (
        "**No types discovered:** pass `--runtime ruby` and point `--modules` at loadable source.",
        "**No types discovered:** point `gg` at loadable source.",
    ),
    (
        "**No provider types:** pass `--runtime php`, verify module root, and ensure dependencies are installed.",
        "**No provider types:** point `gg` at the module root and ensure dependencies are installed.",
    ),
    (
        "gg --runtime <runtime> --modules <module>",
        "gg <module-path>",
    ),
    (
        "gg --runtime <runtime> --modules <built-module>",
        "gg <path-to-built-module>",
    ),
    (
        "gg --runtime <runtime> --modules <module> \\",
        "gg <module-path> \\",
    ),
    (
        "Use explicit module/runtime arguments",
        "Pass the built module path explicitly",
    ),
    (
        "The current Gateway supports a first positional module path or `--modules`. If neither is supplied, it scans the current directory. `--runtime` can select a runtime explicitly or use `auto`.",
        "Pass the built module as the first positional argument (`gg ./path/to/module.dll`). If no path is supplied, Gateway scans the current directory and attempts runtime detection. Use `--runtime` only when auto-detection is wrong.",
    ),
]


def transform(text: str) -> str:
    text = PROJECT_RUNTIME_MODULES.sub(r"gg \1 \2", text)
    text = RUNTIME_MODULES.sub(r"gg \1", text)
    text = GRAFT_ONLY.sub("gg --graftOnly <module-path>", text)
    text = CMD_RUNTIME_MODULES.sub(r'["gg", "\1"]', text)
    text = CMD_MODULES_ONLY.sub(r'["gg", "\1"]', text)
    text = MODULES_ONLY.sub(r"gg \1", text)
    text = GATEWAY_VERSION.sub("Gateway", text)
    text = re.sub(
        r"This tutorial was verified with a local \.NET build, Docker-hosted Gateway, its exact dynamically",
        "This tutorial was verified with a local .NET build, a Docker-hosted Gateway, its exact dynamically",
        text,
    )
    for old, new in PROSE_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> None:
    changed: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if path.suffix not in {".md", ".py", ""} and path.name != "Dockerfile":
            continue
        if path.is_dir():
            continue
        if path.name == "simplify-gg-commands.py":
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))

    print(f"Updated {len(changed)} files:")
    for item in changed:
        print(f"  - {item}")


if __name__ == "__main__":
    main()
