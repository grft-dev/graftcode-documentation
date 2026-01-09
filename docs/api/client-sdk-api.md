---
title: "Client SDK API"
order: 21
description: "Reference for Graftcode client SDK methods, initialization, and method invocation patterns."
---

# Client SDK API

## Service Client

### Constructor

```typescript
new ServiceName(options?: ClientOptions)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `options` | ClientOptions | No | Client configuration options |

**ClientOptions:**

```typescript
interface ClientOptions {
  endpoint?: string;           // Custom gateway endpoint
  timeout?: number;            // Request timeout in milliseconds
  retries?: number;            // Number of retry attempts
  headers?: Record<string, string>;  // Custom headers
  configFile?: string;        // Path to configuration file
  mode?: 'remote' | 'in-memory';  // Execution mode
  debug?: boolean;            // Enable debug logging
  logLevel?: 'DEBUG' | 'INFO' | 'WARN' | 'ERROR';
}
```

**Example:**

```typescript
import { UserService } from '@graftcode/user-service';

// Default configuration
const service1 = new UserService();

// Custom configuration
const service2 = new UserService({
  endpoint: 'http://custom-gateway:8080',
  timeout: 10000,
  retries: 3
});

// In-memory mode (monolith)
const service3 = new UserService({
  mode: 'in-memory'
});
```

## Method Invocation

All public methods from your backend service are automatically available on the client.

### Synchronous Methods

```typescript
const result = service.methodName(param1, param2, ...);
```

**Example:**

```typescript
const user = userService.getUser(123);
const users = userService.searchUsers({ name: 'John' });
```

### Asynchronous Methods

```typescript
const result = await service.methodName(param1, param2, ...);
```

**Example:**

```typescript
const user = await userService.getUserAsync(123);
const order = await orderService.createOrder(orderData);
```

## Client Methods

### `healthCheck()`

Check if the service is available.

**Returns:** `Promise<HealthStatus>`

```typescript
interface HealthStatus {
  status: 'ok' | 'error';
  message?: string;
  latency?: number;
}
```

**Example:**

```typescript
const health = await service.healthCheck();
if (health.status === 'ok') {
  console.log('Service is healthy');
}
```

### `getEndpoint()`

Get the current endpoint URL.

**Returns:** `string`

**Example:**

```typescript
const endpoint = service.getEndpoint();
console.log(`Connected to: ${endpoint}`);
```

### `setEndpoint(endpoint: string)`

Update the endpoint URL.

**Parameters:**
- `endpoint`: New endpoint URL

**Example:**

```typescript
service.setEndpoint('http://new-gateway:8080');
```

### `getTimeout()`

Get the current timeout value.

**Returns:** `number`

**Example:**

```typescript
const timeout = service.getTimeout();
console.log(`Timeout: ${timeout}ms`);
```

### `setTimeout(timeout: number)`

Update the timeout value.

**Parameters:**
- `timeout`: New timeout in milliseconds

**Example:**

```typescript
service.setTimeout(15000);
```
