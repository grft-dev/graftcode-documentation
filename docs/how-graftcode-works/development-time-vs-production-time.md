---
title: "Development-time vs production-time behavior"
description: "Understand how Graftcode behaves differently during development and production, what happens at each stage, and why the cloud is involved only when it adds value."
keywords: "graftcode development time, production time behavior, runtime execution, interface discovery, distributed systems lifecycle"
---

# Development-time vs production-time behavior

One of the most common sources of confusion in distributed systems is **when** certain things happen.

Client generation, interface discovery, routing, execution, monitoring—these concerns often blend together, making it unclear which parts are design-time, build-time, or runtime responsibilities.

Graftcode makes a clear distinction between **development time** and **production time**, and each phase has a very different role.

Understanding this separation is key to understanding both the architecture and the security model.

---

## Development time: discovering and consuming interfaces

Development time is when developers:
- write code
- explore services
- add dependencies
- evolve interfaces

In Graftcode, this phase is centered around **interfaces**, not traffic.

---

### Exposing interfaces during development

During development, a service is started together with a **Graftcode Gateway**.

When the Gateway starts, it:
- loads the configured runtimes
- loads the specified modules
- analyzes public interfaces
- builds a Unified Graft Model (UGM)

At this stage:
- no production traffic exists
- no business logic is executed on behalf of consumers
- only interface metadata is made available

This metadata is what enables everything that follows.

---

### Discovering services with Graftcode Vision

Developers typically use **Graftcode Vision** at development time to:
- see what a service exposes
- understand available methods
- copy package manager commands
- obtain configuration examples

Vision operates directly against the running Gateway, which means it always reflects the current state of the code.

There is no separate documentation lifecycle.

---

### Adding remote services as dependencies

When a developer decides to use a remote service, they do not generate a client manually.

Instead, they:
- copy a package manager command
- install the dependency
- import the generated client

At that moment, the Graftcode engine:
- generates a strongly typed client **on demand**
- tailored to the requested technology
- based on the current Unified Graft Model

The result behaves like any other dependency in the project.

---

### Immediate feedback through tooling

Because Grafts are normal dependencies:
- IDEs provide autocomplete
- type errors appear immediately
- signature changes are visible without running code

If an interface evolves:
- new methods appear after dependency update
- removed members cause compile-time errors
- mandatory changes are detected early

This tight feedback loop is one of the main benefits of the development-time model.

---

## Production time: executing calls

Production time begins once services are deployed and real calls start flowing.

In this phase, the focus shifts from discovery to **execution**.

---

### No cloud in the execution path

A critical distinction in Graftcode is that **the cloud is not part of production execution**.

Once a Graft has been generated:
- calls go directly from caller to receiver
- execution happens through Hypertube
- communication uses TCP/IP or WebSocket

The Graftcode cloud:
- does not forward calls
- does not process payloads
- does not see runtime data

Execution is fully under your control.

---

### Runtime execution through Hypertube

At production time, execution happens through **Hypertube™**, but it is important to understand what this actually means.

Hypertube is not an external service and not a remote system operated by Graftcode.

It is a **runtime connection engine** that runs entirely within the customer’s environment:
- partially inside the generated Graft (on the caller side)
- partially inside the Graftcode Gateway (on the receiver side)

Both sides are deployed and controlled by the user.

There is no traffic routed outside the customer’s network and no execution leaving their infrastructure.

---

### Direct, internal communication

When a caller invokes a method on a Graft:
- the Graft uses its embedded Hypertube component
- the call is translated into a binary runtime-level message
- the message is sent directly to a Graftcode Gateway
- execution happens inside the target runtime hosted by that Gateway

This communication is:
- direct
- point-to-point
- over standard TCP/IP or WebSocket
- entirely within the customer’s network

There is no intermediary, proxy, or cloud service involved in call execution.

---

### Hypertube is part of your runtime, not ours

Hypertube does not operate as a shared platform component.

It:
- does not aggregate traffic
- does not inspect payloads centrally
- does not relay calls through third-party infrastructure

From a deployment and security perspective, Hypertube behaves like a **runtime library**, not like a service.

If your systems can communicate directly today, they can communicate through Hypertube in exactly the same way—just with a different execution model.

---

### Why this matters

This design ensures that:
- all production execution stays within your network boundary
- existing network controls, firewalls, and load balancers apply unchanged
- Graftcode does not become a runtime dependency for production traffic

The Graftcode cloud is involved only in **development-time interface discovery and client generation**.

At production time, Graftcode does not sit in the execution path.

---

### Configuration replaces code changes

At production time, architectural decisions are expressed through configuration.

For example:
- which Gateway instance to call
- which transport channel to use
- whether calls are local or remote
- which plugins are enabled

These decisions do not require changes to application code.

This allows:
- DevOps to control deployment behavior
- developers to focus on business logic
- architecture to evolve independently

---

## Versioning and evolution across phases

The separation between development time and production time also clarifies how interfaces evolve.

During development:
- interfaces are explored
- changes are discovered through tooling
- compatibility is enforced by the type system

During production:
- older Grafts continue to work
- newer Grafts unlock additional capabilities
- deprecation can be managed safely

There is no forced synchronization between producers and consumers.

---

## Why this separation matters

Many systems mix concerns:
- runtime behavior depends on design-time artifacts
- documentation lags behind implementation
- execution paths depend on build-time choices

Graftcode avoids this by clearly separating responsibilities:
- **development time** is about understanding and consuming interfaces
- **production time** is about executing calls efficiently and safely

Each phase uses the cloud only where it provides value.

---

## In short

In Graftcode:
- development time focuses on discovery, typing, and feedback
- production time focuses on execution and performance
- the cloud enables interface discovery, not call execution
- runtime behavior remains local and controllable

This separation makes distributed systems easier to reason about, easier to secure, and easier to evolve.

---

Next, we’ll take a closer look at **what information is sent to the Graftcode cloud—and what never leaves your environment**.
