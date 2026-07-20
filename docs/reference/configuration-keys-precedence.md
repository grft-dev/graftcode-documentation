---
title: "Configuration keys and precedence"
description: "Six-level generated GraftConfig resolution order and accepted source formats."
---

# Configuration keys and precedence

Generated .NET and Node.js packages use this priority order; lower numeric priority wins:

| Priority | Source | Generated source name |
| --- | --- | --- |
| 1 | Runtime/graft-specific environment | `<graft-name>-config` |
| 2 | Global environment | `graftcode-config` |
| 3 | Runtime/graft-specific file | `<graft-name>-config.json`, `.yaml`, `.txt` |
| 4 | Global file | `graftcode-config.json`, `.yaml`, `.txt` |
| 5 | Programmatic user config | `SetConfig(...)` / `setConfig(...)` |
| 6 | Generated library default | registered by `GraftConfig` |

At equal name and priority, the inspected dictionary keeps the first added configuration. Relative
files resolve from the application's current working directory.

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
reset/re-resolve operation is exposed by the inspected templates.

**Gap:** this page does not claim identical naming or behavior for every generated runtime. Verify the
installed package outside .NET and Node.js.

## Next steps

- [Configure invocation](../how-to-guides/configure-invocation)
- [Environment variables](environment-variables.md)

## Source anchors

- `HYPERTUBE/src/netcore/Hypertube.Netcore.Sdk/Configuration/ConfigPriority.cs`
- `HYPERTUBE/src/js/hypertube-nodejs-sdk/lib/sdk/configuration/ConfigPriority.js`
- `graftcode-code-generator/src/netcore/GraftCodeCodeGenerator/Core/Generator/Handler/Utils/GraftConfigClassProvider.cs`
- `graftcode-code-generator/src/nodejs/src/core/generator/templates/config.template.js`
