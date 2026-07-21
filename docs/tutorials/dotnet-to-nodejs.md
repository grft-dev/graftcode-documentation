---
title: "Call a .NET BillingService from Node.js"
description: "Build a .NET provider, host it in Docker with Graftcode Gateway, and call it from Node.js."
---

# Call a .NET BillingService from Node.js

In this tutorial you will expose one synchronous .NET method, install the generated npm Graft using
the exact command from your live Gateway, and call the method from Node.js.

```text
Node.js consumer
  -> generated npm Graft
  -> ws://localhost/ws
  -> Docker-hosted Gateway
  -> BillingService.CalculateMonthlyBill(...)
  -> result
```

![Graftcode module, generated package, consumer, and execution path](../../assets/diagrams/one-picture-overview.svg)

## Prerequisites

- Docker Desktop running with Linux containers.
- .NET 9 SDK.
- Node.js 22 or newer and npm.
- Ports `80` and `81` available.
- A shell opened in this tutorial's sample directory:
  `docs/tutorials/dotnet-to-nodejs`.

Check the tools:

```bash
docker version
dotnet --version
node --version
npm --version
```

This repository includes complete files under
[`docs/tutorials/dotnet-to-nodejs/`](dotnet-to-nodejs/). The code blocks below duplicate them so the
tutorial remains complete in renderers that expose only Markdown pages.

## 1. Inspect the .NET provider

Path: `provider/BillingService.csproj`

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <AssemblyName>BillingService</AssemblyName>
  </PropertyGroup>
</Project>
```

Path: `provider/BillingService.cs`

```csharp
namespace BillingProvider;

public static class BillingService
{
    public static double CalculateMonthlyBill(double unitPrice, int units)
    {
        if (unitPrice < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(unitPrice));
        }

        if (units < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(units));
        }

        return unitPrice * units;
    }
}
```

The public method is synchronous and uses only portable primitive types. The class library has no
controller, route, HTTP request type, or Graftcode attribute.

Build from `docs/tutorials/dotnet-to-nodejs`:

```bash
dotnet build ./provider/BillingService.csproj
```

Expected build result includes `Build succeeded.` and creates
`provider/bin/Debug/net9.0/BillingService.dll`.

## 2. Build the Gateway container

Path: `provider/Dockerfile`

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0

WORKDIR /usr/app
COPY . .

RUN dotnet publish BillingService.csproj -c Release -o /usr/app/publish
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && wget -O /tmp/gg.deb https://github.com/grft-dev/graftcode-gateway/releases/latest/download/gg_linux_amd64.deb \
    && dpkg -i /tmp/gg.deb \
    && rm /tmp/gg.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app/publish
EXPOSE 80
EXPOSE 81

CMD ["gg", "BillingService.dll"]
```

Path: `provider/.dockerignore`

```text
bin/
obj/
```

Build from `docs/tutorials/dotnet-to-nodejs`:

```bash
docker build --pull -t billing-service:graftcode ./provider
```

Run Gateway:

```bash
docker run -d -p 80:80 -p 81:81 --name billing-service-gateway billing-service:graftcode
```

Follow startup output:

```bash
docker logs -f billing-service-gateway
```

Wait for output that confirms `BillingProvider.BillingService` is enabled and the Unified Graft
Model upload succeeded. Stop following logs with `Ctrl+C`; this does not stop the container.

