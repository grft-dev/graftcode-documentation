# Graftcode Documentation

## Table of Contents

This file defines the documentation structure and ordering. Categories can be nested to any depth.

### Structure Format

Each category entry follows this format:
- `### N. Category Name` - Top-level category (N = category order)
- `#### N.M. Subcategory Name` - Nested subcategory (M = subcategory order within parent)
- `N.M.P. [Title](path/to/file.md)` - Article (P = article order within subcategory)

### Documentation Tree

### 1. Getting Started
1. [Graftcode Introduction](getting-started/introduction.md)
2. [Installation](getting-started/installation.md)
3. [Quick Start](getting-started/quick-start.md)

### 2. Concepts
1. [Core Concepts](concepts/core-concepts.md)
2. [Integration Scenarios](concepts/integration-scenarios.md)

### 3. Guides
1. [Configuration](guides/configuration.md)
2. [Examples](guides/examples.md)
3. [Troubleshooting](guides/troubleshooting.md)
4. [Best Practices](guides/best-practices.md)

### 4. Testing
1. [Testing Overview](testing/overview.md)
2. [Testing Setup](testing/setup.md)
3. [Unit Testing](testing/unit-testing.md)
4. [Integration Testing](testing/integration-testing.md)
5. [End-to-End Testing](testing/e2e-testing.md)
6. [Performance Testing](testing/performance-testing.md)
7. [Mocking and Stubbing](testing/mocking.md)
8. [Test Utilities](testing/test-utilities.md)
9. [CI/CD Integration](testing/cicd.md)
10. [Testing Best Practices](testing/best-practices.md)

### 5. API Reference
#### 5.1. Gateway
1. [Gateway CLI](api/gateway/cli.md)
2. [Gateway HTTP API](api/gateway/http.md)

#### 5.2. Client SDK
1. [Client SDK API](api/client-sdk-api.md)
2. [Configuration API](api/configuration-api.md)
3. [Error Handling](api/error-handling.md)
4. [Type Definitions](api/type-definitions.md)
5. [Events and Hooks](api/events-hooks.md)

### 6. Reference
1. [Quick Reference](reference/quick-reference.md)

---

## Machine-Readable Structure (YAML)

```yaml
categories:
  - name: "Getting Started"
    order: 1
    path: "getting-started"
    items:
      - title: "Graftcode Introduction"
        path: "getting-started/introduction.md"
        order: 1
      - title: "Installation"
        path: "getting-started/installation.md"
        order: 2
      - title: "Quick Start"
        path: "getting-started/quick-start.md"
        order: 3
  
  - name: "Concepts"
    order: 2
    path: "concepts"
    items:
      - title: "Core Concepts"
        path: "concepts/core-concepts.md"
        order: 1
      - title: "Integration Scenarios"
        path: "concepts/integration-scenarios.md"
        order: 2
  
  - name: "Guides"
    order: 3
    path: "guides"
    items:
      - title: "Configuration"
        path: "guides/configuration.md"
        order: 1
      - title: "Examples"
        path: "guides/examples.md"
        order: 2
      - title: "Troubleshooting"
        path: "guides/troubleshooting.md"
        order: 3
      - title: "Best Practices"
        path: "guides/best-practices.md"
        order: 4
  
  - name: "Testing"
    order: 4
    path: "testing"
    items:
      - title: "Testing Overview"
        path: "testing/overview.md"
        order: 1
      - title: "Testing Setup"
        path: "testing/setup.md"
        order: 2
      - title: "Unit Testing"
        path: "testing/unit-testing.md"
        order: 3
      - title: "Integration Testing"
        path: "testing/integration-testing.md"
        order: 4
      - title: "End-to-End Testing"
        path: "testing/e2e-testing.md"
        order: 5
      - title: "Performance Testing"
        path: "testing/performance-testing.md"
        order: 6
      - title: "Mocking and Stubbing"
        path: "testing/mocking.md"
        order: 7
      - title: "Test Utilities"
        path: "testing/test-utilities.md"
        order: 8
      - title: "CI/CD Integration"
        path: "testing/cicd.md"
        order: 9
      - title: "Testing Best Practices"
        path: "testing/best-practices.md"
        order: 10
  
  - name: "API Reference"
    order: 5
    path: "api"
    subcategories:
      - name: "Gateway"
        order: 1
        path: "api/gateway"
        items:
          - title: "Gateway CLI"
            path: "api/gateway/cli.md"
            order: 1
          - title: "Gateway HTTP API"
            path: "api/gateway/http.md"
            order: 2
      - name: "Client SDK"
        order: 2
        path: "api"
        items:
          - title: "Client SDK API"
            path: "api/client-sdk-api.md"
            order: 1
          - title: "Configuration API"
            path: "api/configuration-api.md"
            order: 2
          - title: "Error Handling"
            path: "api/error-handling.md"
            order: 3
          - title: "Type Definitions"
            path: "api/type-definitions.md"
            order: 4
          - title: "Events and Hooks"
            path: "api/events-hooks.md"
            order: 5
  
  - name: "Reference"
    order: 6
    path: "reference"
    items:
      - title: "Quick Reference"
        path: "reference/quick-reference.md"
        order: 1
```
