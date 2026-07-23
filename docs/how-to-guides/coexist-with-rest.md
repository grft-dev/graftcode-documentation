---
title: "Use Graftcode alongside an existing REST API"
description: "Keep HTTP endpoints for external clients while adding Graftcode for typed internal integration."
articleTitle: "Use Graftcode alongside an existing REST API"
---
Graftcode and REST solve different integration problems. They can coexist in one product when each
boundary has a clear owner.

## When to keep REST

Keep REST (or OpenAPI) when:

- external clients require a public HTTP contract;
- partners integrate via webhooks or fixed URLs;
- Callers cannot install a generated Graft.

See [When to use Graftcode](../introduction/when-to-use-graftcode.md).

## When to add Graftcode

Add Graftcode for **internal** or **controlled** callers that can install generated packages:

- service-to-service method calls across languages;
- sharing a Receiver library without hand-written HTTP clients;
- flipping between in-memory and remote execution with configuration alone.

## Typical layout

```text
┌─────────────────────────────────────┐
│  Monolith or API host               │
│  ├─ REST controllers (public)       │
│  └─ Receiver module (Graftcode)     │──► Gateway ──► remote Callers
└─────────────────────────────────────┘
```

1. Extract callable business logic into a **plain module** (class library or package)—not controller
   types on the public Graft surface.
2. Keep REST controllers as thin adapters that call the same module internally if needed.
3. Host the module with Gateway for Graft Callers.
4. Do not expose database or HTTP framework types on the Graft contract.

## Caller example

After installing the Graft from Vision, configure remote execution before the first call. See
[Configure invocation](configure-invocation.md).

REST traffic and Graft traffic use separate paths: HTTP routes for REST, generated Graft + Gateway
transport for Graftcode.

## How they compare

![Graftcode removes application-authored controllers, DTO mapping, transport clients, and serialization code that a REST or gRPC integration would require; the runtime still represents and transfers invocation data](../../assets/diagrams/performance-comparison.png)

REST and gRPC keep a protocol contract (URLs/operations, schemas, and a client) separate from your
business code. With Graftcode the supported public method surface is the contract and the installed
Graft is the client. Neither is universally faster; the right choice depends on who owns the contract,
who the Callers are, and your interoperability, streaming, and browser needs.

Graftcode removes application-authored controllers, DTO mapping, transport clients, and serialization
code for controlled Callers. Its runtime still represents and transfers invocation data, so the
resulting performance depends on the runtime pair, execution mode, payload, transport, topology, and
workload. This documentation does not publish comparative performance numbers without a documented,
reproducible benchmark.

## Next steps

- [Expose code](expose-code.md)
- [Caller and receiver](../core-concepts/caller-and-receiver.md)
- [Authentication operations](../operations/authentication-authorization.md)
