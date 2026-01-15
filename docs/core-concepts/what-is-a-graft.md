---
title: "What is a Graft?"
description: "A Graft is a strongly typed client generated on demand from a public programming interface and delivered through standard package managers, allowing remote services to be consumed like local modules."
keywords: "graftcode graft, strongly typed client, package manager integration, runtime communication, distributed systems"
---


A **Graft** is a strongly typed client generated from a public programming interface and delivered through standard package managers such as NuGet, NPM, Maven, CPAN, RubyGems, Packagist or PyPI.

It allows a remote service to be consumed **as if it were a local module**: installed as a dependency, imported into code, and called using normal method invocations.

The key difference is that a Graft is not written, published, or maintained manually.  
It is **generated on demand**, directly on response for package manager request.

---

## A familiar mental model

Developers already trust the shared module model.

When using a shared library, you:
- add it as a dependency
- import it into your code
- rely on types, signatures, and tooling
- let the compiler and IDE guide you

A Graft follows exactly the same workflow.

The only difference is that the implementation does not live in the same process—or even in the same technology. From the caller’s perspective, that difference disappears.

---

## Generated on demand, not published ahead of time

A common assumption is that Grafts are pre-built packages published to registries.

That is **not** how Graftcode works.

When a package manager requests a Graft:
1. The request goes through the Graftcode registry endpoint.
2. The Graftcode engine analyzes the public interface exposed by the **Graftcode Gateway**.
3. A client package is generated **on the fly** for the requested technology.
4. The generated package is returned to the package manager.
5. The result is cached, so subsequent requests for the same version are served efficiently.

Nothing is generated until something actually asks for it.

Grafts are not created for every service automatically.  
They exist only for the languages and versions that consumers request.

---

## Grafts behave like normal dependencies

Because a Graft is delivered through a package manager, it naturally fits into existing workflows.

When a public interface changes and a new version is exposed:
- consumers update their dependencies
- IDEs immediately reflect the new shape of the interface
- autocomplete shows what changed
- compilation fails if a mandatory parameter was introduced or a member was removed

There is no need for someone to announce changes manually or distribute updated clients.

The programming model already enforces correctness.

This becomes a major advantage in larger teams and distributed systems, where coordination overhead is often higher than the actual change itself.

---

## Strong typing across service boundaries

A Graft preserves strong typing even when calls cross process, machine, or technology boundaries.

Public methods may:
- accept primitive types
- return primitive types
- accept or return structured objects
- accept or return arrays, including multidimensional arrays

From the caller’s point of view, these are just normal types.

The runtime takes care of translating them into equivalent representations in the target technology.

---

## Arrays, collections, and safety

Graftcode fully supports **one-dimensional and multidimensional arrays** for both arguments and return values.

Arrays are treated as data:
- they are transferred eagerly
- they do not hold remote references
- iteration happens locally in the caller’s runtime

This is intentional.

System-level collections or framework-specific types are **not allowed** in public interfaces. The reason is safety and predictability.

Without this restriction, it would be possible to:
- return a remote collection
- iterate over it locally
- unknowingly trigger remote calls on every iteration

While this can be useful in advanced scenarios, it introduces hidden complexity and performance risks.

For now, Graftcode enforces a clear rule:
> **Public interfaces must describe data, not behavior disguised as data.**

In-memory execution is an exception, where richer semantics are supported. Remote execution remains explicit and safe by default. To fully support seamless transition between inmemory and remote execution current version of Graftcode does not allow to use system / framework types and collections in any scenario. This will be enabled for In-Memory only grafts in future. 

---

## Structured objects and DTO detection

When a public method accepts or returns a structured object, Graftcode analyzes how that object behaves.

If the object:
- has no side effects
- contains only data
- exposes no meaningful behavior

it is treated as a **data transfer object**.

In this case:
- the entire object graph is transferred at once
- no additional calls are made for individual fields
- there is no back-and-forth communication

This avoids inefficient call patterns and keeps data transfer predictable.

Automatic DTO detection can be disabled if needed, and is disabled by default for in-memory execution.

---

## Wrapper types and value semantics

Some types represent values, but add semantic meaning or helper behavior—for example:
- dates and times
- identifiers
- coordinates
- colors

Graftcode treats such types as **value wrappers**.

When possible, these values are:
- extracted into their underlying representation
- transferred across the boundary
- reconstructed using native equivalents in the target technology

For example:
- a JavaScript `Date`
- becomes a timestamp
- and is reconstructed as a `.NET DateTime` representing the same point in time

The goal is to preserve meaning, not implementation details.

---

## What a Graft represents

A Graft does not encode:
- transport protocols
- serialization formats
- network topology

It encodes **what can be called**.

How the call is executed—locally, remotely, in memory, over TCP/IP or WebSocket—is a runtime concern handled by Graftcode Hypertube(TM) protocol.

This separation allows interfaces to remain stable while architecture evolves.

---

## Why this matters

Because Grafts behave like real dependencies:
- distributed systems become easier to reason about
- refactoring becomes safer
- tooling becomes more helpful
- AI-assisted development works on real types, not inferred schemas saving a lot of tokens

Developers spend more time writing business logic and less time translating between representations of that logic.

---

## In short

A Graft turns a remote service into a dependency, generated on demand, delivered through familiar tools, and enforced by strong typing.

It brings the discipline of shared modules into distributed systems—without asking developers to think in terms of endpoints, payloads, or protocols.

---

Next, we’ll look at **public interfaces and business logic**, and why respecting that boundary becomes critical when code is consumed remotely.
