---
title: "Zero-boilerplate microservices fabric"
description: "Build high-performance backend-to-backend systems with Graftcode where public static methods are all you write, communication channels are swappable without touching business code, and new microservices take minutes—not days."
keywords: "graftcode use case, microservices fabric, zero boilerplate, backend to backend, service communication, modular monolith, microservices without contracts"
---

# Zero-boilerplate microservices fabric

Write only public static methods. Everything connects as if it were one process—yet you can swap the communication channel (local, remote, different protocol) at any moment without touching a single line of business code.

This is the use case Graftcode was built for.

---

## The scenario

You are building a system—e-commerce, SaaS, fintech, it does not matter.

You have several modules:

- `OrderService`
- `PaymentService`
- `InventoryService`
- `UserService`
- `NotificationService`

Each module is a **completely separate project**. They can even be written in different languages—.NET, Java, Go, Python—it makes no difference.

---

## What you write

In each service you write **only** your business logic as public methods - static (for stateless) or instance (for statefull): 

```csharp
public static class PaymentModule
{
    public static PaymentResult ProcessPayment(string orderId, decimal amount, string currency)
    {
        // your business logic
    }

    public static RefundResult Refund(string paymentId)
    {
        // your business logic
    }
}
```

That is it.

Zero controllers. Zero DTOs. Zero OpenAPI specs. Zero gRPC proto files. Zero message contracts. Zero dependency injection registrations. Zero boilerplate of any kind.

---

## What Graftcode gives you

### 1. Full abstraction over the communication channel

In calling code you always use simple method calls i.e.:

```csharp
var result = PaymentModule.ProcessPayment(orderId, amount, currency);
```

Graftcode decides how that call is executed:

- **in-process** — nearly as fast as a regular method call
- **gRPC** — fast, binary, cross-machine
- **HTTP/2** — standard network transport
- **RabbitMQ / NATS / Kafka** — for asynchronous workflows
- **WebSocket** — for persistent connections

You never choose the transport in code. You configure it in **Graft Connection String** in code, file or through environment variables.

### 2. Swap channels without rewriting anything

| Environment | Configuration | What happens |
|---|---|---|
| Development / Tests | `local` | Everything runs **in-process** — 10–20x faster than gRPC |
| Staging / Production | `remote` | The same code communicates over a dedicated microservice |
| Hybrid | mixed | `Inventory` and `Payment` run locally, `Order` and `Notification` are remote services |

You change a single flag and any part switch between remote, inMemory, queue or whatever. Business code stays the same.

### 3. Create a new microservice in 5–10 minutes

Step by step:

1. Create a new project (e.g. `ShippingService`).
2. Add a class with public static methods.
3. Run it on new `Graftcode Gateway` (or add it to an existing one).
4. Share access to `Graftcode Vision`, add the module name and address (or leave it as `local`).
5. The rest of the team immediately sees `ShippingModule` with full IntelliSense and types.

Done.

No new API gateway deployment. No OpenAPI update. No client generation. No contract negotiation.

---

## Where this shines

**Large teams building modular monoliths** that want the option to extract any module into a standalone service at any time — without an architecture rewrite.

**Performance-critical backend-to-backend systems** — fintech, trading platforms, real-time analytics, gaming backends — where every millisecond of communication overhead matters.

**Flexible architectures** — today everything runs in one process (fast and cheap), tomorrow 15 separate microservices (easy to scale). The same code, the same tests, the same developer experience.

**Teams tired of the "microservices tax"** — the endless cycle of DTOs, contracts, versioning, client generation, and boilerplate that slows down every feature.

---

## What the traditional approach looks like vs. Graftcode

| Traditional microservices | Graftcode |
|---|---|
| Define OpenAPI / protobuf schema | Write public static methods |
| Generate server stubs and client libraries | Install a Graft as a package |
| Maintain DTO mapping layers | Use native types directly |
| Configure routing, controllers, middleware | Configure `in-code, via graftcode config file or env var` |
| Redeploy API gateway on every change | Regenerate Grafts — no gateway redeployment |
| Coordinate contract versions across teams | Compiler catches incompatibilities at build time |

---

## In short

Graftcode turns backend-to-backend communication into a pure software engineering problem:

- You write business logic as **public static methods** — nothing else.
- Consumers call those methods as if they were local — **strongly typed, with full IDE support**.
- The communication channel is **configured, not coded** — swap between in-process, gRPC, HTTP, or messaging with a single config change.
- New services go live in **minutes**, not days.
- There is **zero boilerplate** between your idea and a working integration.

This is the cleanest possible abstraction between backends — and exactly what Graftcode was designed for.
