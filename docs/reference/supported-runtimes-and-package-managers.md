---
title: "Supported runtimes and package managers"
description: "Which runtimes can host Receiver code, act as a Caller, run in-memory, and which package ecosystems they use."
---

# Supported runtimes and package managers

Support has independent parts: hosting Receiver code, acting as a Caller, in-memory execution, and
package generation for a given ecosystem. A runtime being accepted by Gateway does not by itself mean
the full Caller/Receiver path is available. Use this matrix for role support; use the
[Type compatibility matrix](type-compatibility-matrix.md) for type behavior.

## Capability matrix

| Runtime | Host Receiver code | Act as Caller | In-memory | Package ecosystem | Recommended version | Legacy minimum | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET (Core / .NET) | Yes | Yes | Yes | NuGet | .NET 8+ | Core 3.1 / .NET 5 | Available | Public methods must be synchronous |
| .NET Framework (CLR) | Yes | Yes | Yes | NuGet | 4.8 | 4.7.2 | Available | Uses the .NET generation path |
| Java / JVM | Yes | Yes | Yes | Maven | Java 17+ | Java 8 | Available | `java` and `jvm` runtime names accepted; Kotlin/Groovy via JVM bytecode |
| Node.js / TypeScript | Yes | Yes | Yes | npm | Node.js 22+ | Node.js 22 | Available | TypeScript hosted as compiled JavaScript + declarations |
| Python 3 | Yes | Yes | Yes | pip / PyPI | 3.11+ | 3.6 | Available | Import-based analysis runs module init code |
| PHP | Yes | Yes | Yes | Composer | 8.1+ | 7.4 | Available | Composer packages may run post-install steps |
| Ruby | Yes | Yes | Yes | RubyGems | 3.x | 3.0 | Available | Package name and require name may differ |
| Python 2.7 | Listed by CLI | Not documented | Not documented | Not documented | — | 2.7 | Unsupported | Present as a CLI runtime name only |
| Perl | Listed by CLI | No | Not documented | None | — | — | Unsupported | Gateway lists `perl`, but no Graft generation or Caller path exists |

Status labels: **Available** (reachable through a public path and behaves as documented),
**Alpha/Preview** (incomplete or unstable), **Planned** (partial foundations), **Unsupported**.

"Host Receiver code" and "Act as Caller" are separate capabilities. Runtime availability also depends
on the host image or machine and its native dependencies.

## Package ecosystems

| Runtime | Registry / package manager |
| --- | --- |
| .NET / CLR | NuGet |
| Java / JVM | Maven |
| Node.js / TypeScript | npm |
| Python 3 | pip / PyPI |
| PHP | Composer |
| Ruby | RubyGems |

Copy the exact install command from the running Gateway or Vision; never construct registry
identifiers or package names by hand. See
[Obtain and install a Graft](../how-to-guides/obtain-and-install-a-graft.md).

## Perl and Python 2.7

Gateway advertises `perl` and `python27` as host runtime names, but there is no Graft generation,
package endpoint, or Caller path for them today. Do not infer a CPAN workflow or a Python 2.7
generated package. Follow release notes until a complete path is added.

## Next steps

- [Type compatibility matrix](type-compatibility-matrix.md)
- [Generated package structure](generated-package-structure.md)
- [Known limitations](known-limitations.md)
- [Version compatibility and upgrades](../operations/version-compatibility-and-upgrades.md)
