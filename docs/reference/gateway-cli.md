---
title: "Gateway CLI reference"
description: "Verified common options for the Graftcode Gateway command-line interface."
---

# Gateway CLI reference

Run `gg --help` (`gg.exe --help` on Windows) for the installed release. Pass the built module as the
first positional argument:

```bash
gg ./path/to/module.dll
```

Without a module path, Gateway scans the current directory and attempts runtime detection. All
options below are optional.

| Option | Verified behavior |
| --- | --- |
| first positional argument | Main module path (preferred) |
| `--modules` | Comma-separated module paths (alternative to the positional argument) |
| `--runtime` | `auto`, `clr`, `netcore`, `java`, `jvm`, `python`, `python27`, `ruby`, `nodejs`, `php`, `perl` |
| `--projectKey` | Portal project JWT; overridden by `GC_PROJECT_KEY` |
| `--endpoint` | Metadata/service-model endpoint; default `https://grft.dev`, overridden by `GSMU_ENDPOINT` |
| `--port` | WebSocket port; default `80` |
| `--httpPort` | Vision HTTP port; default `81` |
| `--tcpServer` / `--tcpPort` | Enable TCP; default port `82` |
| `--http2Server` / `--http2Port` | Enable HTTP/2; default port `83` |
| `--GV` | Host Vision; default on |
| `--types` | Comma-separated hosted type names |
| `--methods` | Comma-separated hosted method names |
| `--runApp` | Run the application entry point |
| `--mcpBaseClass` | Declaring type FQN for MCP `tools/call` resolution |
| `--corsAllowedOrigins` | Comma-separated CORS origins or `*` |
| `--corsConfig` | CORS `key=value` file; file values can override CLI defaults |
| `--useContext` | Expose request context/headers to hosted code |
| `--noVersioning` | Disable hosted-module versioning |
| `--keepVersioning` | Enable versioning (default `true`; standalone disables unless set) |
| `--doNotExtractBinaries` | Use externally supplied binaries |
| `--config` | External server-plugin JSON path |

No stable `--health`, metrics, drain, reload, TLS-certificate, or global invocation-timeout option is
documented in the inspected README.

## Next steps

- [Run Gateway locally](../how-to-guides/run-gateway-locally.md)
- [Environment variables](environment-variables.md)
- [Ports and protocols](ports-protocols.md)
