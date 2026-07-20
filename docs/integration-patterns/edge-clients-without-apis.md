---
title: "Edge clients without APIs"
description: "Compatibility guidance for evaluating browser and other edge consumers."
keywords: "edge clients, frontend integration, browser, graftcode"
---

# Edge clients without APIs

Browser, mobile, and desktop clients are different deployment and threat models. Do not treat them as interchangeable Graft consumers.

Before exposing a backend directly to an edge client, verify a release-qualified sample for that client and document:

- generated-package support and configuration API;
- Gateway origin, port, path, and CORS behavior;
- `wss://` termination and certificate ownership;
- credential storage and token exposure;
- authentication and authorization on every callable method;
- public-surface minimization, rate limits, and abuse controls;
- reconnect, timeout, and user-visible failure behavior.

Graftcode does not make authentication automatic. A callable backend without an explicitly configured and tested control remains callable at its reachable network boundary.

Use [Callable surface](../core-concepts/callable-surface.md), [Graftcode Gateway](../core-concepts/graftcode-gateway.md), and the relevant [language guide](../language-guides/index.md) as the current canonical references.
