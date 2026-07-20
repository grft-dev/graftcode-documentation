---
title: "Security plugins"
description: "Current evidence boundaries for Graftcode security plugins."
keywords: "graftcode plugins, security plugins, jwt"
---

# Security plugins

This page no longer describes a general, production-supported plugin framework.

The inspected implementation includes a .NET JWT sending/receiving plugin and functional tests for selected success and failure paths. That is narrower than a cross-runtime security product and does not establish release packaging, support policy, configuration stability, or independent security review.

Do not assume plugins can provide arbitrary authentication, authorization, encryption, retries, transactions, routing, or message-broker semantics while preserving call behavior. For any plugin used in a deployment, require:

- a versioned artifact and owner;
- configuration and secret-management guidance;
- exact invocation and failure lifecycle;
- concurrency and credential-isolation tests;
- compatibility and security review;
- operational logging and rollback procedures.

See [Authentication and authorization](authentication-and-authorization.md) and [Security model overview](security-model-overview.md).
