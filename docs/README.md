# Graftcode documentation

**Documentation** (this site) explains concepts, procedures, reference material, operations, and
troubleshooting. **[Quick start](https://docs.graftcode.com/quick-start)** on the same site contains
hands-on tutorials (expose a backend, connect a frontend, connect microservices, and more). Run
Quick start first for your stack; return here when you need to understand *why* something works or
*what* to do in production.

## Start here

1. **[Quick start](https://docs.graftcode.com/quick-start)** — first working call (hands-on).
2. [What is Graftcode?](introduction/what-is-graftcode.md) — definition, before/after, and use cases.
3. [How Graftcode works](introduction/how-graftcode-works.md) — the How it works diagram and mental model.
4. [Choose your scenario](introduction/choose-your-scenario.md) — pick your goal, then your runtime.
5. [Quick Reference](reference/quick-reference.md) — bookmark while coding.
6. [Where does Graftcode fit?](introduction/where-does-graftcode-fit.md).

## Core concepts

1. [What is a Graft?](core-concepts/what-is-a-graft.md)
2. [Callable surface](core-concepts/callable-surface.md)
3. [Public surface vs implementation](core-concepts/public-surface-vs-implementation.md)
4. [Caller and receiver](core-concepts/caller-and-receiver.md)
5. [Static and instance context](core-concepts/static-and-instance-context.md)
6. [Gateway and hosted modules](core-concepts/gateway-and-hosted-modules.md)
7. [Hypertube runtime bridge](core-concepts/hypertube-runtime-bridge.md)
8. [Graftcode Vision](core-concepts/graftcode-vision.md)
9. [Invocation lifecycle](core-concepts/invocation-lifecycle.md)
10. [In-memory, same-machine, and remote execution](core-concepts/in-memory-same-machine-and-remote-execution.md)
11. [Configuration resolution](core-concepts/configuration-resolution.md)
12. [Package generation](core-concepts/package-generation.md)
13. [Type mapping](core-concepts/type-mapping.md)
14. [Contract evolution](core-concepts/contract-evolution.md)
15. [Core-concepts glossary](core-concepts/core-concepts-glossary.md)
16. [Graftcode context](core-concepts/graftcode-context.md)

## How-to guides

- [Expose code as a Graftcode Receiver](how-to-guides/expose-code-as-a-graftcode-receiver.md)
- [Obtain and install a Graft](how-to-guides/obtain-and-install-a-graft.md)
- [Configure Graft invocation](how-to-guides/configure-graft-invocation.md)
- [Run Gateway locally](how-to-guides/run-gateway-locally.md)
- [Deploy Gateway with Docker](how-to-guides/deploy-gateway-with-docker.md)
- [Use a portal project key](how-to-guides/use-a-portal-project-key.md)
- [Gateway module versioning and --noVersioning](how-to-guides/gateway-module-versioning-and-noversioning.md)
- [Filter the callable surface](how-to-guides/filter-the-callable-surface.md)
- [Expose Receiver methods for MCP](how-to-guides/expose-receiver-methods-for-mcp.md)
- [Authenticate Graft calls](how-to-guides/authenticate-graft-calls.md)
- [Stateless vs stateful Graft calls](how-to-guides/stateless-vs-stateful-graft-calls.md)
- [Set the module path for in-memory execution](how-to-guides/set-the-module-path-for-in-memory-execution.md)
- [Use Graftcode alongside an existing REST API](how-to-guides/use-graftcode-alongside-an-existing-rest-api.md)
- [Debug Graft invocations](how-to-guides/debug-graft-invocations.md)
- [Handle Receiver errors](how-to-guides/handle-receiver-errors.md)
- [Update a Receiver contract](how-to-guides/update-a-receiver-contract.md)
- [Dependency injection with stateless facades](how-to-guides/dependency-injection-with-stateless-facades.md)

### Authoring multi-runtime snippets

Use **one file with `multi` code fences** when only code differs by runtime (how-to guides,
reference shortcuts, operations, troubleshooting). The portal renders a tab picker inside each
snippet (`.NET`, `JavaScript`, `Python`, `Java`, `PHP`, `Ruby`) instead of a page-level stack picker:

````markdown
```multi
```dotnet
// .NET example
```
```javascript
// Node example
```
```python
# Python example
```
```java
// Java example
```
```php
// PHP example
```
```ruby
# Ruby example
```
```
````

Use a **folder per runtime** (`how-to-guides/<slug>/dotnet.md`, …) only when prose or steps
materially differ by stack. Regenerate consolidated guides with `scripts/consolidate-howto-articles.py`.

## Operations

- [Operations and deployment model](operations/operations-and-deployment-model.md)
- [Gateway lifecycle](operations/gateway-lifecycle.md)
- [Environment and configuration](operations/environment-and-configuration.md)
- [Authentication and authorization operations](operations/authentication-and-authorization-operations.md)
- [Networking and ports](operations/networking-and-ports.md)
- [Health checks](operations/health-checks.md)
- [Logging, metrics, and tracing](operations/logging-metrics-and-tracing.md)
- [Timeouts and retries](operations/timeouts-and-retries.md)
- [Scaling Gateway Receivers](operations/scaling-gateway-receivers.md)
- [Version compatibility and upgrades](operations/version-compatibility-and-upgrades.md)

## Reference

- [Quick Reference](reference/quick-reference.md)
- [Quick start courses](reference/quick-start-courses.md)
- [Project Key, registry, host, and credentials](reference/project-key-registry-host-and-credentials.md)
- [Gateway CLI reference](reference/gateway-cli-reference.md)
- [Configuration keys and precedence](reference/configuration-keys-and-precedence.md)
- [Environment variable reference](reference/environment-variable-reference.md)
- [Supported runtimes and package managers](reference/supported-runtimes-and-package-managers.md)
- [Type compatibility matrix](reference/type-compatibility-matrix.md)
- [Errors and status reference](reference/errors-and-status-reference.md)
- [Generated package structure](reference/generated-package-structure.md)
- [Ports and protocols reference](reference/ports-and-protocols-reference.md)
- [Known limitations](reference/known-limitations.md)

## Troubleshooting

- [Troubleshooting](troubleshooting/troubleshooting.md)
- [Package installation fails](troubleshooting/package-installation-fails.md)
- [Module, method, or type is missing](troubleshooting/module-method-or-type-is-missing.md)
- [Connection, timeout, or authentication failure](troubleshooting/connection-timeout-or-authentication-failure.md)
- [Installed package is stale](troubleshooting/installed-package-is-stale.md)
- [Gateway or runtime exits](troubleshooting/gateway-or-runtime-exits.md)
- [Vision and runtime disagree](troubleshooting/vision-and-runtime-disagree.md)
- [In-memory execution and Hypertube exceptions](troubleshooting/in-memory-hypertube-exceptions.md)

## Machine-readable navigation

```yaml
categories:
  - name: "Start here"
    order: 1
    path: "introduction"
    items:
      - title: "What is Graftcode?"
        path: "introduction/what-is-graftcode.md"
        order: 1
      - title: "How Graftcode works"
        path: "introduction/how-graftcode-works.md"
        order: 2
      - title: "Choose your scenario"
        path: "introduction/choose-your-scenario.md"
        order: 3
      - title: "Where does Graftcode fit?"
        path: "introduction/where-does-graftcode-fit.md"
        order: 4
  - name: "Core concepts"
    order: 2
    path: "core-concepts"
    items:
      - title: "What is a Graft?"
        path: "core-concepts/what-is-a-graft.md"
        order: 1
      - title: "Callable surface"
        path: "core-concepts/callable-surface.md"
        order: 2
      - title: "Public surface vs implementation"
        path: "core-concepts/public-surface-vs-implementation.md"
        order: 3
      - title: "Caller and receiver"
        path: "core-concepts/caller-and-receiver.md"
        order: 4
      - title: "Static and instance context"
        path: "core-concepts/static-and-instance-context.md"
        order: 5
      - title: "Gateway and hosted modules"
        path: "core-concepts/gateway-and-hosted-modules.md"
        order: 6
      - title: "Hypertube runtime bridge"
        path: "core-concepts/hypertube-runtime-bridge.md"
        order: 7
      - title: "Graftcode Vision"
        path: "core-concepts/graftcode-vision.md"
        order: 8
      - title: "Invocation lifecycle"
        path: "core-concepts/invocation-lifecycle.md"
        order: 9
      - title: "In-memory, same-machine, and remote execution"
        path: "core-concepts/in-memory-same-machine-and-remote-execution.md"
        order: 10
      - title: "Configuration resolution"
        path: "core-concepts/configuration-resolution.md"
        order: 11
      - title: "Package generation"
        path: "core-concepts/package-generation.md"
        order: 12
      - title: "Type mapping"
        path: "core-concepts/type-mapping.md"
        order: 13
      - title: "Contract evolution"
        path: "core-concepts/contract-evolution.md"
        order: 14
      - title: "Core-concepts glossary"
        path: "core-concepts/core-concepts-glossary.md"
        order: 15
      - title: "Graftcode Context library"
        path: "core-concepts/graftcode-context.md"
        order: 16
  - name: "How-to guides"
    order: 3
    path: "how-to-guides"
    items:
      - title: "Expose code as a Graftcode Receiver"
        path: "how-to-guides/expose-code-as-a-graftcode-receiver.md"
        order: 1
      - title: "Obtain and install a Graft"
        path: "how-to-guides/obtain-and-install-a-graft.md"
        order: 2
      - title: "Configure Graft invocation"
        path: "how-to-guides/configure-graft-invocation.md"
        order: 3
      - title: "Run Gateway locally"
        path: "how-to-guides/run-gateway-locally.md"
        order: 4
      - title: "Deploy Gateway with Docker"
        path: "how-to-guides/deploy-gateway-with-docker.md"
        order: 5
      - title: "Use a portal project key"
        path: "how-to-guides/use-a-portal-project-key.md"
        order: 6
      - title: "Gateway module versioning and --noVersioning"
        path: "how-to-guides/gateway-module-versioning-and-noversioning.md"
        order: 7
      - title: "Filter the callable surface"
        path: "how-to-guides/filter-the-callable-surface.md"
        order: 8
      - title: "Expose Receiver methods for MCP"
        path: "how-to-guides/expose-receiver-methods-for-mcp.md"
        order: 9
      - title: "Authenticate Graft calls"
        path: "how-to-guides/authenticate-graft-calls.md"
        order: 10
      - title: "Stateless vs stateful Graft calls"
        path: "how-to-guides/stateless-vs-stateful-graft-calls.md"
        order: 11
      - title: "Set the module path for in-memory execution"
        path: "how-to-guides/set-the-module-path-for-in-memory-execution.md"
        order: 12
      - title: "Use Graftcode alongside an existing REST API"
        path: "how-to-guides/use-graftcode-alongside-an-existing-rest-api.md"
        order: 13
      - title: "Debug Graft invocations"
        path: "how-to-guides/debug-graft-invocations.md"
        order: 14
      - title: "Handle Receiver errors"
        path: "how-to-guides/handle-receiver-errors.md"
        order: 15
      - title: "Update a Receiver contract"
        path: "how-to-guides/update-a-receiver-contract.md"
        order: 16
      - title: "Dependency injection with stateless facades"
        path: "how-to-guides/dependency-injection-with-stateless-facades.md"
        order: 17
  - name: "Operations"
    order: 4
    path: "operations"
    items:
      - title: "Operations and deployment model"
        path: "operations/operations-and-deployment-model.md"
        order: 1
      - title: "Gateway lifecycle"
        path: "operations/gateway-lifecycle.md"
        order: 2
      - title: "Environment and configuration"
        path: "operations/environment-and-configuration.md"
        order: 3
      - title: "Authentication and authorization operations"
        path: "operations/authentication-and-authorization-operations.md"
        order: 4
      - title: "Networking and ports"
        path: "operations/networking-and-ports.md"
        order: 5
      - title: "Health checks"
        path: "operations/health-checks.md"
        order: 6
      - title: "Logging, metrics, and tracing"
        path: "operations/logging-metrics-and-tracing.md"
        order: 7
      - title: "Timeouts and retries"
        path: "operations/timeouts-and-retries.md"
        order: 8
      - title: "Scaling Gateway Receivers"
        path: "operations/scaling-gateway-receivers.md"
        order: 9
      - title: "Version compatibility and upgrades"
        path: "operations/version-compatibility-and-upgrades.md"
        order: 10
  - name: "Reference"
    order: 5
    path: "reference"
    items:
      - title: "Quick Reference"
        path: "reference/quick-reference.md"
        order: 1
      - title: "Quick start courses"
        path: "reference/quick-start-courses.md"
        order: 2
      - title: "Project Key, registry, host, and credentials"
        path: "reference/project-key-registry-host-and-credentials.md"
        order: 3
      - title: "Gateway CLI reference"
        path: "reference/gateway-cli-reference.md"
        order: 4
      - title: "Configuration keys and precedence"
        path: "reference/configuration-keys-and-precedence.md"
        order: 5
      - title: "Environment variable reference"
        path: "reference/environment-variable-reference.md"
        order: 6
      - title: "Supported runtimes and package managers"
        path: "reference/supported-runtimes-and-package-managers.md"
        order: 7
      - title: "Type compatibility matrix"
        path: "reference/type-compatibility-matrix.md"
        order: 8
      - title: "Errors and status reference"
        path: "reference/errors-and-status-reference.md"
        order: 9
      - title: "Generated package structure"
        path: "reference/generated-package-structure.md"
        order: 10
      - title: "Ports and protocols reference"
        path: "reference/ports-and-protocols-reference.md"
        order: 11
      - title: "Known limitations"
        path: "reference/known-limitations.md"
        order: 12
  - name: "Troubleshooting"
    order: 6
    path: "troubleshooting"
    items:
      - title: "Troubleshooting"
        path: "troubleshooting/troubleshooting.md"
        order: 1
      - title: "Package installation fails"
        path: "troubleshooting/package-installation-fails.md"
        order: 2
      - title: "Module, method, or type is missing"
        path: "troubleshooting/module-method-or-type-is-missing.md"
        order: 3
      - title: "Connection, timeout, or authentication failure"
        path: "troubleshooting/connection-timeout-or-authentication-failure.md"
        order: 4
      - title: "Installed package is stale"
        path: "troubleshooting/installed-package-is-stale.md"
        order: 5
      - title: "Gateway or runtime exits"
        path: "troubleshooting/gateway-or-runtime-exits.md"
        order: 6
      - title: "Vision and runtime disagree"
        path: "troubleshooting/vision-and-runtime-disagree.md"
        order: 7
      - title: "In-memory execution and Hypertube exceptions"
        path: "troubleshooting/in-memory-hypertube-exceptions.md"
        order: 8
```
