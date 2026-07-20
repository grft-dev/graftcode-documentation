---
title: "Gateway module versioning and --noVersioning"
description: "Understand hosted-module versioning, when to bump package versions, and how to control versioning with Gateway flags."
articleTitle: "Gateway module versioning and --noVersioning"
---

Hosted-module versioning is separate from the Maven coordinate version on a generated Graft.

## Default behavior

- Standalone Gateway **disables versioning by default**.
- `--noVersioning` forces versioning off.
- Use a [project key](project-key) for stable publication identity.

## Examples

```bash
mvn package
gg --runtime jvm --modules ./target/pricing-1.0.0.jar --noVersioning
```

With project key:

```bash
export GC_PROJECT_KEY="dev:<jwt-from-portal>"
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```

## Next steps

- [Use a project key](project-key)
- [Update a provider contract](../update-provider-contract.md)

## Source anchors

- `graftcode-gateway/README.md`, “Versioning” section
