---
title: Handle Receiver and transport errors
description: >-
  Keep Receiver failures actionable and add retries only where repeat execution
  is safe.
articleTitle: Handle Receiver and transport errors
---
## Receiver boundary

Validate inputs and throw domain exceptions with safe messages—no secrets in exception text.

## Classify before retry

- Domain errors: do not retry.
- Transient upstream `5xx` inside Receiver: bounded retry if idempotent.
- Transport failures: retry only idempotent operations; stateful identity may be lost.
- Package `422`: fix the public contract.

## Host example

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

See [Timeouts and retries](../operations/timeouts-retries.md) and
[Errors reference](../reference/errors-status.md).
