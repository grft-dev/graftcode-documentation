---
title: "Known limitations"
description: "Canonical current limitations for Graftcode runtimes, contracts, packages, security, operations, and compatibility."
keywords: "graftcode alpha, limitations, runtime support, type support, compatibility, troubleshooting"
---

# Known limitations

This is the canonical limitations page for the current release. A runtime name in Gateway, a
declaration in the analyzed surface, or a generated package by itself does not prove that the complete
Receiver-to-Caller path works. Validate the exact runtime pair, generated package, transport, and
deployment you intend to operate.

Status terms used below:

- **Verified** — supported and covered by automated tests.
- **Partial** — some paths are supported, but no complete matrix exists.
- **Unknown** — not established as a guarantee.

This page does not publish roadmap dates or links that have not been independently confirmed.

## Runtime support

### Six runtimes have a complete workflow; Perl does not

- **Scenario:** Choose a Receiver or Caller runtime.
- **Observed behavior:** .NET/CLR, Node.js/TypeScript, Java/JVM, Python 3, PHP, and Ruby have generation
  engines and cross-runtime install/invoke coverage. Gateway advertises Perl hosting, but no Perl code
  generation, package endpoint, caller coverage, or complete Receiver-to-publication path was found.
- **Workaround:** Use one of the six verified caller runtimes. Treat Perl as limited hosting only and do
  not infer a CPAN or generated-client workflow.
- **Status:** **Verified** for the six workflows; **partial** for Perl. See
  [Supported runtimes and package managers](supported-runtimes-package-managers.md).

### A runtime's accepted versions are not a universal compatibility matrix

- **Scenario:** Run Gateway with a particular framework or interpreter version.
- **Observed behavior:** Gateway documents minimum/typical versions, but the repository does not prove
  every patch version, runtime distribution, target framework, or JVM language.
- **Workaround:** Match the runtime documented by the Gateway release, then publish, install, and invoke
  a smoke-test Graft in the target environment.
- **Status:** **Partial**; Gateway runtime loading is implemented, exhaustive version coverage
  is not.

## Direction support

### Support is directional and pair-specific

- **Scenario:** A Receiver in one language is consumed from another.
- **Observed behavior:** Receiver analysis, target generation, package publication, installation, and
  invocation are separate capabilities. Passing one stage does not prove the next, and support in one
  direction does not prove the reverse direction.
- **Workaround:** Test every Receiver-to-Caller direction used by the application. Keep the generated
  package and Vision output from that run as the authority.
- **Status:** **Verified design constraint**; the public and virtual repository suites cover
  many paths, not every type and direction combination.

## Types

### Framework complex types can make package generation fail with HTTP 422

- **Scenario:** A public signature contains a framework type such as `.NET System.DateTime`.
- **Observed behavior:** Package generation classifies this as
  `FRAMEWORK_TYPE_IN_PUBLIC_API` and returns HTTP **422** (“Package not supported”), with a message such
  as “Using complex types from framework in public interfaces is not supported yet.”
- **Workaround:** Use primitives and explicitly modeled public types. Represent dates as ISO-8601
  strings and identifiers as strings unless the exact language pair is tested for a richer mapping.
- **Status:** **Verified** by the Graftcode Engine's error handling and unsupported-type tests.
  Discovery of a type is not proof that package generation accepts it.

### There is no universal supported-type matrix

- **Scenario:** Use arrays, nested models, nullability, enums, unions, maps, sets, streams, files, or
  other non-primitive values.
- **Observed behavior:** Several richer shapes are handled, but support differs across runtimes.
  Unknown values may degrade to `unknown` or `object`.
- **Workaround:** Keep the contract to primitives, arrays of supported values, and plain modeled types;
  generate and smoke-test every target package.
- **Status:** **Partial**. See [Type mapping](../core-concepts/type-mapping.md).

## Generics

### Generic metadata is not equivalent to portable generic contracts

- **Scenario:** Expose generic classes, methods, constraints, or nested generic collections.
- **Observed behavior:** For .NET, the Graftcode Engine records generic parameters and generates them, with
  complex-generic tests. No complete cross-runtime matrix proves equivalent constraints,
  variance, overloads, or nested generic mappings.
