---
title: "Environment variable reference"
description: "Verified Gateway process and generated Graft configuration environment variables."
---

# Environment variable reference

## Gateway

| Variable | Values / purpose | Precedence |
| --- | --- | --- |
| `GG_DEBUG` | `1` or `TRUE` logs incoming/outgoing byte traffic | Independent debug switch |
| `GSMU_ENDPOINT` | Graftcode Engine metadata endpoint | Overrides `--endpoint` |
| `GC_PROJECT_KEY` | Portal project JWT | Overrides `--projectKey` |

Treat `GC_PROJECT_KEY` as a secret. `GG_DEBUG` can expose invocation data and should remain off during
normal production operation.

## Generated Grafts

Generated packages (including .NET and Node.js) attempt:

- `<graft-name>-config` at priority 1;
- `graftcode-config` at priority 2.

Their values identify configuration content understood by the Hypertube resolver. JSON/YAML content
uses a top-level `configurations` object; semicolon-delimited connection strings require `name` and
`runtime`.

Environment variables outrank files, programmatic configuration, and generated defaults. Configure them
before the first generated call.

Example programmatic remote host (field names vary—copy from Vision):

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

**Gap:** plugin-specific variables and variables used by the Graftcode Engine are not Gateway runtime
configuration and are intentionally omitted. For runtimes other than .NET and Node.js, verify behavior
in the installed package.

## Next steps

- [Environment and configuration](../operations/environment-configuration.md)
- [Configuration keys and precedence](configuration-keys-precedence.md)
