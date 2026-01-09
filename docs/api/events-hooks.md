---
title: "Events and Hooks"
order: 25
description: "Use Graftcode event system and hooks for request interception, lifecycle management, and advanced features."
---

# Events and Hooks

## Event System

### Available Events

```typescript
enum GraftcodeEvent {
  CONNECTED = 'connected',
  DISCONNECTED = 'disconnected',
  REQUEST_START = 'request:start',
  REQUEST_SUCCESS = 'request:success',
  REQUEST_ERROR = 'request:error',
  REQUEST_TIMEOUT = 'request:timeout',
  CONFIG_CHANGED = 'config:changed'
}
```

## Event Listeners

### Adding Event Listeners

```typescript
import { GraftcodeEvent } from '@graftcode/core';

// Listen to connection events
service.on(GraftcodeEvent.CONNECTED, () => {
  console.log('Connected to gateway');
});

service.on(GraftcodeEvent.DISCONNECTED, () => {
  console.log('Disconnected from gateway');
});

// Listen to request events
service.on(GraftcodeEvent.REQUEST_START, (event) => {
  console.log('Request started:', event.method);
});

service.on(GraftcodeEvent.REQUEST_SUCCESS, (event) => {
  console.log('Request succeeded:', event.method, event.latency);
});

service.on(GraftcodeEvent.REQUEST_ERROR, (event) => {
  console.error('Request failed:', event.method, event.error);
});
```

### Removing Event Listeners

```typescript
const handler = () => {
  console.log('Request started');
};

service.on(GraftcodeEvent.REQUEST_START, handler);

// Remove listener
service.off(GraftcodeEvent.REQUEST_START, handler);
```

## Hooks

### Request Hooks

```typescript
// Before request hook
service.beforeRequest((request) => {
  // Modify request
  request.headers = {
    ...request.headers,
    'X-Custom-Header': 'value'
  };
  return request;
});

// After response hook
service.afterResponse((response) => {
  // Process response
  console.log('Response received:', response);
  return response;
});

// Error hook
service.onError((error) => {
  // Handle error
  console.error('Error occurred:', error);
  // Return modified error or throw
  throw error;
});
```

### Lifecycle Hooks

```typescript
// On service initialization
service.onInit(() => {
  console.log('Service initialized');
});

// On service destruction
service.onDestroy(() => {
  console.log('Service destroyed');
});
```

## Advanced Features

### Connection Pooling

```typescript
const service = new UserService({
  connectionPool: {
    min: 2,
    max: 10,
    idleTimeout: 30000
  }
});
```

### Request Interceptors

```typescript
service.addInterceptor({
  request: (config) => {
    // Modify request config
    config.headers['Authorization'] = `Bearer ${getToken()}`;
    return config;
  },
  response: (response) => {
    // Process response
    return response;
  },
  error: (error) => {
    // Handle error
    if (error.statusCode === 401) {
      // Refresh token and retry
      refreshToken();
    }
    return Promise.reject(error);
  }
});
```

### Caching

```typescript
const service = new UserService({
  cache: {
    enabled: true,
    ttl: 60000, // 1 minute
    maxSize: 100
  }
});

// Cache is automatically used for GET-like methods
const user = await service.getUser(123); // Cached
```

### Metrics

```typescript
// Enable metrics collection
const service = new UserService({
  metrics: {
    enabled: true,
    endpoint: 'http://metrics-server:8080'
  }
});

// Get metrics
const metrics = service.getMetrics();
console.log('Total requests:', metrics.totalRequests);
console.log('Success rate:', metrics.successRate);
console.log('Average latency:', metrics.averageLatency);
```
