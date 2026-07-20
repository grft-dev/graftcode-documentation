---
title: "Authentication and authorization operations"
description: "Separate project publication identity, transport security, and invocation authorization."
---

# Authentication and authorization operations

Three controls must not be conflated:

1. `--projectKey` / `GC_PROJECT_KEY` authenticates Gateway to portal/project metadata services.
2. TLS/WSS protects transport when terminated by deployment infrastructure.
3. Provider-call authentication and authorization must be explicitly implemented and configured.

The project key is not proof that runtime calls are authorized. Keep it in a secret store, rotate it
through the portal process, and restart/redeploy Gateway as required to load the replacement.

For provider calls, the portable Alpha baseline is to pass a token or API key as a supported method
parameter and validate it before business effects. Generated .NET and Node.js packages also contain
header APIs, and `--useContext` exposes request context/headers to hosted code. Browser WebSocket
handshakes cannot set arbitrary custom headers; use only the HTTP/2 configuration emitted by Vision
when that workflow is required.

Default deny at the provider boundary, log authorization decisions without credentials, and keep
policy logic independent from transport.

**Gap:** a .NET JWT plugin exists in source/tests, but release packaging, configuration, and
cross-runtime support are not established as a generally available feature. Automatic credential
propagation must not be assumed.

## Next steps

- [Networking and ports](networking-ports.md)
- [Environment variables](../reference/environment-variables.md)
- [Known limitations](../how-graftcode-works/alpha-limitations-and-known-constraints.md)

## Source anchors

- `graftcode-gateway/README.md`, `--projectKey`, `--useContext`, and `GC_PROJECT_KEY`
- generated `SetHeaders`/`setHeaders` and `InvokeWithHeaders` helpers in `graftcode-code-generator/`
- [Authentication and authorization](../security-and-trust/authentication-and-authorization.md)
