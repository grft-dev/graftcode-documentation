---
title: "Testing Setup"
description: "Set up your testing environment with Jest, pytest, and test configuration for Graftcode SDK testing."
---

# Testing Setup

## Prerequisites

```bash
# Install testing dependencies
npm install --save-dev jest @types/jest ts-jest
# or
pip install pytest pytest-asyncio
```

## Test Configuration

### Jest Configuration (TypeScript/JavaScript)

`jest.config.js`:

```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

### pytest Configuration (Python)

`pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
asyncio_mode = auto
```

## Test Environment Setup

### Environment Variables

`.env.test`:

```bash
GRAFTCODE_PROJECT_KEY=test-project-key
GRAFTCODE_ENV=TEST
GRAFTCODE_ENDPOINT=http://localhost:9999
GRAFTCODE_TIMEOUT=5000
GRAFTCODE_DEBUG=true
```

### Test Helper: Gateway Manager

```typescript
// tests/helpers/gateway-manager.ts
import { spawn, ChildProcess } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs';

const sleep = promisify(setTimeout);

export class GatewayManager {
  private gatewayProcess: ChildProcess | null = null;
  private readonly port: number;
  private readonly projectKey: string;

  constructor(port: number = 9999, projectKey: string = 'test-key') {
    this.port = port;
    this.projectKey = projectKey;
  }

  async start(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.gatewayProcess = spawn('gcg.exe', [
        '--projectKey', this.projectKey,
        '--env', 'TEST',
        '--port', this.port.toString()
      ]);

      this.gatewayProcess.stdout?.on('data', (data) => {
        if (data.toString().includes('Gateway started')) {
          resolve();
        }
      });

      this.gatewayProcess.stderr?.on('data', (data) => {
        console.error(`Gateway error: ${data}`);
      });

      // Wait for gateway to be ready
      setTimeout(async () => {
        if (await this.isReady()) {
          resolve();
        } else {
          reject(new Error('Gateway failed to start'));
        }
      }, 5000);
    });
  }

  async stop(): Promise<void> {
    if (this.gatewayProcess) {
      this.gatewayProcess.kill();
      await sleep(1000);
      this.gatewayProcess = null;
    }
  }

  private async isReady(): Promise<boolean> {
    try {
      const response = await fetch(`http://localhost:${this.port}/health`);
      return response.ok;
    } catch {
      return false;
    }
  }
}
```
