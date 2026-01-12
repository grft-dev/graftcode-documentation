---
title: "Type Definitions"
description: "TypeScript type definitions for Graftcode SDK including service clients, metadata, and request/response types."
---

# Type Definitions

## Core Types

### `ServiceClient<T>`

Generic service client interface.

```typescript
interface ServiceClient<T> {
  healthCheck(): Promise<HealthStatus>;
  getEndpoint(): string;
  setEndpoint(endpoint: string): void;
  getTimeout(): number;
  setTimeout(timeout: number): void;
}
```

### `HealthStatus`

```typescript
interface HealthStatus {
  status: 'ok' | 'error';
  message?: string;
  latency?: number;
  timestamp?: number;
}
```

### `MethodMetadata`

```typescript
interface MethodMetadata {
  name: string;
  parameters: ParameterMetadata[];
  returnType: string;
  isAsync: boolean;
  documentation?: string;
}

interface ParameterMetadata {
  name: string;
  type: string;
  required: boolean;
  defaultValue?: any;
  documentation?: string;
}
```

### `ServiceMetadata`

```typescript
interface ServiceMetadata {
  name: string;
  namespace: string;
  version: string;
  methods: MethodMetadata[];
  status: 'active' | 'inactive';
}
```

## Request/Response Types

### `ServiceRequest`

```typescript
interface ServiceRequest {
  service: string;
  method: string;
  parameters: any[];
  requestId?: string;
  timeout?: number;
}
```

### `ServiceResponse`

```typescript
interface ServiceResponse<T = any> {
  result?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
  requestId?: string;
  latency?: number;
}
```
