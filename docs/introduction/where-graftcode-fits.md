---
title: "Where does Graftcode fit?"
description: "Current support, verified boundaries, and limitations to check before adopting Graftcode."
---

# Current status and limitations

Graftcode is a runtime integration system for generated, package-based method calls. Before adopting
it, verify the exact provider language, consumer language, contract types, generated package, and
deployment mode you intend to use.

## Current support entry points

- [.NET](../language-guides/dotnet.md): provider and consumer support.
- [Node.js and TypeScript](../language-guides/nodejs-typescript.md): provider and consumer support.
- [Java/JVM](../language-guides/java-jvm.md), [Python](../language-guides/python.md),
  [Ruby](../language-guides/ruby.md), and [PHP](../language-guides/php.md): consult each guide for
  direction, evidence, and gaps.
- [Support status](../language-guides/support-status.md) summarizes the inspected implementation.

Generated Gateway/Vision output is the source of truth for the package, import, configuration, and
call surface produced by your running version.

## Contract limits

- Type support depends on the complete analyzer-to-generator-to-runtime path.
- Current package generation rejects framework complex types in public interfaces.
- For .NET, keep public methods synchronous. Do not expose `Task`, `Task<T>`, `DateTime`, `Guid`,
  streams, cancellation tokens, HTTP abstractions, interfaces, or framework collections.
- Prefer primitives, strings, and plain public models. Use ISO-8601 strings for time and strings for
  identifiers when crossing languages.
- JavaScript numbers cannot safely represent every .NET `long`; use an `int` or decimal string unless
  the exact path is tested.
- Advanced nullability, unions, enums, generics, inheritance, and collection shapes do not have a
  universal compatibility guarantee.

See [type mapping](../core-concepts/type-mapping.md) and
[callable surface](../core-concepts/callable-surface.md).

## Runtime limits

- Generated clients default to in-memory execution. Configure the remote host before the first call.
- Instance methods create remote identity and need lifecycle management and session affinity. Static,
  stateless methods are the safer default for horizontally scaled services.
- A Gateway restart can invalidate stateful remote instances.
- Browser WebSockets cannot attach arbitrary handshake headers; use only the alternative transport
  and configuration actually emitted for your Gateway.
- Remote exceptions and upstream failures reach consumers. Apply timeouts, retries, fallback, and
  idempotency according to the operation.

## Package and registry limits

- A free standalone Gateway receives a dynamic registry ID. Restarting it can produce a different
  install command.
- Never copy an example registry ID, package name, version, namespace, or import from documentation.
  Copy the complete emitted command and generated usage snippet.
- Use a project key when stable project identity and package location are required.
- A changed public contract requires regenerating and updating the consumer package. Internal-only
  implementation changes normally do not.

## Operational boundaries

Graftcode does not replace TLS termination, authentication, authorization, network policy, load
balancing, health checks, deployment orchestration, logging, metrics, tracing, backups, or incident
response. Gateway is in the remote call path, so operate and scale it as part of the service.

Claims about universal performance gains, complete type compatibility, or data egress should be
validated for the deployed version and configuration. Plugins and options can change behavior.

## Production readiness checklist

1. Generate the actual Graft and inspect its declarations.
2. Smoke-test every public operation across the intended language pair.
3. Test contract upgrades and rollback.
4. Test restart, scale-out, timeout, unavailable-provider, and malformed-input behavior.
5. Configure transport security, identity, authorization, and package access.
6. Add telemetry at both the caller and Gateway/provider boundary.
7. Pin versions and retain reproducible install configuration.

Start with [Quick start](https://docs.graftcode.com/quick-start) for a hands-on first call,
then use the [scenario chooser](when-to-use-graftcode.md).
