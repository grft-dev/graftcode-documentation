---
title: "Type mapping"
description: "How UGM primitive categories map to generated .NET and TypeScript types, and where generation can fail."
---

# Type mapping

Type mapping occurs between the producer analyzer, the UGM, and the target code generator. Support is a property of that complete path—not just the source language.

## Verified target mappings

For generated TypeScript/JSDoc, current primitive mappings include:

- string and char → `string`;
- numeric primitive categories → `number`;
- boolean → `boolean`;
- void → `void`;
- nullable values → a union with `null`;
- Graft model types → generated class names.

For generated .NET, current mappings include:

- string → `string`;
- integer and unsigned integer → `int`;
- boolean → `bool`;
- float → `float`;
- byte → `byte`;
- char → `char`;
- long and unsigned long-long → `long`;
- double → `double`;
- nullable supported value types → `?`;
- Graft model types → generated or known local types.

Unknown values can degrade to `unknown` in TypeScript or `object` in .NET, except where an unresolved local class is recognized.

## Supported surface is stricter than discovery

The package-generation engine rejects framework complex types in public interfaces. Its tests use `System.DateTime` as an example. Therefore, a type appearing in analyzer output does not prove that package generation will accept it.

Use simple primitives and explicitly modeled public types. Prefer ISO-8601 strings and string identifiers for cross-language contracts unless the exact producer/consumer pair has generation and runtime tests for richer types.

## Collections, generics, callbacks, and nullability

The implementation contains handlers for arrays, generics, delegates, nested types, and nullable metadata, but support varies by analyzer and target generator. Verify each intended language pair with generator tests or a generated-package smoke test.

## Evidence

Verified against `SharedPrimitiveTypeHandler.cs`, `primitive-type-converter.ts`, nullable generator tests, and package-generation unsupported-type tests. This is not a complete compatibility matrix.
