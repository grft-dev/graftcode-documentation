---
title: Update a Receiver contract
description: 'Evolve a callable surface, publish a new Graft version, and roll Callers over safely.'
articleTitle: Update a Receiver contract
---

# Update a Receiver contract

A Graft contract is the exposed callable surface plus its type information. Changing it can require a
new generated package and coordinated Caller changes. Use a deliberate workflow rather than assuming
old Callers keep working.

## Classify the change

- **Additive change** — adding a new method or a new optional field. Existing Callers can keep using
  the old Graft; new Callers adopt the new version when ready.
- **Breaking change** — renaming or removing a method, changing a signature, or changing a type in a
  way that changes the generated public API. Existing Callers must upgrade.

See [Contract evolution](../core-concepts/contract-evolution.md) for how surface changes map to the
generated public API.

## Additive change example

Add a new method without touching existing ones. Rebuild, host, and publish a new package version.
Existing Callers are unaffected until they choose to upgrade.

```multi
```dotnet
// Existing: Calculate(...). New, additive:
public decimal CalculateWithTax(decimal basePrice, decimal discountPercent, decimal taxPercent) { /* ... */ }
```
```javascript
// Existing: calculate(...). New, additive:
export function calculateWithTax(basePrice, discountPercent, taxPercent) { /* ... */ }
```
```

## Breaking change example

Changing a signature (for example, adding a required parameter or changing a return type) is breaking.
Publish it as a **new package version** and require Callers to upgrade before you retire the old one.

## Rollout workflow

1. Make the surface change and rebuild, then host with Gateway:

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

2. **Compare the generated public API** in Vision and confirm the change is what you intend.
3. **Publish a new Graft package version.** Do not republish a changed surface under an existing
   version — automatic rejection is not guaranteed.
4. **Coexistence period:** keep the old package version available so old Callers continue to work while
   new Callers adopt the new version.
5. **Rollout order:** for a breaking change, deploy the new Receiver first (able to serve both the old
   and new contract if possible), then upgrade Callers.
6. **Canary:** upgrade a small subset of Callers to the new Graft first and verify.
7. **Verify:** compile and smoke-test representative Callers against the new version.
8. **Rollback:** if the canary fails, revert Callers to the pinned previous Graft version. Because the
   old package version is still published, rollback does not require regenerating anything.

## Old Callers using an older Graft

An old Caller keeps calling with the contract baked into its installed Graft version. It does **not**
automatically pick up surface changes. Compatibility depends on:

- **Product/protocol compatibility** — whether the Gateway and runtime versions still interoperate.
- **Receiver contract compatibility** — whether the Receiver still accepts the old contract's calls.

Do not assume old Grafts remain compatible across releases. Pin versions and validate.

See [Version compatibility and upgrades](../operations/version-compatibility-and-upgrades.md) and
[Handle Receiver errors](handle-receiver-errors.md).
