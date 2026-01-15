---
title: "Security model overview"
description: "Understand the security model of Graftcode, how execution is isolated, what data is shared, and how trust boundaries are enforced without introducing a cloud proxy."
keywords: "graftcode security, security model, trust boundaries, runtime isolation, distributed systems security"
---

# Security model overview

Security concerns are one of the first questions teams ask when evaluating a new integration technology.

Graftcode is designed with a simple principle in mind:

> **Execution always happens inside your environment.  
> Graftcode never becomes part of your production data path.**

This section explains how security and trust boundaries are defined, enforced, and preserved.

---

## Graftcode is not a cloud proxy

The most important clarification is what Graftcode is *not*.

Graftcode:
- does not proxy production traffic
- does not process business data in the cloud
- does not participate in runtime execution
- does not observe payloads or method arguments

All execution happens:
- inside your processes
- inside your runtimes
- inside your network boundaries

The Graftcode cloud is used only for **interface metadata and tooling**, not execution.

---

## Clear trust boundaries

Graftcode defines clear and narrow trust boundaries.

### Trusted components (your environment)

- Application code
- Business logic
- Hypertube runtime
- Graftcode Gateway process
- Runtimes loaded by the Gateway
- Transport plugins and security plugins you choose

These components run under your control and follow your security policies.

---

### Untrusted / non-executing components

- Graftcode cloud services
- Registry and metadata services
- Tooling and dashboards

These components:
- never execute your code
- never see your runtime data
- never participate in method calls

They operate strictly at the metadata and orchestration level.

---

## What data is shared with Graftcode cloud

When a Graftcode Gateway starts, it may share **interface metadata**.

This includes:
- names of public classes
- method signatures
- type information
- version identifiers

It explicitly does **not** include:
- method implementations
- runtime values
- business data
- credentials or secrets

The shared data is comparable to a public header or interface definition.

---

## Execution isolation and safety

Execution isolation is provided by:
- runtime boundaries
- process boundaries
- network boundaries

Hypertube executes code:
- inside the native runtime
- using native execution rules
- without injecting or modifying logic

There is no interpreted execution layer and no sandbox escaping risk introduced by Graftcode itself.

---

## Authentication and authorization are explicit

Graftcode does not implement a built-in authentication system.

Instead:
- authentication is handled through plugins
- authorization is enforced explicitly
- identity flows are transparent

This ensures:
- no hidden credentials
- no implicit trust
- no security logic embedded in transport

Security decisions remain visible and auditable.

---

## Network security is unchanged

From a network perspective, Graftcode introduces no exotic requirements.

Communication uses:
- TCP/IP
- or WebSocket

This allows teams to:
- apply existing firewall rules
- use standard TLS / WSS
- rely on existing network monitoring and inspection

Graftcode fits into existing network security models.

---

## Observability without data leakage

Observability data:
- traces
- spans
- logs
- metrics

remains under your control.

Graftcode:
- propagates context
- does not centralize logs
- does not collect payloads

Teams can integrate with their existing observability stack without exposing sensitive data.

---

## Source availability and auditability

Graftcode components that run in customer environments are designed to be auditable.

Where applicable:
- components may be source-available
- behavior can be inspected
- security reviews and penetration testing are possible

This supports enterprise security review processes.

---

## Failure modes and blast radius

Because execution does not leave your environment:
- failures remain local
- blast radius is limited
- outages in Graftcode cloud do not affect production execution

At worst:
- new Grafts cannot be generated temporarily
- existing deployments continue to function normally

This is a deliberate design choice.

---

## Trust through minimalism

The security model of Graftcode is intentionally minimal.

It avoids:
- deep cloud involvement
- opaque runtime behavior
- implicit trust relationships

Instead, it relies on:
- explicit boundaries
- standard protocols
- native runtime execution

This keeps the security surface area small and understandable.

---

## Closing perspective

Graftcode does not ask you to trust a new execution platform.

It asks you to trust:
- your own runtimes
- your own network
- your own security practices

Graftcode stays out of the way—and makes those boundaries clearer, not blurrier.
