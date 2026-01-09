---
title: "Configuration"
order: 6
description: "Configure Graftcode Gateway and client SDKs using command-line options, environment variables, and configuration files."
---

# Configuration

## Gateway Configuration

### Command Line Options

```bash
gcg.exe \
  --projectKey YOUR_KEY \
  --env DEV \
  --port 8080 \
  --config ./config.json \
  --log-level INFO
```

### Configuration File

`gateway.config.json`:

```json
{
  "projectKey": "your-project-key",
  "environment": "DEV",
  "port": 8080,
  "host": "0.0.0.0",
  "logging": {
    "level": "INFO",
    "file": "./logs/gateway.log"
  },
  "services": {
    "autoDiscover": true,
    "scanPaths": ["./services"]
  },
  "security": {
    "apiKey": "optional-api-key",
    "cors": {
      "enabled": true,
      "origins": ["*"]
    }
  }
}
```

## Client Configuration

### In Code

```typescript
import { ServiceName } from '@graftcode/service-name';

const service = new ServiceName({
  endpoint: 'http://localhost:8080',
  timeout: 5000,
  retries: 3,
  headers: {
    'Authorization': 'Bearer token'
  }
});
```

### Environment Variables

```bash
export GRAFTCODE_PROJECT_KEY=your-key
export GRAFTCODE_ENV=DEV
export GRAFTCODE_ENDPOINT=http://localhost:8080
export GRAFTCODE_TIMEOUT=5000
```

### Configuration File

`graftcode.config.json`:

```json
{
  "projectKey": "your-project-key",
  "env": "DEV",
  "defaultEndpoint": "http://localhost:8080",
  "defaultTimeout": 5000,
  "defaultRetries": 3,
  "services": {
    "service1": {
      "endpoint": "http://service1:8080",
      "timeout": 10000
    },
    "service2": {
      "endpoint": "http://service2:8080"
    }
  }
}
```

## Runtime Configuration Switching

### Switching Between Monolith and Microservice

```typescript
// In-memory (monolith)
const service = new ServiceName({
  mode: 'in-memory'
});

// Remote (microservice)
const service = new ServiceName({
  mode: 'remote',
  endpoint: 'http://microservice:8080'
});

// Configuration-based switching
const config = process.env.SERVICE_MODE === 'remote' 
  ? { mode: 'remote', endpoint: process.env.SERVICE_ENDPOINT }
  : { mode: 'in-memory' };

const service = new ServiceName(config);
```
