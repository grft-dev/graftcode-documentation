---
title: "Stateless vs stateful Graft calls"
description: "Choose static stateless calls or instance-bound remote objects and configure GraftConfig.stateless."
articleTitle: "Stateless vs stateful Graft calls"
---

## Concepts

| Mode | Meaning |
| --- | --- |
| **Static method** | Type-level call; no remote object handle |
| **Instance method** | Bound to remote object identity across calls |
| **`stateless = true`** | Generated/runtime hint for independently routable operations |
| **`stateless = false`** | Allows stateful remote object semantics |

`stateless` does not remove serialization or network failure modes for remote calls.

## Examples

```typescript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
const total = await PriceService.calculate(10, 5);

// Instance methods create remote object identity; prefer static when possible
const svc = new PriceService();
const value = await svc.calculate(10, 5);
```

## When to use which

- Prefer **static + stateless** for idempotent reads and independent operations behind load balancers.
- Use **instances** when the domain model requires constructor inputs and follow-up calls on the same
  object—and accept affinity requirements.

See [Static and instance context](../../core-concepts/static-and-instance-context.md).

## Next steps

- [Configure invocation](../configure-invocation)
- [Scaling](../../operations/scaling.md)

## Source anchors

- `core-concepts/static-and-instance-context.md`
- generated `GraftConfig` templates
