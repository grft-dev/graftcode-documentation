---
title: "Integration Testing"
order: 13
description: "Test gateway-client communication and cross-language integration scenarios with Graftcode."
---

# Integration Testing

## Gateway-Client Integration

```typescript
// tests/integration/gateway-client.test.ts
import { GatewayManager } from '../helpers/gateway-manager';
import { UserService } from '@graftcode/user-service';

describe('Gateway-Client Integration', () => {
  let gatewayManager: GatewayManager;
  let userService: UserService;

  beforeAll(async () => {
    gatewayManager = new GatewayManager(9999, 'integration-test');
    await gatewayManager.start();
    
    userService = new UserService({
      endpoint: 'http://localhost:9999'
    });
  });

  afterAll(async () => {
    await gatewayManager.stop();
  });

  it('should connect to gateway', async () => {
    const health = await userService.healthCheck();
    expect(health.status).toBe('ok');
  });

  it('should call remote method', async () => {
    const user = await userService.getUser(1);
    expect(user).toBeDefined();
  });

  it('should handle method with parameters', async () => {
    const users = await userService.searchUsers({ name: 'John' });
    expect(users).toBeInstanceOf(Array);
  });
});
```

## Cross-Language Integration

```typescript
// tests/integration/cross-language.test.ts
import { GatewayManager } from '../helpers/gateway-manager';
import { PythonService } from '@graftcode/python-service';
import { DotNetService } from '@graftcode/dotnet-service';

describe('Cross-Language Integration', () => {
  let gatewayManager: GatewayManager;

  beforeAll(async () => {
    gatewayManager = new GatewayManager();
    await gatewayManager.start();
  });

  afterAll(async () => {
    await gatewayManager.stop();
  });

  it('should call Python service from TypeScript', async () => {
    const pythonService = new PythonService();
    const result = await pythonService.calculate(5, 3);
    expect(result).toBe(8);
  });

  it('should call .NET service from TypeScript', async () => {
    const dotNetService = new DotNetService();
    const result = await dotNetService.processData({ value: 'test' });
    expect(result).toBeDefined();
  });
});
```

## Configuration Testing

```typescript
// tests/integration/configuration.test.ts
import { ServiceName } from '@graftcode/service-name';

describe('Configuration', () => {
  it('should use environment variables', () => {
    process.env.GRAFTCODE_ENDPOINT = 'http://custom-endpoint:8080';
    
    const service = new ServiceName();
    expect(service.getEndpoint()).toBe('http://custom-endpoint:8080');
  });

  it('should use configuration file', () => {
    const service = new ServiceName({
      configFile: './tests/config/test-config.json'
    });
    
    expect(service.getConfig().timeout).toBe(10000);
  });

  it('should override config with code options', () => {
    const service = new ServiceName({
      endpoint: 'http://override:8080',
      timeout: 15000
    });
    
    expect(service.getEndpoint()).toBe('http://override:8080');
    expect(service.getTimeout()).toBe(15000);
  });
});
```
