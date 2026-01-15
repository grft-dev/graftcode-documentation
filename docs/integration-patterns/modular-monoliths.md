---
title: "Modular monoliths"
description: "Learn how Graftcode enables true modular monoliths that evolve into distributed systems without code changes, supporting polyglot modules and runtime-level boundaries."
keywords: "modular monolith, polyglot monolith, graftcode architecture, modular systems"
---

The idea of a *modular monolith* is not new.

For years, it has been presented as a pragmatic alternative to both tightly coupled monoliths and prematurely distributed microservice architectures. In theory, it promises the best of both worlds: the simplicity, performance, and debuggability of a monolith combined with the structure, boundaries, and long-term flexibility of microservices.

In practice, however, most systems that call themselves modular monoliths fail to deliver on that promise.

Not because the idea is wrong—but because the tools used to implement it were never designed to support it fully.

---

## What a modular monolith is meant to be

A true modular monolith is not simply a monolith with folders, namespaces, or conventions.

At its core, a modular monolith is defined by **boundaries**.

Each module should represent a coherent area of responsibility, with a clearly defined public interface and a private implementation. Other parts of the system should be able to interact with that module *only* through its public surface, without relying on internal details.

Crucially, those boundaries must be real—not social contracts enforced by discipline alone.

And most importantly, a modular monolith should allow modules to evolve independently over time. A module that starts life in the same process should be able to move out of process, change runtime, or become an independent service without forcing a rewrite of the code that depends on it.

If extracting a module requires redesigning interfaces, rewriting integration logic, or introducing new communication semantics, then the system was never truly modular to begin with.

---

## Why most modular monoliths break down

Most existing approaches to modular monoliths focus on **compile-time structure**.

They rely on mechanisms such as:
- language-level module systems
- dependency injection containers
- package or namespace boundaries
- architectural rules enforced by convention or tooling

These approaches are valuable, but they stop at the edge of the compiler.

At runtime, everything still executes as direct method calls inside a single address space. There is no enforcement of boundaries beyond what developers remember to respect. Nothing prevents accidental coupling through shared state, internal types, or hidden dependencies.

As long as everything stays in one process, these limitations may remain manageable.

The problem appears the moment a module needs to be extracted.

---

## The extraction cliff

When a module is moved out of process, the system typically falls off an architectural cliff.

Direct method calls must be replaced with some form of remote communication. Interfaces need to be reshaped into DTOs. Serialization must be introduced. Error handling semantics change. Latency becomes visible. Observability has to be rebuilt.

What was once a refactor becomes a redesign.

This is why so many teams either:
- stay stuck in an increasingly tangled monolith, or
- jump too early into microservices and accept the cost of premature distribution

The underlying issue is not organizational or cultural. It is technical.

The integration model changes when the topology changes.

---

## Why traditional integration technologies cannot help

Technologies like REST, gRPC, and messaging systems were never designed to support modular monoliths.

They assume distribution from day one. They introduce transport concerns directly into application design. They require payload-based communication, explicit serialization, and protocol-aware interfaces.

Once introduced, they permanently change how code is written and reasoned about.

These technologies make it possible to build distributed systems—but they make it impossible to *start* as a true monolith and evolve gradually.

They force teams to choose early between:
- local simplicity with long-term rigidity, or
- distributed flexibility with immediate complexity

This is the trade-off modular monoliths were supposed to eliminate.

---

## What a real modular monolith actually requires

To fulfill its promise, a modular monolith needs something fundamentally different.

It needs **runtime-level boundaries**, not just compile-time ones.  
It needs the ability to **virtualize locality**, so that code does not care whether a dependency is in memory or remote.  
It needs **identical execution semantics** regardless of deployment topology.  
And it needs **configuration-driven distribution**, so that architecture can evolve without rewriting code.

In short, integration must operate at the same conceptual level as code execution itself.

This is precisely where existing tools stop—and where Graftcode begins.

---

## Modular monoliths with Graftcode

With Graftcode, modules are defined by public interfaces backed by private implementation, independent of where they run.

Each module exposes a public surface that is consumed through a strongly typed Graft. Internally, the module can evolve freely. Externally, it behaves like a dependency.

Crucially, this dependency model is preserved whether the module runs:
- in the same runtime
- in another runtime within the same process
- or in a completely separate service

From the caller’s perspective, nothing changes.

---

## Starting fully in memory

A system can begin life as a single process where all modules execute in memory.

Calls have near-zero overhead. Debugging feels like working with a traditional monolith. Performance characteristics are predictable and simple.

At the same time, boundaries are real. Public interfaces are enforced. Private implementation details are inaccessible. Modules cannot reach into each other accidentally.

The system behaves like a monolith—but with architectural discipline baked in.

---

## Evolving without rewriting

As requirements change, individual modules can be extracted.

They can be moved to another runtime, another process, or another deployment unit entirely. This evolution is driven by configuration: connection strings, deployment topology, and routing rules.

The code does not change.

The same Grafts continue to be used. The same interfaces remain intact. The same execution semantics apply.

What changes is *where* the code runs, not *how* it is written.

---

## Developing distributed systems like a monolith

One of the most overlooked costs of microservices is local development.

Traditional microservice architectures force developers to run multiple services locally, manage containers or pods, coordinate startup order, and debug across process boundaries. Even simple changes can require a full local environment.

With Graftcode, a logically distributed system can be developed as a single local process.

Multiple modules can be loaded together. All calls execute in memory. Debugging works exactly as it does in a monolith.

Despite this convenience, module boundaries remain intact, and integration semantics are identical to production.

Local development becomes simpler without sacrificing architectural rigor.

---

## The same system, different topologies

The same codebase can be:
- a single-process system during development
- a partially distributed system in staging
- a fully distributed architecture in production

Infrastructure concerns—load balancing, queues, event buses, scaling strategies—are introduced through configuration and plugins, not through code changes.

This separation allows teams to optimize for developer experience locally and operational characteristics in production, without forcing one compromise for the other.

---

## Polyglot modular monoliths

Most discussions of modular monoliths assume a single language and runtime.

Graftcode removes that assumption.

Modules can be implemented in different languages, run in different runtimes, and still participate in the same modular system. A module written in one runtime can be consumed by another as if it were local.

This enables gradual technology evolution, coexistence of legacy and modern code, and truly polyglot systems without fragmentation.

---

## Avoiding premature microservices

Perhaps the greatest advantage of this model is restraint.

Teams can design clear boundaries, keep everything in one process initially, and delay distribution until there is a concrete reason to do so.

Performance remains high. Complexity remains low.

Distribution becomes a deliberate choice—not a forced consequence of tooling.

---

## Observability and safe evolution

Because interactions between modules are strongly typed, traced, and observable, teams gain visibility into how the system actually behaves.

They can see which modules are heavily used, which boundaries are stable, and which areas are ready to be extracted.

Architecture evolves based on evidence, not guesswork.

---

## Closing perspective

A true modular monolith is not defined by folders or frameworks.

It is defined by the ability to change deployment topology without changing code.

By integrating at the runtime level and virtualizing locality, Graftcode finally makes that possible—delivering on the original promise of the modular monolith without forcing early trade-offs or rewrites.
