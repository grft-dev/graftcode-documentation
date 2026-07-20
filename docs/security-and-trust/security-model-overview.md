---
title: "Security model overview"
description: "Shared-responsibility guidance for securing a Graftcode deployment."
keywords: "graftcode security, shared responsibility, trust boundaries"
---

# Security model overview

Graftcode does not supply a universal security boundary. Security depends on the exact provider, generated consumer, Gateway configuration, transport, surrounding network, and cloud/package services used.

For each deployment, document and test:

- the callable surface and who can reach it;
- Gateway listeners, ports, and outbound destinations;
- authentication and authorization defaults;
- credential and request-context handling;
- TLS termination and trust stores;
- metadata and telemetry leaving the environment;
- package provenance and update policy;
- runtime isolation, secrets, logging, and incident response.

Absence of a configured authentication control means authentication must not be assumed. Network placement is not authorization, and generated typing is not input validation.

Use [Graftcode Gateway](../core-concepts/graftcode-gateway.md), [Callable surface](../core-concepts/callable-surface.md), and [Invocation lifecycle](../core-concepts/invocation-lifecycle.md) to build a release-specific threat model. This page intentionally makes no cloud privacy, isolation, source-availability, or outage-containment guarantees.
