---
title: "Deploy Gateway with Docker"
description: "Build a Receiver and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---

# Deploy Gateway with Docker

Graftcode does **not** publish a ready-made Gateway image to `docker pull`. You **build your own**
image: a standard runtime base image, your compiled Receiver artifacts, and the Linux `gg` package
from [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

Typical layout:

1. Start from an official runtime image (for example `mcr.microsoft.com/dotnet/sdk:9.0`).
2. Copy and build/publish your Receiver module inside the image.
3. Download and install `gg` inside the image (see [Run Gateway locally](run-gateway-locally.md#1-install-gateway)).
4. Set `CMD` to the same `gg <module>` command you would run on a host.
5. Expose ports `80` (WebSocket) and `81` (Vision).

Host Gateway on a machine first with [Run Gateway locally](run-gateway-locally.md), then
containerize the same command line. The `.NET` example below uses a multi-stage build, a pinned
Gateway version, a non-root user, and a `GET /status` health check.

## Example: .NET Receiver

```dockerfile
# --- build stage ---
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app

# --- runtime stage ---
FROM mcr.microsoft.com/dotnet/aspnet:9.0

# Pin the Gateway release you deploy. Set a checksum when the release publishes one.
ARG GRAFTCODE_GATEWAY_VERSION=1.3.8
# ARG GRAFTCODE_GATEWAY_SHA256=<sha256-from-release-if-published>

RUN apt-get update && apt-get install -y --no-install-recommends wget curl \
 && wget -O /tmp/gg.deb \
      "https://github.com/grft-dev/graftcode-gateway/releases/download/${GRAFTCODE_GATEWAY_VERSION}/gg_linux_amd64.deb" \
 # && echo "${GRAFTCODE_GATEWAY_SHA256}  /tmp/gg.deb" | sha256sum -c - \
 && dpkg -i /tmp/gg.deb && rm /tmp/gg.deb \
 && apt-get purge -y wget && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=build /app /app

# Run as a non-root user.
RUN useradd --system --uid 10001 gateway && chown -R gateway:gateway /app
USER gateway

EXPOSE 80 81

# Liveness: Gateway serves GET /status on the HTTP port (81).
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:81/status || exit 1

CMD ["gg", "Receiver.dll"]
```

```bash
docker build --build-arg GRAFTCODE_GATEWAY_VERSION=1.3.8 -t receiver:1.0.0 .
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name receiver receiver:1.0.0
```

Operational notes:

- **Pin the version.** Build against a specific `GRAFTCODE_GATEWAY_VERSION`, not a floating "latest",
  so images are reproducible. Add the `sha256sum -c` step once the release publishes a checksum.
- **Secrets.** Inject `GC_PROJECT_KEY` at runtime (environment or secret store); do not bake it into
  the image.
- **Vision exposure.** Port `81` serves Vision and `/status`. Do not expose it publicly in production;
  restrict it to your network or an internal health check.
- **Graceful termination.** Ensure your orchestrator sends `SIGTERM` and allows the process to exit
  cleanly; pin Receiver dependencies in your build so the runtime image is deterministic.

## Other runtimes (illustrative)

Use a base image that includes your runtime, install `gg`, copy Receiver artifacts, and expose ports
`80` and `81`. Host locally first with [Run Gateway locally](run-gateway-locally.md), then
containerize the same `gg` command line.

```multi
```javascript
CMD ["gg", "./dist/index.js"]
```
```python
CMD ["gg", "./pricing/"]
```
```java
CMD ["gg", "./target/pricing-1.0.0.jar"]
```
```php
CMD ["gg", "./src/"]
```
```ruby
CMD ["gg", "./lib/"]
```
```

Complete multi-stage Dockerfiles for every runtime are not maintained here. Apply the same pattern:
multi-stage build, pinned Gateway version, non-root user, and a `GET /status` health check.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Use a project key](use-a-portal-project-key.md)
- [Networking and ports](../operations/networking-and-ports.md)
