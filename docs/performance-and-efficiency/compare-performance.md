---
title: "Compare Performance"
description: "Requirements for a reproducible Graftcode performance comparison."
---

# Compare performance

No reproducible benchmark package was found for the performance, cost, or emissions figures previously published on this route. Those figures have been removed.

A valid comparison must publish:

- source and exact versions for provider, consumer, Gateway, transports, REST/gRPC baselines, and harness;
- hardware, operating system, runtime settings, topology, and network conditions;
- request/response shapes and equivalent business work;
- warm-up, duration, concurrency, sample count, and failure policy;
- latency percentiles, throughput, CPU, allocation/memory, and bytes transferred;
- raw output, analysis code, repeated runs, and limitations.

Until that evidence exists, make no claim that Graftcode is faster, cheaper, more scalable, or lower-carbon than another integration technology.

For the verified call path to measure, see [Invocation lifecycle](../core-concepts/invocation-lifecycle.md).
