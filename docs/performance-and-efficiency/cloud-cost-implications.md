---
title: "Cloud cost implications"
description: "Evidence requirements for estimating Graftcode cloud costs."
keywords: "cloud cost, cost model, graftcode measurement"
---

# Cloud cost implications

The documentation audit found no reproducible cost model supporting savings claims for Graftcode. The previous compute, memory, network, autoscaling, and egress conclusions have been removed.

To estimate cost for a real deployment:

1. measure resource usage and traffic with the intended topology;
2. include Gateway, provider, consumer, proxy, observability, and package-service dependencies;
3. use current prices for the target region and commitment model;
4. model baseline and peak capacity, failures, retries, and data transfer;
5. publish assumptions, formulas, date, and sensitivity ranges.

Do not convert unverified performance assumptions into financial claims. See [CPU, memory, and network usage](cpu-memory-and-network-usage.md) and [Compare performance](compare-performance.md).
