---
title: "Unit Testing"
description: "Learn how to write unit tests for Graftcode services, including testing service methods, error handling, and async operations."
---

# Unit Testing

## Testing Service Methods

### Basic Unit Test

```typescript
// tests/unit/user-service.test.ts
import { UserService } from '@graftcode/user-service';

describe('UserService', () => {
  let userService: UserService;

  beforeEach(() => {
    userService = new UserService({
      endpoint: 'http://localhost:9999'
    });
  });

  describe('getUser', () => {
    it('should retrieve user by id', async () => {
      const user = await userService.getUser(123);
      
      expect(user).toBeDefined();
      expect(user.id).toBe(123);
      expect(user.name).toBeDefined();
    });

    it('should throw error for invalid user id', async () => {
      await expect(userService.getUser(-1)).rejects.toThrow();
    });
  });

  describe('createUser', () => {
    it('should create new user', async () => {
      const userData = { name: 'Test User', email: 'test@example.com' };
      const user = await userService.createUser(userData);
      
      expect(user.id).toBeDefined();
      expect(user.name).toBe(userData.name);
    });
  });
});
```

## Testing Error Handling

```typescript
// tests/unit/error-handling.test.ts
import { OrderService } from '@graftcode/order-service';
import { GraftcodeError } from '@graftcode/core';

describe('Error Handling', () => {
  let orderService: OrderService;

  beforeEach(() => {
    orderService = new OrderService();
  });

  it('should handle service unavailable error', async () => {
    await expect(orderService.createOrder({})).rejects.toThrow(GraftcodeError);
    
    try {
      await orderService.createOrder({});
    } catch (error) {
      expect(error).toBeInstanceOf(GraftcodeError);
      expect(error.code).toBe('SERVICE_UNAVAILABLE');
    }
  });

  it('should handle validation errors', async () => {
    try {
      await orderService.createOrder({ invalid: 'data' });
    } catch (error) {
      expect(error.code).toBe('VALIDATION_ERROR');
      expect(error.message).toContain('validation');
    }
  });
});
```

## Testing Async Operations

```typescript
// tests/unit/async-operations.test.ts
import { DataService } from '@graftcode/data-service';

describe('Async Operations', () => {
  let dataService: DataService;

  beforeEach(() => {
    dataService = new DataService();
  });

  it('should handle parallel requests', async () => {
    const [user, posts, comments] = await Promise.all([
      dataService.getUser(1),
      dataService.getUserPosts(1),
      dataService.getUserComments(1)
    ]);

    expect(user).toBeDefined();
    expect(posts).toBeInstanceOf(Array);
    expect(comments).toBeInstanceOf(Array);
  });

  it('should handle sequential requests', async () => {
    const user = await dataService.getUser(1);
    const posts = await dataService.getUserPosts(user.id);
    const comments = await dataService.getPostComments(posts[0].id);

    expect(user).toBeDefined();
    expect(posts.length).toBeGreaterThan(0);
    expect(comments).toBeDefined();
  });
});
```
