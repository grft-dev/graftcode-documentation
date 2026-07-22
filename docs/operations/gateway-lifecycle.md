---
title: "Gateway lifecycle"
description: "Start, supervise, replace, and stop Gateway safely."
---

# Gateway lifecycle

## Start

Build the Receiver first, then start Gateway with explicit module and runtime values. Startup includes
runtime selection, module loading, callable-surface analysis, listener startup, and model
publication. Do not advertise install commands until discovery and publication succeed.

## Run

Use a service manager or container orchestrator to supervise the process. Capture standard output and
standard error. Keep Receiver dependencies available for the full process lifetime.

## Replace or restart

A restart can invalidate stateful remote object identity. Drain traffic before replacement, preserve
session affinity while connections exist, and prefer static stateless methods for rolling updates.
A free, non-project-backed Gateway can emit a new registry identifier after restart; use a portal
project key when stable publication identity is required.

## Stop

Use the platform's normal termination signal and allow active calls to finish where the platform
supports a grace period. Force termination only after that period.

**Gap:** the Gateway README does not document a dedicated drain, reload, readiness, or graceful
shutdown command, nor a guaranteed response to each operating-system signal. Test termination
behavior for the exact Gateway release and Receiver runtime.

## Next steps

- [Health checks](health-checks.md)
- [Scaling](scaling.md)
- [Version compatibility and upgrades](version-compatibility-upgrades.md)