- **Workaround:** Expose a concrete facade with closed, simple contract types. Keep generic
  implementation details behind that facade.
- **Status:** **Partial**; per-runtime support exists, universal generation and
  invocation compatibility does not.

## Inheritance

### Inheritance semantics are not portable by default

- **Scenario:** Expose base classes, derived classes, interfaces with implementation inheritance, or
  polymorphic values.
- **Observed behavior:** The Graftcode Engine represents inherited or nested type information for some runtimes,
  but no complete language-pair matrix establishes constructor, member, dispatch, and serialization
  semantics for arbitrary hierarchies.
- **Workaround:** Flatten the public contract into standalone facade types and delegate to inherited
  implementation types internally.
- **Status:** **Partial/unknown** depending on the pair; validate generated output rather than
  relying on source-language inheritance.

## Constructors

### Constructors are supported selectively, not uniformly

- **Scenario:** Callers construct a remote instance, including overloaded or parameterized
  constructors.
- **Observed behavior:** For .NET and Node.js, the Graftcode Engine records and generates public constructors, and has
  constructor and overloaded-constructor coverage. This does not prove every overload shape or
  cross-runtime mapping.
- **Workaround:** Prefer one unambiguous constructor with simple parameters, or expose a static factory
  returning an explicit domain identifier.
- **Status:** **Partial**; constructor analysis/generation is verified, a universal matrix is
  not.

## Static and instance members

### Static and instance calls have different lifetime requirements

- **Scenario:** Choose between static methods and object-bound methods.
- **Observed behavior:** Both forms are represented and generated. Instance wrappers retain runtime
  object context, but no universal lifetime guarantee exists across reconnects, retries, Gateway
  restarts, transports, or language pairs. Static does not itself guarantee stateless implementation.
- **Workaround:** Prefer static operations for input-to-output services. Keep durable state behind
  explicit IDs instead of persisting remote object references.
- **Status:** **Verified** representation; **unknown** durable lifetime. See
  [Static and instance context](../core-concepts/static-and-instance-context.md).

## Async

### Async behavior is runtime-specific

- **Scenario:** Expose or consume `Task`, `Promise`, future, or awaitable methods.
- **Observed behavior:** Node-generated methods and declarations include Promise/thenable paths. This
  contradicts a universal “no async” rule. It does not prove that source-level async wrappers are valid
  in every Receiver runtime; in particular, a package can reject an unsupported framework wrapper.
- **Workaround:** Follow the generated package's exact call shape. For a public contract that must span
  runtimes, prefer the simplest supported return type and move async implementation behind the public
  boundary when required.
- **Status:** **Partial**; Node async generation is verified, universal async preservation is
  not.

## Callbacks and delegates

### Bidirectional callback, delegate, and event support has no complete matrix

- **Scenario:** Pass a callback/delegate, subscribe to an event, or rely on reverse invocation.
- **Observed behavior:** Graftcode contains delegate and callback-related handling, but no
  complete Receiver/Caller/transport matrix establishes lifecycle, reconnect, error, or browser
  behavior.
- **Workaround:** Use request/result methods for portable contracts. Introduce callbacks only after an
  end-to-end test for the exact runtimes and transport.
- **Status:** **Partial/unknown**; implementation hooks exist, universal semantics are not
  established.

## Exceptions

### Native exception type and hierarchy preservation is not guaranteed

- **Scenario:** Receiver code throws a framework or custom exception.
- **Observed behavior:** Runtime responses carry failures and generated clients wrap or rethrow them,
  but this does not guarantee that every source exception type, hierarchy, stack, and custom field
  survives every cross-runtime path.
- **Workaround:** Treat the stable error contract as explicit error codes/messages or result models;
  log Receiver details locally and test caller-side exception handling.
- **Status:** **Partial**; failure propagation exists, universal native-type equivalence does
  not.

## Package managers

### Registry coordinates and install commands are dynamic

- **Scenario:** Install a generated NuGet, npm, Maven, pip, Composer, or RubyGems package.
- **Observed behavior:** Registry IDs, package names, versions, repository paths, namespaces, and
  imports depend on the active Gateway/project and target ecosystem. A Gateway restart without a stable
  project key can produce a different registry identity.
