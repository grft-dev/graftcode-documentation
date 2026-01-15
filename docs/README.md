# Graftcode Documentation

## Table of Contents

This file defines the documentation structure and ordering. Categories can be nested to any depth.

### Structure Format

Each category entry follows this format:
- `### N. Category Name` - Top-level category (N = category order)
- `#### N.M. Subcategory Name` - Nested subcategory (M = subcategory order within parent)
- `N.M.P. [Title](path/to/file.md)` - Article (P = article order within subcategory)

### Documentation Tree

### Introduction
1. [What is Graftcode](introduction/what-is-graftcode.md)
2. [What problem does Graftcode solve](introduction/what-problem-does-graftcode-solve.md)
3. [Where Graftcode fits](introduction/where-graftcode-fits.md)
4. [When to use Graftcode](introduction/when-to-use-graftcode.md)

### Core-Concepts

1. [What is a Graft](core-concepts/what-is-a-graft.md)
2. [Public Interface bs Business Logic](core-concepts/public-interface-vs-business-logic.md)
3. [Caller and Receiver](core-concepts/caller-and-receiver.md)
4. [Graftcode Gateway](core-concepts/graftcode-gateway.md)
5. [Hypertube Runtime Bridge](core-concepts/hypertube-runtime-bridge.md)
6. [Graftcode Vision](core-concepts/graftcode-vision.md)

### How Graftcode Works
1. [Development-time vs production-time behavior](how-graftcode-works/development-time-vs-production-time.md)
2. [What goes to Graftcode Cloud](how-graftcode-works/what-goes-to-graftcode-cloud.md)
3. [How Grafts are generated](how-graftcode-works/how-grafts-are-generated.md)
4. [Runtime call execution](how-graftcode-works/runtime-call-execution.md)
5. [Local, remote, and in-memory execution](how-graftcode-works/local-remote-and-in-memory-execution.md)
6. [Observability, tracing, and context propagation](how-graftcode-works/observability-tracing-and-context-propagation.md)
7. [Scaling, load balancers, and proxies](how-graftcode-works/scaling-load-balancers-and-proxies.md)
8. [What happens when interfaces change](how-graftcode-works/what-happens-when-interfaces-change.md)

### Integration Patterns
1. [Service-to-Service Integration](integration-patterns/service-to-service-integration.md)
2. [Edge Clients Without APIs](integration-patterns/edge-clients-without-apis.md)
3. [Internal Business APIs](integration-patterns/internal-business-apis.md)
4. [MCP Hosting and AI Tools](integration-patterns/mcp-hosting-and-ai-tools.md)
5. [Modular Monoliths](integration-patterns/modular-monoliths.md)
6. [Microservices Without Contracts](integration-patterns/microservices-without-contracts.md)
7. [Event-Driven Communication (Preview)](integration-patterns/event-driven-communication-preview.md)

### Security and Trust
1. [Security Model Overview](security-and-trust/security-model-overview.md)
2. [Authentication and Authorization](security-and-trust/authentication-and-authorization.md)
3. [Security Plugins](security-and-trust/security-plugins.md)
4. [Transport Security TLS/WSS](security-and-trust/transport-security-tls-wss.md)
5. [Network Boundaries and Isolation](security-and-trust/network-boundaries-and-isolation.md)
6. [Enterprise Self-Hosted Engine](security-and-trust/enterprise-self-hosted-engine.md)

### 6. Reference
1. [Quick Reference](reference/quick-reference.md)

---

## Machine-Readable Structure (YAML)

