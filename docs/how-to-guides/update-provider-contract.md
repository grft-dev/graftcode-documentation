---
title: Update a Receiver contract
description: 'Change a public surface, regenerate packages, and upgrade Callers safely.'
articleTitle: Update a Receiver contract
---
1. Classify breaking vs additive changes ([Contract evolution](../core-concepts/contract-evolution.md)).
2. Rebuild and host:

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

3. Regenerate every Caller package from Vision.
4. Upgrade Callers with the new install command before removing old compatibility.

See [Version compatibility](../operations/version-compatibility-upgrades.md).
