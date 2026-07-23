---
title: "Ports and protocols reference"
description: "Gateway listener defaults, enabling flags, and deployment caveats."
---

# Ports and protocols reference

| Default port | Surface | Enabled by default | Configuration |
| --- | --- | --- | --- |
| `80` | WebSocket runtime calls | Yes | `--port` |
| `81` | HTTP server for Graftcode Vision | Yes (`--GV`) | `--httpPort` |
| `82` | TCP runtime calls | No | `--tcpServer --tcpPort <port>` |
| `83` | HTTP/2 runtime calls | No | `--http2Server --http2Port <port>` |

For generated WebSocket clients, copy the full `ws://` or `wss://` host, including path, from Vision.
The local route is `/ws`; do not extrapolate routes for other transports.

## Transport support

![The same business code can run over in-memory, WebSocket, TCP, or HTTP/2 transports by changing only the runtime host, with message-queue and broker transports available through plugins](../../assets/diagrams/transport-selection-matrix.png)

"Transport agnostic" means business code is decoupled from a selected transport, not that every
transport has identical semantics. Choose the runtime host accordingly (see
[Execution modes](../core-concepts/in-memory-same-machine-and-remote-execution.md)).

| Transport | How to select | Status |
| --- | --- | --- |
| In-memory | `host = inmemory` | Available (built-in) |
| WebSocket (`ws://`, `wss://`) | `ws://host/ws` or `wss://host/ws` | Available (built-in, default) |
| TCP | `tcp://host:port` (or `host:port`); enable `--tcpServer` | Available (built-in, opt-in) |
| HTTP/2 | HTTP(S) host ending in `h2`; enable `--http2Server` | Available (built-in, opt-in) |
| Message queue / broker (Kafka, RabbitMQ, NATS, SQS, service bus) | Server plugin via `--config` | Preview / plugin-based; availability depends on the specific plugin |

Only in-memory, WebSocket, TCP, and HTTP/2 are built-in. Any queue or broker transport requires a
transport plugin; do not assume a broker is supported because it appears in a diagram or design. WSS
and HTTP/2 do not have identical failure or header semantics — see
[Authentication and authorization](../operations/authentication-and-authorization-operations.md) for the browser
header constraint.

Gateway defaults may require elevated privileges or conflict with another web server. Change ports or
container host mappings as needed. Open only selected listeners through firewalls and security groups.

TLS/WSS termination is infrastructure-specific. Gateway does not provide native certificate flags.
Browser WebSockets cannot attach arbitrary custom handshake headers; when headers are required, use
only the HTTP/2 endpoint/configuration emitted by Vision.

CORS affects browser HTTP surfaces and is configured with `--corsAllowedOrigins` or `--corsConfig`;
it is not a substitute for authentication.

The HTTP listener also serves a built-in `GET /status` liveness endpoint (returns `200 OK`). No
dedicated metrics port, MCP route table, maximum message size, idle timeout, or proxy configuration
is provided.

## Next steps

- [Networking and ports](../operations/networking-and-ports.md)
- [Gateway CLI](gateway-cli-reference.md)
