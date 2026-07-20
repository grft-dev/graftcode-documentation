---
title: "Configure Graft invocation"
description: "Select in-memory or remote execution and configure generated GraftConfig before first use."
articleTitle: "Configure Graft invocation"
---

Point an installed PHP Graft at the intended provider.

## 1. Choose execution mode

- `inmemory` loads the provider in the consumer process.
- `ws://` or `wss://` sends calls to a remote Gateway WebSocket endpoint.

## 2. Configure before the first call

```php
GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;
```

Copy import paths from Vision. Configure before the first generated call.

## 3. State model

Prefer static methods for remote routing. Instance methods require session affinity.

## Next steps

- [Configuration keys and precedence](../../reference/configuration-keys-precedence.md)
- [Stateless vs stateful](../stateless-vs-stateful)

## Source anchors

- [PHP language guide](../../language-guides/php.md)
