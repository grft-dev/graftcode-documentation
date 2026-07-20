---
title: "Scaling, load balancers, and proxies"
description: "Compatibility guidance for validating Graftcode network deployments."
keywords: "graftcode scaling, load balancers, reverse proxies, websocket"
---

# Scaling, load balancers, and proxies

A current Gateway exposes transport-specific listeners and ports; that alone does not prove compatibility with an arbitrary load balancer, ingress, API gateway, or service mesh.

Before documenting or operating a scaled deployment, test:

- the exact Gateway release, server mode, port, and path;
- connection upgrade and idle-timeout behavior for WebSocket;
- health and readiness checks supported by the deployment;
- TLS termination and certificate ownership;
- connection draining, reconnect, and failover behavior;
- whether calls are stateless or require connection/session affinity;
- retry safety and idempotency at the business-method level.

Do not assume infrastructure retries, circuit breakers, sticky sessions, or transport plugins preserve invocation semantics. Use [Graftcode Gateway](../core-concepts/graftcode-gateway.md) for current process options, [Execution modes](../core-concepts/execution-modes.md) for topology terminology, [Networking and ports](../operations/networking-ports.md), and [Health checks](../operations/health-checks.md) for operational guidance.
