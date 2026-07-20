---
title: "Update a provider contract"
description: "Change a public surface, regenerate packages, and upgrade consumers safely."
articleTitle: "Update a provider contract"
---

1. Classify breaking vs additive changes ([Contract evolution](../../core-concepts/contract-evolution.md)).
2. Rebuild and host:

```bash
mvn package
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```

3. Regenerate every consumer package from Vision.
4. Upgrade consumers with the new install command before removing old compatibility.

See [Version compatibility](../../operations/version-compatibility-upgrades.md).
