---
title: "Public surface vs implementation"
description: "Separate the callable contract discovered by Graftcode from private implementation details."
---

# Public surface vs implementation

The **callable surface** is the part of a module represented in its UGM and therefore available for generated Grafts. The **implementation** is everything that executes behind that surface.

![Public callable surface forms the contract while implementation details remain behind it](../../assets/diagrams/public-surface-vs-implementation.svg)

## What analysis includes

For .NET, the inspected analyzer starts from exported, visible top-level types. For each type it records public declared instance and static methods, public constructors, public fields and properties, and public nested types. Special-name methods are excluded, and type and method filters can narrow the result.

For Node.js/TypeScript, analysis starts from runtime exports and supported re-exports, including CommonJS patterns. Type-only exports are skipped. The exact supported export forms are analyzer-specific, so an exported declaration is not automatically proof that every part of it can be generated for every target.

## Keep internals behind the boundary

Helpers, persistence code, transport adapters, secrets, and framework objects should remain non-public or non-exported. A small surface:

- reduces the model that consumers depend on;
- makes generated packages easier to understand;
- limits type-mapping failures;
- makes contract changes easier to classify.

This is a design rule, not a security boundary by itself. Authorization still belongs in the hosted implementation and deployment configuration.

## Public does not mean supported

Discovery and package generation are separate checks. For example, the .NET analyzer can describe public members whose signatures later fail package generation. The package-generation tests explicitly reject unsupported framework complex types such as `System.DateTime`.

Use [Type mapping](type-mapping.md) before publishing a contract.

## Evidence

Verified against:

- `.NET`: `graftcode-module-analyzer/.../LibraryAnalyzer.cs` and `GetTypeAnalyzerHandler.cs`
- `Node.js`: `graftcode-module-analyzer/.../export.analyzer.ts`
- generation rejection: `graftcode-package-generation-engine/.../UnsupportedTypeUsageExceptionTests.cs`

The exact hosted surface can also be narrowed by Gateway `--types` and analyzer method filters; the inspected Gateway README documents `--types`, while analyzer tests verify method filtering.
