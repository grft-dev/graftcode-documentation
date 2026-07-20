---
title: "Configure Graft invocation"
description: "Select in-memory or remote execution and configure generated GraftConfig before first use."
---

# Configure Graft invocation

## Goal

Point an installed Graft at the intended provider.

## 1. Choose execution mode

- `inmemory` loads the provider module in the consumer process.
- `ws://` or `wss://` sends calls to a remote Gateway WebSocket endpoint.
- TCP and HTTP/2 are optional Gateway transports and must be explicitly enabled.

Generated .NET and Node.js Grafts default to `inmemory`.

## 2. Configure before the first call

.NET uses static fields:

```csharp
using <generated_namespace>;

GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```

Node.js uses lower-case static fields:

```typescript
import { GraftConfig } from "<package-copied-from-vision>";

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```

Copy the import and endpoint from Vision. The generated runtime context is cached after
initialization; configure it before the first generated call.

## 3. Pick the state model deliberately

Prefer static methods and stateless calls for independently routable operations. Instance methods and
remote object identity are stateful; they require connection/session affinity and can be lost on
Gateway restart or scale-in.

## 4. Use another configuration source only when needed

Generated packages inspect six source levels: graft-specific environment, global environment,
graft-specific file, global file, programmatic user configuration, then library default. Earlier
levels win in the inspected resolver.

**Gap:** exact field names and supported transport connection strings vary outside generated .NET and
Node.js packages. Use the installed package and Vision output as the authority.

## Next steps

- [Configuration keys and precedence](../reference/configuration-keys-precedence.md)
- [Networking and ports](../operations/networking-ports.md)
- [Scale Gateway instances](../operations/scaling.md)

## Source anchors

- `graftcode-code-generator/src/netcore/GraftCodeCodeGenerator/Core/Generator/Handler/Utils/GraftConfigClassProvider.cs`
- `graftcode-code-generator/src/nodejs/src/core/generator/templates/config.template.js`
- `HYPERTUBE/src/netcore/Hypertube.Netcore.Sdk/Configuration/ConfigPriority.cs`
- `HYPERTUBE/src/js/hypertube-nodejs-sdk/lib/sdk/configuration/ConfigPriority.js`
