---
title: "Scaling, load balancers, and proxies"
description: "Learn how Graftcode scales using standard load balancers, proxies, and network infrastructure, without requiring specialized gateways or custom routing components."
keywords: "graftcode scaling, load balancers, reverse proxies, websocket scaling, distributed systems infrastructure"
---

Scaling is where many distributed systems become complicated—not because scaling is inherently hard, but because tooling often introduces special requirements.

Graftcode is designed so that **scaling works the same way it already does in your infrastructure**.

There are no custom gateways, no proprietary routers, and no special load-balancing components required.

---

## No special infrastructure requirements

From an infrastructure perspective, a Graftcode-based system consists of:
- application processes
- Graftcode Gateways
- direct network connections between them

Communication uses:
- TCP/IP
- or WebSocket

These are standard, well-understood protocols.

As a result, Graftcode works with:
- existing load balancers
- reverse proxies
- API gateways
- service meshes
- cloud-native networking components

Nothing needs to be replaced.

---

## Scaling stateless services

Stateless services scale exactly as expected.

In this model:
- each call is independent
- no execution context is retained between calls
- requests can be routed to any available instance

A load balancer can:
- distribute calls across Gateway instances
- scale horizontally
- apply health checks
- handle failover

This is equivalent to scaling REST-style services—without exposing REST semantics to application code.

---

## Scaling stateful services

Stateful services require **session affinity**.

This is not a limitation specific to Graftcode—it is a property of stateful systems in general.

In this case:
- a caller must continue communicating with the same Gateway instance
- execution context and object state are preserved
- callbacks and events remain connected

Standard infrastructure supports this through:
- sticky sessions
- connection-based routing
- consistent hashing
- WebSocket-aware load balancing

Graftcode does not introduce new requirements here—it relies on established patterns.

---

## WebSocket and TCP/IP friendliness

Because Hypertube uses:
- long-lived TCP connections
- or WebSocket sessions

Graftcode fits naturally into:
- WebSocket-capable load balancers
- L7 proxies
- cloud-native ingress controllers

Once a connection is established:
- execution is duplex
- calls and callbacks flow in both directions
- session context is preserved

This is particularly well-suited for real-time and stateful interactions.

---

## Proxies and API gateways

Graftcode does not bypass existing proxies or gateways.

If your infrastructure uses:
- reverse proxies
- API gateways
- security gateways

Graftcode traffic can flow through them like any other TCP or WebSocket traffic.

Because execution is not HTTP-based:
- there are no routes to manage
- no endpoints to expose
- no payload schemas to validate at the proxy layer

Security and access control remain where they belong—at the network boundary.

---

## Scaling through configuration, not code

Scaling decisions are expressed through configuration:
- how many Gateway instances to run
- how traffic is routed
- which execution mode is used

No application code changes are required.

The same Graft:
- works against a single instance
- works against a load-balanced pool
- works across environments

This separation allows teams to scale independently of development.

---

## Transport plugins and advanced routing

In some scenarios, direct point-to-point execution is not enough.

Teams may need:
- request queuing and delayed execution
- multiple subscribers handling the same invocation
- topic-based routing strategies
- transactional execution coordinated by an event bus
- integration with existing messaging or PaaS infrastructure

Graftcode supports these scenarios through **transport plugins**.

A transport plugin allows Hypertube to route invocation intent through an external system in exactly the same way developers would do manually using that system’s SDK—except without changing application code.

Instead of calling an SDK, constructing messages, or serializing payloads, the invocation intent is passed to the plugin, which forwards it to the chosen transport channel.

From the application’s perspective, the call is still just a method invocation.

The important distinction is that **Graftcode does not replace these systems**.

If a team wants to use:
- a message queue
- a service bus
- a topic-based event system
- or any other transport with specific delivery guarantees

they can do so by enabling the appropriate plugin.

Hypertube forwards the invocation intent through the plugin exactly as if the team had:
- created a message
- sent it using the native SDK
- and implemented the same behavior manually

The difference is that no changes are required in business code, interfaces, or callers.

Gateways that are configured with the same transport plugin can subscribe to selected channels or topics.

Based on configuration:
- specific Gateways receive invocations from those channels
- execution happens inside their hosted runtimes
- results are returned using the configured response channel

This makes it possible to:
- fan out calls to multiple receivers
- process invocations asynchronously
- coordinate execution through external systems
- and still preserve strong typing and execution semantics

Transport plugins affect **routing and delivery**, not programming semantics.

Method signatures remain the same.
Error handling remains the same.
Execution intent remains the same.

Only the path the invocation takes is different.

This allows teams to adopt advanced routing, queuing, or transactional delivery strategies incrementally—without rewriting interfaces or changing how code is written.


---

## Failure handling and resilience

Because Graftcode uses standard networking:
- retries can be handled by infrastructure
- circuit breakers can be applied externally
- failover strategies remain consistent

There is no hidden retry logic or opaque routing layer.

Failures behave like normal network failures—and can be handled using existing patterns.

---

## Why this matters

Scaling should not force architectural lock-in.

By relying on standard protocols and infrastructure:
- Graftcode fits into existing platforms
- operations teams remain in control
- scaling strategies stay flexible

Distributed execution becomes easier to scale—not harder.

---

## In short

Graftcode scales using:
- standard TCP/IP and WebSocket connections
- existing load balancers and proxies
- familiar stateless and stateful scaling patterns

No proprietary infrastructure is required.

---

Next, we’ll look at **what happens when interfaces change**, and how Graftcode keeps systems stable as they evolve.
