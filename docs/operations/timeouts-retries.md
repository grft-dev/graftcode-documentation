---
title: "Timeouts and retries"
description: "Set resilience policy at explicit boundaries and avoid unsafe duplicate invocation."
---

# Timeouts and retries

Treat timeout and retry policy as an application/deployment decision, not a property guaranteed by a
Graft contract.

## Policy

1. Set finite timeouts for third-party calls inside providers.
2. Set caller deadlines appropriate to the selected generated package and transport.
3. Retry only transient transport failures, timeouts, and explicitly classified upstream failures.
4. Use a small attempt limit with backoff and jitter.
5. Never retry validation, authentication, authorization, or package-generation `422` failures.
6. Retry mutating calls only with tested idempotency.

A caller timeout does not prove the provider stopped executing. Design side effects so a repeated
request is safe, or pass a primitive idempotency key and persist its result.

Stateful calls are especially sensitive: reconnecting to another instance cannot restore remote
object identity. Prefer static stateless operations for retryable workflows.

Coordinate proxy idle timeout, transport timeout, application deadline, and provider dependency
timeout so the outer layer does not expire first without useful diagnostics.

**Gap:** timeout, keep-alive, reconnect, and retry behavior differs across current Hypertube runtime
clients and is not documented as one stable cross-runtime configuration surface. Inspect and test the
generated runtime dependency before setting production policy.

## Next steps

- [Errors and status reference](../reference/errors-status.md)
- [Scaling](scaling.md)
- [Handle provider errors](../how-to-guides/handle-provider-errors)

## Source anchors

- `HYPERTUBE/src/*/` WebSocket and HTTP/2 client implementations and tests
- `graftcode-gateway/README.md`, plugin `rpcTimeoutMs` example (plugin-specific, not a global call timeout)