- **Workaround:** Copy the complete command and generated import from the running Gateway/Vision. Never
  derive or reuse example coordinates.
- **Status:** **Verified** package-generation constraint.

### npm dependency behavior must be read from the generated package

- **Scenario:** Install an npm Graft and its runtime dependency.
- **Observed behavior:** Generated npm packages depend on
  `hypertube-nodejs-sdk`, and generated package metadata can declare it as a dependency.
- **Workaround:** Run the registry-qualified npm command emitted for the Graft, keep the lockfile, and
  inspect the installed package metadata if dependency resolution fails. Use only the exact dependency
  name from the generated package.
- **Status:** **Verified** current dependency name; whether a specific published artifact
  resolves it automatically is release/package specific.

## Operating systems

### There is no exhaustive OS, architecture, and native-binary guarantee

- **Scenario:** Move a Gateway or generated package across Windows, Linux, macOS, CPU architectures, or
  containers.
- **Observed behavior:** Gateway and native plugin paths contain OS-specific binary conventions, and
  some runtime tests skip particular operating systems. This is not a complete release matrix.
- **Workaround:** Build and run the smoke test on the deployment OS/architecture. Preserve generated
  install scripts and native assets; verify executable permissions and runtime availability.
- **Status:** **Partial**; multi-OS code paths exist, exhaustive release coverage is unknown.

## Transports

### Transport recognition does not prove deployment support

- **Scenario:** Use in-memory, WebSocket, secure WebSocket, HTTP/2, TCP, or a transport plugin.
- **Observed behavior:** Current resolvers recognize `inmemory`, `ws://`, `wss://`, HTTP(S) hosts ending
  in `h2`, TCP hosts, and plugin connection data. TCP and HTTP/2 Gateway listeners require their
  enabling options. Proxy, ingress, certificate, keepalive, and plugin behavior are deployment-specific.
- **Workaround:** Start with a transport documented by the running Gateway, verify its listener and
  route, then test through the actual proxy/ingress. Terminate TLS using a configuration tested for that
  deployment.
- **Status:** **Verified** parsing/listeners; **unknown** universal proxy and plugin
  compatibility.

### In-memory and remote calls do not have identical failure modes

- **Scenario:** Switch a Graft from `inmemory` to a network host.
- **Observed behavior:** Remote execution adds connection failures, timeouts, authentication, routing,
  latency, and partial failure. In-memory mode requires the Receiver module to be locally loadable.
- **Workaround:** Test both modes separately and configure the host before the first call because
  generated runtime context is cached.
- **Status:** **Verified** configuration behavior.

## Authentication

### Invocation authentication is optional, not automatic

- **Scenario:** Secure runtime calls with JWTs, headers, API keys, or project credentials.
- **Observed behavior:** A .NET JWT plugin and functional failure tests exist. Generated .NET/Node
  configuration also has header APIs. However, shipped packaging, setup, and equivalent cross-runtime
  JWT support were not established. If no authentication plugin or application validation is
  configured, no invocation authentication occurs. `--projectKey` authenticates portal/project
  metadata and must not be treated as runtime-call authorization.
- **Workaround:** Use only an authentication mechanism documented and tested for the deployed runtime;
  otherwise pass explicit credentials/context and validate before business effects. Test rejection as
  well as success. Browser WebSocket handshakes cannot set arbitrary custom headers.
- **Status:** **Verified** .NET JWT source/tests and generated header hooks; **unknown**
  distribution and cross-runtime parity.

## Observability

### Trace propagation is verified only for scoped paths

- **Scenario:** Expect a connected distributed trace and Gateway metrics.
- **Observed behavior:** W3C `traceparent`/`tracestate` behavior is tested in .NET and Node paths, and an
  OpenTelemetry demo exists. There is no guarantee of automatic end-to-end traces, backend export, logs,
  metrics, or identity correlation for every runtime and transport.
- **Workaround:** Configure your own OpenTelemetry/logging stack, verify parent/child relationships in a
  smoke test, and retain Receiver and Gateway logs.
- **Status:** **Partial**; .NET/Node propagation is verified, universal observability is not.

### Configuration has six precedence levels

