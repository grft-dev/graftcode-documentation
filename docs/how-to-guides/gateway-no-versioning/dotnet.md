---
title: "Gateway module versioning and --noVersioning"
description: "Understand hosted-module versioning, when to bump package versions, and how to control versioning with Gateway flags."
articleTitle: "Gateway module versioning and --noVersioning"
---

Hosted-module versioning is separate from the version field on a generated consumer package. Gateway
decides whether each publication of a provider surface is versioned in the service model.

## Default behavior

After CLI and environment parsing:

- Without `--projectKey` or `GC_PROJECT_KEY`, Gateway runs in **standalone mode** and **disables
  versioning by default**.
- `--keepVersioning` (default `true`) can re-enable versioning even without a project key.
- `--noVersioning` **explicitly disables** versioning regardless of project key.

A [portal project key](project-key) ties publication to stable project metadata and is the normal
production path.

## When to bump consumer package versions

Bump the generated package version shown in Vision when the **callable surface** changes in a way
that affects consumers: renamed members, signature changes, removed types, or unsupported type
introduction. See [Update a provider contract](../update-provider-contract.md) and
[Contract evolution](../../core-concepts/contract-evolution.md).

Additive methods are safer but are not guaranteed compatible in every target language. Always
regenerate, reinstall, and smoke-test each consumer ecosystem.

## When to use --noVersioning

Use `--noVersioning` for local experiments where you do not want Gateway to track module versions in
the service model, or when a deployment policy requires a single unversioned hosted surface.

Do not use it to avoid republishing after a **breaking** contract change. Consumers still depend on
the generated package version you install.

## Examples

Host a .NET provider with versioning disabled:

```bash
dotnet build ./Pricing/Pricing.csproj
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll --noVersioning
```

Standalone mode without a project key (versioning off by default):

```bash
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll
```

Re-enable versioning in standalone mode:

```bash
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll --keepVersioning
```

With a project key (store the key in a secret, not in source):

```bash
export GC_PROJECT_KEY="dev:<jwt-from-portal>"
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll
```

## Verify

After startup, confirm discovery and publication in Gateway logs and Vision. If consumers install an
old package while the hosted surface changed, failures appear at invocation time—not as an automatic
drift rejection unless your deployment verifies versions.

**Gap:** automatic rejection of a changed UGM registered under the same version is not established in
the inspected implementation.

## Next steps

- [Use a project key](project-key)
- [Gateway CLI reference](../../reference/gateway-cli.md)
- [Version compatibility and upgrades](../../operations/version-compatibility-upgrades.md)

## Source anchors

- `graftcode-gateway/README.md`, “Versioning” section
