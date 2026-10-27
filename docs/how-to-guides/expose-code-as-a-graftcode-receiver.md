---
title: "Expose code as a Graftcode Receiver"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode Receiver"
---

# Expose code as a Graftcode Receiver

Turn an existing library or module into a Receiver without adding HTTP route handlers, controllers,
or transport types on the public surface.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use a plain module with a small, intentional public API. Prefer primitives, plain models, and
language arrays. Async return types (`Task`, `Promise`, `async def`, …) are allowed on many
Receivers when you need them—results complete on the Receiver; see [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts). Avoid `CancellationToken`, framework collection interfaces, and non-parsable BCL types on the public surface.

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

Use primitives and plain models. For the safest cross-runtime contracts, use ISO-8601 strings for
dates and string identifiers for IDs. You can also use [parsable framework types](../reference/type-compatibility-matrix.md#parsable-framework-types) such as `System.DateTime` or `System.Guid` after you smoke-test each Caller direction. The engine rejects **non-parsable** framework types (for example `List<T>`, `Stream`, `System.Type`) with HTTP `422`.

## 2. Build the Receiver

```multi
```dotnet
dotnet build ./Pricing/Pricing.csproj
```
```javascript
npm ci
npm run build
```
```python
# Build or package the Receiver module per your project layout
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

Install and run **[Graftcode Gateway](../core-concepts/gateway-and-hosted-modules.md)** (`gg`) if you have not
already—it hosts your built module, discovers the public surface, and publishes the callable surface. See
[Run Gateway locally](run-gateway-locally.md#1-install-gateway).

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
surface as a review gate: remove accidental public members before Callers install a Graft.

There is no universal type matrix. Generate and smoke-test every Receiver/Caller language pair that
uses types beyond the portable baseline.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Obtain and install a Graft](obtain-and-install-a-graft.md)
- [Type compatibility matrix](../reference/type-compatibility-matrix.md)
