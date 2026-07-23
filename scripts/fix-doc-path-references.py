#!/usr/bin/env python3
"""Update documentation references after title-based file renames."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Old path -> new path (from rename-docs-to-titles.py run).
RENAME_MAP: dict[str, str] = {
    "core-concepts/in-memory-same-machine-and-remote-execution.md": "core-concepts/in-memory-same-machine-and-remote-execution.md",
    "core-concepts/core-concepts-glossary.md": "core-concepts/core-concepts-glossary.md",
    "core-concepts/gateway-and-hosted-modules.md": "core-concepts/gateway-and-hosted-modules.md",
    "core-concepts/public-surface-vs-implementation.md": "core-concepts/public-surface-vs-implementation.md",
    "how-to-guides/use-graftcode-alongside-an-existing-rest-api.md": "how-to-guides/use-graftcode-alongside-an-existing-rest-api.md",
    "how-to-guides/configure-graft-invocation.md": "how-to-guides/configure-graft-invocation.md",
    "how-to-guides/dependency-injection-with-stateless-facades.md": "how-to-guides/dependency-injection-with-stateless-facades.md",
    "how-to-guides/deploy-gateway-with-docker.md": "how-to-guides/deploy-gateway-with-docker.md",
    "how-to-guides/expose-code-as-a-graftcode-receiver.md": "how-to-guides/expose-code-as-a-graftcode-receiver.md",
    "how-to-guides/expose-receiver-methods-for-mcp.md": "how-to-guides/expose-receiver-methods-for-mcp.md",
    "how-to-guides/filter-the-callable-surface.md": "how-to-guides/filter-the-callable-surface.md",
    "how-to-guides/gateway-module-versioning-and-noversioning.md": "how-to-guides/gateway-module-versioning-and-noversioning.md",
    "how-to-guides/set-the-module-path-for-in-memory-execution.md": "how-to-guides/set-the-module-path-for-in-memory-execution.md",
    "how-to-guides/obtain-and-install-a-graft.md": "how-to-guides/obtain-and-install-a-graft.md",
    "how-to-guides/use-a-portal-project-key.md": "how-to-guides/use-a-portal-project-key.md",
    "how-to-guides/stateless-vs-stateful-graft-calls.md": "how-to-guides/stateless-vs-stateful-graft-calls.md",
    "how-to-guides/update-a-receiver-contract.md": "how-to-guides/update-a-receiver-contract.md",
    "introduction/how-graftcode-works.md": "introduction/how-graftcode-works.md",
    "introduction/choose-your-scenario.md": "introduction/choose-your-scenario.md",
    "introduction/where-does-graftcode-fit.md": "introduction/where-does-graftcode-fit.md",
    "operations/authentication-and-authorization-operations.md": "operations/authentication-and-authorization-operations.md",
    "operations/environment-and-configuration.md": "operations/environment-and-configuration.md",
    "operations/operations-and-deployment-model.md": "operations/operations-and-deployment-model.md",
    "operations/networking-and-ports.md": "operations/networking-and-ports.md",
    "operations/logging-metrics-and-tracing.md": "operations/logging-metrics-and-tracing.md",
    "operations/scaling-gateway-receivers.md": "operations/scaling-gateway-receivers.md",
    "operations/timeouts-and-retries.md": "operations/timeouts-and-retries.md",
    "operations/version-compatibility-and-upgrades.md": "operations/version-compatibility-and-upgrades.md",
    "reference/configuration-keys-and-precedence.md": "reference/configuration-keys-and-precedence.md",
    "reference/environment-variable-reference.md": "reference/environment-variable-reference.md",
    "reference/errors-and-status-reference.md": "reference/errors-and-status-reference.md",
    "reference/gateway-cli-reference.md": "reference/gateway-cli-reference.md",
    "reference/project-key-registry-host-and-credentials.md": "reference/project-key-registry-host-and-credentials.md",
    "reference/ports-and-protocols-reference.md": "reference/ports-and-protocols-reference.md",
    "reference/supported-runtimes-and-package-managers.md": "reference/supported-runtimes-and-package-managers.md",
    "reference/type-compatibility-matrix.md": "reference/type-compatibility-matrix.md",
    "troubleshooting/connection-timeout-or-authentication-failure.md": "troubleshooting/connection-timeout-or-authentication-failure.md",
    "troubleshooting/troubleshooting.md": "troubleshooting/troubleshooting.md",
    "troubleshooting/module-method-or-type-is-missing.md": "troubleshooting/module-method-or-type-is-missing.md",
    "troubleshooting/package-installation-fails.md": "troubleshooting/package-installation-fails.md",
    "troubleshooting/gateway-or-runtime-exits.md": "troubleshooting/gateway-or-runtime-exits.md",
    "troubleshooting/installed-package-is-stale.md": "troubleshooting/installed-package-is-stale.md",
    "troubleshooting/vision-and-runtime-disagree.md": "troubleshooting/vision-and-runtime-disagree.md",
}

LINK_PATTERN = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
PATH_IN_YAML_PATTERN = re.compile(r'(path:\s*")([^"]+\.md)(")')


def resolve_link(source: Path, target: str) -> str:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target

    fragment = ""
    query = ""
    base = target.strip()
    if "#" in base:
        base, fragment = base.split("#", 1)
        fragment = f"#{fragment}"
    if "?" in base:
        base, query = base.split("?", 1)
        query = f"?{query}"
    if not base.endswith(".md"):
        return target

    resolved = (source.parent / base).resolve()
    try:
        rel = resolved.relative_to(DOCS.resolve()).as_posix()
    except ValueError:
        return target

    new_rel = RENAME_MAP.get(rel, rel)
    new_abs = (DOCS / new_rel).resolve()
    new_link = os.path.relpath(new_abs, source.parent.resolve()).replace("\\", "/")
    return f"{new_link}{query}{fragment}"


def update_markdown_links(text: str, source: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, target, suffix = match.groups()
        return f"{prefix}{resolve_link(source, target)}{suffix}"

    return LINK_PATTERN.sub(replace, text)


def update_yaml_paths(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, path, suffix = match.groups()
        return f"{prefix}{RENAME_MAP.get(path, path)}{suffix}"

    return PATH_IN_YAML_PATTERN.sub(replace, text)


def update_plain_paths(text: str) -> str:
    updated = text
    for old, new in sorted(RENAME_MAP.items(), key=lambda item: len(item[0]), reverse=True):
        updated = updated.replace(old, new)
    return updated


def main() -> int:
    targets: list[Path] = list(DOCS.rglob("*.md"))
    targets.extend((ROOT / "scripts").glob("*.py"))
    style_guide = ROOT.parent.parent / ".cursor" / "rules" / "DOCS_STYLE_GUIDE.md"
    if style_guide.exists():
        targets.append(style_guide)

    changed = 0
    for path in targets:
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        updated = original
        if path.suffix == ".md":
            updated = update_markdown_links(updated, path)
            if path.name.lower() == "readme.md":
                updated = update_yaml_paths(updated)
        updated = update_plain_paths(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(path.relative_to(ROOT.parents[1]) if path.is_relative_to(ROOT.parents[1]) else path)

    print(f"Updated {changed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
