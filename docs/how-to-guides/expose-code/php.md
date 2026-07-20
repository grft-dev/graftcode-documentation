---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---

Turn an existing PHP module into a provider without adding framework route handlers.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use plain typed PHP classes:

```php
<?php

namespace Pricing;

final class PriceService
{
    public static function calculate(float $amount, float $discountPercent): float
    {
        return $amount * (1 - $discountPercent / 100);
    }
}
```

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings.

## 2. Prepare the module directory

Run Composer and point Gateway at the module root that contains project classes and autoload metadata.

## 3. Start Gateway with the real module

```bash
composer install
gg --runtime php --modules ./src/
```

Adjust paths to the project. Do not copy package IDs, registry URLs, or project keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** no inspected virtual-repo suite demonstrates the complete first-publish Gateway path for PHP.
Treat that as a release-verification gap, not as permission to invent commands.

## Next steps

- [Run Gateway locally](../run-gateway-locally.md)
- [Obtain and install a Graft](../obtain-install-graft)
- [Type compatibility matrix](../../reference/type-matrix.md)

## Source anchors

- `graftcode-gateway/README.md`, “Usage” and “Runtimes (typical setups)”
