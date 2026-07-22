---
title: "Environment and configuration"
description: "Separate Gateway process settings from generated Graft invocation configuration."
---

# Environment and configuration

Gateway CLI/environment settings and Caller `GraftConfig` are separate configuration domains.

## Gateway process

Gateway environment variables are:

- `GG_DEBUG`: `1` or `TRUE` enables byte-traffic console logging;
- `GSMU_ENDPOINT`: legacy public variable name that overrides the Graftcode Engine endpoint (`--endpoint`);
- `GC_PROJECT_KEY`: overrides `--projectKey`.

Store `GC_PROJECT_KEY` as a secret. Avoid `GG_DEBUG` in production because byte-level traffic can
contain sensitive invocation data.

CLI controls module/runtime selection, listener ports, optional servers, Vision, type filtering,
CORS, context, versioning, and plugin configuration. Use `gg --help` for the installed release.

## Generated Caller package

Generated packages resolve six configuration levels, from highest to lowest priority:

1. graft-specific environment variable;
2. global environment variable;
3. graft-specific file;
4. global file;
5. programmatic user configuration;
6. generated library default.

Configure before the first call because the runtime context is cached.

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

There is no single complete catalog of environment variables for every Gateway plugin or generated
runtime. Plugin config keys are plugin-specific; confirm them for the plugin you use.

## Next steps

- [Environment variable reference](../reference/environment-variables.md)
- [Configuration precedence](../reference/configuration-keys-precedence.md)
- [Authentication and authorization](authentication-authorization.md)
