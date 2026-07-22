---
title: "Gateway or runtime exits"
description: "Diagnose Gateway startup exits, hosted runtime crashes, native binary failures, and invocation-triggered termination."
keywords: "graftcode gateway exits, runtime crash, native binary, startup failure"
---

# Gateway or runtime exits

## Symptoms

- Gateway exits immediately or before Vision becomes available.
- A hosted runtime terminates while loading a module.
- The process stays up until a particular invocation, then exits.
- A container repeatedly restarts without a complete application error.
- The operating system reports a missing or incompatible native library.

## Diagnostics

1. **Capture the process exit code and complete output.** Preserve output from process start, not only
   the final line. In a container, capture both the container state and Gateway output.
2. **Locate the last completed startup stage:** argument parsing, port binding, runtime detection,
   native-runtime load, Receiver dependency load, module analysis, model upload, Vision startup, or
   first invocation.
3. **Make the input deterministic.** Use the exact Receiver module and matching runtime instead of
   current-directory scanning/auto-detection when investigating an exit.
4. **Check runtime prerequisites.** Verify the documented interpreter/framework/JDK is installed and
   visible to the Gateway process. For JVM hosting, verify `JAVA_HOME`; for interpreted Receivers,
   verify their dependencies in Gateway's runtime environment.
5. **Check port binding.** Gateway defaults can be occupied, blocked, or require privileges. Confirm
   the deployment's configured ports are available; do not assume startup reached module loading.
6. **Check OS and architecture.** Native libraries and plugin names differ on Windows, Linux, and
   macOS. Confirm Gateway, runtime, module, plugins, and container architecture agree.
7. **Check Receiver entry-point behavior.** Gateway has a separate application-entry option. Do not
   assume hosting a library should run its application entry point, or vice versa.
8. **Isolate invocation-triggered exits.** Reproduce with one method and simple arguments. Determine
   whether Receiver code, a native dependency, serialization, callback, or plugin is the last observed
   component.
9. **Distinguish handled exceptions from process termination.** A propagated invocation exception
   should reach the caller; an OS-level crash, abort, out-of-memory kill, or native fault requires
   process/platform diagnostics.

## Fixes

- **Wrong runtime/module:** rebuild for the intended target and host the exact output with the matching
  runtime.
- **Missing Receiver dependency:** install it in the Gateway runtime environment or package it using
  the Receiver ecosystem's supported mechanism.
- **Port/permission failure:** configure available non-conflicting ports appropriate to the deployment.
- **Native library failure:** use binaries built for the target OS/architecture and preserve generated
  extraction/install behavior. Use the no-extraction option only when the deployment supplies all
  required binaries correctly.
- **Receiver crash:** fix or isolate the Receiver/native dependency. Do not hide process termination
  behind automatic retries.
- **Out-of-memory or forced kill:** confirm through OS/container signals, then reduce workload or set
  tested resource limits; a missing managed exception is not proof of a Graftcode transport fault.

## Data to collect before reporting

Provide exit code/signal or container termination reason, full startup output, exact Gateway version,
selected runtime and version, OS/architecture, Receiver artifact target, enabled plugins/listeners, and
the smallest invocation that reproduces the exit. Include an OS crash dump or native backtrace when
available, with secrets removed.

## Next steps

Once the process remains running, verify discovery with
[Module, method, or type is missing](module-discovery-missing-method-unsupported-type.md), then verify
remote invocation with [Connection, timeout, or authentication failure](connection-timeouts-auth.md).
