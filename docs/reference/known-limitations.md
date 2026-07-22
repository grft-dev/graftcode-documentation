---
title: "Known limitations"
description: "Current limitations for Graftcode runtimes, contracts, packages, security, operations, and compatibility."
keywords: "graftcode alpha, limitations, runtime support, type support, compatibility, troubleshooting"
---

# Known limitations

This page describes the current limitations of Graftcode for external developers. Graftcode is in
**Alpha**: many paths work end to end, but support is directional and pair-specific. A runtime name in
Gateway, a method in the callable surface, or a generated package by itself does not mean the complete
Receiver-to-Caller path works. Validate the exact runtime pair, generated package, transport, and
deployment you intend to operate.

Statuses used on this page:

- **Available** — supported in the current release.
- **Alpha** — usable but not hardened; expect gaps and validate before depending on it.
- **Preview** — early, incomplete, or plugin-based; not guaranteed.
- **Planned** — not available yet.
- **Unsupported** — not supported; do not depend on it.

Where support depends on the runtime pair, that is stated directly (for example, *Available for .NET
and Node.js; other pairs require validation*).

## Contracts and types

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Primitive and string contracts | Available | — | Prefer primitives, strings, arrays of supported values, and plain models. |
| Framework complex types on the public surface (for example `DateTime`) | Unsupported | Package generation rejects them ("complex types from framework in public interfaces is not supported"). | Use ISO-8601 strings for dates and string identifiers; model your own plain types. |
| Rich shapes (nested models, nullability, enums, unions, maps, sets) | Available for .NET and Node.js; other pairs require validation | Behavior differs across runtimes; unknown values can degrade. | Generate and smoke-test every target package; keep contracts simple. |
| Generics | Available for .NET; other pairs require validation | Constraints, variance, overloads, and nested generics are not portable across all pairs. | Expose a concrete facade with closed, simple types; keep generics behind it. |
| Inheritance and polymorphism | Requires validation | Constructor, member, dispatch, and serialization semantics are not portable for arbitrary hierarchies. | Flatten the public contract into standalone facade types; delegate internally. |
| 64-bit integers and `decimal` to a JavaScript Caller | Requires validation | JavaScript `number` cannot safely represent every 64-bit or exact-decimal value. | Use `int` or a string for exact values unless the exact pair is tested. |

See [Type compatibility matrix](type-matrix.md) and [Type mapping](../core-concepts/type-mapping.md).

## Runtime support

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| .NET, Node.js/TypeScript, Java/JVM, Python 3, PHP, Ruby | Available | Support is directional; one direction working does not prove the reverse. | Test each Receiver-to-Caller direction the application uses. |
| Perl as a Receiver that produces a Graft | Unsupported | Gateway can host Perl code, but there is no Graft-generation path for a Perl Receiver. | Do not plan to publish a Graft from a Perl Receiver. |
| Specific framework/interpreter versions | Available for documented versions | Not every patch version, distribution, target framework, or JVM language is guaranteed. | Match the version the Gateway release documents, then smoke-test in the target environment. |

See [Supported runtimes and package managers](supported-runtimes-package-managers.md).

## Invocation and async

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Async on a .NET Receiver's public method | Unsupported | `Task`/`Task<T>` and cancellation tokens are not accepted on the public surface. | Keep public methods synchronous; use async internally. |
| Asynchronous generated Caller API | Available for Node.js/TypeScript | The generated call may return a `Promise<T>` even when the Receiver method is synchronous. | Follow the exact call shape in the installed package and Vision. |
| Cross-runtime cancellation and timeouts | Unsupported (built-in) | There is no built-in cross-runtime cancellation. | Apply timeouts, retries, and cancellation in Caller code and infrastructure. |
| Callbacks, delegates, and events | Preview | Lifecycle, reconnect, error, and browser behavior are not established across pairs. | Use request/result methods; add callbacks only after an end-to-end test for the exact pair and transport. |

See [Async, cancellation, and timeouts](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts).

## Stateful behavior

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Static (stateless) operations | Available | A static facade is not automatically stateless if it holds shared state. | Prefer static input-to-output operations; keep them free of shared mutable state. |
| Instance / remote object references | Alpha | No durable lifetime guarantee across reconnects, retries, Gateway restarts, transports, or pairs. | Keep durable state behind explicit IDs rather than persisting remote object references. |

See [Static and instance context](../core-concepts/static-and-instance-context.md).

## Package generation and registry

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Registry coordinates and install commands | Available | Names, versions, registry paths, namespaces, and imports depend on the active Gateway/project; a restart without a stable Project Key can change the registry identity. | Copy the complete command and generated import from the running Gateway/Vision; never reuse example coordinates. |
| npm runtime dependency | Available | Generated npm packages depend on a runtime SDK; automatic resolution is package-specific. | Run the exact npm command emitted for the Graft, keep the lockfile, and inspect installed metadata if resolution fails. |
| OS / architecture coverage | Requires validation | Native and plugin paths are OS/architecture specific; there is no exhaustive release matrix. | Build and smoke-test on the deployment OS/architecture; verify executable permissions and native assets. |

## Transports

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| In-memory and WebSocket (`ws://`, `wss://`) | Available | — | Use `wss://` for network calls; copy the exact host and path from Vision. |
| TCP and HTTP/2 listeners | Available (opt-in) | Require their enabling options; do not have identical failure/header semantics. | Enable the listener explicitly and verify the route through your proxy/ingress. |
| Message-queue / broker transports | Preview (plugin-based) | Availability depends on a specific transport plugin; not built in. | Do not assume a broker is supported because it appears in a diagram; verify the plugin. |
| Proxy, ingress, certificate, keepalive behavior | Requires validation | Deployment-specific. | Terminate TLS with a configuration tested for that deployment. |

