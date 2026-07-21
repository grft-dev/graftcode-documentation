# Graftcode documentation

**Documentation** (this site) explains concepts, procedures, reference material, operations, and
troubleshooting. **[Quick start](https://docs.graftcode.com/quick-start)** on the same site contains
hands-on tutorials (expose a backend, connect a frontend, connect microservices, and more). Run
Quick start first for your stack; return here when you need to understand *why* something works or
*what* to do in production.

## Start here

1. **[Quick start](https://docs.graftcode.com/quick-start)** — first working call (hands-on).
2. [What is Graftcode?](introduction/what-is-graftcode.md) — mental model and call flow.
3. [The five-minute mental model](introduction/what-problem-does-graftcode-solve.md).
4. [Choose a scenario](introduction/when-to-use-graftcode.md) — Quick start links per goal.
5. [Quick reference](reference/quick-reference.md) — bookmark while coding.
6. [Current status and limitations](introduction/where-graftcode-fits.md).

## Core concepts

1. [Core concepts overview](core-concepts/index.md)
2. [What is a Graft?](core-concepts/what-is-a-graft.md)
3. [Callable surface](core-concepts/callable-surface.md)
4. [Public interface vs business logic](core-concepts/public-interface-vs-business-logic.md)
5. [Caller and receiver](core-concepts/caller-and-receiver.md)
6. [Static and instance context](core-concepts/static-and-instance-context.md)
7. [Graftcode Gateway](core-concepts/graftcode-gateway.md)
8. [Hypertube runtime bridge](core-concepts/hypertube-runtime-bridge.md)
9. [Graftcode Vision](core-concepts/graftcode-vision.md)
10. [Invocation lifecycle](core-concepts/invocation-lifecycle.md)
11. [Execution modes](core-concepts/execution-modes.md)
12. [Configuration resolution](core-concepts/configuration-resolution.md)
13. [Package generation](core-concepts/package-generation.md)
14. [Type mapping](core-concepts/type-mapping.md)
15. [Contract evolution](core-concepts/contract-evolution.md)
16. [Glossary](core-concepts/glossary.md)

## How-to guides

- [Expose code](how-to-guides/expose-code.md)
- [Obtain and install a Graft](how-to-guides/obtain-install-graft.md)
- [Configure invocation](how-to-guides/configure-invocation.md)
- [Run Gateway locally](how-to-guides/run-gateway-locally.md)
- [Deploy with Docker](how-to-guides/deploy-with-docker.md)
- [Use a project key](how-to-guides/project-key.md)
- [Gateway versioning and --noVersioning](how-to-guides/gateway-no-versioning.md)
- [Filter the callable surface](how-to-guides/filter-callable-surface.md)
- [Expose methods for MCP](how-to-guides/expose-mcp.md)
- [Authenticate Graft calls](how-to-guides/authenticate-graft-calls.md)
- [Stateless vs stateful calls](how-to-guides/stateless-vs-stateful.md)
- [In-memory module path](how-to-guides/inmemory-module-path.md)
- [Use Graftcode alongside REST](how-to-guides/coexist-with-rest.md)
- [Debug Graft invocations](how-to-guides/debug-graft-invocations.md)
- [Handle provider errors](how-to-guides/handle-provider-errors.md)
- [Update a provider contract](how-to-guides/update-provider-contract.md)
- [Dependency injection facades](how-to-guides/dependency-injection.md)

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

## Language guides

1. [Language support overview](language-guides/index.md)
2. [Support status](language-guides/support-status.md)
3. [.NET](language-guides/dotnet.md)
4. [Node.js and TypeScript](language-guides/nodejs-typescript.md)
5. [Java and JVM](language-guides/java-jvm.md)
6. [Python](language-guides/python.md)
7. [Ruby](language-guides/ruby.md)
8. [PHP](language-guides/php.md)
9. [Language guide template](language-guides/template.md)

## Operations

- [Operations and deployment model](operations/index.md)
- [Gateway lifecycle](operations/gateway-lifecycle.md)
- [Environment configuration](operations/environment-configuration.md)
- [Authentication and authorization](operations/authentication-authorization.md)
- [Networking and ports](operations/networking-ports.md)
- [Health checks](operations/health-checks.md)
- [Observability](operations/observability.md)
- [Timeouts and retries](operations/timeouts-retries.md)
- [Scaling](operations/scaling.md)
- [Version compatibility and upgrades](operations/version-compatibility-upgrades.md)

## Reference

- [Quick reference](reference/quick-reference.md)
- [Quick start courses](reference/quick-start-courses.md)
- [Gateway CLI](reference/gateway-cli.md)
- [Configuration keys and precedence](reference/configuration-keys-precedence.md)
- [Environment variables](reference/environment-variables.md)
- [Supported runtimes and package managers](reference/supported-runtimes-package-managers.md)
- [Type compatibility matrix](reference/type-matrix.md)
- [Errors and status codes](reference/errors-status.md)
- [Generated package structure](reference/generated-package-structure.md)
- [Ports and protocols](reference/ports-protocols.md)
- [Known limitations](reference/known-limitations.md)

## Troubleshooting

- [Troubleshooting index](troubleshooting/index.md)
- [Package installation fails](troubleshooting/package-installation.md)
- [Module, method, or type is missing](troubleshooting/module-discovery-missing-method-unsupported-type.md)
- [Connection, timeout, or authentication failure](troubleshooting/connection-timeouts-auth.md)
- [Installed package is stale](troubleshooting/stale-package.md)
- [Gateway or runtime exits](troubleshooting/runtime-exits.md)
- [Vision and runtime disagree](troubleshooting/vision-mismatch.md)

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
      - title: "The five-minute mental model"
        path: "introduction/what-problem-does-graftcode-solve.md"
        order: 2
      - title: "Choose a scenario"
        path: "introduction/when-to-use-graftcode.md"
        order: 3
      - title: "Current status and limitations"
        path: "introduction/where-graftcode-fits.md"
        order: 4
  - name: "Core concepts"
    order: 2
    path: "core-concepts"
    items:
      - title: "Overview"
        path: "core-concepts/index.md"
        order: 1
      - title: "What is a Graft?"
        path: "core-concepts/what-is-a-graft.md"
        order: 2
      - title: "Callable surface"
        path: "core-concepts/callable-surface.md"
        order: 3
      - title: "Public interface vs business logic"
        path: "core-concepts/public-interface-vs-business-logic.md"
        order: 4
      - title: "Caller and receiver"
        path: "core-concepts/caller-and-receiver.md"
        order: 5
      - title: "Static and instance context"
        path: "core-concepts/static-and-instance-context.md"
        order: 6
      - title: "Graftcode Gateway"
        path: "core-concepts/graftcode-gateway.md"
        order: 7
      - title: "Hypertube runtime bridge"
        path: "core-concepts/hypertube-runtime-bridge.md"
        order: 8
      - title: "Graftcode Vision"
        path: "core-concepts/graftcode-vision.md"
        order: 9
      - title: "Invocation lifecycle"
        path: "core-concepts/invocation-lifecycle.md"
        order: 10
      - title: "Execution modes"
        path: "core-concepts/execution-modes.md"
        order: 11
      - title: "Configuration resolution"
        path: "core-concepts/configuration-resolution.md"
        order: 12
      - title: "Package generation"
        path: "core-concepts/package-generation.md"
        order: 13
      - title: "Type mapping"
        path: "core-concepts/type-mapping.md"
        order: 14
      - title: "Contract evolution"
        path: "core-concepts/contract-evolution.md"
        order: 15
      - title: "Glossary"
        path: "core-concepts/glossary.md"
        order: 16
  - name: "How-to guides"
    order: 3
    path: "how-to-guides"
    items:
      - title: "Expose code"
        path: "how-to-guides/expose-code.md"
        order: 1
      - title: "Obtain and install a Graft"
        path: "how-to-guides/obtain-install-graft.md"
        order: 2
      - title: "Configure invocation"
        path: "how-to-guides/configure-invocation.md"
        order: 3
      - title: "Run Gateway locally"
        path: "how-to-guides/run-gateway-locally.md"
        order: 4
      - title: "Deploy with Docker"
        path: "how-to-guides/deploy-with-docker.md"
        order: 5
      - title: "Use a project key"
        path: "how-to-guides/project-key.md"
        order: 6
      - title: "Gateway versioning and --noVersioning"
        path: "how-to-guides/gateway-no-versioning.md"
        order: 7
      - title: "Filter the callable surface"
        path: "how-to-guides/filter-callable-surface.md"
        order: 8
      - title: "Expose methods for MCP"
        path: "how-to-guides/expose-mcp.md"
        order: 9
      - title: "Authenticate Graft calls"
        path: "how-to-guides/authenticate-graft-calls.md"
        order: 10
      - title: "Stateless vs stateful calls"
        path: "how-to-guides/stateless-vs-stateful.md"
        order: 11
      - title: "In-memory module path"
        path: "how-to-guides/inmemory-module-path.md"
        order: 12
      - title: "Use Graftcode alongside REST"
        path: "how-to-guides/coexist-with-rest.md"
        order: 13
      - title: "Debug Graft invocations"
        path: "how-to-guides/debug-graft-invocations.md"
        order: 14
      - title: "Handle provider errors"
        path: "how-to-guides/handle-provider-errors.md"
        order: 15
      - title: "Update a provider contract"
        path: "how-to-guides/update-provider-contract.md"
        order: 16
      - title: "Dependency injection facades"
        path: "how-to-guides/dependency-injection.md"
        order: 17
  - name: "Language guides"
    order: 4
    path: "language-guides"
    items:
      - title: "Overview"
        path: "language-guides/index.md"
        order: 1
      - title: "Support status"
        path: "language-guides/support-status.md"
        order: 2
      - title: ".NET"
        path: "language-guides/dotnet.md"
        order: 3
      - title: "Node.js and TypeScript"
        path: "language-guides/nodejs-typescript.md"
        order: 4
      - title: "Java and JVM"
        path: "language-guides/java-jvm.md"
        order: 5
      - title: "Python"
        path: "language-guides/python.md"
        order: 6
      - title: "Ruby"
        path: "language-guides/ruby.md"
        order: 7
      - title: "PHP"
        path: "language-guides/php.md"
        order: 8
      - title: "Language guide template"
        path: "language-guides/template.md"
        order: 9
  - name: "Operations"
    order: 5
    path: "operations"
    items:
      - title: "Operations and deployment model"
        path: "operations/index.md"
        order: 1
      - title: "Gateway lifecycle"
        path: "operations/gateway-lifecycle.md"
        order: 2
      - title: "Environment configuration"
        path: "operations/environment-configuration.md"
        order: 3
      - title: "Authentication and authorization"
        path: "operations/authentication-authorization.md"
        order: 4
      - title: "Networking and ports"
        path: "operations/networking-ports.md"
        order: 5
      - title: "Health checks"
        path: "operations/health-checks.md"
        order: 6
      - title: "Observability"
        path: "operations/observability.md"
        order: 7
      - title: "Timeouts and retries"
        path: "operations/timeouts-retries.md"
        order: 8
      - title: "Scaling"
        path: "operations/scaling.md"
        order: 9
      - title: "Version compatibility and upgrades"
        path: "operations/version-compatibility-upgrades.md"
        order: 10
  - name: "Reference"
    order: 6
    path: "reference"
    items:
      - title: "Quick reference"
        path: "reference/quick-reference.md"
        order: 1
      - title: "Quick start courses"
        path: "reference/quick-start-courses.md"
        order: 2
      - title: "Gateway CLI"
        path: "reference/gateway-cli.md"
        order: 3
      - title: "Configuration keys and precedence"
        path: "reference/configuration-keys-precedence.md"
        order: 4
      - title: "Environment variables"
        path: "reference/environment-variables.md"
        order: 5
      - title: "Supported runtimes and package managers"
        path: "reference/supported-runtimes-package-managers.md"
        order: 6
      - title: "Type compatibility matrix"
        path: "reference/type-matrix.md"
        order: 7
      - title: "Errors and status codes"
        path: "reference/errors-status.md"
        order: 8
      - title: "Generated package structure"
        path: "reference/generated-package-structure.md"
        order: 9
      - title: "Ports and protocols"
        path: "reference/ports-protocols.md"
        order: 10
      - title: "Known limitations"
        path: "reference/known-limitations.md"
        order: 11
  - name: "Troubleshooting"
    order: 7
    path: "troubleshooting"
    items:
      - title: "Troubleshooting index"
        path: "troubleshooting/index.md"
        order: 1
      - title: "Package installation fails"
        path: "troubleshooting/package-installation.md"
        order: 2
      - title: "Module, method, or type is missing"
        path: "troubleshooting/module-discovery-missing-method-unsupported-type.md"
        order: 3
      - title: "Connection, timeout, or authentication failure"
        path: "troubleshooting/connection-timeouts-auth.md"
        order: 4
      - title: "Installed package is stale"
        path: "troubleshooting/stale-package.md"
        order: 5
      - title: "Gateway or runtime exits"
        path: "troubleshooting/runtime-exits.md"
        order: 6
      - title: "Vision and runtime disagree"
        path: "troubleshooting/vision-mismatch.md"
        order: 7
```
