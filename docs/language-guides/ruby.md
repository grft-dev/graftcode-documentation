---
title: "Ruby Language Guide"
description: "Expose Ruby modules and consume generated Grafts through RubyGems."
---

# Ruby

## Support status and direction

**Provider: supported. Consumer: supported, with gaps.** Gateway lists Ruby hosting, and the inspected
implementation contains Ruby analysis, RubyGems resolution, Ruby code generation, and public
cross-runtime install/invoke tests. No inspected virtual-repository suite verifies Ruby's complete
Gateway first-publish path.

## Prerequisites

- Ruby 3+ per Gateway runtime support.
- RubyGems or Bundler and a loadable module/gem.
- A current [Graftcode Gateway](https://github.com/grft-dev/graftcode-gateway/releases).
- Native runtime dependencies required by the generated Hypertube gem.

## Provider support

Use ordinary Ruby modules/classes. Point Gateway at the module path and verify discovery:

```bash
bundle install
gg --runtime ruby --modules ./lib/
```

The exact path can be a source file or module directory depending on the package. Vision is the
authority for what was loaded.

## Consumer support

Ruby consumers receive a generated gem. The inspected generator defines class accessors
`GraftConfig.host`, `.stateless`, and `.module`, and generated classes use Ruby-style methods. Public
E2E tests cover installation and invocation against all six complete provider ecosystems.

## Package manager

RubyGems; Bundler can reference the emitted gem source. Package and require names can differ.

## Minimal provider example

```ruby
module Pricing
  class PriceService
    def self.calculate(base_price, discount_percent)
      base_price * (1 - discount_percent / 100.0)
    end
  end
end
```

Use stable, homogeneous value shapes because Ruby has no native public signature types.

## Minimal consumer example

```ruby
require '<require-name-copied-from-vision>'

GraftConfig.host = 'ws://localhost/ws'
GraftConfig.stateless = true

price = PriceService.calculate(100.0, 15.0)
puts price
```

`GraftConfig` syntax is verified. The require name, class location, and generated method name must
come from Vision or the installed gem; do not infer them from the gem filename.

## Installation

1. Run Gateway with `--runtime ruby` and wait for publication.
2. Open Vision's RubyGems configuration. Do not assume a route name.
3. Copy the complete emitted gem install/source command, package name, and version exactly.
4. Execute it unchanged, or copy the emitted source and gem declaration into the Gemfile.
5. Copy the exact `require` and generated invocation snippet.

The public E2E harness uses the equivalent shape `gem install <name> -v <version> --source <registry>`,
but the placeholders must be replaced only with values emitted by the running Gateway.

## Configuration

```ruby
GraftConfig.host = 'wss://service.example/ws'
GraftConfig.stateless = true
```

Defaults are `host = 'inmemory'` and `stateless = false`. Configure before the first generated call.
Verified header APIs include:

```ruby
GraftConfig.set_headers('Authorization' => 'Bearer <token>')
GraftConfig.invoke_with_headers({ 'Authorization' => 'Bearer <token>' }) { PriceService.calculate(100, 15) }
```

The header hash is the first argument to `invoke_with_headers` in the inspected generator.

## Supported types

The public E2E simple-car surface verifies strings, integers, booleans, arrays, constructors,
attributes/getters, instance/static methods, and returned objects. Use a conservative contract:

- `String`, `Integer`, `Float`, and booleans;
- small stable value objects;
- homogeneous `Array` values.

Avoid symbols at the boundary, hashes as open-ended maps, sets, enumerators, ranges, procs/blocks as
arguments, I/O objects, framework request/response objects, and `Time`/`Date`. Use strings and arrays
of explicit DTO-like objects.

**Gap:** `nil` unions, keyword-argument variants, Struct/Data classes, inheritance, metaprogrammed
methods, and heterogeneous arrays are not exhaustively verified.

## Runtime-specific limitations

- Explicit `--runtime ruby` is safer than relying on auto-detection.
- Package and require names use different normalization in tested gems.
- Generated module paths have had packaging regressions; current tests contain module-path correction
  helpers for some cross-runtime packages. Prefer current Gateway output and report mismatches.
- Ruby generator compilation is intentionally a no-op; syntax/load errors appear at runtime.
- Stateful instances require affinity and can expire; prefer class methods.

## Troubleshooting

- **`LoadError`:** use the exact emitted require name and confirm the gem is installed from its
  generated source.
- **Hosted file not found:** verify `GraftConfig.module` in the generated gem and the packaged source
  path.
- **No types discovered:** pass `--runtime ruby` and point `--modules` at loadable source.
- **Client attempts local loading:** set `GraftConfig.host`.
- **Inconsistent result mapping:** replace hashes/heterogeneous values with stable objects and arrays.

## Verified samples and tests

- [Gateway runtime documentation](https://github.com/grft-dev/graftcode-gateway#runtimes-typical-setups)
- [Cross-runtime simple-car sample](https://github.com/grft-dev/grft-test-simple-car)
- Inspected generated config:
  `graftcode-code-generator/src/ruby/graftcodecodegenerator/src/core/generator/handler/utils/graft_config_class_provider.rb`
- Inspected Ruby-to-Ruby test:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/ruby/ruby-to-ruby.spec.ts`
- Inspected Ruby caller matrix:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/ruby/`

## Known gaps

No dedicated Ruby Quick Start or Ruby virtual-repository first-publish test was found. Exact
publication output, gem source, require name, module path, and service API must come from the running
Gateway and generated gem.
