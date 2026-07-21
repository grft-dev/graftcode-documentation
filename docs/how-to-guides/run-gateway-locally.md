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
gg ./Pricing/bin/Debug/net9.0/Pricing.dll --types Pricing.PriceService --methods Calculate
```
```javascript
npm ci && npm run build
gg ./dist/index.js --types PriceService --methods calculate
```
```python
gg ./pricing/
```
```java
mvn package
gg ./target/pricing-1.0.0.jar
```
```php
composer install
gg ./src/
```
```ruby
bundle install
gg ./lib/
```
```

Use `gg.exe` on Windows. Pass the built module path explicitly when auto-scan would pick the wrong artifact.

## 3. Custom ports

```bash
gg <module> --port 8080 --httpPort 8081
```

## 4. Verify

Check logs for enabled types and successful publication, then open Vision.

## Next steps

- [Obtain and install a Graft](obtain-install-graft.md)
- [Gateway CLI](../reference/gateway-cli.md)
