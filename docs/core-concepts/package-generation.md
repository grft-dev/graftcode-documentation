---
title: "Package generation"
description: "How the Graftcode Engine turns a callable surface into a target-language Graft package, separate from runtime invocation."
---

# Package generation

The **Graftcode Engine** converts a **Unified Graft Model (UGM)**—the language-neutral record of the
provider's [callable surface](callable-surface.md)—into a package for the caller's ecosystem. It is a
package/build activity, not part of each runtime call.

![User-written modules are analyzed into a UGM, while generated packages supply consumer wrappers](../../assets/diagrams/generated-vs-written.svg)

## Flow

1. The Graftcode Engine analyzes a hosted module and builds a UGM for a producer package and version.
2. On a package request, the Engine selects the target ecosystem and retrieves the UGM and optional
   dependency-tree data.
3. The Engine generates the target-language wrappers and `GraftConfig`, then builds the requested
   package artifact and returns its install location.

Package generation happens once per contract/version, not on every call.

## Generated and user-written boundaries

Generated:

- consumer-facing type and method wrappers;
- runtime invocation bodies;
- the package's `GraftConfig`;
- target package metadata and runtime dependencies.

User-written:

- producer implementation;
- consumer application;
- deployment configuration and policy.

Do not edit generated package code as the source of truth. Change the producer surface, then regenerate.

## Naming and registry caveat

Package names, registry paths, versions, and install commands depend on the producer package, caller ecosystem, and active registry. Obtain them from the current Gateway/Vision or package-manager output. This page intentionally does not invent a naming formula.
