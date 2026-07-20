---
title: "Authentication and authorization"
description: "Current evidence boundaries for authentication and authorization in Graftcode."
keywords: "graftcode authentication, authorization, jwt, request context"
---

# Authentication and authorization

Authentication and authorization are not automatic Gateway guarantees.

The inspected source contains a .NET JWT sending/receiving plugin with functional tests. That evidence does not establish its packaging, release support, configuration, cross-runtime availability, or suitability for a production deployment.

Until a release-qualified guide exists:

1. treat an unconfigured callable surface as unauthenticated;
2. authenticate at a tested network or runtime control;
3. authorize each business operation using server-side policy;
4. validate token issuer, audience, signature, expiry, and required claims;
5. avoid process-global mutable credentials for concurrent callers;
6. test missing, malformed, expired, and insufficient-privilege cases.

Headers or context can carry identity evidence, but carrying a value does not validate it. Verify the generated package API for the specific runtime and release.

See [Security model overview](security-model-overview.md), [Graftcode Gateway](../core-concepts/graftcode-gateway.md), and [Authentication and authorization operations](../operations/authentication-authorization.md).
