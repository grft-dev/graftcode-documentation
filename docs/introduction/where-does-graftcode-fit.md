---
title: "Where does Graftcode fit?"
description: "A quick capability summary and the key limits to check before adopting Graftcode."
---

# Where does Graftcode fit?

Graftcode is a runtime integration system for generated, package-based method calls. This page gives
a quick capability summary and the key limits to check. For the exhaustive list, see
[Known limitations](../reference/known-limitations.md).

## Capability summary

| Runtime | Host code with GG | Generate Graft |
| --- | --- | --- |
| .NET | Yes | Yes |
| Node.js / TypeScript | Yes | Yes |
| Java / JVM | Yes | Yes |
| Python | Yes | Yes |
| PHP | Yes | In development |
| Ruby | Yes | In development |

See [Supported runtimes and package managers](../reference/supported-runtimes-and-package-managers.md) for
versions, package ecosystems, and status. Generated Gateway/Vision output is the source of truth for
the package, imports, configuration, and call surface of your running version.

## Key limits to check

- **Contract types:** prefer primitives, strings, and plain models; framework complex types are
  rejected at generation. Verify advanced types (nullability, unions, enums, generics, collections)
  for your exact Receiver/Caller pair.
- **Execution:** clients default to in-memory; set the remote host before the first call. Static,
  stateless methods scale best; instance identity needs affinity and can break on restart.
- **Packages:** a free standalone Gateway's registry ID can change on restart. Copy the emitted
  install command; use a [project key](../how-to-guides/use-a-portal-project-key.md) for stable identity.
- **Operations:** Graftcode does not replace TLS, auth, authorization, load balancing, health checks,
  or telemetry. Gateway sits in the call path — operate and scale it as part of the service.

Full detail lives in [Known limitations](../reference/known-limitations.md),
[type mapping](../core-concepts/type-mapping.md), and
[callable surface](../core-concepts/callable-surface.md).

## Before production

Generate the real Graft and smoke-test every operation for your language pair; test upgrades,
restart, scale-out, and failure paths; configure transport security, identity, and authorization; add
telemetry at both boundaries; and pin versions. See the full checklist in
[Known limitations](../reference/known-limitations.md).

Start with [Quick start](https://docs.graftcode.com/quick-start) for a hands-on first call, then use
the [scenario chooser](choose-your-scenario.md).
