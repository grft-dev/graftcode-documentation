---
title: "Node.js and TypeScript Language Guide"
description: "Expose JavaScript or TypeScript modules and consume generated Grafts through npm."
---

# Node.js and TypeScript

## Support status and direction

**Provider: supported. Consumer: supported.** Node.js has module analysis, npm package generation, and
cross-runtime public and virtual E2E coverage. TypeScript is supported through compiled JavaScript and
declaration metadata; Node.js is the runtime.

## Prerequisites

- Node.js 22+.
- An npm project whose `main` or `exports` resolves to built JavaScript.
- Type declarations for TypeScript providers.
- A current [Graftcode Gateway](https://github.com/grft-dev/graftcode-gateway/releases).

## Provider support

Expose a plain module, not an Express/Next.js request handler. Build TypeScript before hosting and
point Gateway at the package/module path shown by your project:

```bash
npm ci
npm run build
gg ./dist/index.js
```

The exact module can be a package directory or entry file depending on its metadata. Confirm the
discovered public surface in Vision.

## Consumer support

Node/browser consumers receive an npm package with generated JavaScript and declarations. Generated
remote calls are promise-based; await the top-level call. The generated configuration API uses
`GraftConfig.host` and `GraftConfig.stateless`.

## Package manager

npm. Each generated graft can have its own dynamic registry URL.

## Minimal provider example

```typescript
export class PriceService {
  static calculate(basePrice: number, discountPercent: number): number {
    return basePrice * (1 - discountPercent / 100);
  }
}
```

Export only intentional contract types. Framework request/response objects and infrastructure clients
must remain internal.

## Minimal consumer example

```typescript
import { GraftConfig, PriceService } from "<package-copied-from-vision>";

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;

const price = await PriceService.calculate(100, 15);
console.log(price);
```

Generated names can preserve source casing or adapt cross-runtime conventions. Use package exports and
Vision's snippet rather than guessing.

## Installation

1. Run Gateway against the built provider and wait for successful publication.
2. Open Vision's npm configuration or the npm route emitted by that Gateway.
3. Copy the complete emitted `npm install` command, including `--registry`, package scope, and version.
4. Execute that command unchanged in the consumer.
5. For multiple grafts, install each with the registry emitted for that graft; keep the lockfile.

Never substitute a sample GUID or assume npmjs contains the package.

## Configuration

```typescript
GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
```

Defaults are `host = "inmemory"` and `stateless = false`. In-memory mode loads the provider module
locally; remote mode uses the Gateway endpoint. Configure before the first call. The inspected
generator also provides `setHeaders(...)`, `invokeWithHeaders(...)`, and `setConfig(...)`.

For browsers, WebSocket handshakes cannot carry arbitrary custom headers. If auth headers are needed,
use the HTTP/2 endpoint emitted by Vision and the Gateway context/HTTP2 options; do not invent its URL.

## Supported types

Verified portable baseline:

- `string`, `number`, and `boolean`;
- plain exported object/class shapes;
- homogeneous arrays;
- `Promise<T>` results for consumer-side asynchronous invocation.

Avoid `any`, `unknown`, `Map`, `Set`, typed arrays, `Buffer`, streams, files, callbacks, symbols,
circular objects, framework request/response types, and ORM entities. Prefer ISO-8601 strings for
dates and string IDs.

**Gap:** optional properties, unions, enums, `bigint`, `Date`, and complex generics are not covered by
the simple-car E2E baseline. Verify their generated form before use.

## Runtime-specific limitations

- Build TypeScript first and ensure package metadata points to the emitted JavaScript.
- Generated DTO accessors may be typed as value-or-promise. In stateless mode the object is already
  materialized; await the top-level call, not each local accessor.
- Browser bundlers may need polyfills for Node built-ins used by the generated runtime package.
- Instance methods are stateful remote objects and require affinity; prefer static methods.
- Next.js routes and server actions are adapters, not the Graftcode contract.

## Troubleshooting

- **No methods discovered:** verify exports, declarations, and `main`/`exports`.
- **Package 404 from npmjs:** rerun the exact registry-qualified command from Vision.
- **Old API after reinstall:** restart the dev server; module caches can retain the prior package.
- **Local module load failure:** set `GraftConfig.host` or make the provider module locally resolvable.
- **Browser auth header missing:** use the emitted HTTP/2 configuration; browser WebSockets cannot set
  custom handshake headers.

## Verified samples and tests

- [JavaScript expose-backend Quick Start](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/javascript.md)
- [React consumer Quick Start](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/1-connect-frontend-to-backend/react.md)
- [Cross-runtime simple-car sample](https://github.com/grft-dev/grft-test-simple-car)
- Inspected generated config:
  `graftcode-code-generator/src/nodejs/src/core/generator/templates/config.template.js`
- Inspected E2E caller suite:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/node/`
- Full publish tests:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/node/`

## Known gaps

The inspected tests do not prove every browser/bundler combination or advanced TypeScript type.
Vision's exports and the installed `.d.ts` files are authoritative.