Gateway port `80` handles WebSocket calls. Port `81` serves Graftcode Vision at
[http://localhost:81/GV](http://localhost:81/GV).

## 3. Install the generated npm Graft

Do not use a registry ID or install command copied from this page. A Gateway running without a
project key receives a dynamic free registry ID, and that ID can change whenever Gateway restarts.

1. In the live `docker logs` output or Vision, select the npm consumer instructions.
2. Copy the **complete emitted `npm install` command**, including registry URL, package name, and
   version.
3. Change to the consumer directory:

   ```bash
   cd ./consumer
   ```

4. Run the copied command unchanged.
5. Copy the installed package name from that same command. It is the package spec without its version;
   do not infer it from `BillingService`.

The sample does not contain a fabricated registry ID. The verified provider package name is
`@graft/nuget-billingservice`; npm writes that dependency and the generated version to
`consumer/package.json` when you run the emitted command.

## 4. Configure and run the Node.js consumer

Path: `consumer/index.js`

```javascript
"use strict";

const {
  GraftConfig,
  BillingService,
} = require("@graft/nuget-billingservice");

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;

(async () => {
  const total = await BillingService.calculateMonthlyBill(12.5, 4);
  console.log(`Monthly bill: ${total}`);
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

Run from `docs/tutorials/dotnet-to-nodejs/consumer`:

```bash
npm start
```

The registry ID is never typed manually: it came from the complete install command you already ran.

Expected result:

```text
Monthly bill: 50
```

That output verifies the generated Node method `BillingService.calculateMonthlyBill(12.5, 4)`
reached the .NET provider method `BillingService.CalculateMonthlyBill(12.5, 4)` and returned its
result. Gateway preserves PascalCase in the .NET contract and emits lower camel case in the
Node Graft.

## 5. Verify the call

- Open Vision and confirm `BillingProvider.BillingService.CalculateMonthlyBill` has two parameters
  and a numeric return.
- Stop the container, run `npm start`, and confirm the consumer reports a connection failure:

  ```bash
  docker stop billing-service-gateway
  npm start
  ```

- Start it again and confirm the expected result returns:

  ```bash
  docker start billing-service-gateway
  npm start
  ```

This distinguishes a remote call from in-memory module loading.

## Troubleshooting

**Port 80 or 81 is already allocated**

Stop the conflicting service or container. If you remap the service port, update `GraftConfig.host`
to include the mapped host port. If you remap Vision, open the mapped port instead.

**No enabled BillingService type appears**

Run `docker logs billing-service-gateway`. Confirm the image built `BillingService.dll` and that
`gg BillingService.dll` resolves from `/usr/app/publish`.

**Package installation returns 404**

Do not use the default npm registry and do not reuse an old command. Copy the entire registry-qualified
command from the currently running Gateway after model upload succeeds.

**`Cannot find module`**

Run the emitted install command from `consumer`. Confirm it installed
`@graft/nuget-billingservice` and that `node_modules/@graft/nuget-billingservice` exists.

**The consumer tries to load a local provider**

Configure `GraftConfig.host = "ws://localhost/ws"` before the first generated call. The default
execution mode is in-memory.

**Method or class name is missing**

Inspect the generated exports or Vision snippet. Cross-language naming is generator output. In the
Gateway verification, .NET `BillingService.CalculateMonthlyBill` was emitted as Node
`BillingService.calculateMonthlyBill`; use the declaration installed by your current Gateway.

**Gateway rejects the package model**

Keep the .NET public method synchronous and expose only supported primitives or plain models. Remove
framework types from every public signature and public model member.

## Cleanup

From any directory:

```bash
docker rm -f billing-service-gateway
docker image rm billing-service:graftcode
```

From `docs/tutorials/dotnet-to-nodejs/consumer`, remove generated install state if you do not want to
keep it:

PowerShell:

```powershell
Remove-Item -Recurse -Force node_modules
Remove-Item -Force package-lock.json
```

bash:

```bash
rm -rf node_modules package-lock.json
```

## What to read next

- [What is a Graft?](../core-concepts/what-is-a-graft.md)
- [.NET language guide](../language-guides/dotnet.md)
- [Node.js and TypeScript language guide](../language-guides/nodejs-typescript.md)
- [Configuration resolution](../core-concepts/configuration-resolution.md)
- [Current status and limitations](../introduction/where-graftcode-fits.md)

This tutorial was verified with a local .NET build, Gateway, its exact dynamically
emitted npm install command, and a Node.js remote call. The dynamic registry ID is intentionally not
recorded in this page.
