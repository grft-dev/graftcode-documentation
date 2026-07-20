---
title: Run Gateway locally
description: >-
  Start Graftcode Gateway against a built module and verify discovery and
  publication.
articleTitle: Run Gateway locally
---
## 1. Install Gateway

Download from [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

## 2. Build and host

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

Use `gg.exe` on Windows. Prefer explicit `--runtime` and `--modules` over auto-scan in crowded directories.

## 3. Custom ports

```bash
gg <module> --port 8080 --httpPort 8081
```

## 4. Verify

Check logs for enabled types and successful publication, then open Vision.

## Next steps

- [Obtain and install a Graft](obtain-install-graft.md)
- [Gateway CLI](../reference/gateway-cli.md)

## Source anchors

- `graftcode-gateway/README.md`
