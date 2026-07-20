---
title: "MCP server without MCP boilerplate"
description: "Compatibility route for current MCP evidence and Gateway configuration."
keywords: "graftcode mcp, model context protocol, ai tools"
---

# MCP server without MCP boilerplate

This scenario does not yet have a verified cross-runtime workflow in this documentation.

Gateway exposes MCP-related configuration, but the audit did not establish an end-to-end matrix for endpoint and transport behavior, tool schema generation, sessions, CORS, authentication, errors, or supported provider runtimes. The previous hardcoded endpoint and automatic-security claims have been removed.

Use [MCP hosting and AI tools](../integration-patterns/mcp-hosting-and-ai-tools.md) for the release-validation checklist, then confirm options in [Graftcode Gateway](../core-concepts/graftcode-gateway.md).

Do not expose business methods to an AI client until the exact Gateway release has been tested with the intended MCP client and explicit authentication, authorization, input validation, least privilege, timeout, and audit controls.
