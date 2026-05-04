---
title: "Dependency injection in C#/.NET with stateless facades"
description: "Use dependency injection behind a public static facade in Graftcode modules by building the container in entrypoint methods and resolving scoped or singleton services per invocation."
keywords: "graftcode dependency injection, csharp, dotnet, stateless facade, entrypoint, service provider, scoped services, singleton services"
---

# Dependency injection in C#/.NET with stateless facades

You can apply dependency injection in a backend module built with the Graftcode approach without exposing DI details to consumers.

The key rule is simple:

- keep the public contract as a `public static` facade
- build the container during module startup (entrypoint)
- resolve dependencies inside facade methods

This preserves stateless invocation semantics while still giving you full DI flexibility internally.

---

## Why this pattern fits Graftcode

Graftcode exposes what is public and generates a strongly typed Graft client from it.

That means consumers should see business operations, not DI mechanics.

If constructor parameters or DI-centric methods are made public, they can be grafted and become part of your external contract unintentionally.

Keep DI hidden behind the public facade and expose only stable business methods.

---

## Architecture and pattern

### Public surface (contract)

Expose only a `public static` class with `public static` methods that represent business operations.

### Composition root (entrypoint)

Use module entrypoint methods (for example `Main`) to build your service collection and `IServiceProvider`.

Graftcode Gateway automatically calls module entrypoints when loading a module, so this is the right place to initialize your container.

### Internal implementation

Use regular POCO classes (`internal` or non-public where possible) for repositories, domain services, and infrastructure.

Resolve them from the static facade per call.

---

## C#/.NET example

```csharp
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Text;

namespace GC.Webportals.ActivityFeed.Facade;

public interface IRuntimeModule
{
    void ConfigureServices(IServiceCollection services);
}

#region EntryPoint
internal class Program
{
    internal static IServiceProvider Services { get; private set; } = default!;

    internal static void Main(string[] args)
    {
        var services = new ServiceCollection();

        // Global/shared registrations
        services.AddSingleton<StringBuilder>();
        services.AddScoped<CreditRepository>();
        services.AddScoped<CosmosDbContext>();

        Services = services.BuildServiceProvider(
                new ServiceProviderOptions  {
                    ValidateScopes = true,
                    ValidateOnBuild = true  }
                );
    }
}
#endregion

#region PublicFacade
public static class CreditRatingService
{
    public static string CalculateCredit(int request)
    {
        using var scope = Program.Services.CreateScope();
        var repo = scope.ServiceProvider.GetRequiredService<CreditRepository>();
        return repo.Calculate(request);
    }

    public static void WriteToLog(string request)
    {
        // Singleton lifetime: shared across invocations in this process
        Program.Services
            .GetRequiredService<StringBuilder>()
            .AppendLine(request);
    }
}
#endregion

#region Internal Implementation
internal sealed class CreditRepository
{
    private readonly CosmosDbContext _context;

    internal CreditRepository(CosmosDbContext context)
    {
        _context = context;
    }

    internal string Calculate(int request) => request.ToString();
}

internal sealed class CosmosDbContext
{
}

#endregion
```

---

## Scoped and singleton lifetimes in stateless invocations

You can safely combine lifetimes:

- `Scoped`: create a scope per facade call for request-like dependencies (repositories, unit-of-work, db contexts)
- `Singleton`: use process-level shared services (configuration, caches, log buffers, stateless utilities)

In practice:

- create a new scope in each public method when you need scoped services
- resolve singleton services directly from the root provider

This gives you deterministic per-invocation behavior and efficient shared resources.

---

## What to avoid

Do not expect DI instances to be passed by consumers:

- not via constructor arguments on public facade classes
- not via public method parameters intended for DI plumbing

Anything public is a candidate for graft generation and can become part of the consumer-facing API.

Keep the public API business-oriented and keep DI wiring internal.

---

## Template for future technology variants

Use this article as a template for additional stacks until offical article is released:

- `Architecture and Patterns`
  - `Dependency Injection`
    - `C#/.NET` (this article)
    - `Java/Spring` (future)
    - `Node.js` (future)
    - `Go` (future)

We will keep the same structure in each technology-specific page:

1. Public contract model
2. Entrypoint/composition root
3. Scoped vs singleton strategy
4. What to avoid in public API
5. Minimal reference implementation