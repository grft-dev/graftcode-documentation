---
title: "Why runtime-level integration is faster"
description: "Understand why integrating systems at the runtime level is fundamentally faster than REST or gRPC, and how Graftcode avoids unnecessary layers, serialization, and execution overhead."
keywords: "runtime integration, performance, rest vs runtime, grpc vs runtime, graftcode performance"
---

Performance differences between integration technologies are often explained using benchmarks and charts.

While those are useful, they usually hide the most important question:

> **Where does the work actually happen?**

Graftcode takes a different approach to integration by operating at the **runtime level**, rather than at the protocol or payload level. This section explains why that difference matters and why it leads to lower latency, lower CPU usage, and lower memory pressure.

---

## Integration usually happens above the runtime

Traditional integration technologies—such as REST and gRPC—operate *above* the runtime.

They rely on:
- controllers or service handlers
- request parsing and routing
- serialization and deserialization
- schema validation
- transport-level abstractions

Even highly optimized protocols like gRPC still require:
- marshaling data into protocol-specific formats
- copying data between buffers
- translating between transport types and runtime types

Each of these steps introduces overhead that is independent of business logic.

---

## Runtime-level integration removes entire layers

Runtime-level integration works differently.

Instead of translating execution into payload-oriented protocols, Graftcode translates **invocation intent** into runtime-oriented representations that are executed natively by the target runtime.

There is no intermediate representation shaped like HTTP, JSON, or protobuf schemas that needs to be:
- parsed
- validated
- or mapped into runtime objects

The runtime already knows how to execute the call. Graftcode connects runtimes directly.

---

## No controllers, no handlers, no adapters

Because integration happens at the runtime level:
- there are no controllers
- no request handlers
- no transport adapters
- no schema mappers

A method call is executed as a method call.

This eliminates:
- routing overhead
- framework dispatch costs
- reflection-heavy pipelines common in web frameworks

The execution path becomes significantly shorter and more predictable.

---

## Native type handling instead of serialization pipelines

One of the largest performance costs in distributed systems comes from serialization.

REST systems typically:
- convert objects to JSON
- parse JSON back into objects
- allocate intermediate representations
- traverse complex parsing trees

gRPC improves this with binary formats, but still requires:
- marshaling and unmarshaling
- buffer management
- translation between protocol types and runtime types

Graftcode avoids this entire class of work by:
- operating on runtime-native types
- transferring only what is necessary
- reconstructing native types directly on the receiving side

This results in fewer allocations, fewer copies, and significantly less CPU work.

---

## The current intermediate layer (and why it is still fast)

In the current implementation, invocation intent is internally translated into **structured object representations**, which are then serialized using a compact binary format.

This intermediate layer exists as a pragmatic step that allows the system to evolve safely while preserving:
- strong typing
- stable execution semantics
- and robust tooling

Even with this intermediate step in place, the execution path remains significantly shorter than REST or gRPC pipelines because:
- the representation is runtime-native
- serialization is binary and purpose-built
- no web frameworks or protocol adapters are involved

---

## Object-based, reference-oriented execution

A key characteristic of the current intermediate model is that it is **object-based and reference-oriented**, not text-based.

Invocation intent is represented as structured object graphs that preserve references and identity, rather than being flattened into textual representations.

As a result:
- traversal and processing of invocation data has constant cyclomatic complexity
- execution does not depend on payload size or structure depth
- object identity and relationships are preserved naturally

This is fundamentally different from text-based serialization formats such as JSON, where:
- objects must be flattened into text
- references are lost and reconstructed
- parsing introduces branching logic and variable complexity
- deserialization cost grows with payload complexity

Even before removing the intermediate layer entirely, this model already eliminates the most expensive part of traditional integration pipelines: **text parsing and reconstruction**.

---

## The path to direct binary invocation streams

The long-term direction of Graftcode is to remove the remaining intermediate step entirely.

Future versions will generate the binary invocation stream directly from invocation intent, eliminating the translation step altogether.

This evolution:
- does not change the programming model
- does not affect execution semantics
- further reduces overhead by collapsing the runtime path even closer to native execution

The system becomes simpler—not more complex.

---

## Fewer context switches and lower memory pressure

Every additional layer in an integration stack introduces:
- extra function calls
- additional stack frames
- intermediate objects
- garbage collection pressure

By collapsing integration into the runtime itself, Graftcode:
- reduces call depth
- minimizes temporary allocations
- keeps execution close to business logic

This directly improves:
- latency consistency
- throughput
- memory efficiency

---

## In-memory execution has near-zero overhead

When calls execute in memory—either within the same runtime or across runtimes in the same process—the overhead is minimal.

There is:
- no network latency
- no transport encoding
- no protocol framing

Calls behave almost identically to local method calls, while still respecting module boundaries and execution isolation.

This makes runtime-level integration especially effective for:
- modular monoliths
- local development
- high-throughput internal workflows

---

## Network cost becomes the dominant factor

When execution is remote, the dominant cost becomes **network latency**, not integration overhead.

Because Graftcode minimizes everything else:
- CPU usage drops
- memory usage is reduced
- network cost becomes predictable and isolated

This is why performance differences are especially visible under load.

---

## Execution semantics remain unchanged

A key property of runtime-level integration is that execution semantics do not change when crossing boundaries.

Synchronous calls remain synchronous.  
Asynchronous calls remain asynchronous.  
Exceptions propagate as native exceptions.

There is no need to:
- flatten errors
- encode status codes
- reconstruct call stacks artificially

This removes entire categories of defensive code and runtime checks.

---

## Performance as a consequence of simplicity

Performance in Graftcode is not achieved through:
- unsafe shortcuts
- aggressive caching
- or hidden optimizations

It emerges naturally from:
- removing unnecessary layers
- avoiding repeated work
- and letting runtimes do what they already do well

This makes performance predictable rather than fragile.

---

## Closing perspective

Runtime-level integration is faster not because it is clever, but because it is simpler.

By connecting runtimes directly and avoiding protocol-shaped execution, Graftcode removes entire layers of overhead that traditional integration approaches cannot avoid.

What remains is the work that actually matters: executing your code.
