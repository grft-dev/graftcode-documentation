---
title: "Gateway module versioning and --noVersioning"
description: "Understand hosted-module versioning, when to bump package versions, and how to control versioning with Gateway flags."
articleTitle: "Gateway module versioning and --noVersioning"
---

Hosted-module versioning is separate from the npm version on a generated Graft. Gateway decides
whether each publication of a provider surface is versioned in the service model.

## Default behavior

- Without `--projectKey` or `GC_PROJECT_KEY`, Gateway runs in **standalone mode** and **disables
  versioning by default**.
- `--keepVersioning` (default `true`) re-enables versioning without a project key.
- `--noVersioning` **explicitly disables** versioning regardless of project key.

Use a [portal project key](project-key) for stable project-backed publication in shared environments.

## When to bump consumer package versions

Reinstall from Vision when the callable surface changes. Copy the complete `npm install` command after
each publication; do not reuse an old registry URL after Gateway restart without a project key.

## Examples

```bash
npm ci && npm run build
gg --runtime nodejs --modules ./dist/index.js --noVersioning
```

Standalone (versioning off by default):

```bash
gg --runtime nodejs --modules ./dist/index.js
```

With project key:

```bash
export GC_PROJECT_KEY="dev:<jwt-from-portal>"
gg --runtime nodejs --modules ./dist/index.js
```

## Next steps

- [Use a project key](project-key)
- [Gateway CLI reference](../../reference/gateway-cli.md)
- [Update a provider contract](../update-provider-contract.md)

## Source anchors

- `graftcode-gateway/README.md`, “Versioning” section
