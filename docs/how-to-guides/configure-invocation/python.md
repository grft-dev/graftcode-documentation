---
title: "Configure Graft invocation"
description: "Select in-memory or remote execution and configure generated GraftConfig before first use."
articleTitle: "Configure Graft invocation"
---

Point an installed Python Graft at the intended provider.

## 1. Choose execution mode

- `inmemory` loads the provider module in the consumer process.
- `ws://` or `wss://` sends calls to a remote Gateway WebSocket endpoint.
- TCP and HTTP/2 are optional Gateway transports and must be explicitly enabled.

## 2. Configure before the first call

Python uses class attributes on the generated config type:

```python
from <generated_package_path>.graft_config import GraftConfig

GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
```

Copy the import paths and endpoint from Vision. The generated runtime context is cached after
initialization; configure it before the first generated call.

## 3. Pick the state model deliberately

Prefer static methods and stateless calls for independently routable operations. Instance methods and
remote object identity are stateful; they require connection/session affinity and can be lost on
Gateway restart or scale-in.

## 4. Use another configuration source only when needed

Generated packages inspect multiple configuration source levels. Earlier levels win in the inspected
resolver. Copy exact field names from the generated package.

**Gap:** exact field names and supported transport connection strings outside generated .NET and
Node.js packages must be taken from Vision output.

## Next steps

- [Configuration keys and precedence](../../reference/configuration-keys-precedence.md)
- [Networking and ports](../../operations/networking-ports.md)
- [Scale Gateway instances](../../operations/scaling.md)

## Source anchors

- `graftcode-code-generator` Python config templates and tests
