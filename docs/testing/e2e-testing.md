---
title: "End-to-End Testing"
description: "Create comprehensive end-to-end tests for complete workflows and multi-service interactions."
---

# End-to-End Testing

## Complete Workflow Testing

```typescript
// tests/e2e/complete-workflow.test.ts
import { GatewayManager } from '../helpers/gateway-manager';
import { OrderService } from '@graftcode/order-service';
import { PaymentService } from '@graftcode/payment-service';
import { NotificationService } from '@graftcode/notification-service';

describe('E2E: Complete Order Workflow', () => {
  let gatewayManager: GatewayManager;
  let orderService: OrderService;
  let paymentService: PaymentService;
  let notificationService: NotificationService;

  beforeAll(async () => {
    gatewayManager = new GatewayManager();
    await gatewayManager.start();

    orderService = new OrderService();
    paymentService = new PaymentService();
    notificationService = new NotificationService();
  });

  afterAll(async () => {
    await gatewayManager.stop();
  });

  it('should complete full order process', async () => {
    // 1. Create order
    const order = await orderService.createOrder({
      items: [{ productId: 1, quantity: 2 }],
      customerId: 123
    });
    expect(order.id).toBeDefined();
    expect(order.status).toBe('pending');

    // 2. Process payment
    const payment = await paymentService.processPayment({
      orderId: order.id,
      amount: order.total,
      method: 'credit_card'
    });
    expect(payment.status).toBe('completed');

    // 3. Update order status
    const updatedOrder = await orderService.updateStatus(order.id, 'paid');
    expect(updatedOrder.status).toBe('paid');

    // 4. Send notification
    const notification = await notificationService.send({
      userId: 123,
      type: 'order_confirmation',
      orderId: order.id
    });
    expect(notification.sent).toBe(true);
  });
});
```

## Multi-Service E2E Test

```typescript
// tests/e2e/multi-service.test.ts
describe('E2E: Multi-Service Interaction', () => {
  let gatewayManager: GatewayManager;
  let services: Map<string, any>;

  beforeAll(async () => {
    gatewayManager = new GatewayManager();
    await gatewayManager.start();

    services = new Map([
      ['user', new UserService()],
      ['order', new OrderService()],
      ['inventory', new InventoryService()],
      ['shipping', new ShippingService()]
    ]);
  });

  afterAll(async () => {
    await gatewayManager.stop();
  });

  it('should handle complex multi-service workflow', async () => {
    const userService = services.get('user')!;
    const orderService = services.get('order')!;
    const inventoryService = services.get('inventory')!;
    const shippingService = services.get('shipping')!;

    // Get user
    const user = await userService.getUser(123);

    // Check inventory
    const inventory = await inventoryService.checkAvailability(1, 5);
    expect(inventory.available).toBe(true);

    // Create order
    const order = await orderService.createOrder({
      userId: user.id,
      items: [{ productId: 1, quantity: 5 }]
    });

    // Reserve inventory
    await inventoryService.reserve(order.id, [{ productId: 1, quantity: 5 }]);

    // Create shipping label
    const shipping = await shippingService.createLabel({
      orderId: order.id,
      address: user.address
    });
    expect(shipping.trackingNumber).toBeDefined();
  });
});
```
