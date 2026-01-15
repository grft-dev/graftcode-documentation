---
title: "Where does Graftcode fit?"
description: "Graftcode fits between business logic and infrastructure, removing the need for explicit integration layers while working with existing architectures, tools, and platforms."
keywords: "graftcode architecture, software integration layer, microservices communication, runtime integration, backend architecture"
---


Graftcode does not ask you to redesign your system.  
It fits into architectures you already have.

To understand where it belongs, it helps to look at how modern systems are usually structured—and where most integration complexity quietly accumulates.

---

## A familiar architectural stack

Most applications, regardless of language or scale, tend to follow a similar layered shape:

- **Business logic** – the code that implements real behavior
- **Communication layer** – APIs, RPC endpoints, clients, contracts
- **Infrastructure** – runtimes, networks, load balancers, cloud services

Over time, the communication layer grows into a distinct concern. It has its own abstractions, tooling, and lifecycle, often evolving independently of the business logic it represents.

Graftcode changes the role of that middle layer.

---

## Between business logic and infrastructure

Graftcode sits **between business logic and infrastructure**, removing the need to explicitly design and maintain how services talk to each other.

Instead of expressing communication as endpoints and protocols, you express it as **public programming interfaces**. Graftcode then takes responsibility for making those interfaces callable across boundaries.

From the application’s point of view:
- business logic remains business logic
- infrastructure remains infrastructure
- communication becomes a runtime concern, not an architectural one

---

## Not a replacement for your stack

A common concern when introducing a new platform is whether it replaces existing tools. Graftcode is intentionally narrow in scope.

Graftcode does **not** replace:
- load balancers or reverse proxies
- API gateways
- cloud platforms
- logging, metrics, or tracing systems
- security infrastructure

It works with standard transports such as TCP/IP and WebSocket, which means it scales through the same mechanisms your system already uses.

If your infrastructure can route and scale network traffic, it can route and scale Graftcode.

---

## Where Graftcode adds value

Graftcode is most valuable in places where communication becomes repetitive, fragile, or tightly coupled to architecture choices.

Typical examples include:
- backend-to-backend communication between services
- exposing business capabilities to edge clients (Web Apps, Mobile Apps)
- internal APIs shared across teams
- modular systems that evolve over time

In these scenarios, Graftcode replaces the need to design, version, and distribute explicit communication layers.

---

## Coexisting with existing approaches

Adopting Graftcode does not require an all-or-nothing decision.

It can coexist with:
- REST APIs
- gRPC services
- message-based integrations

Teams often start by introducing Graftcode for a single service or internal interface. Over time, as the benefits become clear, usage expands naturally.

The goal is not to eliminate existing solutions overnight, but to reduce the amount of integration work needed going forward.

---

## Architectural flexibility over time

Because Graftcode decouples code from communication details, architectural decisions become easier to change.

A module can:
- start as an in-process component
- later move to a separate service
- change its transport or hosting model

All without changing how it is called from application code.

This flexibility is especially useful in systems that evolve gradually—where today’s design constraints are rarely tomorrow’s.

---

## A shift in responsibility

Traditionally, communication logic lives in application code. With Graftcode, that responsibility shifts to the runtime.

Developers focus on:
- defining clear public interfaces
- writing business logic
- evolving interfaces carefully over time

The runtime handles:
- client generation
- transport
- execution
- compatibility

This separation allows teams to think about architecture at the right level of abstraction.

---

## In short

Graftcode fits **where communication usually becomes a burden**, without asking you to replace the rest of your stack.

It narrows the gap between local and remote code, allowing distributed systems to be built—and evolved—using the same mental model developers already trust.

---

Next, we’ll look at **when Graftcode is the right choice**, and when other approaches may still make sense.
