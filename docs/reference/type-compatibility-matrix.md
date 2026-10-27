---
title: "Type compatibility matrix"
description: "Portable baseline types, pair-specific types, types that require validation, and unsupported categories."
---

# Type compatibility matrix

Type support is a property of the whole **Receiver → Caller** path, not just the source type. Use the
groups below to design a contract, then install the generated Caller package and test the calls you
plan to make before relying on richer types.

Graftcode validates the **public** methods and models you expose on the Receiver. Types that belong
to your language or framework (standard library dates, IDs, collection interfaces, streams, and similar)
are rejected when you request a Caller package—a type visible in Gateway or Vision does not mean
generation or cross-runtime calls will succeed. See [Errors and status](errors-and-status-reference.md).

Nested plain models and arrays of portable values are the usual starting point for any supported
runtime pair. Maps, sets, and framework collection interfaces (`List<T>`, `Dictionary<,>`, …) are not
part of that baseline. A subset of **framework types** are
[parsable](#parsable-framework-types) and can pass package generation with pair-specific mapping.

## Portable baseline

Expected to work across all currently supported runtime pairs. Prefer these for any cross-runtime
contract.

| Type | Notes |
| --- | --- |
| `string` | Also use for IDs and ISO-8601 timestamps. |
| `bool` / `boolean` | Supported. |
| 32-bit integer (`int`) | Within the safe range of the target's number type. |
| floating point (`double`) | Test precision-sensitive uses. |
| homogeneous arrays of supported values | Prefer language arrays over framework collection interfaces (for example `List<T>`, `Dictionary<,>` on .NET). Includes `byte[]` / `bytes` / `Uint8Array` as primitive byte buffers. |
| plain objects / models of supported values | Every public member must itself be portable. |

## Pair-specific

Supported for selected Receiver–Caller combinations. Confirm the exact pair.

| Type | Behavior | Recommendation |
| --- | --- | --- |
| enums | Representation varies by pair. | Generate and smoke-test; a string or int is more portable. |
| nullable values | Handled by some pairs (for example a TS union with `null`). | Verify the pair; consider an explicit "empty" model. |
| nested models | Supported where every member is portable. | Keep nesting shallow and members simple. |

## Requires validation

Behavior depends on precision, runtime library, or the generated package. Test before depending on
these.

| Type | Risk | Recommendation |
| --- | --- | --- |
| 64-bit integer (`long`) | Target number type may not represent every value. | Use `int` or a string for exact values. |
| `decimal` | No exact equivalent in some Callers. | Represent as a string for exactness. |
| maps / dictionaries / sets | Not a portable baseline. | Use explicit plain models or arrays. |
| inheritance / polymorphism | Constructor, dispatch, and serialization semantics vary. | Flatten to standalone facade types. |
| generics | Constraints, variance, and nesting are not universal. | Expose a concrete facade with closed types. |

## Parsable framework types

Graftcode maintains a **parsable types** catalog (shared protocol): framework types with a stable
wire/string representation. Package generation **does not** apply the opaque “framework complex type”
`422` rule to these names; the code generator maps them to idiomatic Caller types (for example
`System.DateTime` → `DateTimeImmutable` on PHP Callers).

Representative entries (not exhaustive—verify generation for your pair):

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
| callbacks, delegates, events | Preview | Lifecycle and errors differ by runtime and transport. | Prefer explicit request/result methods; use callbacks only after you validate your exact pair. |
| remote object references as durable state | No durable lifetime guarantee. | Keep state behind explicit IDs. |

`Task` / `Task<T>` / `async` on a .NET Receiver **return type** are handled per [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts), not as unsupported opaque framework types.

## Directional pairs to verify

Behavior can differ by direction. Confirm each pair your application uses with a generated-package
smoke test:

- **.NET Receiver → Node Caller:** `long` and `decimal` are unsafe as JavaScript `number`; use `int`
  or strings. Deferred/async shapes follow UGM completion metadata (`Promise<T>`, `executeAsync`, …)—see
  [Invocation lifecycle](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts).
- **Node Receiver → .NET Caller:** confirm numeric width and nullability mapping; a JS `number` maps to
  a floating-point type unless modeled otherwise.
- **Java Receiver → Node Caller:** confirm `long` handling (JavaScript cannot safely hold all 64-bit
  values) and that non-public methods were filtered from the surface.
- **Python Receiver → .NET Caller:** confirm numeric precision and that only intended module-defined
  types are exposed.
- **PHP Receiver → Node Caller:** confirm model shapes and that magic/non-public members are excluded.
- **Ruby Receiver → .NET Caller:** confirm that dynamically defined methods are not relied upon and
  that non-public methods were filtered.

For the safest cross-runtime contract, use primitives, strings, and plain models, and always test the
exact Receiver/Caller pair before depending on richer types.

## Next steps

- [Type mapping](../core-concepts/type-mapping.md)
- [Expose code](../how-to-guides/expose-code-as-a-graftcode-receiver.md)
- [Errors and status](errors-and-status-reference.md)
- [Known limitations](known-limitations.md)
