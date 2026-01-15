---
title: "Modular monoliths"
description: "Learn how Graftcode enables true modular monoliths that evolve into distributed systems without code changes, supporting polyglot modules and runtime-level boundaries."
keywords: "modular monolith, polyglot monolith, graftcode architecture, modular systems"
---

# Modular monoliths

The idea of a *modular monolith* has existed for years.

In theory, it promises the best of both worlds:
- the simplicity and performance of a monolith
- the structure and boundaries of microservices

In practice, however, most “modular monoliths” fall short of that promise.

---

## What a modular monolith is supposed to be

A true modular monolith should:
- consist of clearly separated modules
- enforce explicit boundaries between them
- prevent accidental coupling
- allow independent evolution of modules

Most importantly, it should allow those modules to:
- move out of process
- move to another runtime
- or become separate services

**without changing application code.**

If moving a module requires rewriting integration logic, the system was never truly modular.

---

## Why existing approaches fall short

Most existing approaches rely on:
- framework-level module systems
- dependency injection containers
- package or namespace conventions
- compile-time boundaries only

These approaches help with structure, but they fail at runtime boundaries.

When a module needs to be extracted:
- direct method calls must be replaced
- interfaces must be redesigned
- serialization must be added
- new communication mechanisms must be introduced

At that point, the system stops behaving like a monolith and starts behaving like a rewrite.

---

## Integration technologies don’t solve this

Traditional integration technologies—REST, gRPC, messaging systems—were never designed for modular monoliths.

They assume:
- distribution from day one
- explicit transport concerns
- payload-based communication

They do not allow a system to:
- start in memory
- evolve gradually
- or switch execution topology transparently

As a result, teams are forced to choose too early between:
- a tightly coupled monolith
- or a prematurely distributed system

---

## What a *real* modular monolith requires

A real modular monolith requires something different:

- runtime-level boundaries, not just compile-time ones
- the ability to virtualize locality
- identical execution semantics in-memory and out-of-process
- configuration-driven distribution
- support for multiple runtimes and languages

In other words: **integration must operate at the same level as code execution**.

This is where existing tools stop—and where Graftcode starts.

---

## Modular monoliths with Graftcode

Graftcode allows modules to be defined as **public interfaces backed by private implementation**, regardless of where they run.

Each module:
- exposes a public facade
- is consumed through a strongly typed Graft
- is isolated by runtime boundaries enforced by Hypertube

From the caller’s perspective, a module is just a dependency.

---

## Starting fully in memory

A system can start as a single process where:
- all modules run in memory
- calls have near-zero overhead
- execution behaves like normal method calls

Despite this:
- module boundaries are real
- public interfaces are enforced
- private implementation details are inaccessible

The system behaves like a monolith—but with discipline.

---

## Gradual extraction without code changes

As the system grows, individual modules can be:
- moved to another runtime
- moved to another process
- deployed as separate services

This is done by:
- changing Graft configuration
- updating connection strings
- adjusting deployment topology

**No code changes are required.**

The same Grafts continue to work, and the same interfaces are preserved.

---

## Developing distributed systems like a monolith

One often overlooked cost of microservices is local development.

In a traditional microservice architecture, working on a distributed system usually means:
- running multiple services locally
- starting many containers or pods
- managing ports, configuration, and startup order
- dealing with partial system availability

This makes everyday development slow and cognitively expensive.

---

### One local process, many logical services

With Graftcode, developers can work locally on a system that is **logically distributed**, but **physically unified**.

Instead of running multiple services, a developer can:
- load multiple modules in a single process
- execute all interactions in memory
- debug and step through code as if it were a monolith

Despite this:
- module boundaries are preserved
- public interfaces are enforced
- integration semantics remain exactly the same

Local development becomes significantly simpler, without sacrificing architectural discipline.

---

### The same system, different topology

What runs locally as a single process can be deployed in the cloud as:
- multiple independent services
- separate runtimes
- components scaled independently
- systems connected through queues, topics, or event buses

The critical point is that **the code does not change**.

Only configuration and deployment topology differ between:
- local development
- staging environments
- production systems

---

### No local infrastructure burden

Developers do not need to:
- run multiple pods
- maintain local message brokers
- simulate production-grade infrastructure
- recreate full cloud environments on their machines

They can focus on:
- business logic
- module boundaries
- interface design

Infrastructure concerns are applied later, through configuration and deployment.

---

### Distributed behavior where it belongs

In production:
- calls are routed remotely
- services scale independently
- transport plugins can introduce queuing, fan-out, or transactional processing

Locally, the same system behaves as a single executable unit.

This separation allows teams to optimize:
- developer experience during development
- operational characteristics in production

without forcing one compromise for the other.

---

## Polyglot modular monoliths

Most modular monolith discussions assume a single language.

Graftcode removes that limitation.

Modules within a modular monolith can:
- be implemented in different languages
- run in different runtimes
- coexist within the same process or across processes

A module written in one runtime can be consumed by another as if it were local.

This enables:
- gradual technology adoption
- coexistence of legacy and modern code
- true polyglot architectures without fragmentation

---

## Avoiding premature microservices

One of the biggest advantages of this model is restraint.

Teams can:
- design clear boundaries
- keep everything in one process initially
- delay distribution until it is justified

Performance stays high.
Complexity stays low.

Distribution becomes a choice, not a requirement.

---

## Observability and refactoring safety

Because module interactions:
- are strongly typed
- propagate trace context
- surface errors naturally

teams can:
- refactor with confidence
- observe real usage patterns
- identify which modules are ready to be extracted

Architecture evolves based on evidence, not guesses.

---

## Why this works

This approach works because:
- integration happens at the runtime level
- locality is virtualized
- interfaces are explicit and enforced
- execution semantics never change

The system behaves the same way regardless of deployment topology.

---

## In short

With Graftcode, a modular monolith:
- starts as a single, fast process
- enforces real module boundaries
- supports polyglot modules
- evolves into distributed services without code changes

It finally delivers on the original promise of the modular monolith—without compromise.
