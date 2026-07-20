---
title: "Language Support Status"
description: "Provider, consumer, package-manager, and verification status by runtime."
---

# Language support status

Support has several independent parts: Gateway hosting, module analysis, graft generation, package
publication, package installation, and invocation. A runtime listed by `gg --runtime` is not, by
itself, proof that the complete provider-to-consumer workflow is verified.

| Runtime | Provider direction | Consumer direction | Package manager | Evidence level |
| --- | --- | --- | --- | --- |
| .NET / CLR | Supported | Supported | NuGet | Gateway, generator, and public/virtual E2E coverage |
| Node.js / TypeScript | Supported | Supported | npm | Gateway, generator, and public/virtual E2E coverage |
| Java / JVM | Supported | Supported | Maven | Gateway, generator, and public/virtual E2E coverage |
| Python 3 | Supported | Supported | pip / PyPI | Gateway, generator, and public/virtual E2E coverage |
| PHP | Supported | Supported | Composer | Gateway, generator, and public E2E coverage |
| Ruby | Supported | Supported | RubyGems | Gateway, generator, and public E2E coverage |
| Perl | Limited hosting only | No equivalent verified generated-client workflow | None documented here | Gateway/Hypertube runtime references only |

## What was verified

The inspected package-generation engine contains dedicated generation engines for .NET, Node.js,
JVM, Python, PHP, and Ruby. The public-repository smoke suite is organized by caller runtime and
contains cross-runtime install-and-invoke specifications for those same six callers. The virtual
repository suite additionally covers complete Gateway publish/install flows for .NET, Node.js, JVM,
and Python.

This supports the directions shown above, but it is not a promise that every language type or
framework abstraction is portable. Each guide lists the narrow type baseline demonstrated by tests
and marks broader areas as gaps.

## Perl

Gateway advertises `perl` as a host runtime, and Hypertube contains Perl runtime routing and native
binary references. The inspected package-generation engine has no Perl generation engine, the
code-generator tree has no Perl generator, and the E2E graft matrix has no Perl caller suite.

Therefore Perl belongs only in this status page:

- **Available direction:** limited Gateway/Hypertube hosting.
- **Not verified:** a Perl module analyzer-to-package publication flow equivalent to the embedded GMA
  paths used by the six complete guides.
- **Not verified:** generated Perl consumer packages, a Perl package-manager endpoint, or install and
  invocation tests.

Do not infer a CPAN workflow or fabricate Perl generated APIs. Track the implementation source and
Gateway release notes until a complete path is added.

## Evidence and samples

- [Gateway runtime list](https://github.com/grft-dev/graftcode-gateway#usage)
- [Quick Start repository](https://github.com/grft-dev/graftcode-quick-start-guide)
- [Cross-runtime simple-car sample](https://github.com/grft-dev/grft-test-simple-car)
- [Repository-dependency sample](https://github.com/grft-dev/grft-test-simple-car-repository)
- Inspected E2E evidence:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/`
- Inspected full publish evidence:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/`
