---
title: "Connection, timeout, or authentication failure"
description: "Diagnose Graft host resolution, Gateway listeners, network timeouts, TLS, headers, and authentication rejection."
keywords: "graftcode connection refused, timeout, websocket, authentication, JWT, TLS"
---

# Connection, timeout, or authentication failure

## Symptoms

- The first call tries to load a local provider module or reports file/module not found.
- A remote call is refused, reset, closed, or times out.
- WebSocket, TLS, proxy, CORS, or HTTP/2 negotiation fails.
- The provider is reachable but returns an authentication/authorization failure.
- A configuration change appears to have no effect.

## Diagnostics

1. **Identify the resolved execution mode.** Generated packages default to in-memory unless overridden.
   A local provider-module error often means the caller never switched to the remote host.
2. **Check all six configuration priorities.** Highest first: runtime-specific environment, global
   environment, runtime-specific file, global file, user configuration, generated library default.
   A higher source can override code. There is no seventh precedence level.
3. **Restart after changing configuration.** Generated runtime context is cached after first
   initialization; changing static fields or files after the first call is not a supported reset path.
4. **Match the configured transport to an enabled listener.** Gateway enables WebSocket by default; TCP
   and HTTP/2 require their Gateway options. Use the host/route emitted for the running release rather
   than inventing a URL.
5. **Test each network boundary.** Confirm the Gateway process is listening, the selected port is
   available, firewall and container port publishing permit the connection, DNS resolves from the
   caller, and proxy/ingress supports the chosen protocol and connection lifetime.
6. **Separate TLS from application authentication.** Certificate trust/hostname errors occur before
   JWT or authorization logic. Confirm where TLS terminates and that the caller trusts the presented
   certificate.
7. **Separate project identity from call authentication.** Gateway `--projectKey`/`GC_PROJECT_KEY`
   concerns portal/project metadata. It does not by itself authorize runtime invocations.
8. **Check header constraints.** Generated .NET/Node packages have header hooks in inspected code, but
   browser WebSocket handshakes cannot set arbitrary custom headers. Use only the browser transport and
   auth configuration emitted/documented for that release.
9. **Classify the timeout.** Record whether it occurs during connect, TLS/handshake, authentication,
   invocation, or provider execution. Check provider and Gateway logs at the same timestamp.

`GG_DEBUG=1` is documented to log incoming and outgoing byte traffic. It can expose payload or
credential material; use it only in a controlled environment, redact captured output, and disable it
after diagnosis.

## Fixes

- **Unexpected in-memory loading:** configure the generated Graft host before its first call, then start
  a new caller process. Example by runtime:

```multi
```dotnet
GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```
```javascript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```python
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
```
```java
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```php
GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;
```
```ruby
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true
```
```

- **Connection refused:** start the intended Gateway listener or correct the deployment's port mapping
  using values from Gateway output/configuration.
- **WebSocket/proxy failure:** enable WebSocket forwarding and suitable idle/upgrade behavior in the
  actual proxy; verify with that proxy's documented diagnostics.
- **TLS failure:** correct certificate chain, hostname, trust, or TLS termination. Do not disable
  validation as a production fix.
- **Authentication rejected:** verify that caller and receiver use the same documented mechanism,
  issuer/audience/key/time settings, and that receiver validation runs before business effects.
- **Browser custom-header failure:** use the emitted HTTP/2/context option when available for the
  release, or redesign auth so it does not depend on an unsupported WebSocket handshake header.
- **Invocation timeout:** determine whether the operation completed at the provider before retrying.
  Graftcode does not provide a universal retry/idempotency guarantee; retry only operations designed to
  tolerate duplicates.

## Escalation evidence

Provide redacted resolved configuration source, host scheme (without secrets), enabled Gateway
listeners, proxy/ingress topology, connection-stage error, timestamps, caller/Gateway/provider logs,
runtime versions, and whether the provider observed the invocation.

## Next steps

If the process exits rather than returning a network error, continue with
[Gateway or runtime exits](runtime-exits.md). If calls reach an old method after reconnection, continue
with [Installed package is stale](stale-package.md).
