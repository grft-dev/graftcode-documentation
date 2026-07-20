# Graftcode documentation

Start with a working cross-language call, then use concepts and guides when you need to make a design
decision. This file is both the human learning path and the source for generated navigation.

## Start here

1. [What is Graftcode?](introduction/what-is-graftcode.md)
2. [The five-minute mental model](introduction/what-problem-does-graftcode-solve.md)
3. [Choose a scenario](introduction/when-to-use-graftcode.md)
4. [Current status and limitations](introduction/where-graftcode-fits.md)

## Tutorials

1. [Call a .NET BillingService from Node.js](tutorials/dotnet-to-nodejs.md)

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
- [Handle provider errors](how-to-guides/handle-provider-errors.md)
- [Update a provider contract](how-to-guides/update-provider-contract.md)
- [Service-to-service integration](integration-patterns/service-to-service-integration.md)
- [Edge clients without APIs](integration-patterns/edge-clients-without-apis.md)
- [Internal business APIs](integration-patterns/internal-business-apis.md)
- [MCP hosting and AI tools](integration-patterns/mcp-hosting-and-ai-tools.md)
- [Modular monoliths](integration-patterns/modular-monoliths.md)
- [Microservices without contracts](integration-patterns/microservices-without-contracts.md)
- [Event-driven communication preview](integration-patterns/event-driven-communication-preview.md)
- [Dependency injection in .NET](architecture-and-patterns/dependency-injection/csharp-netcore.md)
- [Zero-boilerplate microservices fabric](use-cases/zero-boilerplate-microservices-fabric.md)
- [MCP server without MCP boilerplate](use-cases/mcp-server-without-mcp-boilerplate.md)

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
- [Development-time vs production-time behavior](how-graftcode-works/development-time-vs-production-time.md)
- [What goes to Graftcode Cloud](how-graftcode-works/what-goes-to-graftcode-cloud.md)
- [How Grafts are generated](how-graftcode-works/how-grafts-are-generated.md)
- [Runtime call execution](how-graftcode-works/runtime-call-execution.md)
- [Local, remote, and in-memory execution](how-graftcode-works/local-remote-and-in-memory-execution.md)
- [Observability, tracing, and context propagation](how-graftcode-works/observability-tracing-and-context-propagation.md)
- [Scaling, load balancers, and proxies](how-graftcode-works/scaling-load-balancers-and-proxies.md)
- [What happens when interfaces change](how-graftcode-works/what-happens-when-interfaces-change.md)
- [Security model overview](security-and-trust/security-model-overview.md)
- [Authentication and authorization](security-and-trust/authentication-and-authorization.md)
- [Graftcode Context](security-and-trust/graftcode-context.md)
- [Security plugins](security-and-trust/security-plugins.md)
- [Transport security: TLS and WSS](security-and-trust/transport-security-tls-wss.md)
- [Network boundaries and isolation](security-and-trust/network-boundaries-and-isolation.md)
- [Enterprise self-hosted engine](security-and-trust/enterprise-self-hosted-engine.md)
- [Compare performance](performance-and-efficiency/compare-performance.md)
- [Why runtime-level integration is faster](performance-and-efficiency/why-runtime-level-integration-is-faster.md)
- [REST vs gRPC vs Graftcode](performance-and-efficiency/rest-vs-grpc-vs-graftcode.md)
- [CPU, memory, and network usage](performance-and-efficiency/cpu-memory-and-network-usage.md)
- [Cloud cost implications](performance-and-efficiency/cloud-cost-implications.md)
- [When performance gains matter](performance-and-efficiency/when-performance-gains-matter.md)

## Reference

