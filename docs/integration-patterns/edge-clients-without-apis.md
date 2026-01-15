---
title: "Edge clients without APIs"
description: "Learn how edge clients can consume backend logic directly through Graftcode without building traditional APIs, while keeping security and architecture under control."
keywords: "edge clients, frontend integration, no api backend, graftcode edge integration, strongly typed clients"
---

# Edge clients without APIs

For years, edge clients—browsers, mobile apps, desktop apps—have been forced to talk to backends through APIs.

Not because APIs were ideal, but because they were the only practical option.

Graftcode introduces a different possibility:
**edge clients can consume backend logic directly, without building traditional APIs**.

This does not remove architectural responsibility—but it simplifies it dramatically.

---

## The traditional edge integration problem

In a typical setup:
- backend teams design APIs
- frontend teams consume them
- DTOs are duplicated
- contracts drift
- changes require coordination

Even small backend changes often require:
- updating API definitions
- regenerating clients
- fixing runtime errors

Most of this effort exists purely to bridge the gap between client and server.

---

## Edge clients as typed consumers

With Graftcode, an edge client can consume backend functionality as a **strongly typed dependency**.

From the client’s point of view:
- a remote service looks like a local module
- methods are discoverable through the IDE
- types are enforced at compile time
- errors are handled using normal language constructs

There are no endpoints to memorize and no schemas to synchronize.

---

## Stateless by design for edge clients

For edge clients, **stateless interaction is the recommended model**.

This is achieved by:
- exposing static methods
- avoiding long-lived server-side state
- treating each call as independent

This maps naturally to:
- browser applications
- mobile clients
- desktop applications
- external consumers

It also aligns well with scalability and security best practices.

---

## Security boundaries remain explicit

Removing APIs does not remove security.

Authentication and authorization are still:
- explicit
- enforced at the Gateway
- implemented through plugins

Edge clients never receive:
- business logic
- internal implementation details
- access beyond what is explicitly exposed

Only public interfaces are reachable—and only through configured security mechanisms.

---

## Strong typing improves frontend development

Because edge clients consume typed dependencies:
- autocomplete becomes the primary documentation
- invalid calls fail at build time
- breaking changes are visible immediately

Frontend developers no longer need to:
- inspect API docs
- reverse-engineer payloads
- guess field names or shapes

The IDE becomes the contract.

---

## Faster iteration, safer changes

When backend interfaces evolve:
- new capabilities appear automatically
- older clients continue to work
- incompatible changes are detected early

This dramatically reduces:
- runtime failures
- silent contract drift
- integration bugs discovered late

Edge development becomes more predictable and less fragile.

---

## When this pattern makes sense

Using Graftcode directly from edge clients works best when:
- interactions are stateless
- exposed methods are coarse-grained
- public interfaces are treated carefully
- security is explicitly configured

It is especially effective for:
- business APIs
- data access layers
- application backends
- internal tools and dashboards

---

## When to be cautious

This pattern should be used thoughtfully.

For edge clients:
- avoid exposing fine-grained internal methods
- avoid stateful object lifetimes
- avoid leaking internal abstractions

Public interfaces should be designed deliberately, just like public libraries.

---

## Why this works

This model works because:
- Graftcode operates at the runtime level
- interfaces are explicit and typed
- execution semantics are consistent
- security remains centralized

The edge client stops being a “special case” and becomes a normal consumer.

---

## In short

With Graftcode, edge clients can:
- consume backend logic directly
- avoid building traditional APIs
- benefit from strong typing and tooling
- detect errors early
- evolve safely over time

APIs become optional—not mandatory.

---

Next, we’ll look at **asynchronous and event-driven integration patterns**, and how Graftcode handles workflows that don’t fit request–response models.
