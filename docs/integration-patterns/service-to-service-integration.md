---
title: "Service-to-service integration"
description: "Learn how to integrate services using Graftcode in a strongly typed, runtime-level way that replaces traditional REST and gRPC communication."
keywords: "service to service integration, microservices communication, graftcode integration patterns, strongly typed services"
---

# Service-to-service integration

Service-to-service communication is one of the most common—and most complex—parts of modern systems.

Traditionally, this communication is implemented using:
- REST APIs
- gRPC services
- message-based RPC layers

Graftcode approaches this problem from a different angle.

Instead of designing *endpoints*, *routes*, or *schemas*, services expose **public code**, and other services consume it as a **typed dependency**.

---

## Services as modules, not endpoints

In Graftcode, a service is treated like a module with a public interface.

What a service exposes is:
- a set of public classes
- with public methods
- defined using normal programming language constructs

What it does *not* expose:
- URLs
- HTTP verbs
- transport-specific payloads
- serialization concerns

From the consumer’s perspective, calling another service looks like calling a method on a local dependency.

---

## Stateless service-to-service calls

The simplest pattern is **stateless integration**.

In this model:
- services expose static methods
- each call is independent
- no execution context is retained between calls

This closely matches how REST-style APIs are typically used, but without requiring:
- controllers
- DTO mapping layers
- HTTP semantics

Stateless calls are well suited for:
- business APIs
- query-style operations
- request–response workflows

They scale easily and work naturally behind load balancers.

---

## Stateful service-to-service interactions

Some integrations require state.

Examples include:
- long-running workflows
- conversational processes
- subscriptions and event streams
- coordinated operations across multiple calls

Graftcode supports **stateful service-to-service integration** by allowing:
- object instances to live across calls
- callbacks and events
- duplex communication

Once a stateful interaction is established:
- execution context is preserved
- subsequent calls are routed consistently
- events can flow back to the caller

This replaces patterns that traditionally require WebSockets, SignalR, or custom session management.

---

## Strong typing across service boundaries

All service-to-service calls are:
- strongly typed
- validated at compile time
- discoverable through IDE tooling

This eliminates a large class of integration errors:
- mismatched payloads
- missing fields
- undocumented behavior changes

If a service interface changes incompatibly, consumers find out immediately—before deployment.

---

## Error handling between services

Errors are propagated using **exceptions**, not status codes.

If a service throws:
- a system exception
- or a custom business exception

the caller receives:
- a corresponding native exception
- with preserved error information
- and a connected trace context

Service-to-service error handling uses the same `try/catch` patterns as local code.

---

## Evolving service contracts safely

Because service interfaces are versioned and consumed as dependencies:
- older and newer consumers can coexist
- upgrades are explicit
- compatibility is validated through builds and tests

This enables gradual evolution without synchronized deployments.

---

## Configuration-driven architecture

Where a service runs is not a programming concern.

A service can:
- start as an in-memory module
- move to another runtime
- be deployed as a remote service
- be scaled independently

The integration code remains unchanged.

Routing decisions are handled through configuration, not application logic.

---

## Why this pattern works

This pattern works because it:
- aligns with how developers already think about code
- removes transport concerns from business logic
- makes contracts explicit and enforceable
- improves tooling and developer feedback

Service-to-service communication becomes a matter of **code reuse**, not protocol negotiation.

---

## In short

With Graftcode, service-to-service integration:
- uses normal programming interfaces
- is strongly typed and discoverable
- supports stateless and stateful workflows
- propagates errors and context naturally
- evolves safely over time

Services stop talking in protocols—and start talking in code.

---

Next, we’ll look at **edge and client integrations**, and how the same model applies when services are consumed from browsers, mobile apps, and other edge clients.
