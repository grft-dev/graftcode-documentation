---
title: "Configuration API"
description: "Configure Graftcode using environment variables, configuration files, and runtime configuration APIs."
---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GRAFTCODE_PROJECT_KEY` | Your project key | `abc123` |
| `GRAFTCODE_ENV` | Environment name | `DEV`, `STAGING`, `PROD` |
| `GRAFTCODE_ENDPOINT` | Gateway endpoint URL | `http://localhost:8080` |
| `GRAFTCODE_TIMEOUT` | Request timeout (ms) | `5000` |
| `GRAFTCODE_RETRIES` | Number of retries | `3` |
| `GRAFTCODE_DEBUG` | Enable debug mode | `true`, `false` |
| `GRAFTCODE_LOG_LEVEL` | Logging level | `DEBUG`, `INFO`, `WARN`, `ERROR` |

## Configuration File

### File Format: `graftcode.config.json`

```json
{
  "projectKey": "your-project-key",
  "env": "DEV",
  "defaultEndpoint": "http://localhost:8080",
  "defaultTimeout": 5000,
  "defaultRetries": 3,
  "debug": false,
  "logLevel": "INFO",
  "services": {
    "UserService": {
      "endpoint": "http://user-service:8080",
      "timeout": 10000
    },
    "OrderService": {
      "endpoint": "http://order-service:8080",
      "mode": "remote"
    }
  }
}
```

### Configuration Schema

```typescript
interface GraftcodeConfig {
  projectKey: string;
  env?: string;
  defaultEndpoint?: string;
  defaultTimeout?: number;
  defaultRetries?: number;
  debug?: boolean;
  logLevel?: 'DEBUG' | 'INFO' | 'WARN' | 'ERROR';
  services?: {
    [serviceName: string]: {
      endpoint?: string;
      timeout?: number;
      retries?: number;
      mode?: 'remote' | 'in-memory';
      headers?: Record<string, string>;
    };
  };
}
```

## Runtime Configuration

### Loading Configuration

```typescript
import { loadConfig } from '@graftcode/core';

// Load from file
const config = loadConfig('./graftcode.config.json');

// Load from environment
const config = loadConfig(); // Reads from environment variables

// Merge configurations
const config = loadConfig({
  file: './graftcode.config.json',
  env: true, // Also read from environment
  defaults: {
    timeout: 5000
  }
});
```

### Updating Configuration

```typescript
import { updateConfig } from '@graftcode/core';

// Update global configuration
updateConfig({
  timeout: 10000,
  retries: 5
});

// Update service-specific configuration
updateConfig('UserService', {
  endpoint: 'http://new-endpoint:8080'
});
```
