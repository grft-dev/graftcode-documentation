---
title: Authenticate Graft calls
description: Pass tokens to remote providers using headers or supported method parameters.
articleTitle: Authenticate Graft calls
---
Gateway `--projectKey` authenticates **publication**, not each invocation. A **call credential**
authorizes one specific call and is validated inside provider methods or through generated header
APIs. See [Project Key, registry, host, and credentials](../reference/identifiers-and-auth.md) for how
this differs from the Project Key, registry URL, and runtime host.

## Option 1: token as a method parameter

Pass `apiKey` or `bearerToken` as a supported primitive parameter and validate before side effects.
This works in every runtime and in browser clients.

## Option 2: generated headers

```multi
```dotnet
using <generated_namespace>;

GraftConfig.Host = "wss://service.example/ws";
GraftConfig.Stateless = true;
GraftConfig.SetHeaders(new Dictionary<string, string> {
    ["Authorization"] = "Bearer <token>"
});

var result = PriceService.Calculate(100, 10);
```
```javascript
import { GraftConfig, PriceService } from "<package-from-vision>";

GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders({ Authorization: "Bearer <token>" });

const result = await PriceService.calculate(100, 10);
```
```python
from <generated_package_path>.graft_config import GraftConfig
from <generated_service_path> import PriceService

GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = True
# Header APIs vary by generated package; copy from Vision.

price = PriceService.calculate(100.0, 10.0)
```
```java
import <generated_package>.GraftConfig;
import <generated_package>.PriceService;

GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders(java.util.Map.of("Authorization", "Bearer <token>"));

double price = PriceService.calculate(100, 10);
```
```php
GraftConfig::$host = 'wss://service.example/ws';
GraftConfig::$stateless = true;
GraftConfig::setHeaders(['Authorization' => 'Bearer <token>']);

$price = PriceService::calculate(100, 10);
```
```ruby
GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = true
# Copy header helper names from the generated gem.

price = PriceService.calculate(100, 10)
```
```

Configure `host` and headers **before** the first generated call. Browser WebSocket clients cannot
set arbitrary handshake headers; use the HTTP/2 configuration emitted by Vision when required.

## Provider-side validation

Default deny: reject missing or invalid tokens with a clear domain exception. Do not log secrets.

## Next steps

- [Authentication operations](../operations/authentication-authorization.md)
- [Configure invocation](configure-invocation.md)
