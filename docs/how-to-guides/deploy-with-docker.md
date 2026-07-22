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
containerize the verified command line. The `.NET` workflow below is a complete reference.

## Verified .NET workflow

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0
WORKDIR /usr/app
COPY . /usr/app/
RUN dotnet build && dotnet publish -c Release -o /usr/app/
RUN apt-get update && apt-get install -y wget \
 && wget -O /usr/app/gg.deb https://github.com/grft-dev/graftcode-gateway/releases/latest/download/gg_linux_amd64.deb \
 && dpkg -i /usr/app/gg.deb && rm /usr/app/gg.deb \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 80 81
CMD ["gg", "Receiver.dll"]
```

```bash
docker build -t Receiver:test .
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name Receiver Receiver:test
```

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

**Gap:** verified multi-stage Dockerfiles for every runtime are not maintained in this documentation
set.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Use a project key](project-key.md)
- [Networking and ports](../operations/networking-ports.md)
