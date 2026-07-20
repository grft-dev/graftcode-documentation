---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---

Turn an existing JVM library into a provider without adding controllers or transport types.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use an ordinary library JAR with public Java classes and synchronous methods:

```java
package pricing;

public final class PriceService {
    public static double calculate(double amount, double discountPercent) {
        return amount * (1 - discountPercent / 100);
    }
}
```

Kotlin and other JVM languages must expose Java-compatible bytecode. Use primitives and plain models.

## 2. Build the provider

```bash
mvn package
```

## 3. Start Gateway with the real module

```bash
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```

`java` and `jvm` are accepted runtime names. Adjust paths to the project.

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
