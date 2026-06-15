---
title: "MCP server without MCP boilerplate"
description: "Expose backend capabilities as MCP tools using Graftcode Gateway with zero MCP server code, no manual tool definitions, and one cross-technology model across .NET, Java, JavaScript, and Python."
keywords: "graftcode mcp, mcp server, model context protocol, ai tools integration, zero boilerplate, cross technology backend"
---

# MCP server without MCP boilerplate

You do not need to write a custom MCP server to expose backend capabilities to AI agents.

With Graftcode, you write normal backend code, run it through Graftcode Gateway, and your public methods become MCP tools automatically.

This gives engineering teams one unified approach for both:

- service-to-service integration
- AI-to-service integration (MCP)

---

## The problem most teams face with MCP

When teams adopt MCP directly, they often build and maintain:

- a separate MCP server runtime
- manual tool definitions and schemas
- adapter code between tools and business services
- duplicated auth, logging, and deployment pipelines

This creates a second integration stack next to existing microservices.

---

## What changes with Graftcode

In Graftcode MCP mode, you keep your backend model code-first:

1. Implement business capabilities as public methods/classes.
2. Run the module in Graftcode Gateway.
3. Gateway auto-discovers the public surface.
4. Gateway exposes MCP endpoint and tools automatically.

No MCP-specific annotations.  
No hand-written tool manifest.  
No OpenAPI/proto contracts for agent calls.

---

## Why this matters to programmers

- **No wrapper tax**: avoid writing and maintaining separate MCP adapters.
- **One contract model**: public method signatures stay your source of truth.
- **Strong typing path**: the same surface can be consumed as strongly typed Grafts by apps and as tools by AI clients.
- **Lower change friction**: you evolve code in one place and ship through one pipeline.
- **Faster debugging**: one runtime surface means fewer moving parts between business code and agent call.

---

## Why this matters to CTOs and platform owners

- **Faster AI adoption**: existing modules can be exposed to AI in hours, not quarters.
- **Lower total cost**: one platform pattern instead of separate API + MCP server programs.
- **Cross-team standardization**: teams expose capabilities the same way across stacks.
- **Governance by design**: only intentional public methods are exposed; internal code stays internal.
- **Vendor flexibility**: MCP-compatible tools can be swapped without rewriting backend services.

---

## Cross-technology, same operating model

The delivery model stays the same in every language:

- write a plain module/class with public methods
- package and run with Docker
- start with `gg`
- connect an AI client to `http://host:81/mcp`

Whether the module is in .NET, Java, JavaScript, or Python, teams follow the same lifecycle and platform controls.

---

## Quick architecture flow

1. **Module authoring**: developer writes business logic as public methods.
2. **Gateway hosting**: `gg` loads module and exposes runtime surface.
3. **MCP exposure**: Gateway publishes MCP tools from that public surface.
4. **AI consumption**: Cursor / Claude Desktop discovers and calls tools.
5. **Platform governance**: teams apply auth, access control, and visibility through the same gateway/portal model.

---

## Practical benefits in production

- **Consistent onboarding**: new team members learn one way to expose both API-like and AI tool capabilities.
- **Unified operations**: one deployment story, one observability posture, one access model.
- **Progressive modernization**: existing modular monoliths can expose MCP first, then split services later if needed.

---

## Balanced view: where to be careful

MCP mode is powerful, but production usage should still follow engineering discipline:

- expose only domain-safe public operations (avoid accidental overexposure)
- apply explicit authorization for high-impact actions
- keep auditability of tool calls as production-grade events
- treat AI-facing interfaces as product contracts, with versioning and compatibility checks

Graftcode reduces integration complexity, but governance and domain ownership remain your responsibility.

---

## Language quick starts on Academy

Expose MCP quick-starts currently available:

- [.NET](https://academy.graftcode.com/quick-start/expose-mcp/dotnet)
- [Java](https://academy.graftcode.com/quick-start/expose-mcp/java)
- [JavaScript](https://academy.graftcode.com/quick-start/expose-mcp/javascript)
- [Python](https://academy.graftcode.com/quick-start/expose-mcp/python)

As Academy expands to additional stacks, this use case remains the same: one public-code model, one gateway runtime, one MCP exposure path.
