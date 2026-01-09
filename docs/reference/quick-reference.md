---
title: "Quick Reference"
order: 26
description: "Quick reference guide with common commands, configuration snippets, and troubleshooting tips for Graftcode SDK."
---

# Quick Reference

## Installation

```bash
# Install Gateway
npm install -g graftcode-gateway

# Run Gateway
gcg.exe --projectKey YOUR_KEY --env DEV

# Install Client (command from Vision portal)
npm install @graftcode/service-name
```

## Basic Usage

```typescript
// Import service
import { UserService } from '@graftcode/user-service';

// Create instance
const service = new UserService();

// Call method
const user = await service.getUser(123);
```

## Configuration

### Environment Variables

```bash
GRAFTCODE_PROJECT_KEY=your-key
GRAFTCODE_ENV=DEV
GRAFTCODE_ENDPOINT=http://localhost:8080
GRAFTCODE_TIMEOUT=5000
```

### Code Configuration

```typescript
const service = new UserService({
  endpoint: 'http://localhost:8080',
  timeout: 10000,
  retries: 3
});
```

### Configuration File

`graftcode.config.json`:
```json
{
  "projectKey": "your-key",
  "env": "DEV",
  "defaultEndpoint": "http://localhost:8080"
}
```

## Integration Scenarios

### Frontend ←→ Backend

```typescript
// Backend exposes methods
// Frontend calls them directly
const backend = new BackendService();
const data = await backend.getData();
```

### AI ←→ Backend

```typescript
// AI agent calls backend methods
const aiService = new AIService();
const result = await aiService.process(request);
```

### Monolith ←→ Microservice

```typescript
// Switch between in-memory and remote
const service = new ServiceName({
  mode: process.env.MODE === 'remote' ? 'remote' : 'in-memory'
});
```

## Error Handling

```typescript
try {
  const result = await service.method(params);
} catch (error) {
  if (error instanceof GraftcodeError) {
    switch (error.code) {
      case 'SERVICE_UNAVAILABLE':
        // Retry
        break;
      case 'TIMEOUT':
        // Increase timeout
        break;
    }
  }
}
```

## Testing

### Unit Test

```typescript
const service = new UserService();
const user = await service.getUser(123);
expect(user).toBeDefined();
```

### Mock Service

```typescript
jest.mock('@graftcode/user-service', () => ({
  UserService: jest.fn().mockImplementation(() => ({
    getUser: jest.fn().mockResolvedValue({ id: 123 })
  }))
}));
```

## Common Commands

```bash
# Start gateway
gcg.exe --projectKey KEY --env DEV

# Health check
curl http://localhost:8080/health

# List services
curl http://localhost:8080/services
```

## Performance Tips

- Use parallel requests: `Promise.all([...])`
- Enable caching for read operations
- Batch related operations
- Monitor latency and throughput

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Gateway won't start | Check port availability |
| Connection failed | Verify endpoint URL |
| Type errors | Regenerate graft package |
| Method not found | Check method is public |

## Links

- **Vision Portal**: `http://localhost:8080/vision`
- **Health Check**: `http://localhost:8080/health`
- **Services**: `http://localhost:8080/services`
