---
title: "What is Graftcode?"
description: "What Graftcode is, a before/after example, protocol comparison, and where teams use it."
---

# What is Graftcode?

Graftcode turns a Receiver module's **public interface** into an installable **Graft** package. A
**Caller** installs that Graft and calls it like local code. **Hypertube** carries the invocation to
**Gateway**, which hosts the Receiver's **service business logic**.

For how Caller, Graft, Hypertube, Gateway, Receiver, Vision, and Graftcode Engine fit together, see
[How Graftcode works](what-problem-does-graftcode-solve.md).

> **New here?** Run a hands-on course in [Quick start](https://docs.graftcode.com/quick-start)
> first. This documentation explains concepts, procedures, and reference material—it does not replace
> those step-by-step tutorials.

## Example: calling a billing method across services

**The problem:** a Node.js application needs `calculateMonthlyBill(unitPrice, units)`, which lives in
a .NET service owned by another team.

### Without Graftcode (typical REST or GraphQL integration)

A separate integration layer usually appears between business code and the remote capability:

1. Agree an HTTP or GraphQL contract (OpenAPI, schema, versioning rules).
2. Generate or hand-write a client, DTOs, and error mapping.
3. Build URLs or queries, serialize payloads, and parse responses on every call.
4. Maintain that layer when the contract changes.

```javascript
// Illustrative REST-style Caller code — not Graftcode
const response = await fetch("https://billing.example/api/v1/monthly-bill", {
  method: "POST",
  headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
  body: JSON.stringify({ unitPrice: 10, units: 5 }),
});
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const { total } = await response.json();
```

### With Graftcode

1. The .NET team exposes a plain public method on a class library (the **Receiver**).
2. **Gateway** hosts that built module, discovers the [callable surface](../core-concepts/callable-surface.md),
   and publishes it for [package generation](../core-concepts/package-generation.md).
3. The Node team installs the generated **Graft** and calls it like local code.

```javascript
// Illustrative Graftcode Caller — copy package name and host from Vision
import { BillingService } from "<package-from-vision>";
import { GraftConfig } from "<package-from-vision>/config.js";

GraftConfig.host = "ws://billing.example/ws"; // before the first call
const total = BillingService.calculateMonthlyBill(10, 5);
```

No hand-written HTTP client, route map, or JSON DTO layer for this internal call—the public method
signature is the contract, and the installed Graft is the client. You still operate a distributed
system (hosts, auth, failures, observability); Graftcode removes the repetitive protocol glue for
callers that can install generated packages.

For a public HTTP API aimed at arbitrary third parties, REST or GraphQL may remain the better
boundary—see [Use Graftcode alongside REST](../how-to-guides/coexist-with-rest.md).

## How this differs from REST, GraphQL, gRPC, and tRPC

REST, GraphQL, gRPC, and tRPC each keep a **protocol contract**—routes, schemas, `.proto` files, or
shared TypeScript types—separate from your business code. You maintain that contract layer and the
clients that speak it. With Graftcode the supported **public method surface** is the contract and the
installed **Graft** is the client for callers that can install generated packages.

| | REST | GraphQL | gRPC | tRPC | Graftcode |
| --- | --- | --- | --- | --- | --- |
| **Contract** | URLs, HTTP methods, request/response shapes (often OpenAPI) | Graph schema, queries, mutations | `.proto` service and message definitions | TypeScript router procedures and shared types | Public methods on the Receiver module |
| **Caller experience** | HTTP client, URLs, serialization | GraphQL client and query documents | Generated stubs from protobuf | Typed client in a TypeScript codebase | Generated Graft — call like local code |
| **Cross-language** | Yes | Yes | Strong (protobuf) | Primarily TypeScript monorepos / full-stack TS | Yes — verify the exact Receiver/Caller pair |
| **Typical fit** | Public HTTP APIs, browsers, partners | Flexible reads, BFFs, varied clients | Service-to-service RPC, polyglot backends | Full-stack TypeScript apps | Internal or controlled callers across languages |
| **What you maintain on change** | Routes, DTOs, clients, versioning rules | Schema, resolvers mapping, clients | `.proto`, generated stubs, compatibility rules | Router types and client wiring | Public surface; reinstall or republish Graft when the contract changes |

Graftcode does not replace every protocol. REST, GraphQL, gRPC, and tRPC remain the better fit for
public HTTP boundaries, arbitrary browser clients, partner integrations, and ecosystems where those
tools are already standard. Many products use Graftcode for internal calls and keep REST or GraphQL for
external APIs — see [Use Graftcode alongside REST](../how-to-guides/coexist-with-rest.md).

A Graft call is still distributed: auth, failures, timeouts, and observability still matter.

## Where teams use Graftcode

- Service-to-service calls across languages, without hand-written HTTP clients.
- Sharing a Receiver library with internal or controlled Callers.
- Flipping the same code between in-memory and remote execution by configuration.
- Exposing Receiver methods as MCP tools.

Pick your goal and runtime in [Choose a scenario](when-to-use-graftcode.md), and review
[current status and limitations](where-graftcode-fits.md) before production.

## Next steps

1. [Quick start](https://docs.graftcode.com/quick-start) — first working call for your stack.
2. [How Graftcode works](what-problem-does-graftcode-solve.md) — the How it works diagram and mental model.
3. [Choose a scenario](when-to-use-graftcode.md) — pick your goal, then your runtime.
4. [Quick reference](../reference/quick-reference.md) — keep open while coding.
