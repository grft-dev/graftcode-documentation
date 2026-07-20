---
title: "Authenticate Graft calls"
description: "Pass tokens to remote providers using headers or supported method parameters."
articleTitle: "Authenticate Graft calls"
---

Gateway `--projectKey` authenticates **publication**, not each invocation. Validate credentials inside
provider methods or through generated header APIs.

## Option 1: token as a method parameter

Pass `apiKey` or `bearerToken` as a supported primitive parameter and validate before side effects.
This works in every runtime and in browser clients.

## Option 2: generated headers

```typescript
import { GraftConfig, PriceService } from "<package-from-vision>";

GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders({ Authorization: "Bearer <token>" });

const result = await PriceService.calculate(100, 10);
```

Configure `host` and headers **before** the first generated call. Browser WebSocket clients cannot
set arbitrary handshake headers; use the HTTP/2 configuration emitted by Vision when required.

## Provider-side validation

Default deny: reject missing or invalid tokens with a clear domain exception. Do not log secrets.

## Next steps

- [Authentication operations](../../operations/authentication-authorization.md)
- [Configure invocation](../configure-invocation)

## Source anchors

- `graftcode-code-generator/` header templates
- `operations/authentication-authorization.md`
