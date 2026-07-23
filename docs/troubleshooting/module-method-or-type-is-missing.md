---
title: "Module, method, or type is missing"
description: "Diagnose Gateway module discovery, missing generated members, filters, and unsupported public types."
keywords: "graftcode module not discovered, missing method, unsupported type, HTTP 422"
---

# Module, method, or type is missing

## Symptoms

- Gateway starts but no expected type or method appears.
- Vision or the generated package omits a public member.
- Gateway loads an unintended runtime or module.
- Package generation returns HTTP **422**, “Package not supported,”
  `FRAMEWORK_TYPE_IN_PUBLIC_API`, or “Using complex types from framework in public interfaces is not
  supported yet.”

## Diagnostics

1. **Verify the input artifact.** Build the Receiver and confirm Gateway is pointed at the actual output
   DLL, JAR, package directory, source directory, or entry file—not a stale or source-only path.
2. **Make runtime selection explicit when auto-detection is ambiguous.** Gateway scans the current
   directory when no module is supplied; mixed files can cause wrong detection. Use the runtime and
   module options shown by `gg --help` for the installed release.
3. **Read startup output in order.** Find runtime selection, module load, discovered/enabled types,
   analysis errors, and model-upload/publication completion. Fix the earliest failed stage.
4. **Check callable-surface rules.**
   - .NET requires visible top-level types and public declared methods; special-name methods are treated
     separately.
   - Node.js/TypeScript starts from runtime exports; type-only exports are not callable.
   - Other runtimes require loadable public declarations; see the [runtime-specific notes](../reference/known-limitations.md#runtime-specific-notes).
5. **Check active filters.** A type or method filter can intentionally remove a member. Compare the
   fully qualified type and bare/qualified method names against the configured patterns.
6. **Inspect the analyzed model before the generated package.** If the member is absent from the model,
   fix visibility, exports, module selection, or filters. If it is present but absent from one target
   package, the target generator/mapping is the failing stage.
7. **For HTTP 422, locate the named type.** Inspect parameters, return types, public properties, generic
   arguments, base types, and constructor parameters. Framework complex types can be rejected even when
   they were discovered.

## Fixes

- **Wrong artifact/runtime:** rebuild, point Gateway at the exact built artifact, and select the matching
  runtime. For JVM Receivers, package the expected JAR; for Node, ensure `main`/`exports` points to the
  built entry; for interpreted runtimes, install Receiver dependencies in Gateway's environment.
- **Member not public/exported:** expose only the intended facade member using the source language's
  public/export mechanism, then republish.
- **Filter excludes member:** correct or remove the active filter and confirm the new model before
  reinstalling.
- **Unsupported framework type:** replace it with primitives or an explicitly modeled public type.
  Common portable representations are ISO-8601 strings for dates/times and strings for identifiers.
- **Generic/inheritance/callback shape fails:** expose a concrete, flattened request/result facade and
  keep the advanced source-language shape internal.
- **Constructor mismatch:** use a single unambiguous constructor with supported parameter types or a
  static factory with explicit IDs.

Do not treat successful discovery as final success. The corrected contract must complete analysis,
publication, target package generation, Caller compilation, and an invocation smoke test.

## Data to collect before reporting

Provide the module path, selected runtime, complete discovery/publication error, relevant public
signature, active type/method filters, target Caller runtime, and the 422 error code/message. Reduce
the Receiver to the smallest public declaration that reproduces the failure.

## Next steps

After the expected model appears, reinstall the package using
[Package installation fails](package-installation-fails.md). If Vision still differs from startup output,
continue with [Vision and runtime disagree](vision-and-runtime-disagree.md).
