---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---

Use a base image that includes the Ruby runtime and install the Linux `gg` package from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

```dockerfile
# Illustrative — pin Gateway version and base image for production
# COPY provider artifacts, install gg.deb, EXPOSE 80 81
CMD ["gg", "--runtime", "ruby", "--modules", "<module-path>"]
```

Host locally first with [Run Gateway locally](../run-gateway-locally), then containerize the same
`gg` command line.

**Gap:** no verified multi-stage Dockerfile for Ruby is maintained here.
