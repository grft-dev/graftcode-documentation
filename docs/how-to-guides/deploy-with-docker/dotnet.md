---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---

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

**Gap:** Docker recipes for every runtime are not verified in this documentation set.
