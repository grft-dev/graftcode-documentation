---
title: "Vision and runtime disagree"
description: "Diagnose Graftcode Vision data that differs from Gateway output, generated packages, or runtime behavior."
keywords: "graftcode vision stale, contract mismatch, gateway UI, generated package mismatch"
---

# Vision and runtime disagree

## Symptoms

- Vision omits a type that Gateway reported as enabled.
- Vision displays an older or different method signature.
- An install command or code sample in Vision does not match the installed package.
- Vision loads, but runtime calls reach another contract or Gateway.
- Vision is unavailable although service calls work, or the reverse.

## Diagnostics

1. **Confirm process identity.** Vision is associated with the Gateway process hosting it. Record the
   Vision address/port and the runtime-call host/port; do not assume two localhost ports, containers, or
   replicas refer to the same process.
2. **Use Gateway startup output as the timeline.** Confirm the intended module/runtime was loaded and
   model publication completed before Vision was opened.
3. **Check Vision's listener separately.** Vision HTTP and runtime-call transports use different ports.
   A working UI does not prove the WebSocket/TCP/HTTP2 listener is reachable, and a working call does
   not prove Vision HTTP is exposed.
4. **Compare the model, package, and runtime as separate artifacts.**
   - Gateway/Vision model: what was analyzed for that process.
   - Generated package: what was produced for a target ecosystem and version.
   - Runtime provider: what the call host currently loaded.
5. **Check filters and artifact freshness.** Type/method filters or a stale built module can make Vision
   correctly display a surface different from the source tree.
6. **Check routing through proxies and replicas.** Vision and runtime traffic can be routed to different
   Gateway instances. Without a proven deployment policy, do not assume replicas have identical loaded
   modules or registry identities.
7. **Refresh only after verifying backend state.** A browser refresh cannot fix wrong process routing,
   failed publication, stale provider artifacts, or an old installed package.
8. **Treat UI snippets as release-scoped evidence.** Exact Vision install-command, execution, and live
   refresh behavior is not established for every release by the inspected backend tests.

## Fixes

- Point both Vision and runtime-call configuration at the intended Gateway deployment.
- Restart/redeploy Gateway with the exact built provider artifact, runtime, and filters; wait for
  successful analysis/publication.
- In a multi-instance deployment, make module/version configuration consistent or route diagnostic
  traffic to one identified instance.
- Copy a fresh install command from that process and verify the installed package version and generated
  declarations.
- If Gateway output and its model are correct but Vision alone is wrong, capture the UI response and
  report a Vision defect; do not mutate the provider contract to compensate for a stale UI.

## Escalation evidence

Provide Gateway instance identity, Vision URL/port, runtime-call host/port, startup output, loaded module
and version, active filters, screenshots or exported UI text, emitted package coordinate, installed
package version, and proxy/replica routing details. Redact project keys and credentials.

## Next steps

If the analyzed model is wrong, continue with
[Module, method, or type is missing](module-discovery-missing-method-unsupported-type.md). If only the
installed consumer remains old, continue with [Installed package is stale](stale-package.md).
