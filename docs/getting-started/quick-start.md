---
title: "Quick Start"
order: 3
description: "Get up and running with Graftcode in three simple steps - from gateway setup to calling your first method."
---

# Quick Start

## Step 1: Run the Gateway with Your Backend

Download and run a lightweight Graftcode Gateway to host your backend logic. It automatically exposes all your public classes and methods and provides Graftcode Vision portal.

```bash
gcg.exe --projectKey YOUR_PROJECT_KEY --env DEV
```

## Step 2: Generate Your Graft

Copy the command for your package manager and import your service as a local dependency. The compatible client package gets automatically generated within milliseconds and refreshes whenever the target API evolves.

```bash
# Command will be provided by Graftcode Vision portal
npm install @graftcode/my-service
```

## Step 3: Call Any Method, Anywhere

Import required classes and call target methods through strongly-typed interface in your calling technology.

```typescript
// TypeScript/JavaScript example
import { MyService } from '@graftcode/my-service';

const service = new MyService();
const result = await service.myMethod(param1, param2);
```

```python
# Python example
from graftcode.my_service import MyService

service = MyService()
result = service.my_method(param1, param2)
```
