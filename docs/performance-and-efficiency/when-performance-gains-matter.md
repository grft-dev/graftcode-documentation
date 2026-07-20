---
title: "When performance gains matter"
description: "Guidance for deciding whether integration performance needs measurement."
keywords: "performance tradeoffs, distributed systems performance, measurement"
---

# When performance gains matter

Measure integration overhead when it can change a service-level objective, capacity plan, user experience, or cost decision. Typical triggers include high call volume, tight latency budgets, large or frequent values, constrained edge environments, or unexpectedly high resource use.

First determine whether the dominant time is business logic, a downstream dependency, queuing, transport, serialization, or runtime dispatch. Optimize the measured bottleneck.

For low-volume or dependency-bound workloads, operability, compatibility, security, and team fit may matter more than transport-level differences.

Graftcode has no documented default performance advantage. Use [Compare performance](compare-performance.md) for reproducibility requirements and [REST vs gRPC vs Graftcode](rest-vs-grpc-vs-graftcode.md) for a neutral responsibility comparison.
