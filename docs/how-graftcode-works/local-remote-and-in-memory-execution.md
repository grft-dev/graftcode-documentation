---
title: "Local, remote, and in-memory execution"
description: "Compatibility route for the canonical execution-modes documentation."
keywords: "graftcode execution modes, in-memory execution, remote execution"
---

# Local, remote, and in-memory execution

This topic moved to [In-memory, same-machine, and remote execution](../core-concepts/execution-modes.md).

Use precise topology terms:

- `inmemory` selects in-memory connection data and requires the needed implementation module to be available locally;
- a Gateway on `localhost` is another process and still uses a network transport;
- a remote host adds availability, latency, authentication, routing, and partial-failure concerns.

Generated packages can expose configuration for different targets, but changing topology is not a guarantee of unchanged behavior. Verify package contents, supported host formats, error behavior, and both in-memory and remote calls for the runtime pair in use.

See [Configuration resolution](../core-concepts/configuration-resolution.md) for source precedence and initialization timing.
