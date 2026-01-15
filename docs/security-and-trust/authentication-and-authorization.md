---
title: "Authentication and authorization"
description: "Understand how authentication and authorization are applied in Graftcode through pluggable runtime hooks that operate around invocation intent without affecting business logic."
keywords: "graftcode authentication, authorization plugins, identity propagation, runtime security, distributed systems"
---

# Authentication and authorization

Authentication and authorization in Graftcode are intentionally designed to sit **outside of business logic**, while still being deeply integrated with runtime execution.

The goal is not to invent a new security model, but to make security:
- explicit
- composable
- and orthogonal to execution

This section explains how identity is attached to execution intent, how authorization decisions are made, and why Graftcode remains transparent rather than prescriptive.

---

## Authentication happens around invocation intent

At runtime, every call in Graftcode is expressed as an **invocation intent** represented using the Intention Invocation Protocol (IIP).

Authentication plugins operate **before and after this intent crosses runtime boundaries**.

On the caller side, before Hypertube sends an IIP message, an authentication plugin can intercept the invocation intent and enrich it with identity information. This may include attaching a JWT token, API key, credentials, or any other form of proof that the receiving side expects.

At this stage, the plugin has full visibility into:
- what method is about to be invoked
- which arguments are being passed
- and what contextual information is available

The invocation intent itself is not modified semantically. It is simply wrapped or annotated with identity context.

---

## Validation before execution, not during execution

On the receiving side, before the invocation intent is translated into an actual method call, the corresponding authentication plugin is invoked again.

Here, the plugin:
- inspects the incoming IIP message
- extracts identity information
- validates credentials or tokens
- reconstructs identity claims and context

Crucially, this happens **before any user code is executed**.

If validation fails and the plugin throws an authorization or authentication exception, execution stops immediately. No business logic runs, no side effects occur, and control returns to the caller with a native exception.

If validation succeeds, execution continues as if the call were local.

---

## Authorization is an explicit decision in user code

Once identity has been established, authorization decisions are made explicitly by user-defined logic.

Because the authentication plugin has access to:
- the target operation
- method metadata
- identity claims

it can delegate authorization to:
- attribute-based rules on methods or classes
- a centralized authorization component
- custom policy logic

This logic can live:
- alongside business code
- in a dedicated authorization module
- or in a shared security layer

If authorization logic throws an exception, the invocation is rejected.  
If it does nothing, execution proceeds.

There is no hidden allow/deny behavior.

---

## Graftcode stays below the security layer

An important property of this design is that **Graftcode itself remains below the security layer**.

It does not:
- interpret identity
- apply authorization rules
- assume trust relationships

It simply provides the hooks where identity can be injected and validated.

This means authentication and authorization can be:
- added later
- replaced
- or extended

without changing business code or interfaces.

---

## Side-car authentication during architectural evolution

This model enables a powerful pattern when evolving architectures.

A system can start as a monolith with:
- no authentication between modules
- purely in-memory execution

As modules are extracted into separate services, authentication plugins can be introduced through configuration alone.

By adding:
- a plugin that injects identity on the caller side
- and a plugin that validates identity on the receiver side

the system gains authentication and authorization **without rewriting integration code**.

This effectively acts as a side-car security layer that grows with the architecture.

---

## Identity propagation as part of execution context

Once identity is validated, it becomes part of the execution context.

This context propagates:
- across runtime boundaries
- through nested calls
- into callbacks and events

As a result:
- authorization decisions remain consistent
- logging can include identity information
- traces can be correlated with users or services

Identity behaves like any other execution context—not like an external header or protocol artifact.

---

## No implicit trust, no hidden credentials

Because identity is always explicit:
- credentials must be provided intentionally
- validation must succeed explicitly
- authorization must allow the operation

There is no implicit trust between services, even if they are hosted in the same Gateway.

If a plugin is not configured, no authentication happens.  
If a plugin is configured, it is fully responsible for enforcement.

---

## Transparent failure behavior

When authentication or authorization fails:
- an exception is thrown
- execution stops
- the caller receives a native exception

There are no partial executions, fallback behavior, or silent failures.

From the caller’s perspective, this behaves exactly like a local authorization failure.

---

## Closing perspective

Authentication and authorization in Graftcode are not features layered on top of execution.

They are **hooks around execution intent**, allowing teams to apply security policies exactly where they belong—at runtime boundaries—without entangling them with business logic.

This keeps security:
- visible
- auditable
- and adaptable

while preserving the simplicity of the programming model.
