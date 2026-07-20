---
title: "What problem does Graftcode solve?"
description: "A five-minute mental model for modules, Grafts, Gateway, configuration, and calls."
---

# The five-minute mental model

Graftcode reduces the separate integration layer that normally sits between a callable business
method and its consumer. It does not make a distributed call local; it makes the consumer-facing
programming model look like an installed dependency.

## Five things to remember

1. **The module is your code.** A provider is an ordinary class library or module. Its intentional,
   supported public methods form the callable surface.
2. **The Graft is generated code.** It is a package for the consumer's package manager and language.
   It mirrors the provider surface; it is not the provider implementation.
3. **Gateway hosts and analyzes modules.** It loads the provider, exposes runtime transports, serves
   Vision, and publishes the model used to generate packages.
4. **Configuration selects execution.** A generated client can resolve in-memory or remote
   execution. Remote calls must configure the Gateway host before the first invocation.
5. **A method call is still distributed.** Serialization, routing, failures, compatibility,
   security, retries, and observability still matter.

```text
provider module
    -> Gateway discovers public surface
    -> package service generates a Graft
    -> consumer installs and calls the Graft
    -> configured runtime path invokes the provider
```

## Build time versus call time

During setup, Gateway analyzes the provider and the package system generates a language-specific
Graft. During normal runtime invocation, the already-installed Graft sends the call through its
resolved execution path. It does not regenerate the package.

## The contract

The contract is the supported public surface: declaring types, methods, parameters, return values,
and public model members. Public does not automatically mean portable. The entire analyzer,
generation, and runtime path must support every exposed type.

Keep transport, database, framework, and implementation types private or internal. For the safest
cross-language surface, use simple primitives, strings, and plain models, then test the exact
provider/consumer pair.

## A useful distinction

- **Written:** provider logic, consumer logic, runtime configuration, operational policy.
- **Generated:** Graft package, language bindings, contract metadata, Vision views.
- **Operated:** Gateway process, transports, package access, deployment, security, telemetry.

That distinction prevents two common mistakes: treating Gateway as the generated client, or treating
the generated client as if it removes remote-system failure modes.

## Continue

- Run the [.NET-to-Node.js tutorial](../tutorials/dotnet-to-nodejs.md).
- Read [caller and receiver](../core-concepts/caller-and-receiver.md).
- Read [invocation lifecycle](../core-concepts/invocation-lifecycle.md).
- [Choose a scenario](when-to-use-graftcode.md).
