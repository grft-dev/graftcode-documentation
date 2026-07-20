---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---
Host Gateway in a container with your provider artifacts and the Linux `gg` package from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

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
CMD ["gg", "--modules", "Provider.dll"]
```

```bash
docker build -t provider:test .
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name provider provider:test
```

## Other runtimes (illustrative)

Use a base image that includes your runtime, install `gg`, copy provider artifacts, and expose ports
`80` and `81`. Host locally first with [Run Gateway locally](run-gateway-locally.md), then
containerize the same `gg` command line.

```multi
```javascript
CMD ["gg", "--runtime", "nodejs", "--modules", "./dist/index.js"]
```
```python
CMD ["gg", "--runtime", "python", "--modules", "./pricing/"]
```
```java
CMD ["gg", "--runtime", "jvm", "--modules", "./target/pricing-1.0.0.jar"]
```
```php
CMD ["gg", "--runtime", "php", "--modules", "./src/"]
```
```ruby
CMD ["gg", "--runtime", "ruby", "--modules", "./lib/"]
```
```

**Gap:** verified multi-stage Dockerfiles for every runtime are not maintained in this documentation
set.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Use a project key](project-key.md)
- [Networking and ports](../operations/networking-ports.md)

## Source anchors

- `graftcode-gateway/README.md`
- [Quick Start — expose backend](https://github.com/grft-dev/graftcode-quick-start-guide/tree/main/2-expose-backend)
