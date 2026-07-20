---
title: "Type mapping"
description: "How UGM values map into supported consumer languages and where generation can fail."
---

# Type mapping

Type mapping occurs between the producer analyzer, the UGM, and the target code generator. Support is a property of that complete path—not just the source language.

## Detailed mappings verified in generators

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

## Portable baselines for all generated consumers

The repository also contains generators and cross-runtime smoke tests for Java/JVM, Python, PHP, and
Ruby. Their conservative public-contract baselines are:

- **Java/JVM:** `String`, primitive numbers, `boolean`, plain Java objects, and homogeneous arrays.
- **Python:** `str`, `int`, `float`, `bool`, simply typed classes, and homogeneous `list[T]` values.
- **PHP:** `string`, `int`, `float`, `bool`, typed plain classes, and homogeneous sequential arrays.
- **Ruby:** `String`, `Integer`, `Float`, booleans, small value objects, and homogeneous `Array` values.

These are interoperability baselines, not exhaustive mappings. Boxed and nullable values, unions,
enums, records, generics, maps, framework collections, date/time classes, arbitrary object values,
and inheritance require verification for the exact provider-consumer pair.

Consumer-side asynchronous syntax also does not change the provider contract automatically. For
example, a generated Node.js call can return `Promise<T>` even when the .NET provider method must
remain synchronous.

## Language-specific references

- [.NET](../language-guides/dotnet.md#supported-types)
- [Node.js and TypeScript](../language-guides/nodejs-typescript.md#supported-types)
- [Java and JVM](../language-guides/java-jvm.md#supported-types)
- [Python](../language-guides/python.md#supported-types)
- [PHP](../language-guides/php.md#supported-types)
- [Ruby](../language-guides/ruby.md#supported-types)

Perl has no equivalent generated-client/type-mapping path verified in this repository. See
[Language support status](../language-guides/support-status.md#perl).

## Supported surface is stricter than discovery

The package-generation engine rejects framework complex types in public interfaces. Its tests use `System.DateTime` as an example. Therefore, a type appearing in analyzer output does not prove that package generation will accept it.

Use simple primitives and explicitly modeled public types. Prefer ISO-8601 strings and string identifiers for cross-language contracts unless the exact producer/consumer pair has generation and runtime tests for richer types.

## Collections, generics, callbacks, and nullability

The implementation contains handlers for arrays, generics, delegates, nested types, and nullable metadata, but support varies by analyzer and target generator. Verify each intended language pair with generator tests or a generated-package smoke test.

## Evidence

Detailed mappings were verified against `SharedPrimitiveTypeHandler.cs`,
`primitive-type-converter.ts`, nullable generator tests, and package-generation unsupported-type
tests. The additional language baselines come from their dedicated generation engines and public
cross-runtime smoke suites. This is not a complete compatibility matrix.
