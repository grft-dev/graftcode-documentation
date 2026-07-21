---
title: "Cross-runtime verification sample (.NET → Node.js)"
description: "Maintained BillingService sample used to verify documentation claims; hands-on steps live in Quick start."
---

# Cross-runtime verification sample (.NET → Node.js)

This page describes a **maintained sample** in the documentation repository. It is used to verify
cross-language publication and remote invocation behavior. **Step-by-step tutorials live in
[Quick start](https://docs.graftcode.com/quick-start)**—do not treat this page as the
primary learning path.

## Run the hands-on course instead

| Goal | Quick start course |
| --- | --- |
| Host a .NET provider | [Expose a backend service (.NET)](https://docs.graftcode.com/quick-start/expose-backend/dotnet) |
| Call from Node.js | [Connect microservices (JavaScript)](https://docs.graftcode.com/quick-start/connect-microservices/javascript) |
| Cross-language module install | [Use modules (.NET)](https://docs.graftcode.com/quick-start/use-modules-from-any-technology/dotnet) · [Use modules (JavaScript)](https://docs.graftcode.com/quick-start/use-modules-from-any-technology/javascript) |

After your first successful call, use [Configure invocation](../how-to-guides/configure-invocation.md)
and [Quick reference](../reference/quick-reference.md) while coding.

## What the sample demonstrates

```text
Node.js consumer
  -> generated npm Graft
  -> ws://localhost/ws
  -> Docker-hosted Gateway
  -> BillingService.CalculateMonthlyBill(...)
  -> result
```

- A synchronous .NET `BillingService` with primitive parameters.
- Gateway hosting via `gg BillingService.dll` inside a container.
- npm Graft installation from the **live** Gateway/Vision output (dynamic registry).
- Remote execution after `GraftConfig.host = "ws://localhost/ws"` before the first call.
- Cross-language method naming (PascalCase provider, lower camel case generated Node API).

## Sample layout

Complete files live under [`docs/tutorials/dotnet-to-nodejs/`](dotnet-to-nodejs/):

| Path | Purpose |
| --- | --- |
| `provider/BillingService.cs` | Provider contract |
| `provider/Dockerfile` | Gateway + published assembly |
| `consumer/index.js` | Node consumer using the generated Graft |

Use this tree when validating documentation changes or reproducing reported issues—not as a
substitute for Quick start tutorials.

## Documentation to read next

- [What is Graftcode?](../introduction/what-is-graftcode.md)
- [Caller and receiver](../core-concepts/caller-and-receiver.md)
- [.NET language guide](../language-guides/dotnet.md)
- [Node.js language guide](../language-guides/nodejs-typescript.md)
- [Troubleshooting: connection failures](../troubleshooting/connection-timeouts-auth.md)
