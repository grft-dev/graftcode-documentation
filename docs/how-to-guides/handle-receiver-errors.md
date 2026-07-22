---
title: Handle Receiver errors
description: >-
  Classify Receiver, transport, and contract failures, surface them safely to the
  Caller, and retry only where repeat execution is safe.
articleTitle: Handle Receiver errors
---

# Handle Receiver errors

## Goal

Make failures from a Graft call predictable: classify what went wrong, surface a stable error to the
Caller, and retry only operations that are safe to repeat.

## Failure categories

A remote Graft call can fail in several distinct ways. Handle them differently:

| Category | Origin | Retry? | Caller sees |
| --- | --- | --- | --- |
| Domain error | Receiver business logic (invalid input, rule violation) | No | An error/exception carrying your domain message or code |
| Authentication error | Invocation credential missing or invalid | No (fix the credential) | An authorization failure surfaced by the Receiver |
| Authorization error | Caller authenticated but not permitted | No | A permission failure surfaced by the Receiver |
| Transport error | Connection dropped, host unreachable, TLS failure | Only if idempotent | A connection/transport error from the Graft |
| Timeout | Call exceeded the Caller/infra deadline | Only if idempotent | A timeout raised in Caller code or infrastructure |
| Unavailable Receiver | Gateway/Receiver down or not yet ready | Only if idempotent | A connection failure |
| Contract mismatch | Caller's Graft version and Receiver surface disagree | No (regenerate/upgrade) | A generation/`422` or a method/shape mismatch |

## Receiver domain error example

Validate inputs and raise a domain error with a safe message. Do not put secrets, tokens, or internal
stack details in the exception text — the message can reach the Caller.

```multi
```dotnet
public decimal Calculate(decimal basePrice, decimal discountPercent)
{
    if (discountPercent < 0 || discountPercent > 100)
        throw new ArgumentException("discountPercent must be between 0 and 100.");
    return basePrice * (1 - discountPercent / 100);
}
```
```javascript
export function calculate(basePrice, discountPercent) {
  if (discountPercent < 0 || discountPercent > 100) {
    throw new Error("discountPercent must be between 0 and 100.");
  }
  return basePrice * (1 - discountPercent / 100);
}
```
```

## Caller-side handling example

Treat a Graft call as a fallible remote call. Catch failures, and distinguish domain errors (do not
retry) from transport/timeout errors (retry only if idempotent).

```multi
```dotnet
try
{
    var price = pricing.Calculate(basePrice, discountPercent);
}
catch (Exception ex)
{
    // Log locally; do not assume the exception type equals the Receiver's native type.
    logger.LogWarning(ex, "Pricing call failed");
    throw;
}
```
```javascript
try {
  const price = await pricing.calculate(basePrice, discountPercent);
} catch (err) {
  // Log locally; the error shape may differ from the Receiver's native type.
  logger.warn({ err }, "pricing call failed");
  throw err;
}
```
```

## What is stable across runtime pairs

Native exception types, hierarchies, stack traces, and custom fields are **not** guaranteed to survive
a cross-runtime call. Depend on a stable, explicit error contract instead:

- an error **code** and a human-readable **message**, or
- a result model with an explicit success/failure field.

Log rich Receiver-side detail locally; return only the stable contract to the Caller.

## Retry guidance

- Retry only operations you have designed and tested as **idempotent**.
- Retrying a non-idempotent call can repeat business effects (double charge, duplicate record).
- Use bounded retries with backoff, and use explicit operation IDs for deduplication where possible.
- See [Timeouts and retries](../operations/timeouts-retries.md).

## Logging guidance

- Never log complete credentials or tokens, and never place them in an exception message.
- Log the failure category, operation, and a correlation/trace ID (see [Observability](../operations/observability.md)).
- Keep Receiver-internal detail on the Receiver side.

## Expected output

- Domain errors reach the Caller as a clear, safe error and are **not** retried.
- Transport/timeout errors are retried only for idempotent operations, then surfaced.
- Contract mismatches are resolved by regenerating and upgrading the Graft, not by retrying.

## Troubleshooting

- [Errors and status reference](../reference/errors-status.md)
- [Connection, timeout, and auth failures](../troubleshooting/connection-timeouts-auth.md)
- [Update a Receiver contract](update-receiver-contract.md)
