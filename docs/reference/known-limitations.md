---
title: "Known limitations"
description: "Current limitations for Graftcode runtimes, contracts, packages, security, operations, and compatibility."
keywords: "graftcode limitations, runtime support, type support, compatibility, troubleshooting"
---

# Known limitations

This page describes the current limitations of Graftcode for external developers. Many paths work end
to end, but support is **directional and pair-specific**. A runtime name in Gateway, a method in the
callable surface, or a generated package by itself does not mean the complete Receiver-to-Caller path
works. Validate the exact runtime pair, generated package, transport, and deployment you intend to
operate.

Statuses used on this page:

- **Available** — documented path exists and is used in supported scenarios.
- **Requires validation** — may work for your pair; smoke-test before you depend on it.
- **Unsupported** — not supported; do not depend on it.
- **Application-defined** — you implement the behavior (for example readiness checks).
- **Version-dependent** — behavior depends on pinned Gateway, protocol, and package versions.
- **Plugin-based** — requires an optional Gateway transport plugin; verify the plugin and config.

Where support depends on the runtime pair, that is stated directly (for example, *Available for .NET
and Node.js; other pairs require validation*).

## Contracts and types

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Primitive and string contracts | Available | — | Prefer primitives, strings, arrays of supported values, and plain models. |
| Non-parsable framework types on the public surface (for example `System.Type`, `List<T>`, `Stream`, most BCL types not in the parsable catalog) | Unsupported | Installing or generating the Caller package fails with HTTP `422` and a message that a framework type is not supported. The rule applies to types from **your Receiver's** runtime libraries, not only .NET. | Use primitives, plain models, language arrays, [parsable types](type-compatibility-matrix.md#parsable-framework-types), or ISO-8601 strings for maximum portability. See [Errors and status](errors-and-status-reference.md). |
| Parsable framework types (`System.DateTime`, `System.Guid`, selected `java.time.*`, `datetime.datetime`, …) | Requires validation | Listed in the cross-runtime **parsable types** catalog; package generation does not treat them like opaque framework models. Mapping and timezone semantics vary by Receiver→Caller pair. | Prefer ISO-8601 strings for the safest cross-runtime contract, or smoke-test the exact pair. See [Parsable framework types](type-compatibility-matrix.md#parsable-framework-types). |
| Nested models, nullability, enums, and primitive arrays | Available | Supported across the documented runtimes when every member stays portable. Edge cases still differ by Receiver→Caller direction. | Design shallow models; generate a Caller package and run your own integration test for each direction you use. |
| Maps, sets, framework collections (`List<T>`, `Dictionary<,>`, …), and rich unions | Requires validation | Not in the portable baseline; mapping varies by language pair. | Prefer plain models and language arrays; test the exact pair before shipping. |
| Generics | Requires validation | May work for your pair, but constraints, variance, overloads, and nested generics are not guaranteed across runtimes. | Expose a concrete facade with fixed types on the public surface. |
| Binary buffers (`byte[]`, `bytes`, `Uint8Array`, …) on the public surface | Available | Mapped as primitive byte arrays over Hypertube, not as opaque framework types. | Smoke-test each Receiver→Caller pair; very large payloads still need operational limits (timeouts, size). |
| Inheritance and polymorphism | Requires validation | Constructor, member, dispatch, and serialization semantics are not portable for arbitrary hierarchies. | Flatten the public contract into standalone facade types; delegate internally. |
| 64-bit integers and `decimal` to a JavaScript Caller | Requires validation | JavaScript `number` cannot safely represent every 64-bit or exact-decimal value. | Use `int` or a string for exact values unless the exact pair is tested. |

See [Type compatibility matrix](type-compatibility-matrix.md) and [Type mapping](../core-concepts/type-mapping.md).

## Runtime support

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| .NET, Node.js/TypeScript, Java/JVM, Python 3, PHP, Ruby | Available | Support is directional; one direction working does not prove the reverse. | Test each Receiver-to-Caller direction the application uses. |
| Perl as a Receiver that produces a Graft | Unsupported | Gateway can host Perl code, but there is no Graft-generation path for a Perl Receiver. | Do not plan to publish a Graft from a Perl Receiver. |
| Specific framework/interpreter versions | Available for documented versions | Not every patch version, distribution, target framework, or JVM language is guaranteed. | Match the version the Gateway release documents, then smoke-test in the target environment. |

See [Supported runtimes and package managers](supported-runtimes-and-package-managers.md).

## Invocation and async

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| `CancellationToken` and similar on a public method | Unsupported | Not a portable cross-runtime contract. | Keep cancellation internal; use Caller-side timeouts. |
| Async completion on the Receiver (`Task`/`Task<T>`, `ValueTask`, `Promise`, `async def`, …) | Requires validation | Results are completed on the Receiver; handles are not sent over the wire. UGM `METHOD_COMPLETION` drives the generated Caller wrapper. | Follow Vision and the installed package; see [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts). |
| Asynchronous generated Caller API | Available (runtime-specific) | Deferred returns and `execute_async`/`ExecuteAsync` appear in .NET, Node.js, Python, Ruby, PHP, JVM, and others depending on metadata and pair. | Follow the exact call shape in the installed package and Vision. |
| Cross-runtime cancellation and timeouts | Unsupported (built-in) | There is no built-in cross-runtime cancellation. | Apply timeouts, retries, and cancellation in Caller code and infrastructure. |
| Callbacks, delegates, and events | Requires validation | Lifecycle, reconnect, error, and browser behavior are not established across pairs. | Use request/result methods; add callbacks only after an end-to-end test for the exact pair and transport. |

See [Async, cancellation, and timeouts](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts).

## Stateful behavior

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Static (stateless) operations | Available | A static facade is not automatically stateless if it holds shared state. | Prefer static input-to-output operations; keep them free of shared mutable state. |
| Instance / remote object references | Requires validation | No durable lifetime guarantee across reconnects, retries, Gateway restarts, transports, or pairs. | Keep durable state behind explicit IDs rather than persisting remote object references. |

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
| Message-queue / broker transports | Plugin-based | Availability depends on a specific transport plugin; not built in. | Do not assume a broker is supported because it appears in a diagram; verify the plugin. |
| Proxy, ingress, certificate, keepalive behavior | Requires validation | Deployment-specific. | Terminate TLS with a configuration tested for that deployment. |

See [Ports and protocols](ports-and-protocols-reference.md).

## Security

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Invocation authentication and authorization | Requires validation | Not automatic; if nothing is configured, no invocation authentication occurs. The Project Key is not runtime-call authorization. | Pass and validate credentials before business effects; test rejection as well as success. See [Authentication and authorization](../operations/authentication-and-authorization-operations.md). |
| Browser custom headers on the WebSocket handshake | Unsupported | Browser WebSocket handshakes cannot set arbitrary custom headers. | Pass credentials as a supported method parameter, or use the HTTP/2 configuration emitted by Vision. |

## Observability

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| W3C Trace Context propagation | Requires validation | .NET Callers are the primary documented path; other runtimes depend on Gateway/SDK version. No guarantee on every transport. | Instrument Caller and Receiver with OpenTelemetry; verify parent/child spans in a smoke test. See [Observability](../operations/logging-metrics-and-tracing.md). |
| Built-in metrics / log collector | Unsupported | Gateway does not provide a built-in collector. | Export telemetry with your own OpenTelemetry/logging stack. |

## Configuration

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Six-level configuration precedence | Available | Each generated Caller package loads configuration in the same priority order (environment, files, programmatic defaults). Settings are applied once at first use; at equal priority, the first registered value wins. | Set host, modules, and other options before the first call; copy field names from Vision or your installed package. See [Configuration resolution](../core-concepts/configuration-resolution.md). |

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
| Expose a callable surface over MCP | Available | Scope depends on the runtime and configuration. | Follow the [MCP Quick Start](https://docs.graftcode.com/quick-start/expose-mcp) for the end-to-end flow; see [Expose methods over MCP](../how-to-guides/expose-receiver-methods-for-mcp.md). |

## Compatibility

| Capability | Status | Current limitation | Recommended approach |
| --- | --- | --- | --- |
| Backward compatibility across releases | Version-dependent | No universal wire, binary, source, or old-Caller/new-Receiver guarantee. Additive source changes can still change generated names, overloads, exports, or mappings. | Pin all participating versions, regenerate deliberately, compare the generated public API, then compile and smoke-test representative Callers before rollout. See [Contract evolution](../core-concepts/contract-evolution.md). |
| Operating at production scale | Requires validation | Advanced types, every pair, security distribution, upgrades, HA, and every platform need explicit design and testing. | Define and test a narrow supported profile (exact versions, simple contract, locked packages, TLS/auth, timeouts, failure handling, restart, rollback, upgrade). |

## Runtime-specific notes

**.NET**

- SDK-style projects compile all `.cs` files recursively. Keep Caller and test projects outside the
  Receiver library directory so unintended code does not enter the callable surface.
- Public `async`/`Task<T>`/`ValueTask` are supported as **completed-result** contracts; `CancellationToken` on the public surface is not. Prefer language arrays over `List<T>` on signatures. See [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts).

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

See [Supported runtimes and package managers](supported-runtimes-and-package-managers.md) and the
[Type compatibility matrix](type-compatibility-matrix.md) for role support and type behavior.

## Next steps

1. Select the exact runtime direction in [Supported runtimes and package managers](supported-runtimes-and-package-managers.md).
2. Reduce the public contract using [Callable surface](../core-concepts/callable-surface.md) and
   [Type mapping](../core-concepts/type-mapping.md).
3. Publish once, copy package coordinates from the running Gateway/Vision, and run local and remote
   smoke tests.
4. Use the [Troubleshooting index](../troubleshooting/troubleshooting.md) for symptom-based diagnostics.
