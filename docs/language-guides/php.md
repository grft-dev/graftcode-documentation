---
title: "PHP Language Guide"
description: "Expose PHP modules and consume generated Grafts through Composer."
---

# PHP

## Support status and direction

**Provider: supported. Consumer: supported, with gaps.** Gateway lists PHP hosting, and the inspected
implementation contains PHP analysis, Composer resolution, PHP code generation, and public
cross-runtime install/invoke tests. Unlike .NET, Node.js, JVM, and Python, no inspected virtual-repo
suite demonstrates the complete first-publish Gateway path for PHP. Treat that as a documentation and
release-verification gap, not as permission to invent commands.

## Prerequisites

- PHP 7.4+ per Gateway runtime support; use a current supported PHP release.
- Composer and PSR-4 package metadata.
- A current [Graftcode Gateway](https://github.com/grft-dev/graftcode-gateway/releases).
- Native runtime dependencies required by the generated Hypertube package.

## Provider support

Use plain typed PHP classes and point Gateway at the module directory:

```bash
composer install
gg --runtime php --modules ./src/
```

The exact module root must make project classes and Composer autoload metadata available. Confirm
loaded types and publication in Vision before consuming.

## Consumer support

PHP consumers receive a Composer package containing generated classes. The inspected generator
defines public static properties `GraftConfig::$host`, `::$stateless`, and `::$module`, plus
`setHeaders(...)` and scoped invocation methods. Generated namespaces and method names vary by source
runtime.

## Package manager

Composer with a generated Composer repository. The package name can contain generator-specific
normalization; copy it exactly.

## Minimal provider example

```php
<?php
declare(strict_types=1);

namespace Pricing;

final class PriceService
{
    public static function calculate(float $basePrice, float $discountPercent): float
    {
        return $basePrice * (1 - $discountPercent / 100);
    }
}
```

Declare parameter, return, and DTO property types.

## Minimal consumer example

Use the namespaces and autoload instructions emitted by Vision:

```php
<?php
require __DIR__ . '/vendor/autoload.php';

use <Generated\ConfigNamespace>\GraftConfig;
use <Generated\ServiceNamespace>\PriceService;

GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;

$price = PriceService::calculate(100.0, 15.0);
echo $price;
```

The `GraftConfig` property syntax is verified in generator source. The two `use` paths and service
method must be copied from the actual generated package.

## Installation

1. Run Gateway with `--runtime php` against the provider and wait for successful publication.
2. Open Vision's Composer configuration. Do not assume a route name.
3. Copy the emitted Composer repository configuration and `composer require` command exactly.
4. Run them in the consumer project unchanged.
5. Run any generated package post-install scripts shown by Composer/package metadata.
6. Use `vendor/autoload.php` and the exact generated namespaces.

Never derive a registry ID, package vendor/name, or version from the provider namespace.

## Configuration

```php
GraftConfig::$host = 'wss://service.example/ws';
GraftConfig::$stateless = true;
```

Defaults are `host = 'inmemory'` and `stateless = false`. Configure before the first generated call.
The inspected generated class also supports:

```php
GraftConfig::setHeaders(['Authorization' => 'Bearer <token>']);
```

## Supported types

The public E2E simple-car surface verifies strings, integers, booleans, arrays, object construction,
instance/static methods, and returned objects. For portable contracts, limit the public surface to:

- `string`, `int`, `float`, and `bool`;
- typed plain DTO classes;
- homogeneous, sequential arrays.

Avoid `mixed`, untyped `object`, associative maps, `iterable`, generators, resources, streams,
closures/callables, framework request/response types, and date objects. Use arrays of explicit key/value
DTOs for maps and ISO-8601 strings for dates.

**Gap:** nullable and union types, enums, attributes, advanced inheritance, and generic PHPDoc-only
shapes are not comprehensively verified.

## Runtime-specific limitations

- Explicit `--runtime php` is safer than relying on auto-detection.
- Composer package generation may require Hypertube post-install extraction scripts; retain generated
  package scripts and inspect Composer output.
- Autoloading alone may not expose every generated class in older packages; the E2E harness includes
  package-file discovery. Prefer the current generated package's documented autoload path.
- Stateful instances require affinity and can expire; prefer static methods.

## Troubleshooting

- **Class not found:** run `composer dump-autoload`, verify PSR-4 metadata, and use Vision's namespace.
- **Native binary/extraction error:** retain generated Composer scripts and ensure platform
  architecture compatibility.
- **No provider types:** pass `--runtime php`, verify module root, and ensure dependencies are installed.
- **Client attempts local loading:** set `GraftConfig::$host`.
- **Unexpected generated shape:** replace associative or weakly typed public values with explicit DTOs.

## Verified samples and tests

- [PHP simple-car package source](https://github.com/grft-dev/sdn-test-simple-car)
- [Gateway runtime documentation](https://github.com/grft-dev/graftcode-gateway#runtimes-typical-setups)
- Inspected generated config:
  `graftcode-code-generator/src/php/GraftcodeCodeGenerator/Core/Generator/Handler/Utils/GraftConfigClassProvider.php`
- Inspected PHP-to-PHP test:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/php/php-to-php.spec.ts`
- Inspected PHP caller matrix:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/php/`

## Known gaps

No dedicated PHP Quick Start or PHP virtual-repository first-publish test was found in the inspected
trees. Exact provider packaging, installation output, namespaces, and service calls must come from the
running Gateway and generated Composer package.
