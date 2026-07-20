---
title: "Why runtime-level integration is faster"
description: "Compatibility route for a neutral explanation of Graftcode invocation work."
keywords: "runtime integration, performance, graftcode invocation"
---

# Why runtime-level integration is faster

The title reflects an unsupported conclusion. The current implementation evidence does not establish that runtime-level integration is inherently faster than REST, gRPC, or another approach.

A Graftcode call still constructs an invocation operation and can serialize, transmit, deserialize, dispatch, execute, and map a response. The exact work depends on runtime pair, execution mode, transport, types, generated package, and Gateway release.

Use [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) to identify the stages in the measured path and [Compare performance](compare-performance.md) for minimum reproducibility requirements.

Do not infer lower latency, CPU use, memory pressure, allocations, copies, or network traffic from architecture alone.
