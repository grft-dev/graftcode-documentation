---
title: "Supported runtimes and package managers"
description: "Verified provider, consumer, and package-manager directions by runtime."
---

# Supported runtimes and package managers

| Runtime | Gateway baseline | Provider | Generated consumer | Package manager |
| --- | --- | --- | --- | --- |
| .NET Core / .NET | Core 3.1 or .NET 5+ | Verified | Verified | NuGet |
| CLR | .NET Framework 4.7.2+ | Hosted | .NET generation path | NuGet |
| Java / JVM | Java 8+ | Verified | Verified | Maven |
| Python | Python 3.6+ | Verified | Verified | pip / PyPI |
| Python 2.7 | CLI runtime listed | Gap | Gap | Not documented here |
| Ruby | Ruby 3+ | Verified | Verified | RubyGems |
| Node.js / TypeScript | Node.js 22+ | Verified | Verified | npm |
| PHP | PHP 7.4+ | Verified | Verified | Composer |
| Perl | CLI host runtime listed | Limited evidence | Not verified | None documented |

“Verified” means corresponding analyzer/generator and cross-runtime smoke evidence was inspected. It
does not mean every source type, framework, target version, browser, or package-manager feature works.

TypeScript providers are hosted as compiled JavaScript with declarations/metadata. `java` and `jvm`
are accepted runtime names. Runtime availability also depends on the host image/machine and native
Hypertube dependencies.

## Next steps

- [Language support status](../language-guides/support-status.md)
- [Type matrix](type-matrix.md)
- [Version compatibility and upgrades](../operations/version-compatibility-upgrades.md)
