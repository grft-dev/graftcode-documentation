---
title: "Use a portal project key"
description: "Obtain a project key from the portal, configure Gateway, and understand how it differs from a registry URL."
articleTitle: "Use a portal project key"
---

A **project key** authenticates Gateway to Graftcode portal and project metadata services. It is not
the same as the **registry URL** shown on the dashboard for installing a generated Graft.

## What each identifier is for

| Identifier | Used by | Purpose |
| --- | --- | --- |
| **Project key** (`--projectKey`, `GC_PROJECT_KEY`) | Gateway at startup | Portal/project identity, stable publication context |
| **Registry URL** (in Vision install commands) | Consumer package managers | Download a specific generated Graft package |

A Gateway without a project key can receive a **new registry identifier after restart**. Consumers must
copy install commands from the **currently running** Gateway or Vision—not from an old log line.

The project key does **not** authenticate individual Graft invocations. See
[Authenticate Graft calls](authenticate-graft-calls) and
[Authentication operations](../../operations/authentication-authorization.md).

## Obtain a project key

1. Sign in to [Graftcode Portal](https://portal.graftcode.com/).
2. Open or create a project for the provider you host.
3. Copy the project key from the project settings or onboarding flow shown in the portal UI for your
   account.

The key is a JWT, often used in `env:jwt` form (for example `dev:eyJ...`) or as a bare token. Copy
the exact format the portal displays.

**Gap:** portal screen names and navigation can change between releases. Use the live portal UI as
authority.

## Configure Gateway

Prefer environment variables in deployment; they override CLI flags:

```bash
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"
gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll
```

Or pass on the command line (avoid in shared shells and images):

```bash
gg --projectKey "dev:<jwt-copied-from-portal>" --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll
```

For Docker, inject `GC_PROJECT_KEY` through the platform secret store—never bake it into the image.
See [Deploy with Docker](../deploy-with-docker).

## Versioning interaction

With a project key, Gateway uses project-backed publication semantics. In standalone mode without a
key, versioning is disabled by default unless `--keepVersioning` is set. See
[Gateway versioning](gateway-no-versioning).

## Next steps

- [Obtain and install a Graft](../obtain-install-graft)
- [Environment variables](../../reference/environment-variables.md)
- [Core-concepts glossary — Project key](../../core-concepts/glossary.md#project-key)

## Source anchors

- `graftcode-gateway/README.md`, `--projectKey` and `GC_PROJECT_KEY`
- [Graftcode Portal](https://portal.graftcode.com/)
