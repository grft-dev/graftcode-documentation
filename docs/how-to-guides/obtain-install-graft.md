---
title: "Obtain and install a Graft"
description: "Use Gateway or Vision output to install the generated package without guessing registry details."
---

# Obtain and install a Graft

## Goal

Install the generated consumer package for a running provider.

## 1. Wait for publication

Start the provider Gateway and wait until its output confirms module discovery and successful model
publication. If publication fails, fix the provider contract before trying to install.

## 2. Open the running Gateway's Vision UI

The default Vision HTTP port is `81`; the verified local Docker workflow opens
`http://localhost:81/GV`. If `--httpPort` was changed, use that mapped port.

## 3. Select the consumer ecosystem

Select NuGet, npm, Maven, PyPI/pip, Composer, or RubyGems as appropriate. Copy the complete command
shown by this Gateway, including registry/feed, generated package name, and version.

Do not derive those values from the provider assembly or module name. A Gateway without a project key
can receive a different registry identifier after restart. A portal project key provides a stable
project-backed address; obtain the key from the portal and never commit it.

## 4. Run the command unchanged

Run the copied command in the consumer project. Keep the resulting lockfile or package lock. For
NuGet, retain `nuget.org` for ordinary dependencies and use package-source mapping in controlled
builds if needed.

Current Alpha npm packages may require the runtime dependency separately:

```bash
npm install hypertube-nodejs-sdk
```

Confirm this requirement against the generated package and current Gateway output.

## 5. Verify the installed API

Inspect the package exports, generated namespace, or declarations. Use the generated names and
invocation form; do not infer casing from the provider language.

## Next steps

- [Configure invocation](configure-invocation.md)
- [Generated package structure](../reference/generated-package-structure.md)
- [Update a provider contract](update-provider-contract.md)

## Source anchors

- `graftcode-package-generation-engine/` and `graftcode-package-manager-gateway/`
- `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/`
- [Connect .NET microservices](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/3-connect-microservices/dotnet.md)
- [Known limitations](../how-graftcode-works/alpha-limitations-and-known-constraints.md)
