---
title: "Alpha limitations and known constraints"
description: "Understand the current limitations of Graftcode Alpha, including interface constraints, type restrictions, portal capabilities, and what to expect as the product evolves toward Beta."
keywords: "graftcode alpha, limitations, known constraints, alpha version, backward compatibility, type restrictions, portal"
---

# Graftcode is currently in **Alpha**.

You can already use it to build real, large-scale distributed systems—but you need to be aware of the constraints that apply in this stage.

This page lists the current limitations, practical workarounds, and links to roadmap items that address them.

---

## Interface and type constraints

### Public methods with simple types

Your API must consist of **public methods** that accept either:
- primitive / simple types (e.g. `string`, `int`, `bool`, `double`)
- objects composed exclusively of simple types
- arrays of those types

This applies to both method parameters and return types.

These types can also be objects composed of simple types with additional nesting—objects within objects are supported as long as every leaf value is a simple type.

---

### No Task or async return types

Method results **cannot** be a `Task`, `Promise`, or any equivalent async wrapper.

Graftcode runs every method invocation in its own thread. There is no need to return async handles—execution is inherently parallel at the infrastructure level.

---

### No class inheritance in interfaces

The classes exposed through your public interface **cannot inherit from other classes**.

Only flat, standalone classes are supported. If your design relies on inheritance hierarchies, refactor the public surface into standalone classes that delegate internally.

---

### Primitive-type wrappers must be passed by value

Types that wrap primitives—such as `Date`, `TimeSpan`, `Guid`, `Point`, `Color`—are **not** supported as first-class types in the current Alpha.

You must pass them by value using their underlying representation:
- `Date` → pass as `string` (e.g. ISO 8601 format) or as a numeric timestamp
- `TimeSpan` → pass as `long` (milliseconds or ticks)
- `Guid` → pass as `string`
- `Point`, `Color` → pass as `string` or as an object with simple-type fields

Parse and reconstruct them on the receiving side.

In beta release Grafts will accept calling side counterparts and perform the pass by value implicitly. Monitor Roadmap item below to be notified when its ready.