- [Quick reference](reference/quick-reference.md)
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
- [Alpha limitations and known constraints](how-graftcode-works/alpha-limitations-and-known-constraints.md)
- [Language support status](language-guides/support-status.md)
- Runtime-specific troubleshooting is included in each [language guide](language-guides/index.md).

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
  - name: "Tutorials"
    order: 2
    path: "tutorials"
    items:
      - title: "Call a .NET BillingService from Node.js"
        path: "tutorials/dotnet-to-nodejs.md"
        order: 1
  - name: "Core concepts"
    order: 3
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
    order: 4
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
      - title: "Handle provider errors"
        path: "how-to-guides/handle-provider-errors.md"
        order: 6
      - title: "Update a provider contract"
        path: "how-to-guides/update-provider-contract.md"
        order: 7
      - title: "Service-to-service integration"
        path: "integration-patterns/service-to-service-integration.md"
        order: 8
      - title: "Edge clients without APIs"
        path: "integration-patterns/edge-clients-without-apis.md"
        order: 9
      - title: "Internal business APIs"
        path: "integration-patterns/internal-business-apis.md"
        order: 10
      - title: "MCP hosting and AI tools"
        path: "integration-patterns/mcp-hosting-and-ai-tools.md"
        order: 11
      - title: "Modular monoliths"
        path: "integration-patterns/modular-monoliths.md"
        order: 12
      - title: "Microservices without contracts"
        path: "integration-patterns/microservices-without-contracts.md"
        order: 13
      - title: "Event-driven communication preview"
        path: "integration-patterns/event-driven-communication-preview.md"
        order: 14
      - title: "Dependency injection in .NET"
        path: "architecture-and-patterns/dependency-injection/csharp-netcore.md"
        order: 15
      - title: "Zero-boilerplate microservices fabric"
        path: "use-cases/zero-boilerplate-microservices-fabric.md"
        order: 16
      - title: "MCP server without MCP boilerplate"
        path: "use-cases/mcp-server-without-mcp-boilerplate.md"
        order: 17
  - name: "Language guides"
    order: 5
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
    order: 6
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
      - title: "Development-time vs production-time"
        path: "how-graftcode-works/development-time-vs-production-time.md"
        order: 11
      - title: "What goes to Graftcode Cloud"
        path: "how-graftcode-works/what-goes-to-graftcode-cloud.md"
        order: 12
      - title: "How Grafts are generated"
        path: "how-graftcode-works/how-grafts-are-generated.md"
        order: 13
      - title: "Runtime call execution"
        path: "how-graftcode-works/runtime-call-execution.md"
        order: 14
      - title: "Local, remote, and in-memory execution"
        path: "how-graftcode-works/local-remote-and-in-memory-execution.md"
        order: 15
      - title: "Observability and context propagation"
        path: "how-graftcode-works/observability-tracing-and-context-propagation.md"
        order: 16
      - title: "Scaling, load balancers, and proxies"
        path: "how-graftcode-works/scaling-load-balancers-and-proxies.md"
        order: 17
      - title: "Interface changes"
        path: "how-graftcode-works/what-happens-when-interfaces-change.md"
        order: 18
      - title: "Security model"
        path: "security-and-trust/security-model-overview.md"
        order: 19
      - title: "Authentication and authorization"
        path: "security-and-trust/authentication-and-authorization.md"
        order: 20
      - title: "Graftcode Context"
        path: "security-and-trust/graftcode-context.md"
        order: 21
      - title: "Security plugins"
        path: "security-and-trust/security-plugins.md"
        order: 22
      - title: "TLS and WSS"
        path: "security-and-trust/transport-security-tls-wss.md"
        order: 23
      - title: "Network boundaries"
        path: "security-and-trust/network-boundaries-and-isolation.md"
        order: 24
      - title: "Enterprise self-hosted engine"
        path: "security-and-trust/enterprise-self-hosted-engine.md"
        order: 25
      - title: "Compare performance"
        path: "performance-and-efficiency/compare-performance.md"
        order: 26
      - title: "Runtime-level performance"
        path: "performance-and-efficiency/why-runtime-level-integration-is-faster.md"
        order: 27
      - title: "REST vs gRPC vs Graftcode"
        path: "performance-and-efficiency/rest-vs-grpc-vs-graftcode.md"
        order: 28
      - title: "CPU, memory, and network"
        path: "performance-and-efficiency/cpu-memory-and-network-usage.md"
        order: 29
      - title: "Cloud cost implications"
        path: "performance-and-efficiency/cloud-cost-implications.md"
        order: 30
      - title: "When performance gains matter"
        path: "performance-and-efficiency/when-performance-gains-matter.md"
        order: 31
  - name: "Reference"
    order: 7
    path: "reference"
    items:
      - title: "Quick reference"
        path: "reference/quick-reference.md"
        order: 1
      - title: "Gateway CLI"
        path: "reference/gateway-cli.md"
        order: 2
      - title: "Configuration keys and precedence"
        path: "reference/configuration-keys-precedence.md"
        order: 3
      - title: "Environment variables"
        path: "reference/environment-variables.md"
        order: 4
      - title: "Supported runtimes and package managers"
        path: "reference/supported-runtimes-package-managers.md"
        order: 5
      - title: "Type compatibility matrix"
        path: "reference/type-matrix.md"
        order: 6
      - title: "Errors and status codes"
        path: "reference/errors-status.md"
        order: 7
      - title: "Generated package structure"
        path: "reference/generated-package-structure.md"
        order: 8
      - title: "Ports and protocols"
        path: "reference/ports-protocols.md"
        order: 9
      - title: "Known limitations"
        path: "reference/known-limitations.md"
        order: 10
  - name: "Troubleshooting"
    order: 8
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
      - title: "Alpha limitations and known constraints"
        path: "how-graftcode-works/alpha-limitations-and-known-constraints.md"
        order: 8
```
