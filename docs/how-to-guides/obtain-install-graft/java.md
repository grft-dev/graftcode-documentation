---
title: "Obtain and install a Graft"
description: "Use Gateway or Vision output to install the generated package without guessing registry details."
articleTitle: "Obtain and install a Graft"
---

## 1. Wait for publication

Start Gateway against the built provider and wait for successful model upload in logs or Vision.

## 2. Open Vision

Default HTTP port is `81` (`http://localhost:81/GV` in local Docker workflows).

## 3. Copy the install command

For JVM consumers, copy the **complete** command from Vision, including registry, package
name, and version.

```bash
# Copy Maven dependency block from Vision
```

Never derive registry URLs from the provider assembly name. Use a [project key](../project-key) when
stable publication identity is required.

## 4. Verify exports

Inspect generated namespaces, imports, and method names in the installed package.

## Next steps

- [Configure invocation](../configure-invocation)
- [Generated package structure](../../reference/generated-package-structure.md)

## Source anchors

- `graftcode-package-manager-gateway/`