> [Roadmap: Support for using calling technology classes wrapping value types (i.e. Date)](https://graftcode.featurebase.app/p/support-for-using-calling-technology-classes-wrapping-value-types-ie)

---

## Complex objects and stateful execution

When you use objects composed of simple types as method parameters or return values, the current Alpha introduces a **side effect**: requests become **stateful**.

This means:
- you must ensure **session stickiness** at the load balancer level, or use a single backend instance
- every access to a property on a returned object results in a **separate call** to the backend, which can significantly reduce performance

This is a known constraint and will be addressed in **Beta**, where object state will be resolved locally without requiring round-trips.

> [Roadmap: Support for Stateless Unary Calls with DTO](https://graftcode.featurebase.app/p/support-for-stateless-unary-calls-with-dto)

---

## No backward compatibility guarantee

Graftcode Alpha **does not guarantee backward compatibility** between major releases.

A new major release may require you to:
- replace the Graftcode Gateway binary
- regenerate and refresh all Grafts consumed by your services

Plan accordingly and pin specific versions in production environments until you are ready to upgrade.

> [Roadmap: Guarantee Backward Compatibility for Grafts, Protocol and Gateways](https://graftcode.featurebase.app/p/guarantee-backward-compatibility-for-grafts-protocol-and-gateways)

---

## npm: manual SDK dependency

When installing a Graft via npm, you must **manually install** the underlying Hypertube dependency:

```bash
npm install javonet-nodejs-sdk
```

This dependency is not pulled automatically during Graft installation in the current Alpha.

> [Roadmap: Automated resolution of Hypertube Dependency from Graftcode Registry for other than Nuget technologies](https://graftcode.featurebase.app/p/automated-resolution-of-hypertube-dependency-from-graftcode-registry-for-other)

---

## Authentication and authorization

JWT tokens, API keys, or any other authentication and authorization credentials must be **explicitly passed as a method parameter**.

Graftcode does not support plugins tht could pass JWT automatically in the Alpha version. Before executing any business logic, validate the token or key inside your implementation.

```csharp
public OrderResult PlaceOrder(string jwtToken, int productId, int quantity)
{
    ValidateToken(jwtToken); // your responsibility
    // ... business logic
}
```

> [Roadmap: Release of the first JWT authentication plugin](https://graftcode.featurebase.app/p/release-of-the-first-jwt-authentication-plugin)

---

## Filtering exposed types

If your service has many public interfaces but you only want to expose a subset, create **one static class with static methods** as your public facade, and use the `--types` filter when running `gg`:

```bash
gg --types MyNamespace.MyFacade,MyNamespace.AnotherFacade --modules yourlib.dll
```

Only methods from the specified types (provided as fully qualified names separated by commas) will be exposed through the Gateway.

> [Roadmap: Filter types support in Gateway](https://graftcode.featurebase.app/p/filter-types-support-in-gateway)

---

## Modules: AI-powered search across all package repositories

The [**Modules**](https://modules.graftcode.com) section in Graftcode Portals lets you search for modules across all major package repositories—PyPi, npm, NuGet, Packagist, RubyGems, Maven, and more—using natural language powered by AI.

You describe what you need, and Graftcode finds the best matching module regardless of which language it was written in. It suggests the module, shows its public interface, and provides a ready-to-use installation command for your project—no matter what technology you are using on the caller side.

This effectively removes the barrier between programming languages when it comes to discovering and reusing open-source modules.

Modules found this way can be used **in-memory within a single process** through Graftcode Gateway. However, in the current Alpha most modules from public repositories **will fail to generate a Graft**. This is expected—the Alpha restricts many interface structures (no inheritance, no complex wrapper types, limited generics), and the majority of real-world libraries expose interfaces that go beyond what is currently supported.

When Graft generation fails, you will see an explicit error explaining which interface structure is not yet supported.

As Alpha constraints are lifted in upcoming releases, the share of publicly available modules that can be successfully Grafted will grow significantly.

---

## Portals limitations

The Graftcode Portals are in early Alpha with limited functionality.

### What works

- **Creating workspaces and projects** — fully functional
- **Stable registry address** — once a project is created, you receive a permanent registry URL. This allows you to:
  - use Grafts from CI/CD pipelines
  - install and refresh Grafts from multiple machines
  - update hosted module versions without changing the registry address in your package manager configuration

### What does not work yet

- Most **KPIs, dashboards, and controls** are not functional
- You **cannot invite colleagues** to a project or workspace — collaboration features are not yet available

Some of upcoming items to Portals:
> [Roadmap: Inviting team members to project or workspace](https://graftcode.featurebase.app/p/inviting-team-members-to-project-or-workspace)
> [Roadmap: Settings section for Account, Workspace and Project](https://graftcode.featurebase.app/p/settings-section-for-account-workspace-and-project)

---

## In short

Graftcode Alpha is production-capable for real distributed systems, provided you work within these constraints:

| Constraint | Workaround |
|---|---|
| Simple types only in API signatures | Use primitives and flat objects |
| No `Task` / async returns | Graftcode parallelizes execution automatically |
| No class inheritance | Use standalone classes, delegate internally |
| Primitive wrappers (`Date`, `Guid`, etc.) | Pass as `string` or `int`, parse on receiver |
| Complex objects cause stateful calls | Use session stickiness or single instance |
| No backward compatibility | Pin versions, plan for Gateway + Graft refresh |
| npm requires manual SDK install | Run `npm install javonet-nodejs-sdk` |
| No automatic auth propagation | Pass tokens explicitly, validate in code |
| Modules: most public libs fail to Graft | Alpha interface constraints block most real-world libraries |
| Portal is limited | Projects and registries work; dashboards and collaboration do not |

These constraints reflect the current Alpha stage. Most are actively being addressed on the [Graftcode roadmap](https://graftcode.featurebase.app/roadmap) and will be resolved in upcoming releases.

---

Next, we'll move into **Integration patterns**, where we explore common architectures that Graftcode enables.
