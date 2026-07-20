---
title: "Static and instance context"
description: "How analyzers and generators distinguish type-level calls from object-bound calls."
---

# Static and instance context

The UGM and code generators distinguish **static** operations from **instance** operations.

## Static operations

A static method belongs to the type. The .NET analyzer records it as `STATIC_METHOD`; the Node.js analyzer has a corresponding static-method handler. Generated wrappers invoke it without first constructing an object.

Static does not automatically mean stateless. A static implementation can still read or mutate process state. `stateless` is also a separate configuration value in generated `GraftConfig`.

## Instance operations

Public constructors are represented separately, and instance methods are represented as `INSTANCE_METHOD`. Generated instance wrappers retain runtime object context used by subsequent operations.

This distinction is visible in analyzer nodes and generated static/instance invocation handlers.

## Lifetime and routing caveat

The inspected generator tests establish that constructors and instance operations are generated and carry context. They do not establish a universal object-lifetime guarantee across Gateway restarts, reconnects, retries, all transports, or all language pairs.

Treat an instance Graft as bound to runtime context. Do not persist it as a durable identifier unless a specific runtime and version documents and tests that behavior.

## Choosing a shape

- Prefer static methods when the operation naturally depends only on supplied inputs and shared services.
- Prefer instances when constructor inputs and a sequence of operations are part of the domain model.
- Keep durable identity in explicit domain IDs when it must survive process or connection lifetime.

See [Contract evolution](contract-evolution.md) before changing between static and instance forms; it changes generated consumer code.
