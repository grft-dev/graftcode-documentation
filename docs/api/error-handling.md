---
title: "Error Handling"
description: "Handle errors in Graftcode SDK with error types, error codes, and retry logic patterns."
---

# Error Handling

## Error Types

### `GraftcodeError`

Base error class for all Graftcode errors.

```typescript
class GraftcodeError extends Error {
  code: string;
  statusCode?: number;
  details?: any;
}
```

## Error Codes

| Code | Description | Status Code |
|------|-------------|-------------|
| `SERVICE_UNAVAILABLE` | Gateway or service is not available | 503 |
| `TIMEOUT` | Request timed out | 504 |
| `VALIDATION_ERROR` | Invalid request parameters | 400 |
| `METHOD_NOT_FOUND` | Method does not exist | 404 |
| `AUTHENTICATION_ERROR` | Authentication failed | 401 |
| `AUTHORIZATION_ERROR` | Insufficient permissions | 403 |
| `INTERNAL_ERROR` | Internal server error | 500 |
| `NETWORK_ERROR` | Network connection failed | - |

## Error Handling Examples

### Basic Error Handling

```typescript
import { GraftcodeError } from '@graftcode/core';

try {
  const result = await service.methodName(params);
} catch (error) {
  if (error instanceof GraftcodeError) {
    console.error(`Error: ${error.code} - ${error.message}`);
    console.error('Details:', error.details);
  } else {
    console.error('Unknown error:', error);
  }
}
```

### Error Code Handling

```typescript
try {
  const result = await service.methodName(params);
} catch (error) {
  if (error instanceof GraftcodeError) {
    switch (error.code) {
      case 'SERVICE_UNAVAILABLE':
        // Retry logic
        await retry(() => service.methodName(params));
        break;
      case 'TIMEOUT':
        // Increase timeout and retry
        service.setTimeout(service.getTimeout() * 2);
        await service.methodName(params);
        break;
      case 'VALIDATION_ERROR':
        // Handle validation errors
        console.error('Validation failed:', error.details);
        break;
      default:
        // Handle other errors
        console.error('Error:', error.message);
    }
  }
}
```

### Retry Logic

```typescript
import { retry } from '@graftcode/core';

async function callWithRetry<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3
): Promise<T> {
  let lastError: Error;
  
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      if (i < maxRetries - 1 && error instanceof GraftcodeError) {
        if (error.code === 'SERVICE_UNAVAILABLE' || error.code === 'TIMEOUT') {
          await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
          continue;
        }
      }
      throw error;
    }
  }
  
  throw lastError!;
}

// Usage
const result = await callWithRetry(() => service.methodName(params));
```
