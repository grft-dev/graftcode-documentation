---
title: "MCP hosting and AI tools"
description: "Current evidence boundaries for exposing Gateway-hosted methods through MCP."
keywords: "mcp hosting, ai tools, model context protocol, graftcode gateway"
---

# MCP hosting and AI tools

The current Gateway documents MCP-related options, including selection by `--mcpBaseClass`. That establishes a configuration surface, not a complete interoperability or security guarantee.

Do not expose production tools until an end-to-end test for the exact Gateway release confirms:

- the MCP endpoint and transport;
- tool names, descriptions, and input/output schema mapping;
- supported method and type shapes;
- client initialization and session behavior;
- CORS where a browser client is involved;
- authentication, authorization, and error responses;
- cancellation, timeout, and concurrent-call behavior.

MCP exposure does not automatically provide authentication, observability, or safe tool semantics. Keep callable methods narrow, validate arguments in business logic, and apply least privilege.

See [Graftcode Gateway](../core-concepts/graftcode-gateway.md), [Callable surface](../core-concepts/callable-surface.md), and [Type mapping](../core-concepts/type-mapping.md). Copy runtime commands from current Gateway output rather than from this compatibility route.
