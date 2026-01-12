---
title: "Gateway HTTP API"
description: "Complete reference for Graftcode Gateway HTTP API endpoints."
---

# Gateway HTTP API

## Health Check

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

## List Services

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

## Get Service Methods

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

## Service Invocation

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

## Authentication

**Endpoint:** `POST /auth/token`

**Description:** Authenticate and get access token.

**Request Body:**
```json
{
  "apiKey": "your-api-key",
  "projectKey": "your-project-key"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600
}
```
