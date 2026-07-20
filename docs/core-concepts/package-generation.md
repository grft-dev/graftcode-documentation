---
title: "Package generation"
description: "How analyzer output becomes a target-language Graft package, separate from runtime invocation."
---

# Package generation

Package generation converts a UGM into a package for the caller's ecosystem. It is a package/build activity, not part of each runtime call.

![User-written modules are analyzed into a UGM, while generated packages supply consumer wrappers](../../assets/diagrams/generated-vs-written.svg)

## Verified flow

1. A module analyzer creates a UGM for a producer package and version.
2. The service-model path stores or retrieves that model.
3. The package manager gateway receives version or package requests.
4. The package-generation engine selects engines for the calling and called technologies.
5. It retrieves the UGM and optional dependency-tree data.
6. Code generators create target-language wrappers and `GraftConfig`.
7. Repository/package builders produce the requested package artifact.

The current package manager gateway queues generation requests and streams the resulting package link. Its tests verify version metadata and package retrieval behavior.

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

Do not edit generated package code as the source of truth. Change the producer surface or generator, then regenerate.

## Naming and registry caveat

Package names, registry paths, versions, and install commands depend on the producer package, caller ecosystem, and active service-model/registry path. Obtain them from the current Gateway/Vision or package-manager output. This page intentionally does not invent a naming formula.

## Evidence

Verified against `graftcode-package-manager-gateway`, `graftcode-package-generation-engine`, both code-generator implementations, and their tests.
