---
title: Set the module path for in-memory execution
description: Configure modules and GraftConfig.module when host is inmemory.
articleTitle: Set the module path for in-memory execution
---
`host=inmemory` loads the Receiver in the Caller process. The Caller must resolve the Receiver
artifact locally.

## Configuration file example

`graftcode-config.json`:

```json
{
  "configurations": {
    "default": {
      "name": "default",
      "runtime": "<runtime>",
      "modules": "<Receiver-artifact-path>",
      "host": "inmemory",
      "stateless": true
    }
  }
}
```

## Programmatic configuration

```multi
```dotnet
GraftConfig.Host = "inmemory";
GraftConfig.Module = "Pricing.dll"; // copy exact module id from generated package / Vision
```
```javascript
GraftConfig.host = "inmemory";
// Ensure the Receiver JS module is resolvable on disk; copy module path from Vision.
```
```python
GraftConfig.host = "inmemory"
GraftConfig.module = "<module-path-from-generated-package>"
```
```java
GraftConfig.host = "inmemory";
GraftConfig.module = "<module-path-from-generated-package>";
```
```php
GraftConfig::$host = 'inmemory';
GraftConfig::$module = '<module-path-from-generated-package>';
```
```ruby
GraftConfig.host = "inmemory"
GraftConfig.module = "<module-path-from-generated-package>"
```
```

If you see `FileNotFound` for the Receiver module, the client remained in `inmemory` without a
resolvable module path. See [Errors reference](../reference/errors-status.md).

## Next steps

- [Configure invocation](configure-invocation.md)
- [Execution modes](../core-concepts/execution-modes.md)
