---
title: "Run Gateway locally"
description: "Start Graftcode Gateway against a built module and verify discovery and publication."
---

# Run Gateway locally

## Goal

Host a built provider on a development machine.

## 1. Install Gateway

Download the current release for the host operating system from the
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases) page. Do not invent a
download URL for an unlisted platform.

## 2. Build the provider

Build or publish the actual module and install its runtime dependencies. Gateway supports explicit
module and runtime selection:

```bash
gg --runtime netcore --modules ./path/to/Provider.dll
```

On Windows, use `gg.exe`. `gg --help` is the authority for the installed release.

Gateway can scan the current directory and auto-detect the runtime, but explicit values are safer in
directories that contain unrelated files. A module path can also be the first positional argument.

## 3. Avoid local port conflicts

Defaults are WebSocket `80` and Vision HTTP `81`. Use non-privileged custom ports when required:

```bash
gg ./path/to/Provider.dll --port 8080 --httpPort 8081
```

## 4. Verify startup

Confirm that:

1. the intended runtime was selected;
2. the expected types were enabled;
3. model upload/publication succeeded;
4. Vision loads on the configured HTTP port;
5. an invocation succeeds before sharing an install command.

Stop the process with the host's normal process-management mechanism. No dedicated reload or
zero-downtime lifecycle command is documented.

## Next steps

- [Gateway lifecycle](../operations/gateway-lifecycle.md)
- [Obtain and install a Graft](obtain-install-graft.md)
- [Gateway CLI reference](../reference/gateway-cli.md)

## Source anchors

- `graftcode-gateway/README.md`, “Usage,” “Examples,” and “Known issues”
- [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases)
