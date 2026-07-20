---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container using the verified .NET workflow."
---

# Deploy Gateway with Docker

## Goal

Package a .NET provider and Gateway in one container.

## 1. Create the provider image

This workflow is verified for a .NET 9 class library and the published Linux AMD64 Debian package:

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0
WORKDIR /usr/app
COPY . /usr/app/
RUN dotnet build
RUN dotnet publish -c Release -o /usr/app/
RUN apt-get update && apt-get install -y wget \
 && wget -O /usr/app/gg.deb https://github.com/grft-dev/graftcode-gateway/releases/latest/download/gg_linux_amd64.deb \
 && dpkg -i /usr/app/gg.deb && rm /usr/app/gg.deb \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 80
EXPOSE 81
CMD ["gg", "--modules", "Provider.dll"]
```

Replace `Provider.dll` with the published assembly. Add `bin/` and `obj/` to `.dockerignore`.

For repeatable production builds, pin a reviewed Gateway release instead of `latest`. The exact
versioned asset URL must come from the release page; it is intentionally not guessed here.

## 2. Build and run

```bash
docker build -t provider:test .
docker run -d -p 80:80 -p 81:81 --name provider provider:test
```

If those host ports are occupied, change only the host side of each mapping or configure Gateway
ports explicitly.

## 3. Verify

Inspect container logs for type discovery and successful publication, then open
`http://localhost:81/GV` and invoke a method.

## 4. Supply project identity safely

For stable project-backed publication, pass `GC_PROJECT_KEY` through the deployment platform's secret
mechanism. The environment variable overrides `--projectKey`. Do not bake the key into the image.

**Gap:** no Docker recipe is verified here for every Gateway runtime or CPU
architecture. Base images must include the provider runtime and native dependencies for that runtime.

## Next steps

- [Environment and configuration](../operations/environment-configuration.md)
- [Health checks](../operations/health-checks.md)
- [Ports and protocols](../reference/ports-protocols.md)

## Source anchors

- [Expose a .NET backend: Dockerfile and run commands](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/dotnet.md#step-3-host-it-with-graftcode-gateway)
- `graftcode-gateway/README.md`, “Environment variables”
