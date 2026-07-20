---
title: "Environment and configuration"
description: "Separate Gateway process settings from generated Graft invocation configuration."
---

# Environment and configuration

Gateway CLI/environment settings and consumer `GraftConfig` are separate configuration domains.

## Gateway process

Verified Gateway environment variables are:

- `GG_DEBUG`: `1` or `TRUE` enables byte-traffic console logging;
- `GSMU_ENDPOINT`: overrides the `--endpoint` value;
- `GC_PROJECT_KEY`: overrides `--projectKey`.

Store `GC_PROJECT_KEY` as a secret. Avoid `GG_DEBUG` in production because byte-level traffic can
contain sensitive invocation data.

CLI controls module/runtime selection, listener ports, optional servers, Vision, type filtering,
CORS, context, versioning, and plugin configuration. Use `gg --help` for the installed release.

## Generated consumer package

Generated .NET and Node.js packages resolve six levels, from highest to lowest priority:

1. graft-specific environment variable;
2. global environment variable;
3. graft-specific file;
4. global file;
5. programmatic user configuration;
6. generated library default.

Configure before the first call because the runtime context is cached.

**Gap:** no complete, stable environment-variable catalog is verified for every Gateway plugin or
generated runtime. Plugin config keys are plugin-specific.

## Next steps

- [Environment variable reference](../reference/environment-variables.md)
- [Configuration precedence](../reference/configuration-keys-precedence.md)
- [Authentication and authorization](authentication-authorization.md)

## Source anchors

- `graftcode-gateway/README.md`, “Environment variables”
- `HYPERTUBE/src/netcore/Hypertube.Netcore.Sdk/Configuration/ConfigPriority.cs`
- `HYPERTUBE/src/js/hypertube-nodejs-sdk/lib/sdk/configuration/ConfigPriority.js`
- generated `GraftConfig` templates in `graftcode-code-generator/`
