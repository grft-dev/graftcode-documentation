---
title: "Network boundaries and isolation"
description: "Shared-responsibility guidance for Gateway network placement and isolation."
keywords: "network boundaries, isolation, graftcode security, gateway"
---

# Network boundaries and isolation

Gateway placement is a deployment choice, not an automatic isolation guarantee.

Create a topology for each environment that identifies:

- every Gateway listener and exposed port;
- consumers allowed to connect;
- outbound metadata, package, logging, and telemetry destinations;
- TLS termination and authentication controls;
- provider runtime and process boundaries;
- secrets, filesystem, and host permissions;
- failure dependencies and resource limits.

A service may have its own Gateway or share a host according to the deployed architecture. Neither arrangement proves that failures cannot cascade or that identity is validated per call.

Apply least-privilege network policy, process/container isolation, resource limits, and explicit authentication. Validate the resulting boundary with connection and failure tests.

See [Security model overview](security-model-overview.md), [Graftcode Gateway](../core-concepts/graftcode-gateway.md), and [Execution modes](../core-concepts/execution-modes.md).
