---
title: "Transport security: TLS and WSS"
description: "Learn how transport-level security works in Graftcode using standard TLS and secure WebSocket protocols without introducing custom encryption layers."
keywords: "graftcode tls, wss, transport security, encrypted communication, websocket security"
---

# Transport security: TLS and WSS

Transport security in Graftcode is intentionally simple and conventional.

Instead of introducing custom encryption schemes or proprietary protocols, Graftcode relies on **standard, well-understood transport security mechanisms** provided by the underlying network stack.

This keeps transport security predictable, auditable, and compatible with existing infrastructure.

---

## Encrypted transport, not encrypted logic

Graftcode secures communication at the **transport layer**, not at the application logic layer.

When invocation intent is transmitted between runtimes:
- it is carried over TCP/IP or WebSocket
- encryption is provided by TLS or WSS
- message payloads are protected in transit

Graftcode does not introduce:
- custom cryptographic formats
- application-level encryption layers
- proprietary key exchange mechanisms

Security is delegated to proven standards.

---

## TLS for TCP/IP communication

When Graftcode uses direct TCP/IP transport—typically in backend-to-backend or cloud-to-cloud scenarios—encryption is provided through **TLS**.


This ensures:
- confidentiality of data in transit
- integrity of invocation messages
- protection against eavesdropping and tampering

TLS termination can occur:
- directly at the Graftcode Gateway
- at a load balancer
- at an ingress or reverse proxy

From Graftcode’s perspective, TLS behaves exactly as it does for any other TCP-based service.

---

## Secure WebSocket (WSS)

When Graftcode is used by edge clients—such as browser-based applications—communication must go through HTTP-compatible protocols.

Because browsers do not allow direct TCP/IP connections, **Secure WebSocket (WSS) is mandatory** in these scenarios. All invocation intent exchanged with edge clients is therefore transported over WSS, ensuring encrypted, standards-compliant communication.

This is not a design preference but a technical requirement of the browser security model.

This applies both to:
- stateful interactions (objects, subscriptions, callbacks)
- and stateless calls using static methods

In the stateless case, Graftcode still uses WSS, but behaves closer to a traditional request–response model. A WebSocket connection is opened and kept alive while calls are being made. If no calls occur for a configurable timeout period, the connection is closed. Subsequent calls simply reopen the connection.

From the application’s perspective, this behaves similarly to REST with keep-alive connections—except that communication remains strongly typed and duplex-capable.

This is particularly useful for:
- duplex communication
- stateful interactions
- event subscriptions and callbacks

WSS provides:
- encrypted, persistent connections
- standard certificate-based security
- compatibility with existing network tooling

There is no special handling required in application code.

For non-edge scenarios—such as service-to-service communication inside a cloud environment, between clouds, or within private networks—Graftcode can use direct TCP/IP connections secured with TLS.

In these environments, there is no HTTP constraint, and using TLS over raw TCP/IP is both supported and commonly preferred for efficiency.

In summary, WSS is required for edge clients due to browser constraints, while TLS over TCP/IP is the natural choice for backend and infrastructure-level communication.

---

## Certificate management and infrastructure integration

Graftcode does not manage certificates internally.

Certificates can be:
- provisioned by the hosting environment
- managed by cloud platforms
- rotated by existing infrastructure tooling

This allows teams to:
- reuse established certificate practices
- integrate with enterprise PKI
- comply with organizational security policies

Transport security remains an infrastructure concern, not an application concern.

---

## No impact on execution semantics

Transport security does not change how execution behaves.

Method calls:
- execute the same way
- propagate the same context
- return the same results

Whether communication is encrypted or not has no effect on:
- method signatures
- exception handling
- tracing or observability

Security is applied transparently at the transport boundary.

---

## Interaction with plugins and routing

Transport security works independently of:
- authentication plugins
- authorization plugins
- transport routing plugins

A system can:
- encrypt communication with TLS or WSS
- inject identity through plugins
- route invocation intent through queues or brokers

Each concern remains isolated and composable.

---

## Aligning with existing security models

Because Graftcode uses standard transport security:
- firewall rules remain unchanged
- network inspection tools continue to work
- compliance audits remain straightforward

There is no need to introduce special exceptions or new trust models.

---

## Closing perspective

Graftcode treats transport security as an infrastructure responsibility.

By relying on TLS and WSS, it ensures:
- secure communication
- predictable behavior
- compatibility with existing systems

Encryption is present where it matters—without complicating the programming model.
