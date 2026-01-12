---
title: "Test Utilities"
description: "Useful test utilities including test data factories, helpers, and assertion utilities for Graftcode testing."
---

## Test Data Factory

```typescript
// tests/utils/test-data-factory.ts
export class TestDataFactory {
  static createUser(overrides?: any): any {
    return {
      id: Math.floor(Math.random() * 1000),
      name: 'Test User',
      email: 'test@example.com',
      createdAt: new Date(),
      ...overrides
    };
  }

  static createOrder(overrides?: any): any {
    return {
      id: Math.floor(Math.random() * 1000),
      userId: 1,
      items: [{ productId: 1, quantity: 1 }],
      total: 99.99,
      status: 'pending',
      ...overrides
    };
  }

  static createUsers(count: number): any[] {
    return Array(count).fill(null).map(() => this.createUser());
  }
}
```

## Test Helpers

```typescript
// tests/utils/test-helpers.ts
export async function waitForGateway(
  service: any,
  timeout: number = 5000
): Promise<boolean> {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    try {
      await service.healthCheck();
      return true;
    } catch (error) {
      await new Promise(resolve => setTimeout(resolve, 100));
    }
  }
  throw new Error('Gateway not available within timeout');
}

export async function retry<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  delay: number = 1000
): Promise<T> {
  let lastError: Error;
  
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      if (i < maxRetries - 1) {
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }
  
  throw lastError!;
}

export function createTestConfig(overrides?: any): any {
  return {
    projectKey: 'test-key',
    env: 'TEST',
    endpoint: 'http://localhost:9999',
    timeout: 5000,
    ...overrides
  };
}
```

## Assertion Helpers

```typescript
// tests/utils/assertions.ts
export function assertUser(user: any): void {
  expect(user).toBeDefined();
  expect(user.id).toBeDefined();
  expect(user.name).toBeDefined();
  expect(user.email).toBeDefined();
  expect(typeof user.email).toBe('string');
  expect(user.email).toMatch(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
}

export function assertOrder(order: any): void {
  expect(order).toBeDefined();
  expect(order.id).toBeDefined();
  expect(order.userId).toBeDefined();
  expect(order.items).toBeInstanceOf(Array);
  expect(order.total).toBeGreaterThan(0);
  expect(['pending', 'paid', 'shipped', 'cancelled']).toContain(order.status);
}
```
