---
title: "Performance Testing"
description: "Test Graftcode services under load with load testing, stress testing, and latency measurement strategies."
---

# Performance Testing

## Load Testing

```typescript
// tests/performance/load.test.ts
import { performance } from 'perf_hooks';
import { UserService } from '@graftcode/user-service';

describe('Load Testing', () => {
  let userService: UserService;

  beforeEach(() => {
    userService = new UserService();
  });

  it('should handle 1000 concurrent requests', async () => {
    const iterations = 1000;
    const start = performance.now();

    const promises = Array(iterations)
      .fill(null)
      .map((_, i) => userService.getUser(i % 100));

    const results = await Promise.all(promises);
    const end = performance.now();

    expect(results.length).toBe(iterations);
    console.log(`Completed ${iterations} requests in ${end - start}ms`);
    console.log(`Average: ${(end - start) / iterations}ms per request`);
    console.log(`Throughput: ${(iterations / (end - start)) * 1000} req/s`);
  });

  it('should maintain performance under sustained load', async () => {
    const duration = 60000; // 1 minute
    const start = Date.now();
    let requestCount = 0;

    while (Date.now() - start < duration) {
      await userService.getUser(Math.floor(Math.random() * 100));
      requestCount++;
    }

    const actualDuration = Date.now() - start;
    const throughput = (requestCount / actualDuration) * 1000;
    
    console.log(`Processed ${requestCount} requests in ${actualDuration}ms`);
    console.log(`Sustained throughput: ${throughput.toFixed(2)} req/s`);
    
    expect(throughput).toBeGreaterThan(100); // Minimum threshold
  });
});
```

## Stress Testing

```typescript
// tests/performance/stress.test.ts
describe('Stress Testing', () => {
  it('should handle burst traffic', async () => {
    const userService = new UserService();
    const burstSize = 10000;
    
    const start = performance.now();
    const promises = Array(burstSize)
      .fill(null)
      .map(() => userService.getUser(Math.floor(Math.random() * 100)));
    
    const results = await Promise.allSettled(promises);
    const end = performance.now();

    const successful = results.filter(r => r.status === 'fulfilled').length;
    const failed = results.filter(r => r.status === 'rejected').length;

    console.log(`Burst: ${burstSize} requests`);
    console.log(`Successful: ${successful}, Failed: ${failed}`);
    console.log(`Time: ${end - start}ms`);
    
    expect(successful / burstSize).toBeGreaterThan(0.95); // 95% success rate
  });
});
```

## Latency Testing

```typescript
// tests/performance/latency.test.ts
describe('Latency Testing', () => {
  it('should meet latency requirements', async () => {
    const userService = new UserService();
    const iterations = 100;
    const latencies: number[] = [];

    for (let i = 0; i < iterations; i++) {
      const start = performance.now();
      await userService.getUser(i % 100);
      const end = performance.now();
      latencies.push(end - start);
    }

    const avgLatency = latencies.reduce((a, b) => a + b, 0) / latencies.length;
    const p50 = latencies.sort((a, b) => a - b)[Math.floor(latencies.length * 0.5)];
    const p95 = latencies.sort((a, b) => a - b)[Math.floor(latencies.length * 0.95)];
    const p99 = latencies.sort((a, b) => a - b)[Math.floor(latencies.length * 0.99)];

    console.log(`Average latency: ${avgLatency.toFixed(2)}ms`);
    console.log(`P50: ${p50.toFixed(2)}ms`);
    console.log(`P95: ${p95.toFixed(2)}ms`);
    console.log(`P99: ${p99.toFixed(2)}ms`);

    expect(p95).toBeLessThan(100); // P95 < 100ms
    expect(p99).toBeLessThan(200); // P99 < 200ms
  });
});
```
