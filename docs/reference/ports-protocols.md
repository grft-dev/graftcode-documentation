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
The verified local route is `/ws`; do not extrapolate routes for other transports.

Gateway defaults may require elevated privileges or conflict with another web server. Change ports or
container host mappings as needed. Open only selected listeners through firewalls and security groups.

TLS/WSS termination is infrastructure-specific. The inspected Gateway CLI does not document native
certificate flags. Browser WebSockets cannot attach arbitrary custom handshake headers; when headers
are required, use only the HTTP/2 endpoint/configuration emitted by Vision.

CORS affects browser HTTP surfaces and is configured with `--corsAllowedOrigins` or `--corsConfig`;
it is not a substitute for authentication.

**Gap:** no stable health/metrics port, MCP route table, maximum message size, idle timeout, or proxy
configuration is documented here.

## Next steps

- [Networking and ports](../operations/networking-ports.md)
- [Gateway CLI](gateway-cli.md)

## Source anchors

- `graftcode-gateway/README.md`, lines 18–40 and 139–146
- generated WebSocket host examples in the .NET and Node.js language guides
