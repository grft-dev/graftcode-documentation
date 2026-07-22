---
title: "Invocation lifecycle"
description: "The verified sequence from generated wrapper call through configuration, transport, dispatch, and response."
---

# Invocation lifecycle

![Caller business logic calls the generated Graft; Hypertube carries the invocation through Graftcode Gateway to the Receiver's business logic and returns the result](../../assets/diagrams/how-it-works-diagram.svg)

1. **Application code calls a generated member.** Static and instance members use different generated handlers.
2. **The generated `GraftConfig` initializes once.** It loads known environment and file sources, registers the generated default, and initializes a named runtime context.
3. **Configuration resolution selects connection data.** The winning source determines in-memory, WebSocket, HTTP/2, TCP, or plugin behavior.
4. **Generated code builds an operation.** Instance operations carry the generated instance context; static operations target the type directly.
5. **Hypertube serializes the command.**
6. **The selected execution path sends or dispatches it.** In-memory .NET commands can call the receiver directly; network paths use their configured clients or native transmitter.
7. **The receiver deserializes and handles the command.**
8. **A response is serialized, returned, and converted by generated code.**

## Failure points

Failures can occur before execution (missing package or invalid configuration), during connection/transport, during dispatch, in user implementation code, or while mapping a response. Remote calls therefore require normal distributed-systems handling even though the call site resembles ordinary code.

## What does not happen per call

The module is not re-analyzed and the Graft package is not regenerated during an ordinary invocation. Those belong to the package/build path.
