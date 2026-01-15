---
title: "Public interface vs business logic"
description: "Learn how Graftcode separates public interfaces from business logic, why this boundary matters in distributed systems, and how it enables safe evolution, stateful and stateless services."
keywords: "public interface, business logic, stateless services, stateful services, distributed systems design, graftcode"
---

In every codebase—whether local or distributed—there is an implicit boundary between **what is exposed** and **what is internal**.

In small applications, this boundary is often informal.  
In shared libraries, it is explicit and carefully designed.

In distributed systems, however, this boundary is frequently blurred.

Graftcode restores that boundary and makes it explicit again—even when code runs remotely.

---

## A rule developers already know

When working with shared modules, developers instinctively follow a few rules:

- only selected classes and methods are public
- internal details remain private
- changes to public interfaces are deliberate
- breaking changes are avoided or carefully versioned

This discipline exists because shared modules are consumed directly as code.  
Any mistake is immediately visible to the compiler and the IDE.

Remote services rarely benefit from the same discipline—not because developers don’t care, but because traditional integration tools do not encourage it.

---

## What changes when code becomes remote

Once code is accessed remotely, the notion of `public` often loses its meaning.

Everything exposed through an API:
- becomes reachable
- becomes callable
- becomes someone else’s dependency

As a result, interfaces tend to grow organically:
- internal details leak out
- abstractions erode
- compatibility becomes harder to maintain

Graftcode treats remote services the same way shared modules are treated locally.

If something is public, it is public by design.  
If something is private, it stays private—even across the network.

---

## Public interfaces in Graftcode

In Graftcode, the **public interface** is the only part of a service that is visible to consumers.

It is defined using normal programming constructs:
- classes
- methods
- method signatures
- argument and return types

Only what is explicitly public becomes callable.

Everything else—internal helpers, state management, implementation details—remains invisible and inaccessible.

This makes the public interface a **deliberate contract**, not an accidental one.

---

## Business logic stays business logic

Business logic does not need to be reshaped to fit a communication protocol.

With Graftcode:
- there are no controllers to design
- no request or response models to mirror
- no transport-specific abstractions to introduce

Business logic is written as business logic.  
The public interface is simply a façade over it.

This keeps code readable, testable, and close to its intent.

---

## Stateless and stateful services

The way a public interface is designed determines whether a service behaves as stateless or stateful.

### Stateless interfaces

Stateless services expose **static methods on static classes**.

Each call:
- is independent
- carries all required input
- produces a single response

This model resembles traditional request–response APIs and is well suited for:
- edge clients
- browser-facing APIs
- simple backend integrations

Statelessness is explicit and visible in the code.

---

### Stateful interfaces

Stateful services expose **objects with lifecycle and behavior**.

Clients may:
- create instances
- invoke multiple methods
- subscribe to events
- maintain long-lived, duplex connections

This model allows richer interaction patterns, similar to:
- in-memory objects
- session-based services
- real-time communication

Because state is explicit, the runtime can route calls consistently to the correct execution context.

---

## Choosing deliberately

Neither stateless nor stateful is “better” by default.

What matters is that the choice is:
- intentional
- visible in code
- aligned with how the service is meant to be used

For example:
- public APIs for browsers typically expose stateless interfaces
- internal services may safely expose richer, stateful behavior

Graftcode supports both, but does not blur the line between them.

---

## Interface evolution and stability

Public interfaces are promises.

Once exposed, they should evolve carefully:
- new methods can be added
- optional parameters can be introduced
- existing methods should remain compatible

This approach allows older consumers to keep working while newer ones adopt additional capabilities.

When an interface is no longer needed, it can be deprecated and eventually removed—once usage has dropped.

This mirrors how shared modules evolve and avoids forced, synchronized upgrades.

---

## Why this boundary matters more in distributed systems

In distributed systems, the cost of breaking a public interface is higher:
- failures happen at runtime
- errors propagate across services
- debugging becomes harder

By enforcing a clear separation between public interfaces and business logic, Graftcode:
- reduces accidental coupling
- makes changes safer
- improves long-term maintainability

The same rules that make shared libraries reliable also make distributed systems easier to evolve.

---

## In short

Graftcode brings back a familiar and disciplined model:

- public interfaces are explicit and intentional
- business logic remains internal
- stateless and stateful behavior is visible in code
- interface evolution follows proven rules

Remote services stop being special cases and start behaving like shared modules—just deployed somewhere else.

---

Next, we’ll introduce **callers and receivers**, and how Graftcode connects them at runtime.
