---
title: "Local, remote, and in-memory execution"
description: "Learn how Graftcode executes the same method calls in memory, locally, or remotely without changing application code, and how architecture can evolve through configuration."
keywords: "graftcode execution modes, in-memory execution, remote execution, distributed systems architecture"
---

One of the core ideas behind Graftcode is that **execution location is not a programming concern**.

Whether code runs:
- in memory
- in the same process
- or on a remote node

the programming model remains the same.

This section explains how these execution modes differ operationally, while remaining identical from the application’s point of view.

---

## One programming model, three execution modes

From the developer’s perspective:
- the same Graft is used
- the same methods are called
- the same types are passed and returned
- the same error handling applies

What changes is **where Hypertube executes the call**, and that decision is made through configuration.

This allows architecture to evolve without rewriting code.

---

## In-memory execution

In-memory execution is the default mode when no routing configuration is provided.

In this mode:
- all runtimes are loaded into a single process
- Hypertube executes calls directly
- no network communication is involved
- overhead is effectively zero

This mode is ideal for:
- local development
- modular monoliths
- early-stage systems
- performance-critical paths

It allows teams to structure code as if it were distributed, while running everything together.

---

## Local multi-runtime execution

Local execution extends the in-memory model to multiple runtimes.

In this mode:
- multiple runtimes (for example, .NET and Python) are hosted side by side
- Hypertube routes calls between runtimes within the same process
- execution remains local
- latency is minimal

This enables:
- true polyglot applications
- gradual technology adoption
- mixing runtimes without network complexity

From the code’s point of view, nothing changes.

---

## Remote execution

Remote execution moves execution to another node.

In this mode:
- calls are routed over TCP/IP or WebSocket
- Hypertube runs on both sides
- execution happens inside a remote runtime hosted by a Graftcode Gateway
- network latency becomes the dominant cost

Despite this:
- call semantics remain the same
- types are preserved
- errors propagate normally
- stateful and stateless behavior works as defined by the interface

Remote execution does not introduce protocol-specific concerns into application code.

---

## Switching execution modes through configuration

Execution mode is selected through the **Graft Connection String**.

This configuration can be:
- omitted (defaulting to in-memory)
- set in code
- overridden via configuration files
- overridden via environment variables

The same application binary can:
- run fully in memory in development
- use local multi-runtime execution in staging
- execute remotely in production

No code changes are required.

---

## Incremental architectural evolution

This model supports gradual evolution.

A typical path looks like this:
1. Start with in-memory execution.
2. Extract a module while keeping the same interface.
3. Route calls to another runtime or process.
4. Move execution to a remote node.
5. Scale and load-balance without touching application code.

At every step, the programming model stays stable.

---

## Performance considerations

Each execution mode has different characteristics:

- **In-memory**  
  Near-zero overhead, maximal performance.

- **Local multi-runtime**  
  Minimal overhead, limited to runtime boundaries.

- **Remote**  
  Network latency applies, but execution remains efficient due to binary, runtime-level communication.

Teams can choose the right mode per use case.

---

## Why this matters

By decoupling code from execution location:
- architectural decisions become reversible
- systems are easier to refactor
- premature distribution is avoided
- distributed systems become easier to reason about

Graftcode allows teams to design for distribution without paying its cost upfront.

---

## In short

Graftcode supports three execution modes:
- in memory
- locally across runtimes
- remotely across nodes

All three use the same interfaces, the same code, and the same execution semantics.

Only configuration changes.

---

Next, we’ll look at **observability, tracing, and context propagation**, and how visibility is preserved across execution boundaries.
