---
title: "How Grafts are generated"
description: "Learn how Graftcode generates strongly typed Grafts on demand when a package manager requests them, using live interface metadata instead of prebuilt clients."
keywords: "graft generation, on-demand clients, package manager integration, unified graft model, strongly typed services"
---

# How Grafts are generated

A common assumption when first encountering Graftcode is that Grafts are prebuilt packages published to registries.

They are not.

Grafts are generated **on demand**, at the moment a package manager asks for them, and only for the specific technology and version that is requested.

This section explains how that process works step by step.

---

## The starting point: a running Gateway

Everything begins with a running **Graftcode Gateway**.

When the Gateway starts, it:
- loads the configured runtimes
- loads the specified modules
- analyzes their public interfaces
- builds a **Unified Graft Model (UGM)**

The UGM is a language-agnostic description of what the service exposes:
- public classes
- public methods
- method signatures
- argument and return types

This model is the foundation for Graft generation.

---

## Registering interface metadata

Once the Unified Graft Model is built, the Gateway sends **only this metadata** to the Graftcode cloud.

At this point:
- no clients exist yet
- no code is generated
- nothing is published to registries

The cloud simply holds enough information to generate clients **when requested**.

---

## A package manager makes a request

Graft generation begins when a developer runs a package manager command, such as:

- `npm install`
- `dotnet add package`
- `pip install`
- `mvn dependency:get`

The request is routed to the Graftcode registry endpoint.

Crucially, this happens using standard package manager workflows—no custom tooling is required.

---

## Generating the Graft on demand

When the request arrives:
1. The Graftcode engine identifies the requested service, version, and target technology.
2. The corresponding Unified Graft Model is loaded.
3. A strongly typed client is generated **specifically for that technology**.
4. The generated client is packaged in the native format expected by the package manager.
5. The package is returned as the response to the request.

Generation happens only once per unique combination of:
- service
- interface version
- target language

---

## Caching and repeatability

After a Graft is generated:
- it is cached
- subsequent requests for the same combination are served from cache
- no regeneration is required

This ensures:
- consistent results
- predictable behavior
- fast package installation

Caching is an implementation detail and does not change the programming model.

---

## Grafts in CI/CD pipelines

Grafts are consumed through standard package managers, which means they fit naturally not only into developer workflows, but also into **CI/CD pipelines**.

A Graft can be:
- installed locally by a developer
- restored automatically during a build
- updated as part of a continuous integration process

There is no distinction between “manual” and “automated” usage—the same mechanisms apply in both cases.

---

## Automatic updates through version ranges

Because Grafts are versioned like normal dependencies, teams can use version ranges instead of fixed versions.

For example:
- a dependency can be declared as “greater than or equal to version X”
- or constrained to a compatible major version

This allows a pipeline to:
- automatically pull the newest available Graft
- reflect the latest public interface
- detect incompatibilities early

When a new interface version is published, the next build can pick it up automatically.

---

## Validation through tests, not coordination

In this model, compatibility is validated by **tests**, not by manual coordination.

A typical flow looks like this:
1. A new version of a public interface is exposed.
2. A new Graft version becomes available.
3. CI/CD pipelines update dependencies automatically.
4. Unit and integration tests run.
5. The build confirms whether everything still works.

If the build passes, the system moves forward.  
If it fails, the incompatibility is detected immediately—before deployment.

This shifts responsibility from communication to automation.

---

## Safe by default

This approach works best when interfaces evolve in an evolutionary way:
- new methods are added
- optional parameters are introduced
- existing behavior remains compatible

In these cases:
- older consumers continue to work
- newer consumers gain additional capabilities
- automated upgrades remain safe

Breaking changes are still possible, but they become explicit decisions rather than accidental side effects.

---

## One workflow for developers and pipelines

Because Grafts are standard dependencies:
- developers and pipelines use the same tools
- no special CI configuration is required
- no custom generators or scripts are needed

What works locally works in CI.  
What works in CI works in production.

---

## Why this matters

This model enables:
- faster feedback loops
- earlier detection of breaking changes
- safer interface evolution
- less cross-team coordination

Distributed systems start behaving more like well-managed codebases, where change is verified by builds—not negotiated by meetings.

---

## What a generated Graft contains

A Graft is not a stub and not a proxy.

It contains:
- strongly typed representations of public interfaces
- runtime bindings to Hypertube
- configuration hooks for selecting execution targets
- error and exception mappings

What it does **not** contain:
- business logic
- serialized payloads
- network protocols exposed to the developer

From the developer’s point of view, it behaves like a normal library.

---

## Versioning and interface evolution

Grafts are versioned according to the exposed public interface.

When an interface evolves:
- existing versions remain available
- new versions generate new Grafts
- consumers choose when to upgrade

As long as interfaces evolve in a compatible way:
- older Grafts continue to work
- newer Grafts unlock additional capabilities

This mirrors how shared libraries evolve over time.

---

## No manual client regeneration

Because Grafts are generated on demand:
- there is no client build step
- no code generation pipeline to maintain
- no artifacts to publish manually

Developers do not need to:
- re-run generators
- commit generated code
- coordinate updates across teams

The package manager becomes the synchronization mechanism.

---

## Why this matters

This model:
- eliminates client drift
- keeps interfaces and clients aligned
- reduces coordination overhead
- improves developer productivity

It also makes distributed systems easier to reason about, because consuming a remote service feels the same as consuming a local dependency.

---

## In short

Grafts are:
- generated on demand
- built from live interface metadata
- tailored to specific languages
- delivered through standard package managers
- cached for consistency and performance

They bring the shared-module workflow to distributed systems—without the manual effort.

---

Next, we’ll look at **how versioning and evolutionary changes work in practice**, and how Graftcode helps teams evolve interfaces safely.
