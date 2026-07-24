---
title: "Timeouts and retries"
description: "Set resilience policy at explicit boundaries and avoid unsafe duplicate invocation."
---

# Timeouts and retries

Treat timeout and retry policy as an application/deployment decision, not a property guaranteed by a
Graft contract.

## Policy

1. Set finite timeouts for third-party calls inside Receivers.
2. Set caller deadlines appropriate to the selected generated package and transport.
3. Retry only transient transport failures, timeouts, and explicitly classified upstream failures.
4. Use a small attempt limit with backoff and jitter.
5. Never retry validation, authentication, authorization, or package-generation `422` failures.
6. Retry mutating calls only with tested idempotency.

A caller timeout does not prove the Receiver stopped executing. Design side effects so a repeated
request is safe, or pass a primitive idempotency key and persist its result.

Stateful calls are especially sensitive: reconnecting to another instance cannot restore remote
object identity. Prefer static stateless operations for retryable workflows.

Coordinate proxy idle timeout, transport timeout, application deadline, and Receiver dependency
timeout so the outer layer does not expire first without useful diagnostics.

Timeout, keep-alive, reconnect, and retry behavior differs across runtimes and is not a single
cross-runtime configuration surface. Check and test the generated runtime dependency before setting
production policy.

## Next steps

- [Errors and status reference](../reference/errors-and-status-reference.md)
- [Scaling](scaling-gateway-receivers.md)
- [Handle Receiver errors](../how-to-guides/handle-receiver-errors.md)
