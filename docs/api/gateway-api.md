---
title: "Gateway API"
order: 20
description: "Complete reference for Graftcode Gateway command-line interface and HTTP API endpoints."
---

# Gateway API

## Command Line Interface

### `gcg.exe`

Main gateway executable for hosting services.

**Syntax:**
```bash
gcg.exe [options]
```

**Options:**

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `--projectKey` | string | Yes | - | Your unique project key |
| `--env` | string | No | DEV | Environment name (DEV, STAGING, PROD) |
| `--port` | number | No | 8080 | Port number for gateway |
| `--host` | string | No | 0.0.0.0 | Host address |
| `--config` | string | No | - | Path to configuration file |
| `--log-level` | string | No | INFO | Logging level (DEBUG, INFO, WARN, ERROR) |
| `--log-file` | string | No | - | Path to log file |

**Examples:**

```bash
# Basic usage
gcg.exe --projectKey abc123 --env DEV

# With custom port
gcg.exe --projectKey abc123 --env DEV --port 9090

# With configuration file
gcg.exe --projectKey abc123 --env DEV --config ./gateway.config.json

# Debug mode
gcg.exe --projectKey abc123 --env DEV --log-level DEBUG
```

## Gateway HTTP API

### Health Check

**Endpoint:** `GET /health`

**Description:** Check gateway health status.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "uptime": 3600,
  "services": {
    "count": 5,
    "healthy": 5
  }
}
```

### List Services

**Endpoint:** `GET /services`

**Description:** Get list of all exposed services.

**Response:**
```json
{
  "services": [
    {
      "name": "UserService",
      "namespace": "com.example.users",
      "methods": 10,
      "status": "active"
    }
  ]
}
```

### Get Service Methods

**Endpoint:** `GET /services/{serviceName}/methods`

**Description:** Get all methods for a specific service.

**Parameters:**
- `serviceName` (path): Name of the service

**Response:**
```json
{
  "service": "UserService",
  "methods": [
    {
      "name": "getUser",
      "parameters": [
        {
          "name": "userId",
          "type": "number",
          "required": true
        }
      ],
      "returnType": "User"
    }
  ]
}
```

### Service Invocation

**Endpoint:** `POST /services/{serviceName}/methods/{methodName}`

**Description:** Invoke a service method (internal use, clients use SDK).

**Parameters:**
- `serviceName` (path): Name of the service
- `methodName` (path): Name of the method

**Request Body:**
```json
{
  "parameters": [123]
}
```

**Response:**
```json
{
  "result": {
    "id": 123,
    "name": "John Doe"
  }
}
```
