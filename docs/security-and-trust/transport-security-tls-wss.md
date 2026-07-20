---
title: "Transport security: TLS and WSS"
description: "Deployment checks for transport encryption and TLS termination."
keywords: "graftcode tls, wss, transport security, websocket security"
---

# Transport security: TLS and WSS

The inspected Gateway documentation exposes WebSocket, HTTP, TCP, and HTTP/2 server modes, but it does not establish a supported native TLS configuration for every listener.

Do not infer that `wss://` or raw TLS terminates inside Gateway. In a deployment that uses an external reverse proxy or ingress, document:

- where TLS terminates and whether traffic is re-encrypted upstream;
- certificate issuance, renewal, trust, and hostname validation;
- WebSocket upgrade forwarding and idle timeouts;
- the internal listener, port, and network policy;
- client configuration and certificate-error behavior.

Test the full path with the exact Gateway, proxy, and generated-package versions. Transport encryption does not provide application authentication or authorization by itself.

See [Graftcode Gateway](../core-concepts/graftcode-gateway.md), [Authentication and authorization](authentication-and-authorization.md), and [Networking and ports](../operations/networking-ports.md).
