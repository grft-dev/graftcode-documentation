# What is a Graft

A Graft is a strongly-typed client library that represents a remote module or package as if it were a local dependency in your application. From the developer’s perspective, using a graft does not feel like calling an API, a microservice, or a remote system. It feels exactly like calling ordinary code: creating objects, invoking methods, passing arguments, and receiving return values using the native types of the programming language you are working in.

The core idea behind grafts is to remove the traditional integration layer from software development. Instead of defining REST endpoints, gRPC contracts, DTOs, OpenAPI specifications, or client SDKs, a developer simply exposes public methods in a module or consumes an existing package. Graftcode automatically discovers public interfaces and generates a graft — a native, strongly-typed client package — for any supported target technology. This graft mirrors the exposed interface precisely, including method signatures, types, return values, and errors, and stays continuously in sync with the original module or package.

A Graft is not limited to representing remote services. A Graft can represent **any package** — from the same technology or a completely different one — whether it comes from a public artifact repository or a private feed. This means that libraries written in foreign technologies can be consumed directly and safely in-memory, without spinning up separate services or rewriting code. A JavaScript application can call into a .NET or Java package, a .NET service can invoke Python or Node.js libraries, and all of this can happen within a single process if desired. In such scenarios, Grafts act as a universal bridge between technologies, enabling true in-memory cross-technology execution.

A Graft is a first-class package distributed through standard package managers such as npm, NuGet, or PyPI. From the point of view of the consuming application, the Graft is just another dependency. The fact that its implementation executes in a different runtime, process, or even on a different machine is completely transparent and controlled purely through configuration.

What makes this possible is Graftcode's runtime-level communication layer, which connects programming language runtimes directly rather than communicating through application-level protocols such as HTTP or JSON. Method calls performed on a Graft are translated into a binary, runtime-aware representation of the developer's intent and executed on the target runtime using the most efficient transport available. This can happen in-process, between processes on the same machine, or remotely over the network, without changing a single line of calling code. As a result, the same Graft can represent a module that is embedded locally during development and later moved to a remote microservice in production.

Strong typing is preserved end-to-end. Primitive values such as strings, numbers, booleans, and dates are passed using the native types of the calling language. Complex objects are handled as remote references. When a method accepts a complex type, the argument is represented as a Graft of that type. When a method returns a complex object, Graftcode automatically provides a strongly-typed Graft instance that references the remote object. These returned objects are fully functional: subsequent method calls on them are executed remotely, just as if the object existed locally.

Because Grafts are generated directly from the actual interfaces of modules and packages, they eliminate an entire class of integration problems. There is no duplicated contract, no hand-written serialization logic, and no version drift between producer and consumer. If a module's public interface changes, the corresponding Graft changes as well, and incompatibilities surface immediately at compile time or import time rather than as runtime errors. This makes distributed, cross-technology systems behave much closer to a single, strongly-typed codebase.

In practice, a Graft is simply the most natural way to consume remote or foreign business logic. It allows developers to think in terms of code, not infrastructure. Architecture decisions such as whether a module runs locally in-memory or remotely on another node become configuration concerns rather than design constraints. This is the foundation on which Graftcode enables modular monoliths, microservices, cross-language integration, and dynamic architectures without the usual integration overhead.

Once this model is understood, using a Graft becomes straightforward.

---

## Where Does the Graft Come From?

For services and modules that you own, Grafts are discovered and distributed through **Graftcode Vision**. Vision is the central discovery and documentation portal that lists all modules exposed through Graftcode Gateways. When you run a Graftcode Gateway hosting your module, Vision automatically publishes its interface and provides an **Installation** section with ready-to-use package manager commands, as well as a **Configuration** section showing how to connect a Graft to a specific running instance. (See [Graftcode Gateway](../core-concepts/graftcode-gateway.md) for more details.)

For third-party or reusable libraries, Grafts can be discovered using **Graftcode Modules**, a search engine that indexes public and private artifact feeds across all supported technologies. It allows you to find modules using natural language queries powered by LLMs, locate the correct package regardless of its original ecosystem, and install its Graft directly. Once a package is grafted, it can be consumed like any other dependency and used across technologies.

For your own remote services and modules, the typical path is Vision (because it is driven by your Gateway and your runtime instances). For public or private packages living in artifact repositories, the typical path is Modules (because it is driven by indexed artifact feeds). In both cases, the outcome is the same: you end up with an install command for a Graft package and configuration guidance to connect to the right execution target.

