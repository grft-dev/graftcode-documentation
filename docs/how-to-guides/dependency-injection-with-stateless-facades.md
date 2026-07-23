---
title: "Dependency injection with stateless facades"
description: "Keep dependency injection internal while exposing a small Graftcode-compatible facade."
articleTitle: "Dependency injection with stateless facades"
---
# Dependency injection with stateless facades

Keep framework containers and infrastructure types off the public callable surface. Expose a small
facade with primitive or plain-model parameters and wire dependencies inside the facade method or
through internal modules.

## Example: .NET Receiver

Start with a public business method and keep the container private:

```csharp
using Microsoft.Extensions.DependencyInjection;

public static class CreditRatingService
{
    private static readonly ServiceProvider Services =
        new ServiceCollection()
            .AddScoped<CreditRepository>()
            .BuildServiceProvider();

    public static string CalculateCredit(int score)
    {
        using var scope = Services.CreateScope();
        return scope.ServiceProvider
            .GetRequiredService<CreditRepository>()
            .Calculate(score);
    }
}

internal sealed class CreditRepository
{
    internal string Calculate(int score) => score.ToString();
}
```

Only the facade and its supported primitive/string or plain-DTO values belong on the callable surface.
Keep `IServiceProvider`, repositories, database contexts, framework types, and DI constructors
internal.

## Lifetime, disposal, and concurrency

A static facade is **not** automatically stateless. The method above holds no per-call state, but the
static `ServiceProvider` is process-wide shared state. Treat these as separate concerns:

- **Per-invocation work:** create a scope inside each public call (as above) when dependencies are
  scoped, so each call gets its own scoped instances.
- **Singleton safety:** singleton lifetime means process-wide shared state reused across concurrent
  calls. Use it only when the dependency is thread-safe and that lifecycle is intended.
- **Concurrency:** Gateway can invoke the facade concurrently. Do not store per-caller or
  request-specific state in static fields; pass request-specific identity as method parameters or
  per-invocation context.
- **Disposal and graceful shutdown:** a process-wide provider lives for the process lifetime. If your
  dependencies hold connections or files, dispose per-call scoped instances (the `using` scope handles
  this) and dispose the root provider on graceful shutdown rather than leaking resources.

The example initializes lazily through CLR type initialization and does not require a module
entrypoint. If an application instead depends on an entrypoint such as `Main` to build its container,
start Gateway with the release's `--runApp` option and verify startup before invoking the facade;
entrypoint execution is not unconditional.

## Other runtimes

Dedicated DI walkthroughs for Node.js, Python, Java, PHP, and Ruby are not included here. Apply the
same facade pattern: internal container, public static or module-level methods with portable types
only. See [Supported runtimes and package managers](../reference/supported-runtimes-and-package-managers.md) for runtime-specific packaging notes.

## Next steps

- [Filter the callable surface](filter-the-callable-surface.md)
- [Callable surface](../core-concepts/callable-surface.md)
- [Type mapping](../core-concepts/type-mapping.md)
- [Runtime-specific notes](../reference/known-limitations.md#runtime-specific-notes)
