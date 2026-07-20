---
title: "Health checks"
description: "Define startup, liveness, and readiness checks without relying on undocumented endpoints."
---

# Health checks

Use different signals for different lifecycle decisions.

## Startup

Wait for Gateway logs to confirm the expected runtime, enabled type surface, listener startup, and
successful publication. A listening socket alone does not prove the provider loaded.

## Liveness

At minimum, supervise the Gateway process and selected listener. A process/socket check answers
whether the host is alive, not whether calls are correct.

## Readiness

Use a small, side-effect-free provider method through an installed Graft from the same network path as
real consumers. It should verify only dependencies required to accept traffic and must have a bounded
timeout.

Do not use Graftcode Vision availability alone as provider readiness: Vision runs on its own HTTP
listener.

## Removal from service

After readiness fails, stop new traffic before terminating the instance. Stateful sessions cannot be
moved transparently; a restart may invalidate remote object identity.

**Gap:** no stable built-in `/health`, `/ready`, or `/live` endpoint is documented in the inspected
Gateway README. Do not publish an invented route. Platform probes must use process/socket checks or an
explicit provider method until a release documents a native endpoint.

## Next steps

- [Gateway lifecycle](gateway-lifecycle.md)
- [Timeouts and retries](timeouts-retries.md)
- [Logging, metrics, and tracing](observability.md)
