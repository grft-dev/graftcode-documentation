---
title: "Configuration keys and precedence"
description: "Six-level generated GraftConfig resolution order and accepted source formats."
---

# Configuration keys and precedence

Generated Caller packages use this priority order; lower numeric priority wins. .NET and Node.js are
fully covered; other runtimes follow the same conceptual levels—confirm field names and helpers in the
installed package:

| Priority | Source | Generated source name |
| --- | --- | --- |
| 1 | Runtime/graft-specific environment | `<graft-name>-config` |
| 2 | Global environment | `graftcode-config` |
| 3 | Runtime/graft-specific file | `<graft-name>-config.json`, `.yaml`, `.txt` |
| 4 | Global file | `graftcode-config.json`, `.yaml`, `.txt` |
| 5 | Programmatic user config | `SetConfig(...)` / `setConfig(...)` |
| 6 | Generated library default | registered by `GraftConfig` |

At equal name and priority, the first added configuration is kept. Relative files resolve from the
application's current working directory.

## Keys

Generated defaults include:

- `name`;
- `runtime`;
- `modules`;
- `host` (`inmemory` by default);
- `stateless` (`false` by default).

JSON and YAML require a top-level `configurations` object. Text accepts semicolon-delimited
connection-string data and requires at least `name` and `runtime`.

Set generated static fields before the first call. The runtime context is cached and no supported
reset/re-resolve operation is exposed by generated packages.

Programmatic remote host example (copy imports and names from Vision):

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

Naming and resolver behavior is not identical for every generated runtime. .NET and Node.js are fully
covered; confirm the installed package for other runtimes.

## Next steps

- [Configure invocation](../how-to-guides/configure-graft-invocation.md)
- [Environment variables](environment-variable-reference.md)
