---
title: "What is Graftcode?"
description: "Start with a concrete .NET-to-Node.js Graftcode call, then learn what is generated and what runs."
---

# What is Graftcode?

Graftcode turns a module's public methods into an installable, typed package called a **Graft**. A
consumer calls the generated package like ordinary code; Graftcode Gateway routes the call to the
hosted module. You write business methods and consumer logic. Graftcode discovers the callable
surface, generates the package, and bridges the runtimes.

## See a real call first

The provider is a plain .NET class library:

```csharp
namespace BillingProvider;

public static class BillingService
{
    public static double CalculateMonthlyBill(double unitPrice, int units) =>
        unitPrice * units;
}
```

Build it, then host the resulting assembly with Gateway:

```bash
dotnet build ./BillingService.csproj
gg --runtime netcore --modules ./bin/Debug/net9.0/BillingService.dll
```

For the Docker-hosted workflow used by the tutorial, the equivalent container command is:

```dockerfile
CMD ["gg", "--runtime", "netcore", "--modules", "BillingService.dll"]
```

Wait for Gateway to report the enabled type and successful model upload. Then copy the **complete npm
install command emitted by that running Gateway or shown in its Vision UI**. Run it unchanged. The
free registry ID is generated at runtime and can change after a restart, so this documentation does
not print or invent one.

For this provider, Gateway 1.3.6 generated the package name
`@graft/nuget-billingservice`. Run this Node.js consumer:

```javascript
const {
  GraftConfig,
  BillingService,
} = require("@graft/nuget-billingservice");

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;

(async () => {
  const total = await BillingService.calculateMonthlyBill(12.5, 4);
  console.log(`Monthly bill: ${total}`);
})();
```

The registry address remains dynamic and must come from the running Gateway's install command.
Gateway 1.3.6 generated lower camel case for the Node method while the .NET contract remained
`BillingService.CalculateMonthlyBill`. Expected result:

```text
Monthly bill: 50
```

For every command, file, and working directory, follow the
[executable .NET-to-Node.js tutorial](../tutorials/dotnet-to-nodejs.md).

## What you write and what Graftcode generates

| You write | Graftcode provides |
| --- | --- |
| The .NET class library and public method | A discovered callable model |
| The Node.js business code | A generated npm Graft with typed classes and methods |
| Runtime host configuration | Runtime bridging and invocation dispatch |
| Deployment, security, retries, and observability policy | Vision metadata and package installation instructions |

![Module, generated Graft, consumer, and execution choices](../../assets/diagrams/one-picture-overview.svg)

Text version: `.NET module -> Gateway analysis -> generated npm Graft -> Node.js call -> Gateway -> .NET method -> result`.

## The call flow

1. Gateway loads `BillingService.dll` and discovers the supported public surface.
2. Gateway produces and uploads the Unified Graft Model used for package generation.
3. The developer copies the exact npm command from the live Gateway output or Vision.
4. npm installs the generated Graft in the Node.js project.
5. The consumer configures `GraftConfig.host` before its first generated call.
6. Node `BillingService.calculateMonthlyBill(...)` serializes an invocation of the .NET
   `BillingService.CalculateMonthlyBill(...)` method through the Graft.
7. Gateway dispatches the invocation to the .NET method and returns its result.
8. The generated promise resolves to `50` in Node.js.

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

1. Run [Call a .NET BillingService from Node.js](../tutorials/dotnet-to-nodejs.md).
2. Learn [what a Graft is](../core-concepts/what-is-a-graft.md).
3. Check [.NET](../language-guides/dotnet.md) and
   [Node.js/TypeScript](../language-guides/nodejs-typescript.md) support.
4. Review [current limitations](where-graftcode-fits.md) before production use.
