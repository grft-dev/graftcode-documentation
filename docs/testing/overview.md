---
title: "Testing Overview"
description: "Introduction to testing strategies for Graftcode SDK implementations, including the testing pyramid and different testing types."
---

# Testing Overview

This guide provides comprehensive testing strategies for Graftcode SDK implementations. Testing Graftcode services requires understanding both the gateway and client components, as well as their interactions.

## Testing Pyramid

```
        /\
       /E2E\          ← Few, critical user journeys
      /------\
     /Integration\    ← Service interactions
    /------------\
   /   Unit Tests \   ← Many, fast, isolated
  /----------------\
```

## Testing Types

- **Unit Tests**: Test individual methods and components in isolation
- **Integration Tests**: Test gateway-client communication
- **End-to-End Tests**: Test complete workflows
- **Performance Tests**: Test under load and measure metrics
