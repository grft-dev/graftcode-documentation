---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---

Turn an existing Python module into a provider without adding web-framework route handlers.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Type every public parameter and return value. Prefix non-contract helpers with `_`:

```python
class PriceService:
    @staticmethod
    def calculate(amount: float, discount_percent: float) -> float:
        return amount * (1 - discount_percent / 100)
```

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings.

## 2. Prepare the module directory

Keep test scripts and unrelated public functions outside the provider directory.

## 3. Start Gateway with the real module

```bash
gg --runtime python --modules ./pricing/
```

Adjust paths to the project. Do not copy package IDs, registry URLs, or project keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** there is no verified universal type matrix. Generate and smoke-test every producer/consumer
language pair that uses types beyond the portable baseline.

## Next steps

- [Run Gateway locally](../run-gateway-locally)
- [Obtain and install a Graft](../obtain-install-graft)
- [Type compatibility matrix](../../reference/type-matrix.md)

## Source anchors

- `graftcode-gateway/README.md`, “Usage” and “Runtimes (typical setups)”
- [Expose a Python backend](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/python.md)
