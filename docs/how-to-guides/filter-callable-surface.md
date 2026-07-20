---
title: Filter the callable surface
description: Limit which types and methods Gateway hosts using --types and --methods.
articleTitle: Filter the callable surface
---
Narrow the **callable surface** before consumers install a Graft. Use Gateway flags plus an
intentional public API in source code.

## CLI filters

| Flag | Purpose |
| --- | --- |
| `--types` | Comma-separated type names to expose |
| `--methods` | Comma-separated method names to expose |

Example by runtime:

```multi
```dotnet
dotnet build ./Pricing/Pricing.csproj
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll --types Pricing.PriceService --methods Calculate
```
```javascript
npm ci && npm run build
gg --runtime nodejs --modules ./dist/index.js --types PriceService --methods calculate
```
```python
gg --runtime python --modules ./pricing/
```
```java
mvn package
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```
```php
composer install
gg --runtime php --modules ./src/
```
```ruby
bundle install
gg --runtime ruby --modules ./lib/
```
```

Combine with `--GMA` when you need analyzer output without starting servers:

```bash
gg --graftOnly --runtime <runtime> --modules <module> --types <Type> --methods <Method>
```

Analyzer-level method filters also exist for some runtimes (wildcard patterns). See
[Callable surface](../core-concepts/callable-surface.md).

## Workflow

1. Start with the smallest public API in code (internal helpers stay non-public).
2. Add `--types` / `--methods` when Gateway would otherwise discover too much.
3. Open Vision and confirm only intended members appear.
4. Generate and smoke-test the consumer package.

## Next steps

- [Expose code](../expose-code.md)
- [Dependency injection facade](dependency-injection.md)
- [Gateway CLI reference](../reference/gateway-cli.md)
