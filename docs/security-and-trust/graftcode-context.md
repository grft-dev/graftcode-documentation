---
title: "Graftcode Context libraries"
description: "Current evidence and constraints for carrying invocation context."
---

# Graftcode Context Libraries

This legacy cross-language reference has been retired because the generated APIs, package names, versions, imports, and concurrency behavior were not verified for every ecosystem.

The inspected Node.js generated-package templates include global header configuration and per-invocation header support. The Gateway also exposes a context-related option. These facts do not prove identical APIs or lifecycle semantics in other runtimes.

Before using request context:

1. check the generated package for the exact methods and types it exposes;
2. configure values before invocation according to that package's lifecycle;
3. prefer per-invocation values for concurrent users or tenants;
4. validate all security-sensitive values on the provider;
5. test nested calls, parallel calls, failure cleanup, and absent headers.

Do not use a process-global mutable header store for request-specific credentials unless the runtime package explicitly documents and tests safe isolation.

See the relevant [language guide](../language-guides/index.md), [Invocation lifecycle](../core-concepts/invocation-lifecycle.md), and [Authentication and authorization](authentication-and-authorization.md).
