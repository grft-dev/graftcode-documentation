---
title: "When should you use Graftcode?"
description: "Graftcode works best when systems communicate through well-defined interfaces that evolve over time. Learn when Graftcode is a good fit and when other approaches may still make sense."
keywords: "when to use graftcode, service communication patterns, microservices integration, api alternatives, distributed systems design"
---

# When should you use Graftcode?

Graftcode is not a universal answer to every communication problem.  
It is designed for a specific set of scenarios—ones that appear frequently in modern systems and tend to grow in complexity over time.

Understanding when Graftcode fits well helps teams adopt it naturally, without forcing it into places where simpler solutions are sufficient.

---

## When Graftcode is a good fit

### Backend-to-backend communication

Graftcode works especially well when services call other services.

Instead of defining endpoints and clients, you expose a public interface and consume it as a dependency. Calls remain strongly typed, errors propagate as native exceptions, and changes are easier to reason about.

This is often the first place teams see immediate value.

---

### Internal business APIs

Many systems expose APIs not for the outside world, but for other internal components or teams.

In these cases:
- stability matters more than protocol standardization
- strong typing matters more than URL structure
- evolution matters more than strict versioning schemes

Graftcode allows internal APIs to behave like shared modules, even when they are deployed separately.

Optionally, anything you expose via Graftcode Gateway can also be published as MCP tools for AI clients—without rewriting your API surface.

---

### Edge clients calling backend logic

When frontend or edge applications need access to business capabilities, APIs are often shaped around transport rather than intent.

Graftcode allows those clients to consume business logic directly through typed interfaces, while still operating over standard network transports.

This reduces duplication between backend logic and API representations of that logic.

---

### Systems that evolve over time

Architectures rarely stay fixed.

Services are split, merged, moved, or rehosted. Communication patterns change. Infrastructure decisions are revisited.

Graftcode decouples *how code is called* from *where it runs*, making these changes easier to apply without rewriting application logic.

---

### Teams working across technologies

When different parts of a system are written in different languages or runtimes, communication often becomes the least common denominator.

Graftcode allows each side to remain idiomatic to its own technology while sharing a single interface definition at the runtime level.

This is particularly useful in organizations that standardize on interfaces rather than implementations.

---

## When Graftcode may not be necessary

### Simple, static integrations

If you have a small number of services with stable, rarely changing interfaces, a traditional API may be sufficient.

Graftcode shines when communication evolves. If it doesn’t, the benefits may be less pronounced.

---

### Public, protocol-driven APIs

Some APIs are designed primarily for external consumers and are intentionally shaped around widely adopted standards.

In these cases, REST or similar approaches may still be the right choice—especially when human readability or protocol-level compatibility is a primary concern.

Graftcode does not prevent you from continuing to offer such APIs alongside it.

---

### One-off data exchange

For simple, asynchronous data handoffs or batch-style processing, introducing runtime-level integration may be unnecessary.

Graftcode is optimized for **calling behavior**, not for occasional data transfer.

---

## Using Graftcode alongside existing solutions

Adopting Graftcode does not require replacing existing communication mechanisms.

Many teams:
- start with a single service
- use Graftcode for internal communication
- keep REST or gRPC for external access

Over time, usage expands naturally where it provides clear value.

This incremental approach allows teams to learn the model and validate it in real systems.

---

## A practical rule of thumb

Graftcode is a strong candidate when:

- you care about type safety across service boundaries
- interfaces change and evolve
- communication logic is starting to influence architecture decisions
- you want remote code to feel closer to local code

If those statements resonate, Graftcode is likely worth exploring.

---

## Choosing deliberately

The goal of Graftcode is not to replace every form of communication, but to reduce the cost of the most common ones.

Used deliberately, it becomes a tool that simplifies systems rather than adding another layer to manage.

---

Next, we’ll move from *when* to *how*, starting with the core building block behind everything: **the Graft**.