- **Scenario:** A host or runtime setting appears to be ignored.
- **Observed behavior:** Current SDK priority is: runtime-specific environment, global environment,
  runtime-specific file, global file, user configuration, generated library default. There is no
  seventh `GraftSpecificDefault` level. At equal name and priority, first registration wins, and runtime
  context is cached after first initialization.
- **Workaround:** Inspect higher-priority environment/file sources and set configuration before the
  first generated call.
- **Status:** **Verified** for .NET and Node.js configuration resolution. See
  [Configuration resolution](../core-concepts/configuration-resolution.md).

## Deployment

### Gateway does not provide universal resilience

- **Scenario:** Deploy behind load balancers, service meshes, multiple replicas, or unreliable
  networks.
- **Observed behavior:** Beyond the basic `GET /status` liveness endpoint, Gateway does not provide
  universal readiness, session-affinity, failover, retry, backoff, circuit-breaker, idempotency, or
  exactly-once behavior. Retrying an invocation can repeat business effects.
- **Workaround:** Add deployment-specific health checks and resilience at an owned layer. Retry only
  operations designed and tested as idempotent; use explicit operation IDs for deduplication.
- **Status:** **Unknown** as a general guarantee; validate each topology.

### Default ports and runtime detection can fail operationally

- **Scenario:** Gateway fails to start or loads the wrong module/runtime.
- **Observed behavior:** Default ports can be occupied, blocked, or require privileges. Auto-detection
  and current-directory scanning can select unrelated files or the wrong runtime.
- **Workaround:** Provide the exact module and runtime, use available deployment ports, and confirm
  discovery and publication before installing a Graft.
- **Status:** **Verified** Gateway behavior and documented known issues.

## Compatibility

### There is no universal backward-compatibility guarantee

- **Scenario:** Upgrade Gateway, Hypertube, the Graftcode Engine, Receiver contract, or generated package.
- **Observed behavior:** The implementation contains versions and package-query paths, but no complete
  test suite proves wire, binary, source, or old-client/new-Receiver compatibility across releases and
  ecosystems. Additive source changes can still alter generated names, overloads, exports, or mappings.
- **Workaround:** Pin all participating versions, regenerate packages deliberately, compare the UGM and
  generated API, then compile and smoke-test representative Callers before rollout.
- **Status:** **Unknown** as a universal guarantee. See
  [Contract evolution](../core-concepts/contract-evolution.md).

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

- Import-based analysis can run module initialization code. Keep Receiver imports deterministic and
  free of unsafe startup side effects.
- Distribution names and import paths often differ; use the exact import emitted by Vision.

**Ruby**

- The package name and require name can use different normalization; use the emitted require name.
- Prefer current Gateway output for generated module paths and report mismatches.

**PHP**

- Composer packages may run post-install steps; retain the generated package scripts.
- Verify the generated autoload path rather than relying on autoloading alone in older packages.

See [Supported runtimes and package managers](supported-runtimes-package-managers.md) and the
[Type compatibility matrix](type-matrix.md) for role support and type behavior.

## Production readiness

### Alpha is not a blanket production-readiness certification

- **Scenario:** Decide whether a workload is ready for production.
- **Observed behavior:** Working E2E paths exist, but support matrices for advanced types, all runtime
  pairs, security distribution, upgrades, retries, high availability, observability, and every
  deployment platform are incomplete.
- **Workaround:** Define and test a narrow supported profile: exact Receiver/Caller versions, simple
  contract, package lock, transport/TLS/auth setup, timeout behavior, failure handling, observability,
  restart behavior, capacity, rollback, and contract-upgrade procedure.
- **Status:** **Partial**. Production suitability is workload- and deployment-specific.

## Next steps

1. Select the exact runtime direction in [Supported runtimes and package managers](supported-runtimes-package-managers.md).
2. Reduce the public contract using [Callable surface](../core-concepts/callable-surface.md) and
   [Type mapping](../core-concepts/type-mapping.md).
3. Publish once, copy package coordinates from the running Gateway/Vision, and run local and remote
   smoke tests.
4. Use the [Troubleshooting index](../troubleshooting/index.md) for symptom-based diagnostics.
