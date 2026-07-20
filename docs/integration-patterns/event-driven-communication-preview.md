---
title: "Event-driven communication (preview)"
description: "Compatibility notice for event-driven and messaging capabilities."
keywords: "event-driven architecture, messaging, graftcode plugins"
---

# Event-driven communication (preview)

General event-driven communication is not documented as a currently available Graftcode capability.

The inspected product evidence does not establish queue or topic adapters, fan-out, delayed execution, retries, dead-letter handling, transactions, ordering, at-least-once or exactly-once delivery, or unchanged method semantics over a message broker. Do not design or operate a system assuming those behaviors.

Use a broker's supported SDK and explicitly model messages, delivery semantics, idempotency, retries, and observability when event-driven communication is required.

This route is retained only for compatibility. Current Graftcode invocation behavior is documented in [Invocation lifecycle](../core-concepts/invocation-lifecycle.md), and supported connection forms are bounded by [Execution modes](../core-concepts/execution-modes.md) and the active Gateway/runtime release.
