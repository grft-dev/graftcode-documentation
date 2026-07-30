---
title: "Gateway lifecycle"
description: "Start, supervise, replace, and stop Gateway safely."
---

# Gateway lifecycle

## Start

Build the Receiver first, then start Gateway with explicit module and runtime values. Startup includes
runtime selection, module loading, callable-surface analysis, listener startup, and callable-surface
publication. Do not advertise install commands until discovery and publication succeed.

A successful startup reports the Gateway version, the detected runtime, the loaded module, the exposed
types, the runtime listener, the Vision URL, and the publication result. Representative output (values
are environment-specific — copy the real coordinates from your own Gateway or Vision):

```text
Graftcode Gateway (gg) 1.3.8
Runtime detected: .NET 9.0
Loading module: Pricing.dll
Type enabled: Pricing.PriceService
  method: Calculate
Listening: ws://0.0.0.0:80/ws
Liveness:  http://0.0.0.0:81/status
Vision:    http://0.0.0.0:81/GV
Publishing callable surface... done
Install command available in Vision
```

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

Gateway does not provide a dedicated drain, reload, readiness, or graceful-shutdown command, nor a
guaranteed response to each operating-system signal. Test termination behavior for the exact Gateway
release and Receiver runtime.

## Next steps

- [Health checks](health-checks.md)
- [Scaling](scaling-gateway-receivers.md)
- [Version compatibility and upgrades](version-compatibility-and-upgrades.md)
