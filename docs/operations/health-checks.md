---
title: "Health checks"
description: "Define startup, liveness, and readiness checks without relying on undocumented endpoints."
---

# Health checks

Use different signals for different lifecycle decisions.

## Startup

Wait for Gateway logs to confirm the expected runtime, enabled type surface, listener startup, and
successful publication. A listening socket alone does not prove the Receiver loaded.

## Liveness

At minimum, supervise the Gateway process and selected listener. A process/socket check answers
whether the host is alive, not whether calls are correct.

Gateway also exposes a built-in **`GET /status`** endpoint on its HTTP listener (default port `81`,
available when the HTTP server is enabled). It returns `200 OK` with the body `OK` once the HTTP
server is running, which is a convenient liveness probe:

```bash
curl -f http://<gateway-host>:81/status
```

`/status` confirms the Gateway HTTP server is responsive. It does not prove that a specific Receiver
method executes correctly or that the WebSocket runtime-call listener is ready — use a Receiver
method for readiness (below).

## Readiness

Use a small, side-effect-free Receiver method through an installed Graft from the same network path as
real Callers. It should verify only dependencies required to accept traffic and must have a bounded
timeout.

Do not use Graftcode Vision availability alone as Receiver readiness: Vision runs on its own HTTP
listener.

## Removal from service

After readiness fails, stop new traffic before terminating the instance. Stateful sessions cannot be
moved transparently; a restart may invalidate remote object identity.

**Note:** Gateway provides `GET /status` for liveness but no dedicated `/ready` or `/live` routes.
Use `/status` (or a process/socket check) for liveness and an explicit Receiver method for readiness.
Do not invent other routes.

## Next steps

- [Gateway lifecycle](gateway-lifecycle.md)
- [Timeouts and retries](timeouts-retries.md)
- [Logging, metrics, and tracing](observability.md)
