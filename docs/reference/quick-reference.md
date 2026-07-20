---
title: "Quick Reference"
description: "Verified Gateway, package installation, invocation, ports, and troubleshooting shortcuts."
---

# Quick reference

## Provider

Build a plain module, then host the actual artifact:

```bash
gg --runtime <runtime> --modules <built-module>
```

Use `gg.exe` on Windows. Supported CLI runtime names and version baselines are listed in
[Gateway CLI](gateway-cli.md). Confirm discovery and successful publication before installation.

## Install a Graft

Open the running Gateway's Vision UI, choose the consumer package manager, and copy the entire install
command. Never guess or reuse an example registry URL, identifier, package name, import, or version.

## Configure a remote call

.NET generated packages use fields:

```csharp
GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```

Node.js generated packages use lower-case fields:

```typescript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```

Copy the host from Vision and configure before the first call. The default is `inmemory`, which
requires the provider module to be locally loadable.

## Ports

- `80`: WebSocket calls, enabled by default;
- `81`: Vision HTTP, enabled by default;
- `82`: TCP, only with `--tcpServer`;
- `83`: HTTP/2, only with `--http2Server`.

All ports are configurable.

## Configuration priority

Highest to lowest in the inspected generated .NET and Node.js packages:

1. graft-specific environment;
2. global environment;
3. graft-specific file;
4. global file;
5. programmatic user configuration;
6. generated library default.

## Frequent failures

- Provider `FileNotFound`: remote host was not configured; `inmemory` tried to load the module.
- No types: pass explicit `--runtime` and `--modules`; verify public/exported members.
- Install `404`: repeat the exact registry-qualified command from the current Vision instance.
- Package generation `422`: remove the named framework complex type from every public signature and
  public model member.
- State lost after restart/scale-in: recreate the remote object or redesign as static/stateless.

## Operations

- Store `GC_PROJECT_KEY` as a secret; it overrides `--projectKey`.
- Use `GG_DEBUG` only for controlled diagnosis because it logs byte traffic.
- No built-in stable health or metrics endpoint is documented.
- Pin and test Gateway plus generated packages together; Alpha has no cross-major compatibility
  guarantee.

## Detailed references

- [Gateway CLI](gateway-cli.md)
- [Configuration keys and precedence](configuration-keys-precedence.md)
- [Environment variables](environment-variables.md)
- [Supported runtimes and package managers](supported-runtimes-package-managers.md)
- [Type matrix](type-matrix.md)
- [Errors and status](errors-status.md)
- [Generated package structure](generated-package-structure.md)
- [Ports and protocols](ports-protocols.md)
- [Known limitations](known-limitations.md)

## Next steps

- [Expose code](../how-to-guides/expose-code)
- [Run Gateway locally](../how-to-guides/run-gateway-locally)
- [Use a project key](../how-to-guides/project-key)
- [Gateway versioning](../how-to-guides/gateway-no-versioning)
- [Filter callable surface](../how-to-guides/filter-callable-surface)
- [Authenticate Graft calls](../how-to-guides/authenticate-graft-calls)
- [Debug invocations](../how-to-guides/debug-graft-invocations)
- [Operations and deployment model](../operations/index.md)

## Source anchors

- `graftcode-gateway/README.md`
- generated `GraftConfig` templates in `graftcode-code-generator/`
- `HYPERTUBE/src/*/Configuration/ConfigPriority.*`
- `graftcode-package-manager-gateway/src/jvm/src/test/java/com/graftcode/gpmg/integration/SoennekerExtensionsTypeArrayIntegrationTest.java`
