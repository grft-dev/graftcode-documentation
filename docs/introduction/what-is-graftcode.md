---
title: "What is Graftcode?"
description: "What Graftcode generates, how Gateway fits in, and how a cross-language call flows."
---

# What is Graftcode?

Graftcode turns a module's public methods into an installable, typed package called a **Graft**. A
consumer calls the generated package like ordinary code; Graftcode Gateway routes the call to the
hosted module. You write business methods and consumer logic. Graftcode discovers the callable
surface, generates the package, and bridges the runtimes.

> **New here?** Run a hands-on course in [Quick start](https://docs.graftcode.com/quick-start)
> first. This documentation explains concepts, procedures, and reference material—it does not replace
> those step-by-step tutorials.

## What a successful call looks like

A typical cross-language flow:

1. A **provider** exposes a plain public method (for example a static `CalculateMonthlyBill` on a .NET
   class).
2. **Gateway** hosts the built module (`gg ./path/to/module.dll`), discovers the surface, and
   publishes the model.
3. You copy the **complete install command** from that Gateway's Vision UI—never guess registry URLs or
   package names.
4. The **consumer** installs the generated Graft, sets `GraftConfig.host` to the Gateway WebSocket
   endpoint **before the first call**, and invokes the generated method.
5. The result returns as if the remote method were local—still a distributed call under the hood.

Expected outcome for a billing example: `unitPrice * units` computed on the provider and returned to
the caller. Method naming may differ by target language (for example PascalCase on .NET, lower camel
case in generated JavaScript).

## What you write and what Graftcode generates

| You write | Graftcode provides |
| --- | --- |
| The provider library and public methods | A discovered callable model |
| Consumer business code | A generated Graft with typed classes and methods |
| Runtime host configuration | Runtime bridging and invocation dispatch |
| Deployment, security, retries, and observability policy | Vision metadata and package installation instructions |

![Module, generated Graft, consumer, and execution choices](../../assets/diagrams/one-picture-overview.svg)

Text version: `provider module -> Gateway analysis -> generated Graft -> consumer call -> Gateway -> provider method -> result`.

## The call flow

1. Gateway loads the provider module and discovers the supported public surface.
2. Gateway produces and uploads the Unified Graft Model used for package generation.
3. The developer copies the exact install command from the live Gateway output or Vision.
4. The consumer installs the generated Graft in the target project.
5. The consumer configures the generated host field before its first call.
6. The generated client serializes an invocation of the provider method.
7. Gateway dispatches the invocation and returns the result.

Package generation is not repeated on every call.

## How this differs from REST

With REST, a team normally defines an HTTP resource or operation, chooses URLs and verbs, serializes
payloads, and writes or generates a client from a separate contract such as OpenAPI. With Graftcode,
the supported public programming surface is the contract and the installed Graft is the client.

This is a difference in developer workflow, not a claim that networks disappear. Remote Graft calls
still cross a transport, can fail, require compatible contract types, and need authentication,
authorization, observability, timeouts, retries, and deployment controls appropriate to the system.
REST remains useful for public protocol-oriented APIs, webhooks, broad third-party interoperability,
and clients that cannot install a generated Graft.

## Boundaries

- Graftcode does not replace business logic, infrastructure, deployment, security, or monitoring.
- Public contracts must use types supported by the complete provider-to-consumer generation path.
- Current .NET public methods must be synchronous; keep `Task`, framework types, streams, HTTP
  abstractions, and cancellation tokens out of the public surface.
- Prefer static stateless methods for remote work. Stateful instances require affinity and have a
  lifecycle across calls.
- `Host` defaults to in-memory execution. Set the generated host field before the first remote call.
- A free Gateway registry ID is dynamic. A project key is required when stable project identity is
  needed.
- Generated output and Vision from the running Gateway are authoritative for package names, imports,
  versions, and configuration snippets.

## Next steps

1. [Quick start](https://docs.graftcode.com/quick-start) — first working call for your stack.
2. [The five-minute mental model](what-problem-does-graftcode-solve.md).
3. [What is a Graft?](../core-concepts/what-is-a-graft.md).
4. [Quick reference](../reference/quick-reference.md) — keep open while coding.
5. [Choose a scenario](when-to-use-graftcode.md) — Quick start links for your integration goal.
6. [Current limitations](where-graftcode-fits.md) before production use.
