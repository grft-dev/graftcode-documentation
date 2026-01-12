---
title: "Examples"
description: "Practical code examples demonstrating how to use Graftcode in various scenarios and programming languages."
---

# Examples

## Basic Example

```typescript
// Backend service (C# example)
public class UserService
{
    public User GetUser(int userId)
    {
        return new User { Id = userId, Name = "John Doe" };
    }
}

// Frontend client (TypeScript)
import { UserService } from '@graftcode/user-service';

const userService = new UserService();
const user = await userService.getUser(123);
console.log(user.name); // "John Doe"
```

## Cross-Language Example

```python
# Python backend service
class CalculatorService:
    def add(self, a: int, b: int) -> int:
        return a + b

# Node.js client
const { CalculatorService } = require('@graftcode/calculator-service');

const calc = new CalculatorService();
const result = await calc.add(5, 3);
console.log(result); // 8
```

## Async Operations Example

```typescript
import { DataService } from '@graftcode/data-service';

const dataService = new DataService();

// Sequential calls
const user = await dataService.getUser(userId);
const posts = await dataService.getUserPosts(userId);

// Parallel calls
const [user, posts, comments] = await Promise.all([
  dataService.getUser(userId),
  dataService.getUserPosts(userId),
  dataService.getUserComments(userId)
]);
```

## Error Handling Example

```typescript
import { OrderService } from '@graftcode/order-service';
import { GraftcodeError } from '@graftcode/core';

const orderService = new OrderService();

try {
  const order = await orderService.createOrder(orderData);
} catch (error) {
  if (error instanceof GraftcodeError) {
    switch (error.code) {
      case 'SERVICE_UNAVAILABLE':
        // Retry logic
        break;
      case 'VALIDATION_ERROR':
        // Handle validation
        break;
      default:
        // Handle other errors
    }
  }
}
```

## Configuration-Based Routing Example

```typescript
// config.json
{
  "services": {
    "payment": {
      "mode": "remote",
      "endpoint": "http://payment-service:8080"
    },
    "notification": {
      "mode": "in-memory"
    }
  }
}

// Usage
import { PaymentService } from '@graftcode/payment-service';
import { NotificationService } from '@graftcode/notification-service';

// Payment service calls remote microservice
const paymentService = new PaymentService();

// Notification service uses in-memory implementation
const notificationService = new NotificationService();
```
