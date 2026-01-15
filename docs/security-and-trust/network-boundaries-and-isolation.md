---
title: "Network boundaries and isolation"
description: "Learn how Graftcode respects network boundaries, isolates execution, and fits into existing infrastructure without expanding blast radius or trust zones."
keywords: "network boundaries, isolation, graftcode security, blast radius, distributed systems"
---

Clear network boundaries are fundamental to secure system design.

One of the common concerns when introducing a new integration technology is whether it:
- bypasses existing network controls
- expands the blast radius of failures
- or silently introduces new trust zones

Graftcode is designed to do none of these.

This section explains how network boundaries are preserved, how isolation works, and how Graftcode fits into existing network topologies.

---

## Execution stays inside network boundaries

All execution in Graftcode happens **inside the network where the code is deployed**.

Business logic:
- runs in your processes
- inside your runtimes
- within your private networks

Invocation intent may cross network boundaries, but **execution never does**.

There is no central execution plane and no shared runtime outside your infrastructure.

---

## Gateways define explicit network entry points

The Graftcode Gateway acts as a **well-defined network boundary**.

It is:
- the only component that accepts incoming invocation intent
- the only place where external connections terminate
- the point where authentication, authorization, and transport security are enforced

This makes the Gateway comparable to:
- an API gateway
- a reverse proxy
- or a service ingress

but without acting as an execution proxy.

---

## No implicit lateral movement

Graftcode does not enable implicit service-to-service trust.

A service:
- cannot call another service
- unless a Gateway is reachable
- and invocation is explicitly allowed

There is no hidden mesh behavior and no automatic peer discovery.

All network paths must be:
- explicitly configured
- reachable through network policy
- and permitted by security rules

---

## Isolation between services and runtimes

Each service instance:
- runs its own Gateway
- hosts its own Hypertube runtime
- loads only the modules it is configured to expose

There is no shared memory, shared runtime, or shared execution context across services.

Isolation is enforced by:
- process boundaries
- runtime boundaries
- and network boundaries

---

## Blast radius remains contained

Failures in one service:
- do not propagate automatically
- do not crash other services
- do not compromise unrelated runtimes

If a Gateway becomes unavailable:
- invocation routing to that service fails
- callers receive errors
- other services continue operating normally

There is no cascading execution dependency.

---

## Edge clients and perimeter boundaries

For edge clients, the Gateway typically sits:
- behind a load balancer
- behind an ingress
- or behind an API gateway

This ensures that:
- only intended traffic reaches the Gateway
- perimeter security controls remain intact
- existing WAF, firewall, and rate-limiting rules apply

The Gateway does not bypass or weaken these controls.

---

## Internal networks and private connectivity

Within private networks or cloud environments:
- Gateways can communicate over private IPs
- traffic can stay entirely within a VPC or VNet
- TLS can be terminated or passed through as required

Graftcode adapts to the network topology—it does not redefine it.

---

## No hidden control plane traffic

Beyond metadata exchange and tooling:
- there is no background communication
- no control-plane traffic involved in execution
- no dependency on external connectivity at runtime

If outbound internet access is restricted or disabled, production execution continues to function normally.

---

## Compatibility with zero-trust architectures

Graftcode works well in zero-trust environments because:
- every call is explicit
- every boundary is enforced
- identity is validated per invocation or per session

There is no assumption of trust based on network location alone.

---

## Deployment-time responsibility

Network boundaries in Graftcode are defined at deployment time, not at code time.

This allows:
- DevOps teams to control exposure
- security teams to define trust zones
- developers to remain focused on logic

Each concern remains in its proper layer.

---

## Closing perspective

Graftcode does not flatten networks or blur trust zones.

It respects:
- existing boundaries
- existing controls
- existing isolation models

By making invocation explicit and execution local, it keeps network architecture understandable, auditable, and secure.
