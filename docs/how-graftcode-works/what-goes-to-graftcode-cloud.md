---
title: "What goes to the Graftcode cloud?"
description: "Understand exactly what information is sent to the Graftcode cloud, what never leaves your environment, and how Graftcode enforces clear security and network boundaries."
keywords: "graftcode cloud, security model, interface metadata, distributed systems security, runtime boundaries"
---


One of the most important questions teams ask when evaluating Graftcode is simple and reasonable:

> **What data leaves my environment?**

Graftcode is designed so that this question has a clear, precise, and verifiable answer.

The short version is:
- **interface metadata goes to the cloud**
- **execution and runtime data NEVER DO**

This section explains exactly what that means in practice.

---

## The role of the cloud in Graftcode

The Graftcode cloud exists to support **development-time workflows**.

Its responsibilities are limited to:
- enabling on-demand Graft generation
- supporting package manager requests
- providing project-level visibility and dashboards (when enabled)

The cloud is not involved in production execution.

Understanding this separation is key to understanding the security model.

---

## What is sent to the cloud

When a **Graftcode Gateway** starts in project-bound mode, it analyzes the modules it hosts and builds a **Unified Graft Model (UGM)**.

Only the following information is sent to the Graftcode cloud:

- public class names
- public method names
- method signatures
- argument and return types
- structural information required to generate typed clients

This information describes **what can be called**, not **how it is implemented**.

---

## What is explicitly not sent

The Graftcode Gateway does **not** send:

- business logic
- source code
- compiled binaries
- runtime data
- method arguments
- return values
- exceptions thrown during execution
- configuration secrets
- environment variables

At no point does production traffic or execution data leave your environment.

---

## No production execution in the cloud

Once a Graft is generated:
- calls go directly from caller to receiver
- execution happens through Hypertube
- communication stays within your network

The Graftcode cloud:
- does not forward calls
- does not observe payloads
- does not participate in execution
- does not sit in the data path

From a runtime perspective, production systems do not depend on the cloud.

---

## Package manager requests and client generation

When a package manager requests a Graft:
- the request reaches the Graftcode engine
- the Unified Graft Model is used to generate a client
- the generated package is returned to the requester
- the result is cached for efficiency

The cloud sees:
- which interface was requested
- which language and version were requested

It does not see:
- how the client will be used
- where it will be deployed
- what data it will process

---

## Metrics and dashboards (optional)

When a Graftcode Gateway is linked to a project, it may optionally report:
- high-level usage metrics
- interface-level activity counts
- version adoption information

These metrics are:
- aggregated
- non-payload
- configurable

They exist to help teams understand:
- which interfaces are used
- which versions are still active
- where deprecations are safe

All detailed logging and observability remains local and under your control.

---

## Security boundaries and network control

From a network perspective:
- all production execution stays inside your network
- all communication uses standard transports
- existing firewalls, proxies, and load balancers apply unchanged

There are no hidden connections or backchannels.

If your infrastructure can enforce network boundaries today, it can enforce them with Graftcode.

---

## Verifiability and transparency

The Graftcode Gateway is intended to be **source-available**, allowing teams to:
- inspect exactly what it does
- verify what data it sends
- perform independent security analysis and penetration testing

This design ensures that security does not rely on trust alone, but on inspectable behavior.

---

## Why this model exists

Graftcode separates concerns deliberately:

- **interfaces** are shared
- **execution** remains local
- **control** stays with the user

This allows teams to benefit from:
- strongly typed integration
- on-demand client generation
- runtime-level execution

Without surrendering control over their systems or data.

---

## In short

The Graftcode cloud:
- receives only interface metadata
- enables client generation and discovery
- is not part of production execution

Your code:
- runs in your environment
- communicates directly
- remains under your control

This clear boundary is foundational to the Graftcode security model.

---

Next, we’ll look at **how Grafts are generated on demand**, and what happens when a package manager requests a client.
