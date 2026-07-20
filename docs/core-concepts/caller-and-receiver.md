---
title: "Caller and receiver"
description: "Canonical names for the code initiating a Graft invocation and the runtime executing it."
---

# Caller and receiver

The **caller** is the code that starts an invocation through a Graft. The **receiver** is the runtime side that handles the command and executes the target member.

These names describe one invocation. An application can be a caller in one interaction and host receiving code in another.

## Caller responsibilities

Generated caller code:

- initializes the Graft configuration on first use;
- obtains a runtime context;
- creates commands for static or instance operations;
- returns generated target-language values or raises an error.

Application code remains responsible for choosing configuration and handling latency, failures, retries, and authorization appropriate to the deployment.

## Receiver responsibilities

The receiver:

- accepts serialized commands through an enabled execution path;
- deserializes and dispatches them;
- invokes the hosted member;
- serializes the response.

For remote execution, “looks like a method call” does not mean “has local failure semantics.” Network and receiver failures remain possible.

## REST and Graftcode

REST starts from manually designed resources, routes, HTTP verbs, and payloads. Graftcode starts from an analyzed callable surface and generated package. Both remote forms still cross a process or network boundary.

![REST exposes routes and payloads while Graftcode generates calls from a callable surface](../../assets/diagrams/rest-vs-graftcode.svg)

## Evidence

The terms align with the caller-side `Interpreter.Execute` and receiver-side `Interpreter.Process` paths in Hypertube. Bidirectional callbacks and event guarantees are intentionally not claimed here because the inspected core-concept evidence did not establish their supported scope across runtimes and transports.
