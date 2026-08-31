---
title: "Errors and status reference"
description: "Package-generation status behavior and operational failure categories."
---

# Errors and status reference

## Package generation

| Signal | Meaning | Action |
| --- | --- | --- |
| HTTP `422 Unprocessable Entity` | Package generation understood the request but the public contract uses an unsupported feature | Fix the Receiver surface, republish, and request the package again |
| `[GRAFT:FRAMEWORK_TYPE_IN_PUBLIC_API]` | A framework complex type appears in a public API | Replace the named type in signatures and public model members |
| `Using complex types from framework in public interfaces is not supported yet. Type used <type>` | Framework-type error message | Use primitives/plain models; regenerate |

Treat `422` as the signal that a public type is unsupported for package generation. Do not generalize
it into a complete HTTP status contract for every package-manager route.

## Gateway and invocation

| Failure | Likely boundary | Action |
| --- | --- | --- |
| No discovered type | Module/runtime selection or public exports | Pass the module path explicitly; inspect Vision |
| Local module `FileNotFound` | Caller remained in `inmemory` | Configure generated remote host before first call |
| Connection failure | Listener, route, firewall, proxy, or Gateway | Verify selected port/protocol and process readiness |
| Receiver exception | User code or Receiver dependency | Preserve actionable message; do not retry domain errors |
| State missing after restart | Remote object identity was stateful | Recreate state or redesign static/stateless |
| Package `404` | Wrong/stale registry-qualified command | Copy the current command from Vision |

There is no universal mapping from Receiver exceptions to HTTP-like status codes. Runtime calls
surface native/runtime errors through Hypertube, so test error handling for each generated Caller.

## Next steps

- [Handle Receiver errors](../how-to-guides/handle-receiver-errors.md)
- [In-memory execution and Hypertube exceptions](../troubleshooting/in-memory-hypertube-exceptions.md) — embedded
  runtime paths, activation, and Hypertube exception catalog
- [Timeouts and retries](../operations/timeouts-and-retries.md)