```yaml
categories:
  - name: "Introduction"
    order: 1
    path: "introduction"
    items:
      - title: "What is Graftcode"
        path: "introduction/what-is-graftcode.md"
        order: 1
      - title: "What problem does Graftcode solve"
        path: "introduction/what-problem-does-graftcode-solve.md"
        order: 2
      - title: "Where Graftcode fits"
        path: "introduction/where-graftcode-fits.md"
        order: 3
      - title: "When to use Graftcode"
        path: "introduction/when-to-use-graftcode.md"
        order: 4

  - name: "Core Concepts"
    order: 2
    path: "core-concepts"
    items:
      - title: "What is a Graft"
        path: "core-concepts/what-is-a-graft.md"
        order: 1
      - title: "Public Interface vs Business Logic"
        path: "core-concepts/public-interface-vs-business-logic.md"
        order: 2
      - title: "Caller and Receiver"
        path: "core-concepts/caller-and-receiver.md"
        order: 3
      - title: "Graftcode Gateway"
        path: "core-concepts/graftcode-gateway.md"
        order: 4
      - title: "Hypertube Runtime Bridge"
        path: "core-concepts/hypertube-runtime-bridge.md"
        order: 5
      - title: "Graftcode Vision"
        path: "core-concepts/graftcode-vision.md"
        order: 6

  - name: "How Graftcode Works"
    order: 3
    path: "how-graftcode-works"
    items:
      - title: "Development-time vs production-time behavior"
        path: "how-graftcode-works/development-time-vs-production-time.md"
        order: 1
      - title: "What goes to Graftcode Cloud"
        path: "how-graftcode-works/what-goes-to-graftcode-cloud.md"
        order: 2
      - title: "How Grafts are generated"
        path: "how-graftcode-works/how-grafts-are-generated.md"
        order: 3
      - title: "Runtime call execution"
        path: "how-graftcode-works/runtime-call-execution.md"
        order: 4
      - title: "Local, remote, and in-memory execution"
        path: "how-graftcode-works/local-remote-and-in-memory-execution.md"
        order: 5
      - title: "Observability, tracing, and context propagation"
        path: "how-graftcode-works/observability-tracing-and-context-propagation.md"
        order: 6
      - title: "Scaling, load balancers, and proxies"
        path: "how-graftcode-works/scaling-load-balancers-and-proxies.md"
        order: 7
      - title: "What happens when interfaces change"
        path: "how-graftcode-works/what-happens-when-interfaces-change.md"
        order: 8

  - name: "Integration Patterns"
    order: 4
    path: "integration-patterns"
    items:
      - title: "Service-to-Service Integration"
        path: "integration-patterns/service-to-service-integration.md"
        order: 1
      - title: "Edge Clients Without APIs"
        path: "integration-patterns/edge-clients-without-apis.md"
        order: 2
      - title: "Internal Business APIs"
        path: "integration-patterns/internal-business-apis.md"
        order: 3
      - title: "MCP Hosting and AI Tools"
        path: "integration-patterns/mcp-hosting-and-ai-tools.md"
        order: 4
      - title: "Modular Monoliths"
        path: "integration-patterns/modular-monoliths.md"
        order: 5
      - title: "Microservices Without Contracts"
        path: "integration-patterns/microservices-without-contracts.md"
        order: 6
      - title: "Event-Driven Communication (Preview)"
        path: "integration-patterns/event-driven-communication-preview.md"
        order: 7

  - name: "Security and Trust"
    order: 5
    path: "security-and-trust"
    items:
      - title: "Security Model Overview"
        path: "security-and-trust/security-model-overview.md"
        order: 1
      - title: "Authentication and Authorization"
        path: "security-and-trust/authentication-and-authorization.md"
        order: 2
      - title: "Security Plugins"
        path: "security-and-trust/security-plugins.md"
        order: 3
      - title: "Transport Security TLS/WSS"
        path: "security-and-trust/transport-security-tls-wss.md"
        order: 4
      - title: "Network Boundaries and Isolation"
        path: "security-and-trust/network-boundaries-and-isolation.md"
        order: 5
      - title: "Enterprise Self-Hosted Engine"
        path: "security-and-trust/enterprise-self-hosted-engine.md"
        order: 6

  - name: "Reference"
    order: 6
    path: "reference"
    items:
      - title: "Quick Reference"
        path: "reference/quick-reference.md"
        order: 1
```
