---
title: "Mocking and Stubbing"
description: "Learn how to mock Graftcode services and stub network calls for effective unit testing."
---

## Mocking Graftcode Services

```typescript
// tests/mocks/user-service.mock.ts
import { UserService } from '@graftcode/user-service';

export class MockUserService extends UserService {
  private mockUsers: Map<number, any> = new Map();

  constructor() {
    super({ endpoint: 'mock://localhost' });
    this.setupMocks();
  }

  private setupMocks() {
    this.mockUsers.set(1, { id: 1, name: 'Test User 1', email: 'test1@example.com' });
    this.mockUsers.set(2, { id: 2, name: 'Test User 2', email: 'test2@example.com' });
  }

  async getUser(id: number): Promise<any> {
    const user = this.mockUsers.get(id);
    if (!user) {
      throw new Error(`User ${id} not found`);
    }
    return user;
  }

  async createUser(userData: any): Promise<any> {
    const newId = Math.max(...Array.from(this.mockUsers.keys())) + 1;
    const user = { id: newId, ...userData };
    this.mockUsers.set(newId, user);
    return user;
  }
}
```

## Using Jest Mocks

```typescript
// tests/unit/with-mocks.test.ts
import { UserService } from '@graftcode/user-service';

jest.mock('@graftcode/user-service', () => ({
  UserService: jest.fn().mockImplementation(() => ({
    getUser: jest.fn().mockResolvedValue({
      id: 1,
      name: 'Mocked User',
      email: 'mocked@example.com'
    }),
    createUser: jest.fn().mockResolvedValue({
      id: 2,
      name: 'New User',
      email: 'new@example.com'
    })
  }))
}));

describe('With Mocks', () => {
  it('should use mocked service', async () => {
    const userService = new UserService();
    const user = await userService.getUser(1);
    
    expect(user.name).toBe('Mocked User');
    expect(userService.getUser).toHaveBeenCalledWith(1);
  });
});
```

## Stubbing Network Calls

```typescript
// tests/helpers/network-stub.ts
export class NetworkStub {
  private responses: Map<string, any> = new Map();

  stub(method: string, path: string, response: any) {
    this.responses.set(`${method}:${path}`, response);
  }

  async fetch(url: string, options?: any): Promise<Response> {
    const key = `${options?.method || 'GET'}:${url}`;
    const response = this.responses.get(key);
    
    if (!response) {
      throw new Error(`No stub for ${key}`);
    }

    return new Response(JSON.stringify(response), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
```
