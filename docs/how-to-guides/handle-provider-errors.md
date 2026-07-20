---
title: "Handle provider and transport errors"
description: "Keep provider failures actionable and add retries only where repeat execution is safe."
---

# Handle provider and transport errors

## Goal

Distinguish provider failures from transport and package-generation failures.

## 1. Make provider failures explicit

Validate input at the public method boundary and throw exceptions with non-sensitive, actionable
messages. Remote provider exceptions propagate to the consumer, so do not include credentials,
tokens, connection strings, or internal stack details in messages.

Keep custom exception classes internal. A public exception type can become part of the discovered
contract and trigger unsupported-type generation.

## 2. Classify failures before retrying

- **Provider/domain error:** invalid input, authorization denial, or business rule. Do not retry.
- **Transient provider dependency:** timeout or upstream `5xx`. Retry inside the provider only if the
  operation is safe and bounded.
- **Gateway/transport failure:** unavailable connection or interrupted session. Retry only idempotent
  operations; stateful object identity may already be lost.
- **Package generation `422`:** fix the public contract; retrying unchanged input cannot help.

## 3. Bound third-party calls

Use one reusable client, a finite timeout, and a small retry count with backoff for transient status
codes. Preserve the final cause in a domain-focused exception. Do not put `HttpClient`, request,
response, stream, cancellation, or framework date types on the public contract.

## 4. Prevent duplicate effects

Graftcode does not establish a universal exactly-once guarantee. If a mutating call can be retried,
design an application-level idempotency key as a supported primitive and store the result.

**Gap:** automatic retry, reconnect, and timeout defaults are runtime/transport-specific and not
documented as a stable cross-runtime contract. Configure resilience in the provider, caller, or
infrastructure only after testing the selected generated package.

## Next steps

- [Timeouts and retries](../operations/timeouts-retries.md)
- [Errors and status reference](../reference/errors-status.md)
- [Logging, metrics, and tracing](../operations/observability.md)

## Source anchors

- `graftcode-package-generation-engine/src/netcore/GraftCodePackageGenerationEngine/Exceptions/UnsupportedTypeUsageException.cs`
- `graftcode-package-manager-gateway/src/jvm/src/test/java/com/graftcode/gpmg/integration/SoennekerExtensionsTypeArrayIntegrationTest.java`
- `HYPERTUBE/src/*/` WebSocket and HTTP/2 client implementations
