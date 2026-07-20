---
title: "Internal business APIs"
description: "Compatibility route for service boundaries expressed as callable surfaces."
keywords: "internal services, business capabilities, callable surface"
---

# Internal business APIs

This topic is now covered by:

- [Service-to-service integration](service-to-service-integration.md) for the provider-to-consumer workflow;
- [Public interface vs business logic](../core-concepts/public-interface-vs-business-logic.md) for boundary design;
- [Callable surface](../core-concepts/callable-surface.md) for visibility, filters, and runtime eligibility.

“Internal” is an ownership label, not a security control. Keep the exposed surface narrow and enforce network access, authentication, authorization, and operational policy independently.

Only analyzer-eligible members selected by the active filters and supported type mappings become usable contracts; it is not accurate to assume that every public member is safely callable.
