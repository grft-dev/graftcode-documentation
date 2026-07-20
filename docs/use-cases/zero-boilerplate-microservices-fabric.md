---
title: "Zero-boilerplate microservices fabric"
description: "Compatibility route for the supported service-to-service workflow."
keywords: "graftcode use case, microservices, service communication"
---

# Zero-boilerplate microservices fabric

This legacy use-case page has been replaced by the bounded [Service-to-service integration](../integration-patterns/service-to-service-integration.md) workflow.

Graftcode can derive a callable contract and generate consumer packages, but it does not eliminate all DTO, dependency injection, deployment, configuration, security, observability, or resilience work. Supported runtimes, type shapes, and execution modes are release-specific.

The prior claims about arbitrary languages, interchangeable Kafka/NATS/RabbitMQ/gRPC/HTTP2 channels, one-flag topology changes, delivery in minutes, and 10–20× performance are not supported by the audited evidence and must not be used for technical or commercial decisions.

Start with:

- [Callable surface](../core-concepts/callable-surface.md)
- [Package generation](../core-concepts/package-generation.md)
- [Execution modes](../core-concepts/execution-modes.md)
- [Language support status](../language-guides/support-status.md)
