---
title: "Configuration resolution"
description: "The generated GraftConfig sources, priority order, supported formats, and initialization behavior."
---

# Configuration resolution

Generated .NET and Node.js Grafts include `GraftConfig`. On first initialization, it loads known sources, registers a package default, and asks Hypertube for the named configuration.

## Priority order

The inspected SDK resolves lower enum values first:

1. runtime-specific environment variable;
2. global environment variable;
3. runtime-specific file;
4. global file;
5. user configuration supplied through `SetConfig`/`setConfig`;
6. generated library default.

This order means environment and file sources override a programmatic user configuration in the current implementation. At the same name and priority, the first added configuration wins.

## Generated source names

Generated templates attempt:

- `<graft-name>-config` environment variable;
- `graftcode-config` environment variable;
- `<graft-name>-config.json`, `.yaml`, or `.txt`;
- `graftcode-config.json`, `.yaml`, or `.txt`.

Relative file paths resolve from the application's current working directory. The generated default uses the package's graft name, runtime, module, `Host`/`host` (default `inmemory`), and `Stateless`/`stateless`.

## Accepted content

The resolver accepts JSON, YAML, or semicolon-delimited connection-string data. JSON and YAML use a top-level `configurations` object. A connection string requires at least `name` and `runtime`; normal generated defaults also specify `modules`, `host`, and `stateless`.

## Initialization timing

`GraftConfig` caches its runtime context. Change static configuration fields or add sources before the first generated call. The inspected templates do not expose a supported reset/re-resolve operation.

## Evidence

Verified against generated config templates, `ConfigPriority`, `ConfigsDictionary`, resolver implementations, and `ConfigSourceResolverTests` in .NET and Node.js Hypertube SDKs.
