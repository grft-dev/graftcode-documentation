---
title: "Package installation fails"
description: "Diagnose generated Graft package restore, registry, dependency, and import failures."
keywords: "graft package install failure, NuGet, npm, Maven, pip, Composer, RubyGems"
---

# Package installation fails

## Symptoms

- The package manager reports not found, unauthorized, unreachable, or dependency resolution errors.
- Installation succeeds but the generated namespace, import, or class cannot be found.
- A normal public dependency stops resolving after adding a Graft registry.
- npm cannot resolve `hypertube-nodejs-sdk` or resolves a different SDK name from old instructions.

## Diagnostics

1. **Return to the Gateway that published this contract.** Confirm module discovery and model
   publication succeeded before troubleshooting the consumer.
2. **Copy the complete emitted command again.** Compare registry URL, project/registry identifier,
   package name, version, scope/group, and source options character for character. Do not normalize
   casing or construct a coordinate from the provider namespace.
3. **Confirm the package manager is running in the intended project/environment.** Check the active
   .NET project, Node working directory, Python virtual environment, Maven/Gradle project, Composer
   project, or Ruby bundle.
4. **Separate registry failures from package failures.** A not-found response from the default public
   registry commonly means the dynamic Graft registry was omitted. An authorization response means the
   configured source credentials/project access must be checked; it is not a runtime-call failure.
5. **Inspect resolved package metadata and the lockfile.** Verify the generated package version and its
   declared runtime dependency. Current Node generator/package-manager evidence uses
   `hypertube-nodejs-sdk`; do not substitute `javonet-nodejs-sdk`.
6. **Preserve ordinary public sources.** A generated feed may not mirror every unrelated dependency.
   Use the package manager's supported source mapping/order so normal packages still resolve from their
   normal registry.
7. **Use generated imports, not package filenames.** Distribution names and code import names can
   differ by casing, separators, scopes, and nested namespaces.

## Fixes by failure stage

- **Package not found:** use the exact registry-qualified command emitted by the active Gateway/Vision.
  If Gateway restarted without a stable project identity, obtain the new emitted command.
- **Unauthorized:** verify the registry/project credentials configured for the package manager. Do not
  put a Gateway `--projectKey` into application source or assume it authenticates runtime calls.
- **Dependency missing:** inspect the generated package manifest and use the dependency name/version it
  declares. If the artifact does not declare a needed dependency, record the artifact version and
  report it as a packaging defect rather than applying a universal manual-install rule.
- **Import/namespace missing:** inspect the installed package exports, declarations, or assembly and
  copy the usage snippet produced for that artifact.
- **Public packages no longer restore:** restore the normal public source and apply source mapping
  appropriate to the package manager.
- **Native extraction/platform error:** verify OS and architecture compatibility and retain generated
  install scripts. Do not copy native binaries from another platform.

## Escalation evidence

Provide the redacted emitted install command, package-manager error, package manifest metadata, lockfile
entry, Gateway publication output, OS/architecture, and runtime versions. Never include credentials or
project keys.

## Next steps

If installation now succeeds but the API is old, continue with
[Installed package is stale](stale-package.md). If the expected package or method was never generated,
continue with [Module, method, or type is missing](module-discovery-missing-method-unsupported-type.md).
