---
title: "Scaling Gateway providers"
description: "Scale stateless calls horizontally and preserve affinity for stateful calls."
---

# Scaling Gateway providers

## Stateless providers

Static, stateless methods are the safest scaling unit. Run identical Gateway/provider instances
behind infrastructure that supports the selected transport. Route each independent call to any ready
instance.

Keep module, Gateway, generated-package, and configuration versions aligned across the pool. Remove an
instance from readiness before stopping it.

## Stateful providers

Instance methods and complex remote objects can retain identity on one receiver. Keep the connection
and session on the same Gateway instance with WebSocket-aware affinity. Scale-in or restart can
invalidate that identity; callers must recreate state or fail clearly.

## Capacity

Measure provider duration, concurrent connections, CPU, memory, dependency limits, and error rates.
Scale on observed saturation rather than assuming one call maps to one lightweight request.

## Publication identity

Use one reviewed project identity strategy. A project key gives stable project-backed registry
addressing, but it does not replace load balancing or runtime-call authorization.

**Gap:** no verified universal autoscaling formula, connection-drain API, distributed object-state
store, or transparent state migration is documented. Infrastructure compatibility must be tested for
WebSocket, optional TCP, or optional HTTP/2 traffic.

## Next steps

- [Networking and ports](networking-ports.md)
- [Health checks](health-checks.md)
- [Version compatibility and upgrades](version-compatibility-upgrades.md)

## Source anchors

- `HYPERTUBE/` stateful/static invocation and connection implementations
- `graftcode-gateway/README.md`, listener options
- [Static and instance context](../core-concepts/static-and-instance-context.md)
- [Known limitations](../reference/known-limitations.md)
