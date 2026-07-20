---
title: "Expose code as a Graftcode provider"
description: "Prepare a small public contract and verify that Gateway discovers it."
articleTitle: "Expose code as a Graftcode provider"
---

Turn an existing Ruby module into a provider without adding framework route handlers.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use ordinary Ruby modules and classes:

```ruby
module Pricing
  class PriceService
    def self.calculate(amount, discount_percent)
      amount * (1 - discount_percent / 100.0)
    end
  end
end
```

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings.

## 2. Prepare the module directory

Run Bundler and point Gateway at the module path shown by the package.

## 3. Start Gateway with the real module

```bash
bundle install
gg --runtime ruby --modules ./lib/
```

Adjust paths to the project. Do not copy package IDs, registry URLs, or project keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** no inspected virtual-repository suite verifies Ruby's complete Gateway first-publish path.

## Next steps

- [Run Gateway locally](../run-gateway-locally)
- [Obtain and install a Graft](../obtain-install-graft)
- [Type compatibility matrix](../../reference/type-matrix.md)

## Source anchors

- `graftcode-gateway/README.md`, “Usage” and “Runtimes (typical setups)”
