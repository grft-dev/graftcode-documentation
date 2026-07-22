---
title: "Use a portal project key"
description: "Obtain a project key from the portal, configure Gateway, and understand how it differs from a registry URL."
articleTitle: "Use a portal project key"
---
A **project key** authenticates Gateway to Graftcode portal and project metadata services. It is not
the same as the **registry URL**, the **runtime host**, or a **call credential**.

> **Project Key** registers the Gateway in a project. The **registry URL** installs the Graft. The
> **runtime host** executes methods. The **call credential** authorizes a specific call.

See [Project Key, registry, host, and credentials](../reference/identifiers-and-auth.md) for the
canonical diagram and table.

A Gateway without a project key can receive a **new registry identifier after restart**. Consumers must
copy install commands from the **currently running** Gateway or Vision—not from an old log line.

The project key does **not** authenticate individual Graft invocations. See
[Authenticate Graft calls](authenticate-graft-calls.md) and
[Authentication operations](../operations/authentication-authorization.md).

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

```multi
```dotnet
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\ndotnet build ./Pricing/Pricing.csproj
gg ./Pricing/bin/Debug/net9.0/Pricing.dll
```
```javascript
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\nnpm ci && npm run build
gg ./dist/index.js
```
```python
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\ngg ./pricing/
```
```java
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\nmvn package
gg ./target/pricing-1.0.0.jar
```
```php
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\ncomposer install
gg ./src/
```
```ruby
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\nbundle install
gg ./lib/
```
```

Or pass on the command line (avoid in shared shells and images):

```multi
```dotnet
gg --projectKey "dev:<jwt-copied-from-portal>" ./Pricing/bin/Debug/net9.0/Pricing.dll
```
```javascript
gg --projectKey "dev:<jwt-copied-from-portal>" ./dist/index.js
```
```python
gg --projectKey "dev:<jwt-copied-from-portal>" ./pricing/
```
```java
gg --projectKey "dev:<jwt-copied-from-portal>" ./target/pricing-1.0.0.jar
```
```php
gg --projectKey "dev:<jwt-copied-from-portal>" ./src/
```
```ruby
gg --projectKey "dev:<jwt-copied-from-portal>" ./lib/
```
```

For Docker, inject `GC_PROJECT_KEY` through the platform secret store—never bake it into the image.
See [Deploy with Docker](deploy-with-docker.md).

## Versioning interaction

With a project key, Gateway uses project-backed publication semantics. In standalone mode without a
key, versioning is disabled by default unless `--keepVersioning` is set. See
[Gateway versioning](gateway-no-versioning.md).

## Next steps

- [Obtain and install a Graft](obtain-install-graft.md)
- [Environment variables](../reference/environment-variables.md)
- [Core-concepts glossary — Project key](../core-concepts/glossary.md#project-key)
