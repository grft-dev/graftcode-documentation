---
title: "Set the module path for in-memory execution"
description: "Configure modules and GraftConfig.module when host is inmemory."
articleTitle: "Set the module path for in-memory execution"
---

`host=inmemory` loads the provider in the consumer process. The consumer must resolve the provider
artifact locally.

## Configuration file example

`graftcode-config.json`:

```json
{
  "configurations": {
    "default": {
      "name": "default",
      "runtime": "<runtime>",
      "modules": "<provider-artifact-path>",
      "host": "inmemory",
      "stateless": true
    }
  }
}
```

## Programmatic configuration

```php
GraftConfig::$host = 'inmemory';
GraftConfig::$module = '<module-path-from-generated-package>';
```

If you see `FileNotFound` for the provider module, the client remained in `inmemory` without a
resolvable module path. See [Errors reference](../../reference/errors-status.md).

## Next steps

- [Configure invocation](../configure-invocation)
- [Execution modes](../../core-concepts/execution-modes.md)

## Source anchors

- `reference/configuration-keys-precedence.md`
