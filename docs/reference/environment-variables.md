---
title: "Environment variable reference"
description: "Verified Gateway process and generated Graft configuration environment variables."
---

# Environment variable reference

## Gateway

| Variable | Values / purpose | Precedence |
| --- | --- | --- |
| `GG_DEBUG` | `1` or `TRUE` logs incoming/outgoing byte traffic | Independent debug switch |
| `GSMU_ENDPOINT` | Service-model endpoint | Overrides `--endpoint` |
| `GC_PROJECT_KEY` | Portal project JWT | Overrides `--projectKey` |

Treat `GC_PROJECT_KEY` as a secret. `GG_DEBUG` can expose invocation data and should remain off during
normal production operation.

## Generated Grafts

The inspected .NET and Node.js templates attempt:

- `<graft-name>-config` at priority 1;
- `graftcode-config` at priority 2.

Their values identify configuration content understood by the Hypertube resolver. JSON/YAML content
uses a top-level `configurations` object; semicolon-delimited connection strings require `name` and
`runtime`.

Environment variables outrank files, `SetConfig`/`setConfig`, and generated defaults. Configure them
before the first generated call.

**Gap:** plugin-specific variables and variables used by service-model/package-manager components are
not Gateway runtime configuration and are intentionally omitted. Generated runtimes beyond .NET and
Node.js require package-level verification.

## Next steps

- [Environment and configuration](../operations/environment-configuration.md)
- [Configuration keys and precedence](configuration-keys-precedence.md)

## Source anchors

- `graftcode-gateway/README.md`, lines 93–100
- generated `GraftConfig` templates in `graftcode-code-generator/src/netcore/` and `src/nodejs/`
