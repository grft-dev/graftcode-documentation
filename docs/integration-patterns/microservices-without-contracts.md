---
title: "Microservices without contracts"
description: "Learn how Graftcode enables microservices to communicate without separate API contracts, schemas, or IDLs by using strongly typed public code as the contract."
keywords: "microservices without contracts, api contracts, strongly typed microservices, graftcode architecture"
---

Microservices are often described as “independently deployable units.”

In practice, however, most microservice architectures are held together by a growing number of **contracts**:
- OpenAPI specifications
- protobuf definitions
- JSON schemas
- manually maintained API documentation

These contracts are necessary—but they also introduce friction, duplication, and drift.

Graftcode takes a different approach:
**microservices communicate without separate contracts**, using code itself as the contract.

---

## What “without contracts” actually means

This does **not** mean:
- no interfaces
- no compatibility rules
- no discipline

It means:
- no separate contract artifacts
- no duplicated schemas
- no manually synchronized definitions

The contract still exists—it is just expressed **directly in code**.

---

## Public code as the contract

In Graftcode, a microservice exposes:
- public facade classes
- with public methods
- using native language types

This public surface:
- is analyzed by the Graftcode Gateway
- becomes the Unified Graft Model
- is consumed by other services as a typed dependency

There is no additional schema or IDL layer.

What is public in code *is* the contract.  
What is private remains private.

---

## Strong typing replaces schema validation

Traditional microservice contracts rely on:
- runtime validation
- schema compatibility checks
- defensive deserialization

With Graftcode:
- method signatures are strongly typed
- arguments and return values are validated at compile time
- incompatible changes surface immediately in the IDE or CI

Instead of validating payloads at runtime, systems validate **code at build time**.

---

## No client generators, no drift

In traditional setups:
- contracts are defined
- clients are generated
- implementations evolve
- contracts and clients drift

With Graftcode:
- clients (Grafts) are generated on demand
- directly from the live public interface
- for the target language

There is no manual regeneration step and no opportunity for drift.

---

## Independent deployment without fragile coordination

Microservices still deploy independently.

What changes is how compatibility is handled:
- older Grafts continue to work with older interfaces
- newer Grafts opt into newer interfaces
- upgrades are explicit and deliberate

There is no need for synchronized deployments or “flag days.”

---

## Evolution instead of version explosion

Because interfaces are consumed as code:
- evolutionary changes are natural
- optional parameters and overloads are easy
- multiple versions can coexist

Teams stop versioning defensively and start evolving intentionally.

---

## Clear ownership and responsibility

This model makes ownership explicit.

The service owner is responsible for:
- what is public
- how it evolves
- when breaking changes are introduced

Consumers are responsible for:
- when they upgrade
- how they adapt to new capabilities

There is no ambiguous shared contract artifact in between.

---

## Observability remains intact

Removing separate contracts does not remove visibility.

Calls are still:
- traced
- logged
- observable

Errors still propagate as structured exceptions, not opaque failures.

The operational characteristics of microservices remain unchanged.

---

## When this pattern works best

This approach works particularly well when:
- services are written by teams comfortable with strong typing
- interfaces evolve frequently
- fast feedback is valued over strict upfront specification
- internal microservices dominate the architecture

It is especially effective for internal systems and platforms.

---

## When to be cautious

For external, publicly consumed APIs:
- explicit, long-lived contracts may still be appropriate
- additional governance may be required

Graftcode does not forbid contracts—it removes the *need* for separate ones in many cases.

---

## What changes in practice

Teams adopting this model typically notice:
- fewer integration bugs
- faster refactoring
- less documentation drift
- tighter feedback loops

Microservices start feeling less like distributed endpoints and more like distributed code.

---

## Closing perspective

Microservices without contracts does not mean “microservices without discipline.”

It means:
- one source of truth
- no duplicated definitions
- and contracts enforced by the compiler instead of by convention

Graftcode turns microservice communication back into a software engineering problem—rather than a schema management problem.
