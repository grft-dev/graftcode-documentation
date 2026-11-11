---
title: "Networking and ports"
description: "Expose only the Gateway listeners required by the selected transports."
---

# Networking and ports

Gateway defaults to WebSocket port `80` and a second HTTP listener on `81` (`--httpPort`). Graftcode Vision is reachable in **both** places when `--GV` is on: the process listening on `--port` also serves normal HTTP for `/GV`, `/mcp`, `GET /status`, and related routes (so `http://localhost:<websocket-port>/GV` works). The `--httpPort` listener is an additional HTTP stack (default `81`) for the same UI and `/status` — not the only way to load Vision. TCP port `82` and HTTP/2 port `83` are disabled unless `--tcpServer` or `--http2Server` is enabled.

## Deployment checklist

1. Bind explicit ports in production.
2. Expose only the selected runtime listener and operationally required Vision access.
3. Restrict Vision to trusted networks unless public access is intended and reviewed.
4. Use a WebSocket-capable proxy for `ws://`/`wss://`; preserve upgrade headers and suitable idle
   timeouts.
5. Terminate TLS at reviewed Gateway-capable infrastructure. Gateway does not provide native
   certificate configuration.
6. Keep stateful connections pinned to the same Gateway instance.
7. Configure CORS only for browser-facing HTTP surfaces. `--corsConfig` values can override CLI
   origin defaults during startup.

The generated local WebSocket host is typically copied from Vision and includes the `/ws` path. Do
not invent TCP or HTTP/2 connection strings; use generated configuration for the selected runtime.

Graftcode does not ship a canonical Kubernetes Service/Ingress, reverse-proxy recipe, native TLS flag,
or universal idle-timeout value. Validate upgrades, frame sizes, and long-lived connections through
your actual proxy.

## Next steps

- [Ports and protocols reference](../reference/ports-and-protocols-reference.md)
- [Health checks](health-checks.md)
- [Scaling](scaling-gateway-receivers.md)
