---
title: "Configure Graft invocation"
description: "Select in-memory or remote execution and configure generated GraftConfig before first use."
articleTitle: "Configure Graft invocation"
---
# Configure Graft invocation

Point an installed Graft at the intended Receiver.

The `GraftConfig` **host** is the runtime endpoint that executes your calls. It is **not** the
registry URL used to install the Graft — see
[Project Key, registry, host, and credentials](../reference/project-key-registry-host-and-credentials.md).

## 1. Choose execution mode

- `inmemory` loads the Receiver module in the Caller process.
- `ws://` or `wss://` sends calls to a remote Gateway WebSocket endpoint.
- TCP and HTTP/2 are optional Gateway transports and must be explicitly enabled.

Many generated Grafts default to `inmemory`. Confirm the default for your package in Vision.

## 2. Configure before the first call

Set `host` and `stateless` programmatically **before** the first generated call. Copy imports and
field names from Vision—the generated runtime context is cached after initialization.

```multi
```dotnet
using <generated_namespace>;

GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```
```javascript
import { GraftConfig } from "<package-copied-from-vision>";

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```python
from <generated_package_path>.graft_config import GraftConfig

GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
```
```java
import <generated_package>.GraftConfig;

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

## 3. Pick the state model deliberately

Prefer static methods and stateless calls for independently routable operations. Instance methods and
remote object identity are stateful; they require connection/session affinity and can be lost on
Gateway restart or scale-in.

## 4. Use another configuration source only when needed

Generated packages inspect multiple configuration source levels (environment, files, programmatic
settings, then library defaults). Earlier levels win.

## Next steps

- [Stateless vs stateful](stateless-vs-stateful-graft-calls.md)
- [Configuration keys and precedence](../reference/configuration-keys-and-precedence.md)
- [Networking and ports](../operations/networking-and-ports.md)
- [Scale Gateway instances](../operations/scaling-gateway-receivers.md)
