---
title: "Package generation"
description: "How the Graftcode Engine turns a callable surface into a target-language Graft package, separate from runtime invocation."
---

# Package generation

The **Graftcode Engine** turns metadata from the Receiver's selected
[callable surface](callable-surface.md) into a package for the Caller's ecosystem. It is a
package/build activity, not part of each runtime call.

![User-written modules provide callable-surface metadata, and generated packages supply Caller wrappers](../../assets/diagrams/generated-vs-written.png)

## Flow

1. Gateway identifies the selected callable surface of a hosted Receiver module.
2. On a package request, the Graftcode Engine uses that callable-surface metadata and any dependency
   information for the selected Caller ecosystem.
3. The Engine generates the target-language wrappers and `GraftConfig`, then builds the requested
   package artifact and returns its install location.

Package generation happens once per contract/version, not on every call.

## Generated and user-written boundaries

Generated:

- Caller-facing type and method wrappers;
- runtime invocation bodies;
- the package's `GraftConfig`;
- target package metadata and runtime dependencies.

User-written:

- Receiver implementation;
- Caller application;
- deployment configuration and policy.

Do not edit generated package code as the source of truth. Change the Receiver surface, then regenerate.

## Naming and registry caveat

Package names, registry paths, versions, and install commands depend on the Receiver package, caller ecosystem, and active registry. Obtain them from the current Gateway/Vision or package-manager output. This page intentionally does not invent a naming formula.
