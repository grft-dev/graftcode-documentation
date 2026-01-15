---
title: "Observability, tracing, and context propagation"
description: "Learn how Graftcode propagates trace and span context across runtimes, integrates with existing observability stacks, and avoids vendor lock-in in monitoring and logging."
keywords: "graftcode observability, distributed tracing, trace propagation, logging, monitoring integration"
---

# Observability, tracing, and context propagation

In distributed systems, visibility is not optional.

Teams need to understand:
- what was called
- where it was executed
- how long it took
- and why it failed

Graftcode is designed to integrate with **existing observability standards**, rather than introducing its own monitoring or tracing stack.

---

## Observability as a cross-cutting concern

Observability in Graftcode is treated as a **cross-cutting concern**, not as a framework feature.

This means:
- Graftcode does not replace your logging system
- it does not mandate a specific tracing backend
- it does not introduce a proprietary monitoring format

Instead, it ensures that **context flows correctly across runtime boundaries**, so existing tools continue to work.

---

## Trace and span propagation

When a method call is executed through Graftcode:
- a trace context is created or reused
- trace identifiers are attached to the invocation
- span identifiers are generated per execution segment

This context is propagated automatically:
- across in-memory execution
- across runtime boundaries
- across network calls

From the perspective of observability tools, the call behaves like a single distributed trace.

---

## No broken traces at runtime boundaries

A common issue in distributed systems is trace fragmentation:
- one trace in the caller
- another in the callee
- no reliable correlation

Graftcode avoids this by propagating trace context **as part of the invocation intent**, not as transport-level metadata.

This ensures that:
- spans remain connected
- call chains are preserved
- execution across runtimes appears as a single logical operation

---

## Integration with existing tooling

Graftcode does not ship its own observability backend.

Instead:
- trace and span identifiers can be forwarded to any logger
- metrics can be emitted to existing systems
- structured logs remain structured

Teams can integrate with:
- OpenTelemetry-based stacks
- cloud-native monitoring systems
- self-hosted logging and tracing platforms

No changes to application code are required.

---

## Gateway-level metrics (optional)

When a Graftcode Gateway is connected to a project in the Graftcode portal, it can optionally emit:
- aggregated call counts
- latency distributions
- version usage metrics

These metrics are:
- non-payload
- aggregated
- configurable

They are intended to support architectural visibility, not to replace detailed monitoring.

All fine-grained observability remains local and under your control.

---

## Context propagation beyond tracing

In addition to trace identifiers, Graftcode propagates execution context such as:
- correlation identifiers
- logical call scope
- execution boundaries

This allows:
- consistent logging across services
- reliable correlation in distributed debugging
- uniform behavior across runtimes

Context propagation works the same way regardless of execution mode.

---

## Error visibility and diagnostics

When errors occur:
- exception information is propagated
- error messages are preserved
- trace context remains intact

This makes it possible to:
- correlate failures across services
- inspect full call chains
- debug issues using standard tools

There is no need for protocol-specific error mapping or custom status codes.

---

## No vendor lock-in in observability

Because Graftcode integrates at the runtime level:
- observability data remains portable
- tools can be swapped without changing code
- monitoring strategies evolve independently

Graftcode does not become a dependency for logging, tracing, or monitoring.

---

## Why this matters

Distributed systems fail in complex ways.

By preserving observability context across runtime boundaries:
- failures are easier to diagnose
- performance issues are easier to locate
- systems are easier to operate at scale

Graftcode makes distributed execution transparent—not opaque.

---

## In short

Graftcode:
- propagates trace and span context automatically
- integrates with existing observability stacks
- avoids proprietary monitoring formats
- keeps execution visible across runtimes

Observability remains a first-class concern—without becoming a constraint.

---

Next, we’ll look at **scaling, load balancers, and proxies**, and how Graftcode fits naturally into existing infrastructure.
