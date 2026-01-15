---
title: "Graftcode Gateway"
description: "Graftcode Gateway is a lightweight native runtime host that loads application runtimes, exposes public interfaces, and executes strongly typed calls through Hypertube without acting as a proxy or API gateway."
keywords: "graftcode gateway, runtime host, hypertube, distributed systems runtime, integration architecture"
---


The **Graftcode Gateway** is a lightweight, native runtime host that loads application runtimes, exposes public interfaces, and executes strongly typed calls.

It is the entry point into the Graftcode ecosystem—but it is not a proxy, not an API gateway, and not a middleware layer that intercepts production traffic.

The Gateway exists to host code and connect runtimes, not to sit between them.

---

## A native, dependency-free runtime host

Graftcode Gateway is a **native application** available for:
- Windows
- Linux
- macOS

It has **no external dependencies**.

You can run it:
- as a single executable
- without installing frameworks
- without configuring additional services

The Gateway can be obtained in several ways:
- downloaded directly from GitHub releases (https://github.com/grft-dev/graftcode-gateway/releases/)
- generated through the Graftcode portal wizard for a selected platform
- installed via system package managers (such as Chocolatey or APT)
- pulled as a ready-to-run Docker image

The goal is simple: if you can run a process, you can run a Graftcode Gateway.

---

## Hosting runtimes, not forwarding traffic

When the Graftcode Gateway starts, it does not forward requests or proxy traffic.

Instead, it **loads and hosts application runtimes**.

Much like a native executable can load the CLR, which then loads your .NET application, the Graftcode Gateway can load:
- the CLR
- the JVM
- Python runtimes
- and other supported runtimes

One or multiple runtimes can be loaded at the same time.

Within those runtimes, the Gateway loads the modules you specify. These modules contain your actual business logic.

At this point, the Gateway is no longer just a launcher—it becomes a runtime host.

---

## Discovering public interfaces

Once modules are loaded, the Gateway analyzes them to discover **public interfaces**:
- public classes
- public methods
- method signatures
- argument and return types

From this analysis, the Gateway builds a **Unified Graft Model (UGM)**—a language-agnostic representation of what can be called.

This model describes *intent*, not implementation.

Only this unified interface model is sent to the Graftcode cloud.

No business logic, no implementation code, and no runtime data ever leave your environment.

---

## On-demand Graft generation

The Unified Graft Model is used when a package manager requests a Graft.

At that moment:
1. The request reaches the Graftcode engine.
2. The Unified Graft Model is used to generate a strongly typed client for the requested technology.
3. The generated package is returned to the package manager.
4. The result is cached for subsequent requests.

Grafts are **generated on demand**.

They are not pre-published, not pre-generated, and not created for technologies that nobody uses.

The Gateway itself does not generate Grafts—it provides the model that makes generation possible.

---

## Built-in Hypertube runtime

The Graftcode Gateway contains an embedded **Hypertube™** runtime.

Hypertube is responsible for executing calls between runtimes:
- in memory
- or over the network using TCP/IP or WebSocket

Hypertube is directly linked into the Gateway and can:
- load runtimes
- execute code inside them
- route calls between them efficiently

This applies equally to:
- in-process execution
- cross-process execution
- cross-machine execution

The Gateway delegates execution to Hypertube.

---

## Intention Invocation Protocol (IIP)

Communication between runtimes is performed using a binary message format called the  
**Intention Invocation Protocol (IIP)**.

IIP is designed to represent **programming intent**, not network messages.

An IIP message can describe:
- a single method call
- a chain of nested operations
- complex execution flows, similar to lambda expressions

The same protocol is used:
- for in-memory execution
- for local inter-process communication
- for remote network communication

This consistency is what allows Graftcode to virtualize execution without changing code.

---

## Full-duplex execution model

Hypertube connections are **full duplex**.

Once a session is established:
- calls can flow in both directions
- events can be emitted back to the caller
- callbacks and delegates can be invoked remotely

If a caller subscribes to an event or provides a callback:
- the receiver can invoke it
- the invocation travels back through the same session
- execution remains strongly typed

This enables interaction patterns similar to in-memory objects or real-time systems, without explicit connection management in application code.

---

## Hosting multiple modules and technologies

A single Graftcode Gateway can host:
- multiple modules
- written in the same technology
- or mixed across technologies

For example:
- several .NET modules
- a combination of .NET and Python modules
- or any other supported mix

Each module contributes to the Unified Graft Model, and all are reachable through the same runtime infrastructure.

---

## Performance characteristics

The Gateway itself is extremely lightweight.

Execution overhead is minimal because:
- calls are binary, not text-based
- there is no serialization into JSON or Protobuf
- no MVC pipelines or middleware stacks are involved

In-memory calls have **near-zero overhead** and behave like native calls.

Remote calls add only network latency.

This is why Graftcode-based communication is significantly faster and more resource-efficient than REST or gRPC-based approaches.

---

## Graftcode Vision and IIP tooling

The **Graftcode Gateway** also hosts **Graftcode Vision**.

Graftcode Vision is a tool that understands:
- the Unified Graft Model
- the Intention Invocation Protocol

It uses this knowledge to:
- visualize exposed interfaces
- provide live documentation
- allow interactive “try it” execution of methods

Graftcode Vision is an example of what can be built on top of IIP.

The Intention Invocation Protocol and the Unified Graft Model are designed to be **open and extensible**, allowing third-party tools for:
- monitoring
- debugging
- inspection
- documentation

Over time, more tools can integrate directly at this level.

---

## Source-available and security transparency

The Graftcode Gateway is designed to be a security-critical boundary component, and it is treated as such.

For this reason, the Gateway is expected to be made **source-available** on GitHub.

This means:
- the full source code of the Gateway can be inspected
- security teams can perform static analysis
- organizations can run independent penetration tests
- behavior can be audited rather than assumed

While the Gateway itself is a native binary distributed for convenience, its implementation is intended to be transparent and reviewable.

This approach allows teams to:
- verify exactly what the Gateway does
- understand how interfaces are analyzed
- confirm what data is (and is not) sent outside their environment

Security should not rely on trust alone.  
It should be verifiable.

Making the Graftcode Gateway source-available ensures that organizations can evaluate it using the same standards they apply to other critical infrastructure components.

---

## In short

The Graftcode Gateway is:
- a native, dependency-free runtime host
- a loader of application runtimes
- a producer of unified interface models
- an execution entry point powered by Hypertube

It is not:
- a proxy
- an API gateway
- a traffic interceptor
- a cloud-controlled component

It exists to run code, connect runtimes, and make distributed execution feel local.

---

Next, we’ll look at **Hypertube™**, the runtime bridge that makes this execution model possible.
