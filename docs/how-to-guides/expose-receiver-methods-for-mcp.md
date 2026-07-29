---
title: Expose Receiver methods for MCP
description: Host a module with MCP support and resolve tool calls with --mcpBaseClass.
articleTitle: Expose Receiver methods for MCP
---
# Expose Receiver methods for MCP

Gateway can participate in MCP workflows when the deployment enables the relevant HTTP surfaces and
CORS settings. This is an **Alpha** area—verify behavior on your Gateway release.

## 1. Host the Receiver

```multi
```dotnet
dotnet build ./Pricing/Pricing.csproj
gg ./Pricing/bin/Debug/net9.0/Pricing.dll --types Pricing.PriceService --methods Calculate
```
```javascript
npm ci && npm run build
gg ./dist/index.js --types PriceService --methods calculate
```
```python
gg ./pricing/ --types PriceService --methods calculate
```
```java
mvn package
gg ./target/pricing-1.0.0.jar --types com.example.PriceService --methods calculate
```
```php
composer install
gg ./src/ --types PriceService --methods calculate
```
```ruby
bundle install
gg ./lib/ --types PriceService --methods calculate
```
```

## 2. Set MCP base class

When MCP `tools/call` uses a bare method name and `params.class` is empty, Gateway can resolve the
declaring type from `--mcpBaseClass`:

```bash
gg <module> \
  --mcpBaseClass <fully-qualified-type-name>
```

Use the fully qualified type name for your runtime (for example `Pricing.PriceService`, `com.app.Util`,
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
gg <module> --corsConfig ./cors.config
```

List explicit origins. Do not use a wildcard (`*`) origin in production, and keep
`allowCredentials=false` unless a specific origin requires credentials.

## 4. Verify

Confirm types in Vision, exercise an MCP client against the Gateway HTTP surface, and treat
authorization as explicit application work.

For the complete end-to-end flow, follow the
[MCP Quick Start](https://docs.graftcode.com/quick-start/expose-mcp). See
[Known limitations](../reference/known-limitations.md) for current MCP status and constraints.

## Next steps

- [Filter the callable surface](filter-the-callable-surface.md)
- [Networking and ports](../operations/networking-and-ports.md)
