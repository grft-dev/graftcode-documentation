---
title: "Internal business APIs"
description: "Learn how to design and consume internal business APIs using Graftcode as strongly typed modules instead of traditional REST or gRPC endpoints."
keywords: "internal apis, business apis, internal services, graftcode integration patterns"
---

Most systems have APIs that are not meant for the outside world.

They exist to:
- connect internal systems
- share business capabilities
- coordinate workflows between teams

Yet, these **internal business APIs** are often implemented using the same tools and patterns as public APIs—despite having very different requirements.

Graftcode offers a model that fits internal APIs much more naturally.

---

## The problem with traditional internal APIs

Internal APIs are usually built with:
- REST controllers
- gRPC services
- message-based RPC layers

Over time, this leads to familiar problems:
- everything becomes public “by accident”
- internal details leak into contracts
- refactoring becomes risky
- teams stop trusting internal APIs

The original intent—*“this is just internal”*—gets lost.

---

## Internal APIs are not public contracts

Internal business APIs:
- have known consumers
- evolve together with the organization
- do not need the same level of backward-compatibility guarantees as public APIs

They should behave more like **shared internal libraries**, not internet-facing endpoints.

Graftcode is designed precisely for this use case.

---

## Business capabilities as typed modules

With Graftcode, an internal business API is expressed as:
- a set of public facade classes
- with explicitly public methods
- backed by private implementation details

Only what is marked as `public` becomes callable remotely.

Everything else remains internal—by design, not by convention.

This brings back a discipline that traditional API layers often erode.

---

## Strong boundaries through language semantics

Instead of enforcing boundaries through:
- URL structures
- controller folders
- documentation conventions

Graftcode relies on **language-level visibility rules**.

If something is not public:
- it is not part of the Unified Graft Model
- it cannot be called remotely
- it cannot be consumed by mistake

Developers regain trust in what is actually exposed.

---

## Faster iteration with lower coordination cost

Because internal APIs are consumed as typed dependencies:
- changes are visible immediately in IDEs
- incompatible changes fail at build time
- refactoring is safer and faster

Teams do not need to:
- update OpenAPI specs
- regenerate clients
- synchronize deployments manually

The feedback loop is much tighter.

---

## Error handling that matches business logic

Internal APIs often use rich domain-specific errors.

Graftcode supports this naturally:
- business exceptions are thrown normally
- they propagate across service boundaries
- callers handle them using standard `try/catch` logic

There is no need to flatten errors into status codes or error envelopes.

---

## Versioning when it matters, not by default

For many internal APIs:
- strict versioning is unnecessary
- coordinated evolution is acceptable

Graftcode supports both:
- evolutionary changes without version bumps
- explicit versioning when stability is required

The level of formality can match the real needs of the organization.

---

## Gradual extraction and refactoring

Internal APIs often emerge from existing code.

With Graftcode, teams can:
- start with in-memory modules
- expose selected public interfaces
- extract modules into separate services later
- keep the same integration code throughout

This enables large refactorings without a “big rewrite”.

---

## Why this pattern works

This pattern works because:
- it matches how developers already think about internal code
- boundaries are explicit and enforced by the language
- tooling provides immediate feedback
- architecture can evolve incrementally

Internal APIs stop feeling like fragile integrations—and start feeling like shared code.

---

## In short

With Graftcode, internal business APIs:
- are expressed as typed modules
- expose only intentional public surfaces
- evolve safely and predictably
- integrate naturally with existing codebases

Internal integration becomes disciplined, fast, and trustworthy.
