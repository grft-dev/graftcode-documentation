---
title: "Microservices without contracts"
description: "Compatibility route explaining Graftcode's code-derived service contracts."
keywords: "microservices, code-derived contracts, unified graft model"
---

# Microservices without contracts

The title of this legacy route is imprecise: Graftcode services do have contracts.

The contract is derived from the analyzer-selected callable surface and represented in the Unified Graft Model. Generated consumer packages encode that model for a target ecosystem. This can remove a separately handwritten IDL, but it does not remove versioning, type compatibility, runtime validation, or distributed failure handling.

Use these canonical pages:

- [Callable surface](../core-concepts/callable-surface.md)
- [Type mapping](../core-concepts/type-mapping.md)
- [Package generation](../core-concepts/package-generation.md)
- [Contract evolution](../core-concepts/contract-evolution.md)

For an integration sequence, see [Service-to-service integration](service-to-service-integration.md).
