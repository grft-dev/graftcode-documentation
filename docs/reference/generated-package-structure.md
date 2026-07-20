---
title: "Generated package structure"
description: "Stable responsibilities and intentionally variable details in generated Graft packages."
---

# Generated package structure

A generated Graft package contains consumer-side code, not the provider implementation.

## Verified responsibilities

- generated classes/models matching the accepted UGM surface;
- generated method wrappers that invoke Hypertube;
- `GraftConfig` and its generated defaults;
- target package metadata;
- target runtime dependencies or references;
- declarations/types required by the consumer ecosystem.

.NET generation produces compiled NuGet code with a namespace and PascalCase `GraftConfig` fields.
Node.js generation produces JavaScript/declarations with lower-case configuration fields. Other
ecosystems use their native package conventions.

## Not stable enough to infer

- package name and scope;
- registry/feed/repository URL;
- package version;
- generated namespace/import path;
- source-to-target method casing;
- exact file layout;
- whether runtime dependencies are transitive in the current Alpha.

Read these values from current Gateway/Vision output and the installed artifact. Do not edit generated
files as the source of truth; change the provider contract or generator and regenerate.

Normal runtime calls do not regenerate the package. They use installed wrappers and resolved
configuration to invoke the provider.

**Gap:** this reference describes responsibilities shared by inspected generators, not an ABI or file
layout guarantee across releases.

## Next steps

- [Obtain and install a Graft](../how-to-guides/obtain-install-graft)
- [Update a provider contract](../how-to-guides/update-provider-contract.md)

## Source anchors

- `graftcode-package-generation-engine/`
- `graftcode-code-generator/src/netcore/`
- `graftcode-code-generator/src/nodejs/`
- [Package generation](../core-concepts/package-generation.md)
