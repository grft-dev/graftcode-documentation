---
title: "What is Graftcode?"
description: "What Graftcode is, a before/after example, protocol comparison, and where teams use it."
---

# What is Graftcode?

Graftcode connects two **services you write** — a **Caller** (calling) and a **Receiver** (called) —
through a generated **Graft** that replaces hand-written integration layers. The Receiver's **public
interface** becomes an installable package; the Caller installs it and calls it like local code.
**Hypertube** carries the invocation to **Gateway**, which hosts the Receiver's **service business
logic** when execution is remote.

For how Caller, Graft, Hypertube, Gateway, Receiver, Vision, and Graftcode Engine fit together, see
[How Graftcode works](how-graftcode-works.md).

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
boundary—see [Use Graftcode alongside REST](../how-to-guides/use-graftcode-alongside-an-existing-rest-api.md).

## How this differs from REST, GraphQL, gRPC, and tRPC

Most integration stacks start with a **protocol contract** you design and maintain separately from your
business code — OpenAPI routes, GraphQL schemas, `.proto` files, or shared TypeScript router types.
Graftcode starts from **public methods you already write** on a Receiver module. The **Graft** is the
client; callers install it and invoke those methods like local code.

For teams connecting services that can install a package, **Graftcode is significantly better to use**
than protocol-first stacks in day-to-day work. You write and call methods—not routes, GraphQL
documents, `.proto` definitions, or tRPC router wiring. The generated Graft carries transport and
serialization; the same call site works in-memory or remotely when you change `GraftConfig`. Less
boilerplate, fewer artifacts to keep in sync, and a shorter path from a changed public method to a
working cross-language call.

### Protocol-first vs method-first

| | REST · GraphQL · gRPC · tRPC | Graftcode |
| --- | --- | --- |
| **What you design first** | Routes, schemas, operations, or shared API types | Public methods on your module |
| **What the Caller installs** | HTTP/GraphQL client, protobuf stubs, or tRPC client | Generated **Graft** from Vision or registry |
| **What changes when the API evolves** | Routes, DTOs, clients, compatibility rules | Public surface; regenerate or reinstall the Graft |
| **Best when** | Public HTTP APIs, browsers, partners, or a stack already built on that protocol | Controlled callers can install a package and you care about **performance**, **less integration code**, **readable call sites**, **maintainability**, and **developer experience** |

REST, GraphQL, gRPC, and tRPC are strong choices for **public boundaries** and ecosystems where those
tools are already standard. Graftcode fits **service-to-service** and **controlled internal** callers
that should not maintain a hand-written integration layer.

### At a glance

| | REST | GraphQL | gRPC | tRPC | Graftcode |
| --- | --- | --- | --- | --- | --- |
| **Contract** | URLs, verbs, request/response shapes | Graph schema, queries, mutations | `.proto` services and messages | TS router procedures and shared types | Public methods on the Receiver |
| **Caller experience** | HTTP client and serialization | GraphQL client and documents | Generated stubs | Typed client in TypeScript | Generated Graft — call like local code |
| **Cross-language** | Yes | Yes | Strong (protobuf) | Mainly TypeScript full-stack | Yes — verify the Receiver/Caller pair |
| **Typical fit** | Public HTTP, browsers, partners | Flexible reads, BFFs | Polyglot service RPC | Full-stack TypeScript apps | Service-to-service and controlled cross-language calls where **performance**, **lower boilerplate**, **code readability**, **maintainability**, and **developer experience** are priorities |

You can keep REST or GraphQL for external clients and add Graftcode for internal integration —
see [Use Graftcode alongside REST](../how-to-guides/use-graftcode-alongside-an-existing-rest-api.md).

A Graft call is still distributed: auth, failures, timeouts, and observability still matter.

### How they compare

For **developer experience and integration speed**, Graftcode is the stronger default when Callers can
install generated packages: you skip the protocol layer that REST, GraphQL, gRPC, and tRPC require you
to design, version, and maintain alongside your business code.

![Graftcode removes application-authored controllers, DTO mapping, transport clients, and serialization code that a REST or gRPC integration would require; the runtime still represents and transfers invocation data](../../assets/diagrams/performance-comparison.png)

REST and gRPC keep a protocol contract (URLs/operations, schemas, and a client) separate from your
business code. With Graftcode the supported public method surface is the contract and the installed
Graft is the client. For raw throughput, neither approach is universally faster; the right choice
still depends on who owns the contract, who the Callers are, and your interoperability, streaming,
and browser needs. For **how much code you write and how fast you ship internal integration**,
Graftcode is typically the better fit.

Graftcode removes application-authored controllers, DTO mapping, transport clients, and serialization
code for controlled Callers. Its runtime still represents and transfers invocation data, so the
resulting performance depends on the runtime pair, execution mode, payload, transport, topology, and
workload. This documentation does not publish comparative performance numbers without a documented,
reproducible benchmark.

## Where teams use Graftcode

- Service-to-service calls across languages, without hand-written HTTP clients.
- Sharing a Receiver library with internal or controlled Callers.
- Flipping the same code between in-memory and remote execution by configuration.
- Exposing Receiver methods as MCP tools.

Pick your goal and runtime in [Choose a scenario](choose-your-scenario.md), and review
[current status and limitations](where-does-graftcode-fit.md) before production.

## Next steps

1. [Quick start](https://docs.graftcode.com/quick-start) — first working call for your stack.
2. [How Graftcode works](how-graftcode-works.md) — the How it works diagram and mental model.
3. [Choose a scenario](choose-your-scenario.md) — pick your goal, then your runtime.
4. [Quick reference](../reference/quick-reference.md) — keep open while coding.
