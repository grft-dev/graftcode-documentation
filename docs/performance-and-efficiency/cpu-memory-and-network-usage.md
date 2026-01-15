---
title: "CPU, memory, and network usage"
description: "A detailed look at how REST, gRPC, and Graftcode differ in CPU usage, memory consumption, and network traffic under real workloads."
keywords: "cpu usage, memory usage, network traffic, rest performance, grpc performance, graftcode efficiency"
---

When comparing integration technologies, raw latency numbers rarely tell the full story.

In real systems, the dominant costs are often:
- CPU cycles spent on integration overhead
- memory allocated and reclaimed during request handling
- network bandwidth consumed by payload representation

This section explains how REST, gRPC, and Graftcode differ across these three dimensions, and why those differences appear consistently under load.

---

## CPU usage

CPU consumption in distributed systems is largely driven by **work that is not business logic**.

### REST

In REST-based systems, CPU is consumed by:
- request parsing and routing
- middleware execution
- JSON serialization and deserialization
- validation and model binding
- framework-level abstractions

Even when business logic is trivial, the CPU cost of processing requests remains significant because it scales with request volume, not with logic complexity.

---

### gRPC

gRPC reduces CPU usage compared to REST by:
- using binary encoding instead of JSON
- relying on generated stubs instead of reflection-heavy frameworks

However, CPU is still spent on:
- protobuf marshaling and unmarshaling
- buffer management
- translating protocol types into runtime types

The cost per call is lower than REST, but it remains proportional to message volume and schema complexity.

---

### Graftcode

Graftcode consumes CPU primarily for:
- executing business logic
- minimal runtime-level invocation handling

Because it avoids:
- web framework pipelines
- text parsing
- protocol-specific dispatch

CPU usage grows much closer to the actual work performed by the application.

In practice, this results in significantly lower and more stable CPU utilization under sustained load.

---

## Memory usage

Memory behavior is often the hidden cost of integration.

### REST

REST-based systems allocate memory for:
- request and response objects
- parsed JSON structures
- intermediate DTOs
- framework-internal state

These allocations:
- increase garbage collection pressure
- introduce latency variability
- scale with request volume

Memory usage remains elevated even when requests are simple.

---

### gRPC

gRPC reduces some allocation overhead by:
- using binary buffers
- relying on generated code

However, memory is still allocated for:
- protobuf message objects
- intermediate buffers
- conversion between protocol and runtime representations

While more efficient than REST, memory usage still reflects the cost of protocol translation.

---

### Graftcode

Graftcode minimizes memory usage by:
- representing invocation intent as object graphs
- preserving references instead of flattening structures
- avoiding intermediate transport-layer representations

Because fewer temporary objects are created:
- memory usage is lower
- garbage collection is less frequent
- memory pressure remains stable under load

This is especially visible in long-running services.

---

## Network usage

Network usage is influenced by how data is represented and transmitted.

### REST

REST typically transmits:
- verbose JSON payloads
- repeated field names
- text-based representations

This results in:
- larger payload sizes
- higher bandwidth consumption
- increased network cost at scale

---

### gRPC

gRPC improves network efficiency by:
- using compact binary encoding
- eliminating repeated field names

However, payloads still include:
- protocol framing
- schema-driven field encoding

Network usage is reduced compared to REST, but remains tied to protocol representation.

---

### Graftcode

Graftcode transmits:
- only invocation intent
- minimal metadata required for execution
- compact binary representations

Because the runtime already understands the execution model, there is no need to transmit:
- routing information
- protocol metadata
- redundant structural data

This leads to smaller payloads and more predictable network usage.

---

## How these costs compound under load

At low request volumes, differences in CPU, memory, and network usage may seem modest.

As load increases:
- serialization costs accumulate
- memory allocations compound
- garbage collection becomes more frequent
- network traffic grows non-linearly

Because Graftcode removes entire categories of overhead, its resource usage scales more directly with business logic execution rather than with integration mechanics.

---

## Efficiency without tuning

An important observation is that these gains do not depend on:
- custom tuning
- hand-optimized serialization
- specialized configuration

They emerge naturally from:
- runtime-level execution
- reduced abstraction layers
- simpler execution paths

This makes performance behavior easier to predict and reason about in production systems.

---

## Practical implications

Lower CPU usage:
- reduces compute requirements
- improves density on shared nodes
- lowers scaling pressure

Lower memory usage:
- reduces garbage collection overhead
- improves latency consistency
- simplifies capacity planning

Lower network usage:
- reduces bandwidth costs
- improves performance across regions
- minimizes cross-zone traffic

Together, these effects have a direct impact on both performance and operational cost.

---

## Closing perspective

CPU, memory, and network usage are not independent concerns—they are all influenced by how integration is implemented.

By shifting integration to the runtime level, Graftcode reduces unnecessary work across all three dimensions, allowing system resources to be spent where they matter most: executing business logic.
