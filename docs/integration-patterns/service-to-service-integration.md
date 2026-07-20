---
title: "Service-to-service integration"
description: "A bounded pattern for connecting a provider and consumer with a generated Graft."
keywords: "service to service integration, graftcode integration, generated package"
---

# Service-to-service integration

Start with one narrow provider operation, for example `GetCustomerName(string customerId)`, whose parameters and return value are supported by the provider and consumer runtimes.

1. Expose only the intended public surface; keep infrastructure and implementation types non-public.
2. Run the Gateway and verify the discovered type and method in startup output.
3. Copy the exact package install command from that Gateway or Vision instance.
4. Configure the generated package before its first call.
5. Call the generated method and test both success and provider/transport failure.

The generated package is a code-derived contract; it does not remove distributed-system concerns. Define authentication, timeout, retry, idempotency, deployment, and compatibility policy explicitly.

Canonical details:

- [Callable surface](../core-concepts/callable-surface.md)
- [Type mapping](../core-concepts/type-mapping.md)
- [Package generation](../core-concepts/package-generation.md)
- [Invocation lifecycle](../core-concepts/invocation-lifecycle.md)
- [Language guides](../language-guides/index.md)
- [Expose code](../how-to-guides/expose-code.md)
- [Obtain and install a Graft](../how-to-guides/obtain-install-graft.md)
- [Configure invocation](../how-to-guides/configure-invocation.md)
- [Connection, timeout, and authentication troubleshooting](../troubleshooting/connection-timeouts-auth.md)
