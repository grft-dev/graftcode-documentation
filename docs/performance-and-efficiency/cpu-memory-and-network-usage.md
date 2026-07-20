---
title: "CPU, memory, and network usage"
description: "Measurement guidance for Graftcode resource usage."
keywords: "cpu usage, memory usage, network traffic, measurement"
---

# CPU, memory, and network usage

No universal CPU, memory, allocation, or network outcome is documented for Graftcode.

Measure the full deployment under a representative workload:

- caller and provider CPU time and utilization;
- managed and native allocations, working set, and garbage collection;
- transmitted bytes, connection count, reconnects, and protocol overhead;
- throughput, latency percentiles, errors, and timeouts;
- in-memory and remote paths separately.

Record payload shapes, concurrency, runtime and Gateway versions, transport, topology, warm-up, and raw outputs. Compare against a functionally equivalent baseline and include business-logic cost.

Architecture diagrams are not measurements. See [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) and [Compare performance](compare-performance.md).
