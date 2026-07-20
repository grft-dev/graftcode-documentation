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
is `inmemory`, which requires the provider module to be locally loadable.

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

Inspected generated packages resolve configuration in this order (highest wins first). .NET and
Node.js templates are fully verified; other runtimes follow the same conceptual levels—confirm field
names in the installed package:

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

- [Expose code](../how-to-guides/expose-code.md)
- [Run Gateway locally](../how-to-guides/run-gateway-locally.md)
- [Use a project key](../how-to-guides/project-key.md)
- [Gateway versioning](../how-to-guides/gateway-no-versioning.md)
- [Filter callable surface](../how-to-guides/filter-callable-surface.md)
- [Authenticate Graft calls](../how-to-guides/authenticate-graft-calls.md)
- [Debug invocations](../how-to-guides/debug-graft-invocations.md)
- [Operations and deployment model](../operations/index.md)

## Source anchors

- `graftcode-gateway/README.md`
- generated `GraftConfig` templates in `graftcode-code-generator/`
- `HYPERTUBE/src/*/Configuration/ConfigPriority.*`
- `graftcode-package-manager-gateway/src/jvm/src/test/java/com/graftcode/gpmg/integration/SoennekerExtensionsTypeArrayIntegrationTest.java`
