---
title: "Troubleshooting"
description: "Start from a Graftcode symptom and follow evidence-based diagnostics without guessing registry coordinates or commands."
keywords: "graftcode troubleshooting, gateway errors, package installation, module discovery, connection timeout"
---

# Troubleshooting

Start with the visible symptom. Preserve the Gateway output, package-manager output, generated package
version, runtime versions, and the first complete exception before changing configuration.

## Choose the symptom

- **The generated package will not install, restore, or resolve:**  
  [Package installation fails](package-installation.md)
- **Gateway does not discover a module, a method is missing, or generation reports an unsupported
  type/HTTP 422:**  
  [Module, method, or type is missing](module-discovery-missing-method-unsupported-type.md)
- **A call cannot connect, times out, or is rejected by authentication:**  
  [Connection, timeout, or authentication failure](connection-timeouts-auth.md)
- **The installed Graft exposes an older contract:**  
  [Installed package is stale](stale-package.md)
- **Gateway or a hosted runtime exits during startup or invocation:**  
  [Gateway or runtime exits](runtime-exits.md)
- **Vision does not match Gateway output or generated code:**  
  [Vision and runtime disagree](vision-mismatch.md)

## Capture this evidence first

1. The exact provider module path and runtime selected by Gateway.
2. Gateway startup output from process start through module analysis and publication.
3. The package-manager command copied from that same running Gateway/Vision.
4. Provider, Gateway, generated package, Hypertube dependency, and caller runtime versions.
5. Resolved Graft host and execution mode: in-memory, WebSocket, HTTP/2, TCP, or plugin.
6. Whether the failure occurs before publication, during installation, at the first call, or after a
   restart.

Do not post project keys, JWTs, authorization headers, private registry credentials, or package-manager
credential files. Redact values while preserving header names, status codes, and error categories.

## Diagnostic boundaries

- Package generation and package installation happen before normal runtime calls.
- Vision describes the Gateway process that hosts it; another Gateway can show a different model.
- Analyzer discovery does not prove that every target generator accepts the discovered types.
- A remote failure has network and authentication causes that do not exist in in-memory mode.
- Generated runtime context is cached after first initialization; late configuration changes may not
  affect the current process.

## Next steps

Open the symptom page above. If no page matches, reduce the issue to the earliest failing stage:
discovery, publication, installation, import/compile, connection, authentication, invocation, or result
mapping.
