---
title: "Observability, tracing, and context propagation"
description: "Scoped guidance for verified Graftcode trace-context behavior."
keywords: "graftcode observability, distributed tracing, traceparent, OpenTelemetry"
---

# Observability, tracing, and context propagation

The inspected .NET and Node.js runtime paths have tests for W3C `traceparent` injection and extraction. This is evidence for those tested paths, not a guarantee for every provider, consumer, transport, or release.

For a concrete verification:

1. instrument both caller and provider with OpenTelemetry;
2. start a parent span before the generated call;
3. invoke the provider through the configured remote path;
4. confirm the receiver extracts the expected `traceparent`;
5. export both sides and verify parent-child correlation in the selected backend;
6. test failure, sampling, and missing-context cases.

Application logs and metrics still require explicit instrumentation and backend configuration. No Portal metrics, universal automatic spans, sensitive-data policy, or all-runtime propagation guarantee is documented here.

See [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) to identify where propagation can fail and [Observability operations](../operations/observability.md) for deployment guidance.
