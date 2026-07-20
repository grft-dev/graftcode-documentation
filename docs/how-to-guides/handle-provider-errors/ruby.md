---
title: "Handle provider and transport errors"
description: "Keep provider failures actionable and add retries only where repeat execution is safe."
articleTitle: "Handle provider and transport errors"
---

## Provider boundary

Validate inputs and throw domain exceptions with safe messages—no secrets in exception text.

## Classify before retry

- Domain errors: do not retry.
- Transient upstream `5xx` inside provider: bounded retry if idempotent.
- Transport failures: retry only idempotent operations; stateful identity may be lost.
- Package `422`: fix the public contract.

## Host example

```bash
bundle install
gg --runtime ruby --modules ./lib/
```

See [Timeouts and retries](../../operations/timeouts-retries.md) and
[Errors reference](../../reference/errors-status.md).
