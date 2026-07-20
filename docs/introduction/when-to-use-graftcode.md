---
title: "When should you use Graftcode?"
description: "Choose a Graftcode learning path from your integration scenario."
---

# Choose your scenario

Use this page as a route into the documentation. Graftcode is best suited to callable behavior with
an intentional programming interface; it is not a universal replacement for every protocol or data
movement pattern.

## I want one backend to call another

Start with the [.NET-to-Node.js tutorial](../tutorials/dotnet-to-nodejs.md), then read
[caller and receiver](../core-concepts/caller-and-receiver.md).

Good fit when consumers can install generated packages and you want typed method calls across
process or language boundaries.

## I want browser, desktop, or mobile code to call a backend

Read the [language support status](../language-guides/support-status.md) and the target
[language guide](../language-guides/index.md). Verify browser transport, bundler, authentication, and
supported-type constraints for the exact generated Graft.

## I want to split or merge a deployment without rewriting callers

Read [execution modes](../core-concepts/execution-modes.md),
[configuration resolution](../core-concepts/configuration-resolution.md), and the
[invocation lifecycle](../core-concepts/invocation-lifecycle.md).

The consumer programming surface can remain similar while configuration selects in-memory or remote
execution. Deployment changes still require compatible packages and runtime configuration.

## I want to expose methods as AI tools

Review [Graftcode Gateway](../core-concepts/graftcode-gateway.md) and
[known limitations](../reference/known-limitations.md) for current support status. Keep the public
surface small and treat tool authorization, input validation, and data exposure as explicit design
work.

## I am designing a production contract

Read [callable surface](../core-concepts/callable-surface.md),
[type mapping](../core-concepts/type-mapping.md), and
[contract evolution](../core-concepts/contract-evolution.md). Generate and smoke-test the exact
provider/consumer pair before depending on advanced types.

## Keep another integration style when

- external consumers require a public, protocol-defined HTTP API;
- a third party supports only REST, webhooks, gRPC, or another fixed protocol;
- the interaction is event streaming, queueing, bulk transfer, or one-way data exchange rather than
  method invocation;
- consumers cannot install or run a supported generated package;
- a simple stable local function or direct library reference already solves the problem.

These approaches can coexist with Graftcode. Choose per boundary, not per organization.

## Before production

Review [current status and limitations](where-graftcode-fits.md), the relevant language guides,
[authentication and authorization](../operations/authentication-authorization.md), and
[scaling](../operations/scaling.md).
