---
title: "Run Gateway locally"
description: "Start Graftcode Gateway against a built module and verify discovery and publication."
articleTitle: "Run Gateway locally"
---

## 1. Install Gateway

Download from [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

## 2. Build and host

```bash
gg --runtime python --modules ./pricing/
```

Use `gg.exe` on Windows. Prefer explicit `--runtime` and `--modules` over auto-scan in crowded directories.

## 3. Custom ports

```bash
gg <module> --port 8080 --httpPort 8081
```

## 4. Verify

Check logs for enabled types and successful publication, then open Vision.

## Next steps

- [Obtain and install a Graft](../obtain-install-graft)
- [Gateway CLI](../../reference/gateway-cli.md)

## Source anchors

- `graftcode-gateway/README.md`
