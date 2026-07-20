---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---

Turn an existing .NET library into a provider without adding controllers or transport types.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use a class library and synchronous public methods:

```csharp
namespace Pricing;

public static class PriceService
{
    public static double Calculate(double amount, double discountPercent) =>
        amount * (1 - discountPercent / 100);
}
```

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings. The .NET package-generation path rejects framework complex types.

## 2. Build the provider

```bash
dotnet build ./Pricing/Pricing.csproj
```

## 3. Start Gateway with the real module

```bash
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll
```

Adjust paths and runtime versions to the project. Do not copy package IDs, registry URLs, or project
keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** there is no verified universal type matrix. Generate and smoke-test every producer/consumer
language pair that uses types beyond the portable baseline.

## Next steps

- [Run Gateway locally](../run-gateway-locally)
- [Obtain and install a Graft](../obtain-install-graft)
- [Type compatibility matrix](../../reference/type-matrix.md)

## Source anchors

- `graftcode-gateway/README.md`, “Usage” and “Runtimes (typical setups)”
- `graftcode-package-generation-engine/src/netcore/GraftCodePackageGenerationEngine/Exceptions/UnsupportedTypeUsageException.cs`
- [Expose a .NET backend](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/dotnet.md)
