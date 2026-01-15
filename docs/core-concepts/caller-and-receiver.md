---
title: "Caller and Receiver"
description: "Learn how Graftcode models communication using callers and receivers instead of traditional client–server roles, enabling symmetric, runtime-level interaction between systems."
keywords: "caller receiver model, distributed systems communication, graftcode concepts, service interaction model"
---

# Caller and Receiver

In traditional distributed systems, communication is usually described in terms of **clients** and **servers**.

One side sends requests.  
The other side responds.

This model works, but it also introduces assumptions that are not always helpful—especially once systems become more dynamic, stateful, or symmetric.

Graftcode uses a different mental model: **caller** and **receiver**.

---

## Why not client and server?

The client–server distinction is rooted in networking, not in programming.

It implies:
- fixed roles
- directional dependency
- a request–response mindset

In practice, modern systems rarely fit this cleanly:
- services call each other
- roles switch depending on context
- communication becomes bidirectional

Graftcode avoids this framing and instead describes communication in terms of **who is calling** and **who is receiving** at a given moment.

These roles are temporary, not structural.

---

## The caller

A **caller** is any piece of code that invokes a method exposed by a public interface.

From the caller’s perspective:
- it holds a Graft
- it calls methods on it
- it receives return values or exceptions

The caller does not know:
- where the code runs
- how the call is transported
- whether the receiver is local, remote, or in memory

It simply calls code.

---

## The receiver

A **receiver** is the runtime that hosts the actual implementation of the public interface.

From the receiver’s perspective:
- it exposes selected classes and methods
- it executes business logic
- it returns results or throws exceptions

The receiver does not know:
- who the caller is
- which language the caller uses
- whether the call originated locally or remotely

It simply runs code.

---

## A symmetric relationship

The important part is that **caller and receiver are symmetric roles**.

The same application can:
- be a caller in one interaction
- be a receiver in another
- sometimes be both at the same time

There is no permanent “client” or “server” identity.

This symmetry becomes especially important when:
- services call each other in cycles
- systems are composed of many small modules
- responsibilities shift over time

---

## Calls, not messages

In the caller–receiver model, interaction is expressed as **method calls**, not messages.

This has several consequences:
- arguments are passed as values
- results are returned directly
- errors are raised as exceptions

The interaction follows the same rules developers expect from local code.

The runtime is responsible for translating this interaction into an appropriate execution strategy.

---

## State and lifecycle

The caller–receiver model also makes state explicit.

If the public interface:
- exposes only static methods  
  → calls are stateless and independent

If the public interface:
- exposes objects
- maintains subscriptions
- reacts to events  
  → calls are stateful and tied to a lifecycle

The model does not hide state—it makes it visible in code.

This allows developers to reason about behavior before thinking about deployment or transport.

---

## Bidirectional and duplex communication

Because roles are not fixed, communication does not have to be one-way.

A receiver can:
- call back into the caller
- emit events
- participate in long-lived, duplex interactions

From the programming perspective, this still looks like calling methods and handling events—not managing connections or sessions explicitly.

---

## Why this matters

By replacing client–server thinking with caller–receiver thinking, Graftcode:
- removes protocol-driven assumptions
- aligns communication with programming concepts
- supports richer interaction patterns naturally

It becomes easier to design systems where:
- responsibilities are shared
- components evolve independently
- communication patterns change over time

---

## In short

In Graftcode:
- **caller** means “the code that invokes”
- **receiver** means “the code that executes”
- roles are dynamic and symmetric
- communication is expressed as method calls

This shift in perspective prepares the ground for runtime-level integration—where *how* calls are executed becomes a configuration detail, not a design constraint.

---

Next, we’ll look at **the Graftcode Gateway**, and how it connects callers and receivers at runtime.
