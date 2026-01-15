---
title: "Hypertube™ runtime bridge"
description: "Hypertube™ is a runtime-level bridge that connects different runtimes and languages, executing strongly typed calls in memory or over the network using a unified binary protocol."
keywords: "hypertube runtime bridge, runtime integration, distributed systems execution, binary protocol, graftcode performance"
---


**Hypertube™** is the runtime-level bridge that connects callers and receivers in Graftcode.

It is responsible for executing strongly typed calls:
- within a single process
- across multiple runtimes
- or over the network

Hypertube operates **below application code** and **above infrastructure**, allowing distributed execution to behave like local execution.

---

## Runtime-level integration

Most integration technologies operate at the protocol level.

They define:
- how messages are formatted
- how requests are sent
- how responses are returned

Hypertube operates at a different level.

It connects **runtimes**, not endpoints.

Instead of translating code into requests, Hypertube executes **programming intent** directly inside the target runtime.

From the perspective of application code, there is no protocol—only method calls.

---

## One execution model, multiple deployment modes

Hypertube supports the same execution semantics in different environments.

A call can be executed:
- **in memory**, within a single process
- **locally**, across multiple runtimes on the same machine
- **remotely**, across machines using TCP/IP or WebSocket

The important part is that the *programming model does not change*.

The same public interface, the same Graft, and the same call semantics apply in all cases.

Deployment decisions are configuration choices, not design constraints.

---

## In-memory execution

When calls are executed in memory:
- runtimes are loaded into a single process
- calls are dispatched directly
- overhead is effectively zero

There is no serialization, no networking, and no context switching beyond what the runtime itself requires.

In this mode, Graftcode behaves like a polyglot, multi-runtime application running inside one process.

---

## Remote execution

When calls are executed remotely:
- Hypertube uses a binary protocol
- messages are compact and efficient
- execution is dominated by network latency

There is no JSON parsing, no text-based encoding, and no middleware pipeline.

This is why remote execution through Hypertube is significantly faster and more resource-efficient than REST or gRPC-based approaches.

---

## Intention Invocation Protocol (IIP)

Hypertube communicates using a binary format called the  
**Intention Invocation Protocol (IIP)**.

IIP is designed to represent **programming intent**, not network messages.

An IIP message can describe:
- a single method invocation
- nested method calls
- complex execution graphs, similar to lambda expressions

This allows Hypertube to transmit *what should happen*, not just data.

The same protocol is used:
- in memory
- across processes
- across the network

This consistency is essential for runtime virtualization.

---

## Unified Graft Model (UGM)

IIP also defines the format of the **Unified Graft Model (UGM)**.

UGM is a language-agnostic description of:
- public interfaces
- methods and signatures
- argument and return types
- supported interaction patterns

Hypertube uses UGM to:
- validate calls
- route execution
- enforce compatibility

Graftcode Vision uses the same model to visualize and document interfaces.

Both IIP and UGM are designed to be **open and extensible**, enabling third-party tooling such as debuggers, inspectors, and monitoring tools.

---

## Synchronous and asynchronous virtualization

Hypertube virtualizes execution semantics.

This means it adapts how a call is executed based on:
- how the caller invokes it
- what the underlying transport supports

Examples:
- a synchronous call over an asynchronous channel
- an asynchronous call over a stateful, duplex connection
- event subscriptions mapped onto callback invocations

From the developer’s point of view, the call behaves exactly as requested.

Hypertube absorbs the mismatch between programming intent and transport capabilities.

---

## Full-duplex communication

Hypertube connections are **full duplex**.

Once a session is established:
- calls can flow in both directions
- events can be emitted from receiver to caller
- callbacks and delegates can be invoked remotely

This enables interaction patterns similar to:
- in-memory objects
- observer patterns
- real-time communication systems

All of this happens without exposing connection management in application code.

---

## Performance characteristics

Hypertube is designed to minimize overhead.

Key characteristics include:
- binary message format
- no text serialization
- no reflection-based dispatch loops
- no middleware pipelines

In-memory execution is effectively free.

Remote execution adds only network latency, which is why Hypertube-based calls are often significantly faster than REST or gRPC, and require less CPU and memory.

---

## Why Hypertube exists

Hypertube exists to solve a fundamental problem:

> **Programming languages already know how to express intent.  
> Networks do not.**

Instead of forcing intent into network-friendly shapes, Hypertube carries intent directly between runtimes.

This is what allows Graftcode to treat local and remote execution as variations of the same thing.

---

## In short

Hypertube™ is:
- a runtime-level execution bridge
- a carrier of programming intent
- a unifier of in-memory and remote execution

It is the component that makes strongly typed, protocol-free communication possible across runtimes and languages.

---

Next, we’ll look at **Graftcode Vision**, and how live interfaces, documentation, and interactive exploration are built on top of the same runtime model.
