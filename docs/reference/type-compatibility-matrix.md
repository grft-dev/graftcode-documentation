---
title: "Type compatibility matrix"
description: "Portable baseline types, pair-specific types, parsable framework types, and unsupported categories."
---

# Type compatibility matrix

Type support is a property of the whole **Receiver → Caller** path, not just the source type. Use the
groups below to design a contract, then install the generated Caller package and call the operations
you plan to use.

Graftcode validates the **public** methods and models you expose on the Receiver. **Non-parsable**
framework types (collection interfaces, streams, arbitrary BCL classes, and similar) cause Caller
package generation to fail with HTTP `422`. [Parsable framework types](#parsable-framework-types)
(such as `System.DateTime` and `System.Guid`) follow a separate mapping path. A type visible in
Gateway or Vision does not mean generation or cross-runtime calls will succeed. See
[Errors and status](errors-and-status-reference.md).

Nested plain models and arrays of portable values are the usual starting point for any supported
runtime pair. Maps, sets, and framework collection interfaces (`List<T>`, `Dictionary<,>`, …) are not
part of that baseline. A subset of **framework types** are
[parsable](#parsable-framework-types) and pass package generation with pair-specific mapping.

## Portable baseline

Expected to work across all currently supported runtime pairs. Prefer these for any cross-runtime
contract.

| Type | Notes |
| --- | --- |
| `string` | Also use for IDs and ISO-8601 timestamps. |
| `bool` / `boolean` | Supported. |
| 32-bit integer (`int`) | Within the safe range of the target's number type. |
| floating point (`double`) | Mind precision on precision-sensitive domains. |
| homogeneous arrays of supported values | Prefer language arrays over framework collection interfaces (for example `List<T>`, `Dictionary<,>` on .NET). Includes `byte[]` / `bytes` / `Uint8Array` as primitive byte buffers. |
| plain objects / models of supported values | Every public member must itself be portable. |

## Pair-specific

Supported for selected Receiver–Caller combinations with documented mapping rules.

| Type | Behavior | Recommendation |
| --- | --- | --- |
| enums | Representation varies by pair. | A string or int is more portable when you need one contract everywhere. |
| nullable values | Handled by some pairs (for example a TS union with `null`). | Consider an explicit "empty" model when nullability differs. |
| nested models | Supported where every member is portable. | Keep nesting shallow and members simple. |
| 64-bit integer (`long`) | Target number type may not represent every value (especially JavaScript Callers). | Use `int` or a string for exact values. |
| `decimal` | No exact equivalent in some Callers. | Represent as a string for exactness. |
| maps / dictionaries / sets | Not a portable baseline; behavior varies when exposed. | Use explicit plain models or arrays on the public surface. |
| inheritance / polymorphism | Not portable for arbitrary hierarchies on the graft surface. | Flatten to standalone facade types. |
| generics | Constraints, variance, and nesting are not universal. | Expose a concrete facade with closed types. |

## Parsable framework types

Graftcode maintains a **parsable types** catalog (shared protocol): framework types with a stable
wire/string representation. Package generation **does not** apply the opaque “framework complex type”
`422` rule to these names; the code generator maps them to idiomatic Caller types (for example
`System.DateTime` → `DateTimeImmutable` on PHP Callers).

Representative entries (see the protocol catalog for the full list):

| Semantic group | Examples on Receiver surfaces |
| --- | --- |
| Date/time instant | `System.DateTime`, `java.time.Instant`, `datetime.datetime` |
| Offset date/time | `System.DateTimeOffset`, `java.time.OffsetDateTime` |
| Time / duration | `System.TimeOnly`, `System.TimeSpan`, `java.time.Duration`, `datetime.timedelta` |
| UUID | `System.Guid`, `java.util.UUID`, `uuid.UUID` |
| URI | `System.Uri`, `java.net.URI` |

Types **not** in the catalog (for example many `DateOnly` scenarios or ad hoc framework classes) still
trigger `422` when they appear as opaque framework models. ISO-8601 **strings** remain the safest
default for calendar contracts across all pairs.

## Unsupported (keep off the public surface)

| Type | Why | Instead |
| --- | --- | --- |
| Non-parsable framework models (`System.Type`, arbitrary BCL classes, …) | Package generation fails (`422`). | Plain models built from primitives and parsable types. |
| framework collection interfaces (`List<T>`, `Dictionary<,>`, `IEnumerable<T>`, …) | Treated as non-portable framework generics in dependency analysis. | Language arrays (`T[]`, `string[]`, …) and explicit plain models. |
| `CancellationToken` and similar cancellation parameters | Not a portable public contract. | Caller-side timeouts; keep cancellation internal. |
| `Task` / `Promise` as **parameters** or live handles | Not transferred over the graft wire. | Pass completed values; use request/result methods. |
| streams, files, HTTP request/response objects | Not a transferable contract. | Keep internal; expose primitive/model results. |
| callbacks, delegates, events (as cross-runtime contracts) | Not established as portable graft contracts. | Prefer explicit request/result methods. |
| remote object references as durable state | No durable lifetime guarantee. | Keep state behind explicit IDs. |

`Task` / `Task<T>` / `async` on a .NET Receiver **return type** are handled per [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts), not as unsupported opaque framework types.

## Directional notes

Behavior can differ by direction. Use these rules when designing the public surface:

- **.NET Receiver → Node Caller:** `long` and `decimal` are unsafe as JavaScript `number`; use `int`
  or strings. Deferred/async shapes follow UGM completion metadata (`Promise<T>`, `executeAsync`, …)—see
  [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts).
- **Node Receiver → .NET Caller:** numeric width and nullability mapping follow the generated package;
  a JS `number` maps to a floating-point type unless modeled otherwise.
- **Java Receiver → Node Caller:** `long` handling follows JavaScript numeric limits; non-public methods
  are filtered from the surface.
- **Python Receiver → .NET Caller:** numeric precision follows generated mappings; expose only intended
  module-defined types.
- **PHP Receiver → Node Caller:** model shapes follow generation output; magic/non-public members are
  excluded from the surface.
- **Ruby Receiver → .NET Caller:** rely on discovered public methods; non-public methods are filtered.

For the safest cross-runtime contract, use primitives, strings, and plain models. Add parsable types
or pair-specific shapes only when the generated Caller API matches your needs.

## Next steps

- [Type mapping](../core-concepts/type-mapping.md)
- [Expose code](../how-to-guides/expose-code-as-a-graftcode-receiver.md)
- [Errors and status](errors-and-status-reference.md)
- [Known limitations](known-limitations.md)
