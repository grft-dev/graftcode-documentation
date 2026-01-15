---
title: "REST vs gRPC vs Graftcode"
description: "A practical comparison of REST, gRPC, and Graftcode based on execution model, runtime overhead, and real resource usage."
keywords: "rest vs grpc vs graftcode, performance comparison, runtime integration, cpu memory network usage"
---

Comparing integration technologies often starts with protocol features or developer ergonomics.

This article looks at the comparison from a different angle:

> **What actually happens at runtime when a method is called?**

Instead of focusing on syntax or tooling, we examine execution paths and resource usage for REST, gRPC, and Graftcode.

---

## Execution model differences

Although REST, gRPC, and Graftcode all enable remote calls, they do so at very different levels of abstraction.

### REST

REST-based systems execute calls through a web framework pipeline:

- HTTP request handling
- routing and controller dispatch
- JSON serialization and deserialization
- DTO mapping
- framework-level middleware

Even simple calls involve multiple layers before business logic runs.

---

### gRPC

gRPC removes much of the HTTP and JSON overhead, but still operates at the protocol layer:

- protocol framing
- protobuf serialization and deserialization
- generated client and server stubs
- runtime-to-protocol type translation

Compared to REST, gRPC is more efficient, but execution still passes through a protocol-oriented pipeline.

---

### Graftcode

Graftcode integrates at the **runtime level**.

Instead of adapting execution to a protocol, it:
- represents invocation intent directly
- executes methods using native runtime semantics
- avoids controller and handler layers entirely

Execution is shaped like a method call, not a request.

---

## What the measurements show

The charts below show average resource usage for the same operation executed:
- one million times
- against the same business logic
- implemented using REST, gRPC, and Graftcode

The measurements were taken under comparable conditions to highlight relative overhead, not absolute throughput.

---

## 📊 Resource usage comparison

> **Insert the comparison chart image here**

**Recommended placement:**  
👉 *Directly below this heading, before the next section.*

The chart compares:
- average CPU usage
- average memory usage
- average network throughput

for REST, gRPC, and Graftcode under load.

---

## CPU usage

REST and gRPC show sustained CPU usage driven primarily by:
- serialization and deserialization
- request dispatch pipelines
- framework-level processing

Graftcode exhibits significantly lower CPU usage because:
- execution bypasses web frameworks
- invocation intent is handled at the runtime level
- no text parsing or protocol decoding is involved

The CPU difference becomes more pronounced as call volume increases.

---

## Memory usage

Memory usage follows a similar pattern.

REST and gRPC allocate:
- intermediate request objects
- protocol buffers or JSON structures
- temporary objects created by frameworks

Graftcode allocates substantially fewer intermediate objects:
- invocation intent is represented as object graphs
- reference identity is preserved
- garbage collection pressure is reduced

This leads to lower and more stable memory consumption.

---

## Network usage

Network usage reflects payload efficiency rather than execution cost.

REST typically transmits:
- verbose JSON payloads
- repeated field names
- text-based representations

gRPC reduces payload size through binary encoding, but still requires:
- protocol framing
- schema-driven field encoding

Graftcode transmits only what is required to express invocation intent and results, resulting in:
- smaller payloads
- fewer round trips
- more predictable network behavior

---

## Why the differences scale with load

At low traffic volumes, performance differences may appear modest.

As load increases:
- serialization costs compound
- allocation pressure grows
- CPU usage rises faster than business logic complexity

Because Graftcode removes entire classes of overhead, its resource usage grows closer to linearly with actual work performed.

---

## Performance as a side effect of execution model

The performance characteristics shown here are not the result of aggressive optimization or caching.

They are a natural consequence of:
- executing closer to the runtime
- avoiding protocol-shaped execution
- minimizing unnecessary work

This makes performance behavior easier to reason about and more stable under load.

---

## Try it yourself: Performance Lab

To make these differences tangible, Graftcode provides a **Performance Lab** where you can run the same test directly from your browser.

In the lab, you can:
- execute the same method
- using REST, gRPC, or Graftcode
- with a fixed number of invocations (for example, 1,000 calls)
- and observe timing and resource differences

> **Link to Performance Lab:**  
> *(Insert link here once published)*

The goal of the lab is not to win benchmarks, but to let you observe how execution models behave under identical conditions.

---

## Choosing the right tool

REST, gRPC, and Graftcode all have valid use cases.

The key difference is where integration happens:
- REST integrates at the web framework level
- gRPC integrates at the protocol level
- Graftcode integrates at the runtime level

Understanding this distinction makes the performance differences predictable rather than surprising.

---

## Closing perspective

REST and gRPC optimize how requests are transported.

Graftcode changes what *a request is*.

By treating integration as runtime execution rather than protocol exchange, it removes layers that other approaches cannot avoid—leading to lower CPU usage, lower memory consumption, and more efficient network behavior.
