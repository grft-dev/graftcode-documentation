---
title: "Graftcode Vision"
description: "Graftcode Vision is a runtime-based interface explorer that helps developers discover what a service exposes, how to connect to it, and how to consume it as a typed dependency."
keywords: "graftcode vision, service discovery, live api documentation, package manager integration, runtime interfaces"
---

**Graftcode Vision** is a developer tool designed to make it easy to understand **what a service exposes, how to connect to it, and how to consume it**.

Its primary goal is not documentation for documentation’s sake, but **reducing the distance between discovering a service and using it in code**.

In that sense, Vision plays a role similar to tools like Swagger or Postman—but instead of focusing on endpoints and payloads, it focuses on **public programming interfaces and typed clients**.

---

## Discovering what a service exposes

When you open Graftcode Vision for a running service, you are looking directly at the service **that is hosting the code**.

Vision shows:
- public classes exposed by the service
- available methods
- arguments and return types
- overloads and optional parameters

This information is derived from the service’s runtime via the **Unified Graft Model (UGM)**.

There is no separate specification, no generated documentation, and no sync step.  
What Vision shows is what the service actually exposes at that moment.

---

## Always reflecting the current interface

Vision stays up to date because it operates against the running Graftcode Gateway.

If the service changes:
- new methods appear immediately
- removed methods disappear
- signature changes are reflected instantly

This works for the same reason shared libraries stay up to date in an IDE:  
the information comes directly from code, not from an external description.

---

## The first thing most developers do: copy the package manager command

For most developers, the most important part of Graftcode Vision is not browsing methods.

It is this:

> **How do I get a client for this service into my project?**

Vision makes this trivial.

For every exposed service, Vision provides:
- the exact package manager command
- for the selected technology (npm, NuGet, Maven, PyPI, etc.)
- pointing at the correct Graftcode Gateway

It does not matter whether the service exposes:
- one method
- or thousands of methods

A developer can simply copy the command, install the dependency, and immediately start working with a strongly typed client in their IDE.

---

## Configuration examples, ready to copy

Vision also shows how to configure the client to connect to a specific Gateway instance.

Depending on the selected technology, Vision provides:
- example configuration via environment variables
- example configuration via config files
- minimal, working defaults

This allows a developer to:
- connect directly to a specific service instance
- verify behavior quickly
- and later let DevOps override the configuration for other environments

The important part is that **the first working configuration is easy to get**, and changes can be layered on later.

---

## Language-specific code examples

Vision adapts to the selected consumer technology.

When you switch the target to:
- JavaScript
- .NET
- Java
- Python
- or another supported runtime

Vision updates:
- package manager commands
- configuration examples
- import statements
- and code samples

When using the “try it” feature, the code shown is generated **in the selected language**, using the same parameters and values entered during execution.

This code can be copied directly into an application and used as-is.

---

## Interactive execution, similar to Swagger or Postman

Vision allows methods to be executed interactively against the running service.

This is similar in spirit to Swagger’s “Try it out” or Postman requests:
- you provide input values
- you execute the method
- you inspect the result or error

The difference is that you are invoking **methods**, not endpoints.

Execution happens against the same runtime that real clients use, and the result reflects the actual behavior of the service.

---

## No additional exposure or bypass

Graftcode Vision does not introduce a new access path.

It does not:
- bypass security
- expose additional methods
- create special execution routes

Vision operates within the same boundaries enforced by the Graftcode Gateway.

If something is callable through a Graft, it is callable through Vision.  
If it is not, Vision cannot access it either.

---

## Vision today and Vision tomorrow

Today, Graftcode Vision runs alongside individual Gateways and shows what each service exposes locally.

In the future, Vision will also be available at the platform level, allowing teams to:
- browse all registered services
- explore Unified Graft Models across projects
- view a live, global picture of their interface architecture

This creates a form of **always up-to-date, system-wide documentation**, derived from running services rather than maintained manually.

---

## Built on the same runtime foundations

Graftcode Vision understands:
- the Unified Graft Model (UGM)
- the Intention Invocation Protocol (IIP)

It is built on the same foundations as:
- Graft generation
- runtime execution
- cross-language communication

Vision is not a special case—it is simply one consumer of the same runtime-level information.

---

## In short

Graftcode Vision is:
- a discovery tool for exposed services
- a shortcut to installing typed clients
- a source of copy-ready configuration and code
- a live view of what a service actually exposes

It helps developers move from *“what is this service?”* to *“I’m already using it”* in minutes.

---

With this, the **Core Concepts** section is complete.

Next, we’ll move into **How Graftcode works**, starting with the difference between **development-time and production-time behavior**.