---

## Installing and Using a Graft

Grafts are installed using standard package managers. The only additional step compared to installing a regular dependency is pointing the package manager to a Graftcode registry. The registry you use depends on your setup. Free setups use an anonymous registry. Project setups use a project-specific registry associated with a running Graftcode Gateway.

A free registry URL has the form:

```
http://grft.dev/<random-guid>__free
```

A project registry URL has the form:

```
http://grft.dev/<project-id>__graftcode
```

A Graft package name follows a simple convention that encodes both the target package ecosystem and the original module name:

```
graft.<technology_package>.<ModuleName>
```

where `<technology_package>` identifies the target package ecosystem (for example, npm, nuget, or pypi).

For example, a .NET module EnergyPrice.dll, which uses NuGet as its package manager, is exposed as a Graft package named `graft.nuget.EnergyPrice`. The same module, when consumed from Node.js, which uses npm, is installed as `graft.npm.EnergyPrice`.

After adding the appropriate registry, installing a Graft is no different from installing any other dependency.

### NuGet

```bash
dotnet add package graft.nuget.EnergyPrice \
  --source http://grft.dev/<project-id>__graftcode
```

### npm

```bash
npm install graft.npm.EnergyPrice \
  --registry=http://grft.dev/<project-id>__graftcode
```

Once installed, the Graft can be imported and used immediately.

---

## Calling Remote and In-Memory Code as Local Code

Assume the following .NET module is hosted through a Graftcode Gateway or loaded in-memory:

```csharp
public class EnergyService
{
    public decimal GetCurrentPrice(string countryCode)
    {
        return 0.32m;
    }

    public Invoice CalculateInvoice(Customer customer, int kWh)
    {
        return new Invoice
        {
            Customer = customer,
            TotalPrice = kWh * 0.32m
        };
    }
}
```

No controllers, APIs, or transport-specific code are required. Public methods are enough.

From JavaScript, the same module can be used as follows:

```ts
import { EnergyService } from "@graft/npm.EnergyPrice";

const energy = new EnergyService();

const price = await energy.getCurrentPrice("DE");

const invoice = await energy.calculateInvoice(
  { id: "cust-1", name: "ACME Corp" },
  1200
);

console.log(invoice.totalPrice);
```

Primitive values are passed using native JavaScript types. Complex objects such as `Customer` and `Invoice` are represented as Grafts referencing remote or in-memory objects.

---

## Graftcode Gateway, Versioning, and Virtual Feeds

When a Graftcode Gateway is started in project-bound mode, every module it exposes is registered in a single virtual feed per package manager for that project. It does not matter which gateway instance reports the module: the same module, in the same version, can be started on any number of nodes or environments, and the same Graft will continue to work without changes.

Graftcode enforces package-like semantics for Grafts. If a module with the same name and version is reported again but exposes a different public interface, the registration will fail. This prevents accidental interface drift and ensures consistency across the project. To change the public contract, the module version must be incremented, exactly as if a new package version were being published to an artifact repository.

This mechanism allows teams to treat services and modules as immutable, versioned artifacts while still deploying them dynamically across environments. From the consumer's point of view, Grafts behave exactly like normal packages, even though their implementation may be running on multiple nodes or instances.

---

## Configuring a Graft

Each Graft exposes a configuration class named `GraftConfig` in its root namespace. At a minimum, this configuration specifies the target runtime where Graft method calls are executed.

```ts
import { GraftConfig } from "@graft/npm.EnergyPrice";

GraftConfig.host = "tcp://energy-service:9000";
```

Instead of specifying only a host address, a full Graft Connection String can be used to define the transport, authentication, plugins, and other execution details.

```ts
GraftConfig.setConfig("name=graft.nuget.EnergyPrice;runtime=netcore;host=ws://localhost:8004/ws")
```

*Note: Full connection string configuration is not yet supported in the current release.*

Grafts can also be configured without code changes by supplying connection strings through environment variables or configuration files. These can be defined per Graft or globally for all Grafts used by the application.

---

## Summary

A Graft represents remote, cross-language business logic as a local, strongly-typed dependency. You install it like a normal package, configure its execution location, and call methods as if the code were local. Graftcode handles transport, serialization, runtime bridging, and synchronization.
