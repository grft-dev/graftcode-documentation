---
title: "Runtime call execution"
description: "Compatibility route for the canonical invocation and configuration documentation."
keywords: "graftcode runtime execution, invocation lifecycle, configuration"
---

# Runtime call execution

This topic was split into focused canonical pages:

- [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) explains wrapper invocation, configuration, serialization, transport, dispatch, and response.
- [Configuration resolution](../core-concepts/configuration-resolution.md) documents the six verified configuration priorities and initialization behavior.
- [Execution modes](../core-concepts/execution-modes.md) distinguishes in-memory, same-machine, and remote execution.
- [Static and instance context](../core-concepts/static-and-instance-context.md) describes the currently verified generated call shapes.
- [Configure invocation](../how-to-guides/configure-invocation.md) gives the task sequence.
- [Handle provider errors](../how-to-guides/handle-provider-errors.md) covers caller-visible failures.

Remote calls can fail during configuration, connection, transport, dispatch, implementation execution, or response mapping. Generated typing does not make local and remote failure semantics identical.

Universal guarantees about threading, callbacks, exception-type preservation, asynchronous methods, or deadlock prevention are intentionally not made here; support must be verified for the provider runtime, consumer runtime, generated package, and Gateway release in use.
