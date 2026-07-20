---
title: "Java and JVM Language Guide"
description: "Expose JVM libraries and consume generated Grafts through Maven."
---

# Java and JVM

## Support status and direction

**Provider: supported. Consumer: supported.** The JVM path has module analysis, Maven resolution,
Java code generation/compilation, and cross-runtime public and virtual E2E coverage. Java is the
verified source language; Kotlin and other JVM languages must expose Java-compatible bytecode.

## Prerequisites

- Java 8+ with `JAVA_HOME` set; use a modern JDK for builds.
- Maven or Gradle and a built JAR.
- A current [Graftcode Gateway](https://github.com/grft-dev/graftcode-gateway/releases).

## Provider support

Use an ordinary library JAR. Public Java classes and methods form the discovery boundary:

```bash
mvn package
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```

`java` and `jvm` are accepted runtime names. Confirm the exact JAR and discovered surface in Vision.

## Consumer support

JVM consumers receive Maven artifacts containing generated Java APIs. Generated methods are
synchronous. `GraftConfig.host` and `GraftConfig.stateless` are public static fields.

## Package manager

Maven repositories and coordinates. Gradle can consume the same Maven repository. Copy the complete
repository and dependency blocks emitted by Vision.

## Minimal provider example

```java
package pricing;

public final class PriceService {
    public static double calculate(double basePrice, double discountPercent) {
        return basePrice * (1 - discountPercent / 100);
    }
}
```

For Kotlin, use a top-level function or an `@JvmStatic` companion method and verify discovery.

## Minimal consumer example

```java
import <generated.package>.GraftConfig;
import <generated.package>.PriceService;

public class Main {
    public static void main(String[] args) {
        GraftConfig.host = "ws://localhost/ws";
        GraftConfig.stateless = true;
        System.out.println(PriceService.calculate(100, 15));
    }
}
```

The generated package path depends on both provider ecosystem and source namespace. Copy exact
imports from Vision.

## Installation

1. Run Gateway against the built JAR and wait for successful publication.
2. Open Vision's Maven configuration or the Maven route emitted by that Gateway.
3. Copy both the generated repository declaration and dependency coordinates.
4. Paste them unchanged into `pom.xml`, or translate the emitted Maven coordinates into Gradle while
   preserving the exact repository URL, group, artifact, and version.
5. Resolve dependencies and use Vision's generated imports.

Never construct the repository GUID or normalize generated coordinates yourself.

## Configuration

```java
GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
```

Defaults are `host = "inmemory"` and `stateless = false`. The inspected generator also provides
`setHeaders(Map<String,String>)` and scoped invocation helpers. Configure before the first generated
call.

## Supported types

Verified portable baseline:

- `String`, `int`, `long`, `double`, `float`, and `boolean` on tested simple surfaces;
- plain Java objects;
- homogeneous primitive and object arrays.

For the safest cross-runtime contract, use strings, primitive numbers/booleans, simple POJOs, and
arrays. Avoid `CompletableFuture`, reactive types, `Optional`, collections/maps/sets/streams,
`LocalDate`, `Instant`, `UUID`, I/O streams, servlet types, and framework abstractions. Use strings for
timestamps and IDs.

**Gap:** boxed/null values, records, enums, inheritance, `BigDecimal`, generics, and every collection
variant are not exhaustively demonstrated by the inspected E2E matrix.

## Runtime-specific limitations

- Keep the public contract synchronous; block internally if necessary.
- Generated package roots differ for NuGet-, npm-, Maven-, PyPI-, Composer-, and RubyGems-origin
  targets. Do not infer package names from the source artifact.
- Public custom exceptions can leak into discovery; keep them package-private.
- Stateful instance objects require affinity and can expire; prefer static methods.

## Troubleshooting

- **Gateway cannot load the JAR:** verify `JAVA_HOME`, architecture, and the built path.
- **Class/method missing:** ensure it is public and inspect Vision's model.
- **Dependency unresolved:** copy the dynamic repository and coordinates again from the running
  Gateway.
- **Consumer tries local loading:** set `GraftConfig.host`.
- **Kotlin companion method missing:** expose Java-compatible static bytecode with `@JvmStatic`.

## Verified samples and tests

- [Java expose-backend Quick Start](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/java.md)
- [Cross-runtime simple-car sample](https://github.com/grft-dev/grft-test-simple-car)
- Inspected generated config:
  `graftcode-code-generator/src/jvm/graftcode-code-generator/src/main/java/com/graftcode/core/generator/handler/utils/GraftConfigClassProvider.java`
- Inspected E2E caller suite:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/jvm/`
- Full publish tests:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/jvm/`

## Known gaps

The local evidence does not establish equivalent provider behavior for every JVM language. Validate
non-Java bytecode and advanced types in Vision before publishing a production contract.
