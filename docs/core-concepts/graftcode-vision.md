---
title: "Graftcode Vision"
description: "What Graftcode Vision shows in the current release and how to use it as the source for install and configuration details."
---

# Graftcode Vision

**Graftcode Vision** is the developer-facing web UI that Gateway hosts for inspecting the callable
surface of the loaded modules and obtaining the information you need to install and configure a Graft.

- Vision hosting is enabled by the Gateway `--GV` option, on by default.
- The Vision HTTP port defaults to `81` and can be changed with `--httpPort`.
- Vision reflects the callable surface of the modules loaded by that Gateway process.

## Available now

For the modules loaded by the running Gateway, Vision provides:

- callable-surface browsing (modules, types, and methods);
- package coordinates for the generated Graft;
- the installation command;
- configuration information (for example the runtime host to set);
- version information.

## Not currently available

- interactive method execution from the UI;
- a guarantee that every runtime or package ecosystem is represented identically;
- readiness, metrics, or health dashboards (use `GET /status` for liveness — see
  [Health checks](../operations/health-checks.md)).

## Use the running Gateway as the source

Vision is the source for install and configuration details **for the Gateway process it belongs to**.
Module selection, runtime detection, filters, and startup success determine what a Gateway actually
hosts, so copy package names, versions, ports, registry paths, and the runtime host from Vision (or the
Gateway output) for that process rather than inferring them or reusing values from another environment.
