---
title: "Development-time vs production-time behavior"
description: "Compatibility route separating package generation from runtime invocation."
keywords: "graftcode development time, package generation, runtime invocation"
---

# Development-time vs production-time behavior

The former combined lifecycle has been split into two verified flows:

- [Package generation](../core-concepts/package-generation.md) covers analysis, UGM handling, generation, and package construction.
- [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) covers an application call through configuration, transport or in-memory dispatch, execution, and response.

Module analysis and package generation do not occur on every invocation. Conversely, installing a generated package does not remove runtime concerns such as configuration, connectivity, authentication, timeouts, or remote failures.

Claims about which metadata, logs, metrics, identifiers, or package-request fields leave an environment require a field-level inventory from the deployed Gateway and cloud service. This page does not make privacy, cloud-independence, or production-compatibility guarantees.
