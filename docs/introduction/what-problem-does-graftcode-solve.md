---
title: "How Graftcode works"
description: "The How it works diagram, component roles, and the core mental model."
---

# How Graftcode works

Graftcode connects a **Caller** to a **Receiver** through a generated **Graft** and **Hypertube**.
You write service business logic on both sides; Graftcode analyzes the **public interface**,
generates the Graft, and routes runtime calls through **Gateway**.

![How it works: Caller service business logic and Graft connect through Hypertube to Gateway and Receiver service business logic; Graftcode Engine reads each public interface to generate the Graft](../../assets/diagrams/how-it-works-diagram.png)

## The diagram, left to right

**Caller** — Your application. **Service business logic** runs here.

**Graft** — The generated package the Caller installs and imports (`npm install @graft/...` — copy
the command from **Vision**). See [What is a Graft?](../core-concepts/what-is-a-graft.md).

**Hypertube** — The runtime bridge inside the Graft. It carries each invocation to **Gateway** (or
runs in-memory when configured). See [Hypertube runtime bridge](../core-concepts/hypertube-runtime-bridge.md).

**Gateway** — Hosts the Receiver module and receives remote calls. Install and run `gg` — see
[Gateway and hosted modules](../core-concepts/graftcode-gateway.md).

**Receiver** — The module Gateway hosts. **Service business logic** runs here.

**Vision** — Gateway UI for discovery, install commands, and configuration snippets (for Dev and AI
workflows). See [Graftcode Vision](../core-concepts/graftcode-vision.md).

**Graftcode Engine** and **public interface** — Setup-time path only. Gateway captures each side's
public interface; the Engine [generates](../core-concepts/package-generation.md) the installable
Graft. Normal calls use the installed Graft and Hypertube — they do not regenerate the package.

**Runtime flow:** `Caller → Graft → Hypertube → Gateway → Receiver → result`

## Five things to remember

![The five-step Graftcode mental model: your module, the generated Graft, Gateway hosting and analysis, configuration selecting execution, and a still-distributed call](../../assets/diagrams/graftcode-mental-model.svg)

1. **The module is your code.** A Receiver is an ordinary class library or module. Its intentional,
   supported public methods form the [callable surface](../core-concepts/callable-surface.md).
2. **The Graft is generated code.** It is a package for the Caller's package manager and language.
   It mirrors the Receiver surface; it is not the Receiver implementation.
3. **Gateway hosts and analyzes modules.** It loads the Receiver, exposes runtime transports, serves
   Vision, and publishes the model used to generate packages. Install `gg` from
   [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases) or
   [build a container image](../how-to-guides/deploy-with-docker.md).
4. **Configuration selects execution.** A generated client can resolve in-memory or remote
   execution. Remote calls must [configure the Gateway host](../how-to-guides/configure-invocation.md)
   before the first invocation.
5. **A method call is still distributed.** Serialization, routing, failures, compatibility,
   security, retries, and observability still matter.

![Setup happens once — analyze the Receiver, discover its public surface, generate a Graft, and install it; at runtime each Caller call is invoked on the Receiver and a result or error returns](../../assets/diagrams/mental-model-procedure.svg)

## Build time versus call time

During setup, Gateway analyzes the Receiver and the package system generates a language-specific
Graft. During normal runtime invocation, the already-installed Graft sends the call through its
resolved execution path. It does not regenerate the package.

## The contract

The contract is the supported public surface: declaring types, methods, parameters, return values,
and public model members. Public does not automatically mean portable. The whole path—Graftcode
Engine generation and runtime execution—must support every exposed type.

Keep transport, database, framework, and implementation types private or internal. For the safest
cross-language surface, use simple primitives, strings, and plain models, then test the exact
Receiver/Caller pair.

## A useful distinction

- **Written:** Receiver logic, Caller logic, runtime configuration, operational policy.
- **Generated:** Graft package, language bindings, contract metadata, Vision views.
- **Operated:** Gateway process, transports, package access, deployment, security, telemetry.

That distinction prevents two common mistakes: treating Gateway as the generated client, or treating
the generated client as if it removes remote-system failure modes.

## Continue

- [Quick start](https://docs.graftcode.com/quick-start) — hands-on tutorials for your stack.
- [What is Graftcode?](what-is-graftcode.md) — definition, REST vs Graftcode example, and use cases.
- [Caller and receiver](../core-concepts/caller-and-receiver.md)
- [Invocation lifecycle](../core-concepts/invocation-lifecycle.md)
- [Choose a scenario](when-to-use-graftcode.md)