See [Ports and protocols](ports-protocols.md).

## Security

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Invocation authentication and authorization | Alpha | Not automatic; if nothing is configured, no invocation authentication occurs. The Project Key is not runtime-call authorization. | Pass and validate credentials before business effects; test rejection as well as success. See [Authentication and authorization](../operations/authentication-authorization.md). |
| Browser custom headers on the WebSocket handshake | Unsupported | Browser WebSocket handshakes cannot set arbitrary custom headers. | Pass credentials as a supported method parameter, or use the HTTP/2 configuration emitted by Vision. |

## Observability

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| W3C Trace Context propagation | Available for .NET and Node.js; other runtimes require validation | No guarantee of automatic end-to-end traces on every runtime/transport. | Instrument Caller and Receiver with OpenTelemetry; verify parent/child spans in a smoke test. See [Observability](../operations/observability.md). |
| Built-in metrics / log collector | Unsupported | Gateway does not provide a built-in collector. | Export telemetry with your own OpenTelemetry/logging stack. |

## Configuration

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Six-level configuration precedence | Available for .NET and Node.js | Runtime context is cached after first initialization; at equal name and priority, first registration wins. | Set configuration before the first generated call; inspect higher-priority sources when a setting seems ignored. See [Configuration resolution](../core-concepts/configuration-resolution.md). |

## Operations

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Liveness endpoint | Available | Gateway provides `GET /status` for liveness only. | Use `/status` for liveness; implement readiness/dependency checks yourself. |
| Readiness / dependency health | Application-defined | No built-in readiness or dependency-health endpoint. | Add readiness and dependency checks at an owned layer. |
| Retry, backoff, failover, idempotency, exactly-once | Unsupported (built-in) | Retrying an invocation can repeat business effects. | Add resilience at an owned layer; retry only operations designed and tested as idempotent; use explicit operation IDs for deduplication. |
| Ports and runtime detection | Available | Default ports can be occupied or require privileges; auto-detection can select the wrong module/runtime. | Provide the exact module and runtime and use available ports; confirm discovery and publication before installing a Graft. |

## Vision

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Browse callable surface, package coordinates, install command, configuration, version | Available | Reflects only the modules loaded by that Gateway process. | Use Vision as the source for install and configuration details for the running Gateway. See [Graftcode Vision](../core-concepts/graftcode-vision.md). |

## MCP

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Expose a callable surface over MCP | Available | Scope depends on the runtime and configuration. | Follow the [MCP Quick Start](https://docs.graftcode.com/quick-start/expose-mcp) for the end-to-end flow; see [Expose methods over MCP](../how-to-guides/expose-mcp.md). |

## Compatibility

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Backward compatibility across releases | Version-dependent | No universal wire, binary, source, or old-Caller/new-Receiver guarantee. Additive source changes can still change generated names, overloads, exports, or mappings. | Pin all participating versions, regenerate deliberately, compare the generated public API, then compile and smoke-test representative Callers before rollout. See [Contract evolution](../core-concepts/contract-evolution.md). |
| Production readiness | Alpha | Support for advanced types, all pairs, security distribution, upgrades, HA, and every platform is incomplete. | Define and test a narrow supported profile (exact versions, simple contract, locked packages, TLS/auth, timeouts, failure handling, restart, rollback, upgrade). |

## Runtime-specific notes

**.NET**

- SDK-style projects compile all `.cs` files recursively. Keep Caller and test projects outside the
  Receiver library directory so unintended code does not enter the callable surface.
- Public methods must be synchronous; a public `async`/`Task<T>` is not a portable contract.

**Node.js / TypeScript**

- Build TypeScript first and ensure package metadata resolves to the emitted JavaScript.
- In stateless mode, `await` the top-level generated call rather than each returned accessor.
- Browser bundlers may need polyfills for Node built-ins used by the generated package.
- Framework route handlers and server actions are adapters, not the callable surface.

**Java / JVM**

- Expose Kotlin companion methods as JVM-static (`@JvmStatic`) so they appear as static operations.
- Keep custom exception types package-private so they do not enter the callable surface.

**Python**

- Importing the module can run module initialization code. Keep Receiver imports deterministic and
  free of unsafe startup side effects.
- Distribution names and import paths often differ; use the exact import shown in Vision.

**Ruby**

- The package name and require name can use different normalization; use the emitted require name.
- Prefer current Gateway output for generated module paths.

**PHP**

- Composer packages may run post-install steps; retain the generated package scripts.
- Verify the generated autoload path rather than relying on autoloading alone in older packages.

See [Supported runtimes and package managers](supported-runtimes-package-managers.md) and the
[Type compatibility matrix](type-matrix.md) for role support and type behavior.

## Next steps

1. Select the exact runtime direction in [Supported runtimes and package managers](supported-runtimes-package-managers.md).
2. Reduce the public contract using [Callable surface](../core-concepts/callable-surface.md) and
   [Type mapping](../core-concepts/type-mapping.md).
3. Publish once, copy package coordinates from the running Gateway/Vision, and run local and remote
   smoke tests.
4. Use the [Troubleshooting index](../troubleshooting/index.md) for symptom-based diagnostics.
