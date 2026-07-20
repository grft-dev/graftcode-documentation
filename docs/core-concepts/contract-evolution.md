---
title: "Contract evolution"
description: "How changes to the callable surface affect UGM versions, generated packages, and consumers."
---

# Contract evolution

A Graft contract is the analyzer-selected callable surface plus the type information represented in the UGM. Changing that surface can require a new generated package and consumer changes.

## Usually additive

Examples include adding a new type or method without changing existing generated names or signatures. “Additive” does not guarantee compatibility in every target ecosystem: overload resolution, name casing, package exports, and type generation can still change.

## Usually breaking

- removing or renaming a type or member;
- changing parameter order, count, or mapped type;
- changing a return type;
- changing static to instance or instance to static;
- removing or changing a constructor used by consumers;
- changing nullability where the target generator represents it;
- introducing a type unsupported by a target generator.

## Safe workflow

1. Change the producer surface deliberately.
2. Run the module analyzer and compare the resulting UGM.
3. Generate packages for every supported caller ecosystem.
4. Compile/type-check representative consumers.
5. Run in-memory and remote smoke tests as applicable.
6. Publish a new version according to the package ecosystem's compatibility policy.
7. Keep the old hosted contract available while old consumers still depend on it, when the deployment supports side-by-side versions.

## Current evidence gap

The inspected implementation includes module/package versions and version-query paths, but this review did not find tests proving automatic rejection when a different UGM is registered under the same version. Do not rely on automatic contract-drift prevention without verifying the deployed service-model implementation.

The implementation also does not prove that every additive source change is binary- or source-compatible in every generated target.
