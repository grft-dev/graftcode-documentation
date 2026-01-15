---
title: "What happens when interfaces change"
description: "Understand how Graftcode handles interface changes, how older and newer Grafts coexist, and how developers discover and adapt to changes safely."
keywords: "graftcode interface changes, api evolution, backward compatibility, strongly typed services"
---

Interfaces change.  
They always do.

The real question is not *whether* interfaces will evolve, but **how safely and predictably that evolution happens**—especially when interfaces are consumed by multiple teams and services.

Graftcode is designed so that interface changes are:
- explicit
- visible early
- and safe to adopt incrementally

---

## Public interfaces behave like shared libraries

The most important mental model to keep in mind is this:

> A public interface exposed through Graftcode behaves like a shared library API.

Consumers:
- install it as a dependency
- rely on its types
- discover changes through tooling

This is a very different model from traditional remote APIs, where changes are often discovered only at runtime.

---

## Evolutionary changes are the default

Graftcode encourages **evolutionary changes** rather than breaking ones.

Typical evolutionary changes include:
- adding new methods
- introducing optional parameters
- adding overloads
- extending return types in a compatible way

In these cases:
- existing Grafts continue to work
- existing consumers do not break
- newer consumers gain additional capabilities

No coordination is required.

---

## Breaking changes are explicit

Sometimes breaking changes are unavoidable.

In Graftcode, breaking changes are never silent.

When a public interface changes incompatibly:
- a new version of the Graft is produced
- older Grafts remain available
- consumers must explicitly choose to upgrade

There is no scenario where a consumer suddenly starts calling a different interface without noticing.

---

## What developers see when something changes

Because Grafts are strongly typed dependencies, developers discover changes immediately.

Depending on the change, they may see:
- new methods appearing in autocomplete
- new optional parameters
- compilation errors if required parameters were introduced
- renamed or removed members failing to compile

The IDE becomes the primary feedback mechanism.

There is no need to inspect changelogs or compare schemas.

---

## Automatic updates and CI feedback

Teams often configure their dependencies to allow automatic updates within compatible version ranges.

In this setup:
- CI pipelines pull newer Grafts automatically
- unit and integration tests validate compatibility
- failures are detected early in the pipeline

This shifts the cost of change from production incidents to build-time feedback.

---

## Planned: automatic breaking change detection (roadmap)

One natural extension of the Unified Graft Model is the ability to **compare interface versions structurally**, not just syntactically.

Graftcode is designed so that each exposed module produces a Unified Graft Model (UGM).  
This opens the door to detecting **breaking changes automatically** by comparing successive versions of the same module.

---

### Detecting breaking changes at interface level

By comparing two UGM versions of the same module, it becomes possible to detect changes such as:
- removed public methods
- renamed methods or parameters
- removed or renamed return values
- changes to required parameters
- incompatible type changes

These are the same kinds of breaking changes developers already try to avoid in shared libraries—but detected automatically and consistently.

---

### Warnings at Gateway startup

A planned capability is for the Graftcode Gateway to analyze interface evolution when a module is started.

If a new version of a module introduces breaking changes compared to a previous version, the Gateway could:
- detect the breaking changes automatically
- emit clear warnings at startup
- indicate which methods or signatures are incompatible

This makes breaking changes visible immediately, at the point where they are introduced.

---

### Warnings for incompatible Grafts at runtime

Another planned capability is runtime awareness of incompatibility.

If an **older Graft** communicates with a Gateway hosting a **newer, incompatible interface**, the system could:
- detect that the Graft was generated from an older UGM
- identify which methods are now incompatible
- emit warnings on the caller side

These warnings could indicate:
- which methods are no longer compatible
- that calling them will result in failure
- that the consumer should upgrade its Graft

This shifts discovery of breaking changes from runtime failures to **early, actionable warnings**.

---

### CI/CD enforcement before deployment

Beyond runtime warnings, this mechanism enables tooling for build pipelines.

A planned tool could:
- run during CI/CD for modules intended to be hosted on a Gateway
- compare the new UGM with the previously published version
- fail the build if breaking changes are detected

This would allow teams to:
- enforce interface stability automatically
- catch breaking changes before deployment
- treat public interfaces with the same discipline as shared libraries

Breaking changes would become a deliberate decision, not an accidental outcome.

---

### Why this matters

This approach reinforces the core idea behind Graftcode:

> Remote interfaces should be treated with the same rigor as shared code.

By detecting breaking changes at the interface-model level:
- teams gain earlier feedback
- consumers are protected from surprise failures
- interface evolution becomes intentional and observable

This turns interface stability into an automated property of the system, not a matter of convention.

---

### Roadmap note

These capabilities are part of the planned evolution of the Graftcode tooling and build-time ecosystem.

They build directly on:
- the Unified Graft Model
- strong typing
- explicit public interfaces

and are a natural next step in making distributed systems behave like well-managed codebases.

---

## Older and newer Grafts can coexist

Different consumers can use different Graft versions at the same time.

This allows:
- gradual migration
- independent release cycles
- reduced coordination overhead

As long as older interfaces remain available, existing consumers continue to work unchanged.

---

## Knowing when it is safe to remove old interfaces

Over time, some interfaces become unused.

When Gateways are connected to a project, aggregated usage information can show:
- which Grafts are still in use
- which versions are active
- which interfaces have no remaining consumers

This makes it possible to:
- deprecate interfaces confidently
- remove unused versions safely
- avoid breaking unknown consumers

---

## Versioning through facade classes

A common pattern for managing change is to version **facade classes**.

For example:
- `OrdersV1`
- `OrdersV2`

Each class represents a stable public contract, while internal business logic evolves freely.

Graftcode does not enforce this pattern, but it aligns naturally with the programming model and makes intent explicit.

---

## Relaxed versioning for experimentation

During early development or experimentation, teams may choose relaxed versioning.

In this mode:
- incompatible changes result in uniquely identified Grafts
- conflicts are avoided automatically
- experimentation is unblocked

This is useful when interfaces are still fluid and consumers are few.

---

## Why this model works

This approach works because:
- interfaces are explicit
- changes are visible at development time
- consumers control upgrades
- tooling provides immediate feedback

Distributed systems start behaving like evolving codebases—not brittle integrations.

---

## In short

When interfaces change in Graftcode:
- changes are explicit and versioned
- older consumers continue to work
- newer consumers opt in deliberately
- IDEs and CI pipelines surface issues early

Interface evolution becomes a managed process, not a source of risk.

---

With this, the **How Graftcode works** section is complete.

Next, we’ll move into **Get started**, where we’ll show how to go from zero to a working Graft in minutes.
