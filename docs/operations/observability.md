---
title: "Logging, metrics, and tracing"
description: "Capture Gateway logs and integrate verified trace propagation with existing tooling."
---

# Logging, metrics, and tracing

## Logging

Capture Gateway standard output/error and provider logs with instance, release, module, and runtime
labels. Log startup discovery and publication separately from invocation failures.

`GG_DEBUG=1` or `TRUE` logs incoming and outgoing byte traffic. Use it only for controlled diagnosis;
payload bytes can expose sensitive data and increase log volume.

## Tracing

The .NET and Node.js Hypertube SDKs contain tested W3C `traceparent` propagation. Integrate provider
and consumer applications with their normal OpenTelemetry setup and verify one remote call appears in
one trace.

Do not claim equivalent propagation for every runtime without a test. Trace export is an application
or platform responsibility; Gateway does not provide a documented universal collector configuration.

## Metrics

Record at the caller/provider boundary:

- call count and failures by stable operation name;
- duration distributions;
- active/failed connections;
- process CPU, memory, restarts, and instance count;
- dependency timeout/retry counts.

Avoid IDs, argument values, and unbounded exception text as metric labels.

**Gap:** no stable Prometheus/OpenMetrics endpoint or complete Gateway metric catalog is documented.
Instrument applications and infrastructure until a release specifies one.

## Next steps

- [Handle provider errors](../how-to-guides/handle-provider-errors)
- [Timeouts and retries](timeouts-retries.md)
- [Environment variables](../reference/environment-variables.md)

## Source anchors

- `graftcode-gateway/README.md`, `GG_DEBUG`
- `HYPERTUBE/src/netcore/Hypertube.Netcore.Utils/Telemetry/`
- `HYPERTUBE/src/js/hypertube-nodejs-sdk/lib/telemetry/`
- corresponding `GraftTelemetryTests.cs` and `GraftTelemetry.test.js`
