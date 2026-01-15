---
title: "Event-driven communication (preview)"
description: "Explore how Graftcode approaches event-driven communication using runtime-level execution and transport plugins, without introducing a separate event programming model."
keywords: "event-driven architecture, async communication, event bus, graftcode plugins, distributed events"
---

Event-driven communication is a natural requirement in many systems.

Teams use it to:
- decouple producers from consumers
- process work asynchronously
- scale independently
- introduce buffering, retries, and transactional guarantees

Traditionally, adopting event-driven architecture means adopting **a completely different programming model**.

Graftcode approaches this differently.

---

## Event-driven does not have to mean event-shaped code

In most systems, moving to events requires developers to:
- stop calling methods
- start publishing messages
- design event payloads
- manage serialization and schemas
- reason about delivery semantics explicitly

This creates a sharp divide between:
- synchronous, request–response code
- and asynchronous, event-driven workflows

Graftcode aims to remove that divide.

---

## Events as execution routing, not a new abstraction

In Graftcode, event-driven communication is treated as a **routing concern**, not a programming model.

From the developer’s perspective:
- methods are still called
- signatures are still strongly typed
- return values and exceptions still exist

What changes is **how the invocation intent is delivered**.

Instead of being routed directly to a single receiver, execution can be:
- queued
- fanned out
- delayed
- or coordinated through an external system

---

## Transport plugins as the foundation

Event-driven behavior in Graftcode is enabled through **transport plugins**.

A transport plugin can:
- forward invocation intent to a message queue
- publish it to a topic
- enqueue it for later processing
- participate in transactional event flows

From the application’s point of view, this is equivalent to:
- manually using a queue or event bus SDK
- serializing a message
- publishing it

The difference is that:
- no code changes are required
- no new APIs are introduced
- interfaces remain the same

---

## Multiple subscribers and fan-out

When transport plugins support it, invocation intent can be:
- delivered to multiple subscribers
- processed independently by different receivers
- handled with different scaling strategies

Each receiver:
- hosts its own Hypertube
- executes the same strongly typed interface
- returns results or emits follow-up events through configured channels

This enables classic event-driven patterns without fragmenting the programming model.

---

## Asynchronous execution and delayed processing

Transport plugins can also introduce:
- asynchronous execution
- delayed processing
- retry policies
- dead-letter handling

These behaviors are controlled through configuration and plugin choice, not through changes to business code.

A method call can become:
- fire-and-forget
- eventually consistent
- or transactionally coordinated

without changing its signature.

---

## State, transactions, and coordination

Some event-driven systems require:
- transactional guarantees
- coordinated state changes
- ordered processing

By routing invocation intent through external systems that already provide these guarantees, Graftcode can participate in:
- transactional event buses
- exactly-once processing models
- ordered or partitioned execution

Graftcode does not reimplement these systems—it integrates with them.

---

## Local development vs production behavior

As with other Graftcode patterns:
- local development can run fully in memory
- events can execute synchronously
- debugging remains simple

In production:
- the same calls can be routed through queues or topics
- scaling and buffering emerge naturally
- operational complexity is applied only where needed

The programming model remains stable across environments.

---

## Why this is a preview

Event-driven communication through transport plugins is an evolving area.

The core runtime model already supports:
- asynchronous execution
- callbacks and events
- routing through plugins

What is evolving is:
- the ecosystem of plugins
- standardized configuration patterns
- tooling around event flows

This section describes the architectural direction rather than a fixed, final feature set.

---

## How this fits the overall model

Event-driven communication in Graftcode:
- does not introduce a second integration paradigm
- does not replace method-based execution
- does not require event-specific code

It extends the existing runtime-level execution model to cover asynchronous and event-based delivery.

The system remains one system—just with more ways to route execution.
