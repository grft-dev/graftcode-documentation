---
title: "Quick Reference"
description: "Gateway, package installation, invocation, ports, and troubleshooting shortcuts."
---

# Quick reference

## Receiver

Install **Graftcode Gateway** (`gg`) from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases) before hosting a module.
See [Run Gateway locally](../how-to-guides/run-gateway-locally.md#1-install-gateway).

Build a plain module, then host the actual artifact:

```bash
gg <path-to-built-module>
```

Use `gg.exe` on Windows. Supported CLI runtime names and version baselines are listed in
[Gateway CLI](gateway-cli.md). Confirm discovery and successful publication before installation.

## Install a Graft

**Public packages:** install from the Graftcode registry at `https://grft.dev` (Maven:
`https://grft.dev/maven2/`, pip: `https://grft.dev/simple/`) using documented package coordinates.
See [Obtain and install a Graft](../how-to-guides/obtain-install-graft.md#install-a-public-graft) for
sample packages and commands.

**Your own Receiver:** open the running Gateway's Vision UI, choose the Caller package manager, and
copy the entire install command. Never guess or reuse an example registry URL, identifier, package
name, import, or version.

Example shapes by runtime (copy the **complete** command from Vision, not these placeholders):

```multi
```dotnet
dotnet add package <package-id> --version <version> -s <registry-from-vision>
```
```javascript
npm install <package> --registry <registry-from-vision>
```
```python
python -m pip install <package> --extra-index-url <url-from-vision>
```
```java
# Copy the Maven or Gradle dependency block from Vision
```
```php
composer require <vendor/package>:<version> --repository <repo-from-vision>
```
```ruby
gem install <name> --source <source-from-vision>
```
```

## Configure a remote call

Generated packages expose `host` and `stateless` configuration (field names, casing, and access differ
by runtime). Copy the exact API from Vision and set it **before** the first generated call. The default
is `inmemory`, which requires the Receiver module to be locally loadable. The `host` is the runtime
endpoint, **not** the registry URL — see
[Project Key, registry, host, and credentials](identifiers-and-auth.md).

```multi
```dotnet
GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```
```javascript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```python
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
```
```java
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```php
GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;
```
```ruby
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true
```
```

Use `ws://` or `wss://` for remote Gateway WebSocket endpoints. See
[Configure invocation](../how-to-guides/configure-invocation.md) for imports and file/env sources.

## Ports

- `80`: WebSocket calls, enabled by default;
- `81`: Vision HTTP, enabled by default;
- `82`: TCP, only with `--tcpServer`;
- `83`: HTTP/2, only with `--http2Server`.

All ports are configurable.

## Configuration priority

Generated packages resolve configuration in this order (highest wins first). .NET and
Node.js are fully covered; other runtimes follow the same conceptual levels—confirm field
names in the installed package:

1. graft-specific environment;
2. global environment;
3. graft-specific file;
4. global file;
5. programmatic user configuration;
6. generated library default.

## Frequent failures

- Receiver `FileNotFound`: remote host was not configured; `inmemory` tried to load the module.
- No types: pass the built module path explicitly; verify public/exported members.
- Install `404`: repeat the exact registry-qualified command from the current Vision instance.
- Package generation `422`: remove the named framework complex type from every public signature and
  public model member.
- State lost after restart/scale-in: recreate the remote object or redesign as static/stateless.

## Operations

- Store `GC_PROJECT_KEY` as a secret; it overrides `--projectKey`.
- Use `GG_DEBUG` only for controlled diagnosis because it logs byte traffic.
- Gateway provides `GET /status` for liveness. It does not provide a dedicated readiness or metrics
  endpoint unless a newer product version explicitly adds one.
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

- [Expose code](../how-to-guides/expose-code.md)
- [Run Gateway locally](../how-to-guides/run-gateway-locally.md)
- [Use a project key](../how-to-guides/project-key.md)
- [Gateway versioning](../how-to-guides/gateway-no-versioning.md)
- [Filter callable surface](../how-to-guides/filter-callable-surface.md)
- [Authenticate Graft calls](../how-to-guides/authenticate-graft-calls.md)
- [Debug invocations](../how-to-guides/debug-graft-invocations.md)
- [Operations and deployment model](../operations/index.md)
