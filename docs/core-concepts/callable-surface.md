---
title: "Callable surface"
description: "How .NET and Node.js analyzers select declarations for the Unified Graft Model."
---

# Callable surface

The **callable surface** is the analyzer-selected set of declarations represented in the UGM. It is the input to package generation, not a promise that every target generator supports every represented type.

## .NET

The inspected .NET analyzer:

1. loads exported types from the selected assembly;
2. keeps visible top-level types, subject to a type filter;
3. records public declared instance and static methods, excluding special-name methods;
4. records public constructors, fields, properties, and nested types;
5. applies an optional method filter.

Method filters support comma-separated `*` and `?` patterns against bare or fully qualified method names. Tests verify empty, bare, wildcard, qualified, and combined type/method filters.

## Node.js and TypeScript

The inspected analyzer begins with package runtime exports. It handles direct exports, supported default and CommonJS forms, and re-exports. Type-only exports are skipped. It creates distinct UGM nodes for static and instance methods.

Because export analysis has many syntax paths, use analyzer output—not the source file alone—as the authoritative surface.

## A practical rule

Expose only declarations intended for consumers, then verify:

1. the analyzer includes the intended members;
2. package generation succeeds for the target ecosystem;
3. the generated package has the expected names and types;
4. a runtime smoke test reaches the intended implementation.

See [Public surface vs implementation](public-interface-vs-business-logic.md) and [Type mapping](type-mapping.md).
