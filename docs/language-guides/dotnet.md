---
title: ".NET Language Guide"
description: "Expose .NET libraries and consume generated Grafts through NuGet."
---

# .NET

## Support status and direction

**Provider: supported. Consumer: supported.** The inspected implementation has .NET module analysis,
NuGet generation, compilation, and generated-client tests. Public and virtual E2E suites exercise
.NET as both caller and target. Use `netcore` for modern .NET; `clr` is the .NET Framework host mode.

## Prerequisites

- .NET Core 3.1, or .NET 5+; use an SDK matching your project.
- A class-library project and a built DLL.
- A current [Graftcode Gateway](https://github.com/grft-dev/graftcode-gateway/releases).
- NuGet access from the consuming project.

## Provider support

Expose a class library, not a web application. Public classes, methods, and public DTO members become
contract candidates. Build the specific project, then point Gateway at the resulting DLL:

```bash
dotnet build ./Pricing/Pricing.csproj
gg ./Pricing/bin/Debug/net9.0/Pricing.dll
```

Use the actual target framework and output path. Confirm `Type enabled` and successful model upload in
Gateway output or Vision before installing a graft.

## Consumer support

.NET consumers receive a compiled NuGet package. Generated methods are synchronous and preserve the
provider's names. `GraftConfig` uses PascalCase static fields: `Host`, `Stateless`, and `Module`.

## Package manager

NuGet. The feed URL, package ID, and version are generated for the running Gateway.

## Minimal provider example

```csharp
namespace Pricing;

public static class PriceService
{
    public static double Calculate(double basePrice, double discountPercent) =>
        basePrice * (1 - discountPercent / 100);
}
```

Keep public methods synchronous. If implementation work is asynchronous, block internally and return
the value from the public method.

## Minimal consumer example

The namespace is generated from the real provider and package. Copy it from Vision:

```csharp
using <generated_namespace>;

GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;

double price = PriceService.Calculate(100, 15);
Console.WriteLine(price);
```

`Host` and `Stateless` are fields, not setters or properties. Replace the import and method with the
exact generated API.

## Installation

1. Run Gateway against the built DLL and wait for publication to succeed.
2. Open Vision's NuGet configuration, or use the NuGet route printed by that Gateway.
3. Copy the complete `dotnet add package` command, including its source, package ID, and version.
4. Run that command in the consuming project directory unchanged.
5. Copy the generated namespace and usage snippet from Vision.

Do not reuse an example registry ID. A Gateway without a stable project key can emit a new registry ID
after restart. Preserve `nuget.org` for ordinary dependencies; in controlled builds, map generated
graft package patterns to the Graftcode feed and other packages to `nuget.org`.

## Configuration

```csharp
GraftConfig.Host = "wss://service.example/ws";
GraftConfig.Stateless = true;
```

The default is `Host = "inmemory"` and `Stateless = false`. In-memory mode requires the provider DLL
to be locally loadable. Set a `ws://` or `wss://` Gateway endpoint for remote calls. Configure these
fields before the first generated call because initialization is cached. `SetHeaders(...)` and
`InvokeWithHeaders(...)` are present in the inspected generator.

## Supported types

Verified portable baseline:

- `string`, `int`, `double`, `decimal`, and `bool`;
- plain DTOs composed of portable members;
- homogeneous arrays such as `string[]` and `Price[]`.

The package-generation engine explicitly rejects framework complex types in public APIs. Avoid
`Task`, `Task<T>`, `DateTime`, `DateOnly`, `Guid`, `Stream`, cancellation tokens, HTTP types,
interfaces, dictionaries, and framework collection types. Use ISO-8601 strings for time values,
strings for IDs, and arrays for collections.

**Gap:** the E2E simple-car surface does not exhaustively verify every numeric width, nullable shape,
enum, inheritance form, or generic type. A known cross-runtime risk exists for `long` consumed by
JavaScript; use `int` or a decimal string unless your exact generated graft is tested.

## Runtime-specific limitations

- Public `async` methods expose `Task<T>`, which is not a portable public contract.
- A public custom exception can be discovered as a contract type; keep exception classes internal.
- Instance methods create remote object identity. They need session affinity and can become invalid
  after restart or scale-in; prefer static stateless methods.
- SDK-style projects recursively include `.cs` files. Keep consumer/test projects outside the
  provider library directory.

## Troubleshooting

- **Framework type rejection:** simplify every public signature and DTO member.
- **`FileNotFound` for the provider DLL:** the client remained in `inmemory`; set `GraftConfig.Host`.
- **`NU1301` during clean restore:** keep `nuget.org` and use package-source mapping.
- **Method or namespace not found:** inspect Vision's generated contract; do not infer casing.
- **Remote nested DTO is slow:** use a static provider method and set `Stateless = true`.

## Verified samples and tests

- [.NET expose-backend Quick Start](https://github.com/grft-dev/graftcode-quick-start-guide/blob/main/2-expose-backend/dotnet.md)
- [Cross-runtime simple-car sample](https://github.com/grft-dev/grft-test-simple-car)
- Inspected generated config:
  `graftcode-code-generator/src/netcore/GraftCodeCodeGenerator/Core/Generator/Handler/Utils/GraftConfigClassProvider.cs`
- Inspected E2E caller suite:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/public-repos-smoke-tests/netcore/`
- Full publish tests:
  `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/netcore/`

## Known gaps

The inspected evidence does not establish a universal supported-type matrix or guarantee every
target-framework moniker. Vision and a generated package from your running Gateway are authoritative.
