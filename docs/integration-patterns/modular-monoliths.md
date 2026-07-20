---
title: "Modular monoliths"
description: "A bounded pattern for using generated Grafts within one deployment."
keywords: "modular monolith, graftcode architecture, in-memory execution"
---

# Modular monoliths

A practical starting point is a module with one deliberate callable facade, private implementation types, and a consumer that installs its generated package. Configure and smoke-test the package in its intended in-memory mode.

This can provide a code-derived boundary, but it does not by itself enforce domain ownership or guarantee that later extraction is configuration-only. Before moving the module out of process:

1. confirm the implementation module is available in the original in-memory deployment;
2. preserve or version the callable surface;
3. configure the remote host before the generated package initializes;
4. add authentication and network policy;
5. define timeout, retry, and idempotency behavior;
6. run compatibility and remote failure tests.

Same-process and remote execution have different operational semantics. Cross-runtime in-process support is also runtime-pair specific.

See [Execution modes](../core-concepts/execution-modes.md), [Configuration resolution](../core-concepts/configuration-resolution.md), and [Contract evolution](../core-concepts/contract-evolution.md).
