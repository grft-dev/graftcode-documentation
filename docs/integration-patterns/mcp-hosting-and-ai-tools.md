---
title: "MCP hosting and AI tools"
description: "Learn how services hosted on Graftcode Gateway can be exposed as MCP tools for AI systems, without rewriting APIs or changing business logic."
keywords: "mcp hosting, ai tools, llm integration, model context protocol, graftcode ai integration"
---

# MCP hosting and AI tools

As AI systems become part of everyday software, a new question appears:

> How can AI safely call real business logic?

The Model Context Protocol (MCP) defines a way for AI systems to invoke tools through a JSON-RPC interface.  
However, MCP operates at a **much lower abstraction level** than normal application code.

Graftcode bridges this gap by allowing **existing business logic** to be exposed as MCP tools—without rewriting APIs or restructuring services.

---

## MCP is not a programming model

MCP is a protocol.

It supports:
- stateless method calls
- JSON-RPC invocation
- simple input and output structures

It does **not** support:
- object lifetimes
- stateful sessions
- events or callbacks
- rich execution semantics

Because of this, MCP is not suitable as a primary integration model for applications.

It is, however, a useful *projection* of existing logic for AI consumption.

---

## Exposing business logic through MCP

Graftcode allows selected public classes to be exposed as MCP tools by configuration.

When a class is marked as an MCP base class:
- the class becomes a tool
- each public static method becomes an operation
- method signatures are translated into MCP-compatible schemas

No changes to business logic are required.

The same code can be:
- consumed by other services through Grafts
- consumed by edge clients
- consumed by AI systems through MCP

---

## Why static, stateless methods matter

MCP operates in a stateless, request–response model.

For this reason:
- only static methods are exposed
- each call is independent
- no server-side object state is retained

This aligns naturally with:
- business queries
- command-style operations
- AI-driven automation tasks

Stateful workflows remain available through Graftcode—but are not projected into MCP.

---

## Method comments become MCP tool definitions

When business logic is exposed as MCP tools, **method-level comments are not ignored**.

Graftcode uses comments and documentation attached to public methods as the **source of tool descriptions** for MCP.

This means that:
- method comments become tool descriptions
- parameter comments become input descriptions
- return value comments describe the output

In practice, the same documentation developers already write for humans becomes documentation for AI systems.

---

## Documentation as part of the contract

Because MCP tools are consumed by language models, clarity matters.

Well-written method comments:
- explain intent, not just mechanics
- describe expected behavior
- clarify edge cases and assumptions

By placing this documentation directly on methods, teams ensure that:
- humans see it in the IDE
- AI systems receive it through MCP
- documentation stays close to the code it describes

There is no separate documentation format to maintain.

---

## One source of truth

This approach reinforces a single-source-of-truth model:

- code defines behavior
- public interfaces define contracts
- comments define meaning

The same interface:
- is consumed by services through Grafts
- by edge clients through typed dependencies
- and by AI systems through MCP

All of them rely on the same definitions.

---

## Why this matters for AI tools

AI systems are only as useful as the tools they can understand.

By exposing:
- strongly typed method signatures
- precise input and output shapes
- and meaningful documentation

Graftcode allows AI tools to:
- call real business logic safely
- understand what each operation does
- reduce ambiguous or incorrect tool usage

This improves reliability without introducing AI-specific abstractions.

---

## One flag, no rewrite

Exposing MCP tools does not require:
- new controllers
- new endpoints
- duplicated logic
- special DTOs

A single Gateway configuration flag defines:
- which class is exposed
- how it appears as an MCP tool

Everything else remains unchanged.

This avoids the common anti-pattern of building “AI-only APIs”.

---

## Execution still happens through Hypertube

Although MCP uses JSON-RPC externally, execution inside the system does not.

When an MCP request arrives:
- it is received by the Gateway
- translated into invocation intent
- executed through Hypertube
- results are returned to the MCP caller

The AI system never executes business logic directly.  
It only triggers normal runtime execution.

---

## Security and control remain intact

Exposing logic through MCP does not bypass security.

Authentication and authorization:
- are enforced at the Gateway
- use the same plugin system
- apply equally to MCP and non-MCP calls

Only explicitly exposed classes are reachable.  
Everything else remains private.

---

## No MCP lock-in

MCP is treated as **one of many possible projections**.

If MCP evolves—or is replaced—the core system remains unchanged.

Business logic:
- stays strongly typed
- remains accessible through Grafts
- does not depend on MCP semantics

AI integration becomes an adapter, not a dependency.

---

## Why this matters

Many teams are currently rewriting APIs just to make them “AI-accessible”.

Graftcode avoids this entirely.

AI systems:
- consume existing logic
- through a constrained, explicit interface
- without affecting the rest of the system

This keeps architecture stable while enabling experimentation.

---

## In short

With Graftcode:
- business logic remains the source of truth
- MCP is an optional exposure layer
- no APIs need to be rewritten
- AI tools call real code, not mock endpoints

AI integration becomes additive—not disruptive.
