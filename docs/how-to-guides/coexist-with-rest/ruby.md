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
- consumers cannot install a generated Graft.

See [When to use Graftcode](../../introduction/when-to-use-graftcode.md).

## When to add Graftcode

Add Graftcode for **internal** or **controlled** callers that can install generated packages:

- service-to-service method calls across languages;
- sharing a provider library without hand-written HTTP clients;
- flipping between in-memory and remote execution with configuration alone.

## Typical layout

```text
┌─────────────────────────────────────┐
│  Monolith or API host               │
│  ├─ REST controllers (public)     │
│  └─ Provider module (Graftcode)    │──► Gateway ──► remote consumers
└─────────────────────────────────────┘
```

1. Extract callable business logic into a **plain module** (class library or package)—not controller
   types on the public Graft surface.
2. Keep REST controllers as thin adapters that call the same module internally if needed.
3. Host the module with Gateway for Graft consumers.
4. Do not expose database or HTTP framework types on the Graft contract.

## Consumer example (Ruby)

After installing the Graft from Vision, configure remote execution before the first call. See
[Configure invocation](../configure-invocation).

REST traffic and Graft traffic use separate paths: HTTP routes for REST, generated Graft + Gateway
transport for Graftcode.

## Next steps

- [Expose code](../expose-code)
- [Caller and receiver](../../core-concepts/caller-and-receiver.md)
- [Authentication operations](../../operations/authentication-authorization.md)

## Source anchors

- `introduction/when-to-use-graftcode.md`
- `core-concepts/caller-and-receiver.md`
