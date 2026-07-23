---
title: "Installed package is stale"
description: "Diagnose Callers that still expose or call an older Graft contract after Receiver changes."
keywords: "stale graft package, old contract, package cache, gateway restart, compatibility"
---

# Installed package is stale

## Symptoms

- The Receiver has a new method, but the Caller cannot import or compile against it.
- Reinstalling appears to leave the old generated API in place.
- Vision shows one contract while the caller invokes another.
- A method compiled successfully but fails after a Receiver deployment changed its signature.

## Diagnostics

1. **Establish four versions independently:** Receiver artifact/module version, published model/package
   version, installed generated package version, and the version loaded by the running Caller.
2. **Confirm the new Receiver artifact was analyzed.** A successful Receiver build is not enough; verify
   Gateway loaded that output and completed model publication.
3. **Check registry identity.** A Gateway restart without a stable project key can emit a different
   registry identifier. Reusing an older source can continue to resolve the older package.
4. **Copy the newly emitted install coordinate.** Do not assume the package name or version changed in
   the way a public package manager normally would.
5. **Inspect the installed artifact, not only the manifest request.** Check generated declarations,
   exports, namespaces, assembly/package metadata, and the lockfile/resolved dependency graph.
6. **Eliminate process/tool caches.** Stop the caller or dev server before evaluating the result.
   Language runtimes and bundlers can retain loaded modules even after files change.
7. **Compare the callable surface.** A new source method may still be absent due to visibility, export
   rules, filters, unsupported types, or target-generator mapping.
8. **Treat contract changes as potentially breaking.** Renames, removals, parameter changes, return-type
   changes, static/instance changes, constructors, nullability, and new unsupported types can invalidate
   an old Caller.

## Fixes

- Republish from the intended Receiver artifact and wait for successful model upload.
- Install the exact package coordinate emitted by that same Gateway/Vision instance.
- Update the lockfile/resolved dependency using the package manager's normal supported workflow, then
  verify the installed version and generated source.
- Restart the caller, test runner, dev server, or bundler after replacement.
- If an old Caller must remain live, keep the old hosted contract/version available only after
  proving side-by-side behavior in the deployment. Side-by-side compatibility is not universal.
- For a breaking change, publish and roll out a deliberately versioned facade and compile/smoke-test
  each Caller before switching traffic.

Do not rely on automatic breaking-change detection, silent package refresh, old-package retention, or
old-client/new-Receiver compatibility unless the deployed release has explicit tests for it.

## Data to collect before reporting

Provide the four versions, redacted registry identity, emitted coordinate, lockfile entry, installed
generated declaration/namespace, Gateway model publication output, and the exact source contract
change.

## Next steps

If the new model itself lacks the method, continue with
[Module, method, or type is missing](module-method-or-type-is-missing.md). If the model
is correct but only the UI is stale, continue with [Vision and runtime disagree](vision-and-runtime-disagree.md).
