---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---
Turn an existing library or module into a provider without adding HTTP route handlers, controllers,
or transport types on the public surface.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use a plain module with a small synchronous or async-free public API (per runtime rules):

```multi
```dotnet
namespace Pricing;

public static class PriceService
{
    public static double Calculate(double amount, double discountPercent) =>
        amount * (1 - discountPercent / 100);
}
```
```javascript
export class PriceService {
  static calculate(amount: number, discountPercent: number): number {
    return amount * (1 - discountPercent / 100);
  }
}
```
```python
class PriceService:
    @staticmethod
    def calculate(amount: float, discount_percent: float) -> float:
        return amount * (1 - discount_percent / 100)
```
```java
public class PriceService {
    public static double calculate(double amount, double discountPercent) {
        return amount * (1 - discountPercent / 100);
    }
}
```
```php
class PriceService {
    public static function calculate(float $amount, float $discountPercent): float {
        return $amount * (1 - $discountPercent / 100);
    }
}
```
```ruby
class PriceService
  def self.calculate(amount, discount_percent)
    amount * (1 - discount_percent / 100.0)
  end
end
```
```

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings. The .NET package-generation path rejects framework complex types on the public surface.

## 2. Build the provider

```multi
```dotnet
dotnet build ./Pricing/Pricing.csproj
```
```javascript
npm ci
npm run build
```
```python
# Build or package the provider module per your project layout
```
```java
mvn package
```
```php
composer install
```
```ruby
bundle install
```
```

## 3. Start Gateway with the real module

```multi
```dotnet
gg ./Pricing/bin/Debug/net9.0/Pricing.dll
```
```javascript
gg ./dist/index.js
```
```python
gg ./pricing/
```
```java
gg ./target/pricing-1.0.0.jar
```
```php
gg ./src/
```
```ruby
gg ./lib/
```
```

Adjust paths and runtime versions to the project. Do not copy package IDs, registry URLs, or project
keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** there is no verified universal type matrix. Generate and smoke-test every producer/consumer
language pair that uses types beyond the portable baseline.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Obtain and install a Graft](obtain-install-graft.md)
- [Type compatibility matrix](../reference/type-matrix.md)
