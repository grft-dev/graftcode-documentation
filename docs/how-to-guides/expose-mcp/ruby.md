---
title: "Expose provider methods for MCP"
description: "Host a module with MCP support and resolve tool calls with --mcpBaseClass."
articleTitle: "Expose provider methods for MCP"
---

Gateway can participate in MCP workflows when the deployment enables the relevant HTTP surfaces and
CORS settings. This is an **Alpha** area—verify behavior on your Gateway release.

## 1. Host the provider

```bash
bundle install
gg --runtime ruby --modules ./lib/
```

## 2. Set MCP base class

When MCP `tools/call` uses a bare method name and `params.class` is empty, Gateway can resolve the
declaring type from `--mcpBaseClass`:

```bash
gg --runtime <runtime> --modules <module> \
  --mcpBaseClass <fully-qualified-type-name>
```

Use the UGM type name form for your runtime (for example `Pricing.PriceService`, `com.app.Util`,
`package.module`, `MyModule::MyClass`).

## 3. Configure CORS for MCP clients

Browser or edge MCP clients may require CORS headers such as `MCP-Protocol-Version` and
`Mcp-Session-Id`. Example `cors.config`:

```ini
allowedOrigins=http://localhost:3000
allowedMethods=GET,POST,PUT,PATCH,DELETE,OPTIONS
allowedHeaders=content-type,authorization,MCP-Protocol-Version,Mcp-Session-Id
exposedHeaders=Mcp-Session-Id,MCP-Protocol-Version
allowCredentials=false
```

Start Gateway with:

```bash
gg --modules <module> --corsConfig ./cors.config
```

## 4. Verify

Confirm types in Vision, exercise an MCP client against the Gateway HTTP surface, and treat
authorization as explicit application work.

**Gap:** no verified end-to-end MCP tutorial is maintained in this documentation set. See
[Known limitations](../../reference/known-limitations.md) and
[When to use Graftcode](../../introduction/when-to-use-graftcode.md).

## Next steps

- [Filter the callable surface](../filter-callable-surface)
- [Networking and ports](../../operations/networking-ports.md)

## Source anchors

- `graftcode-gateway/README.md`, `--mcpBaseClass`, CORS config
