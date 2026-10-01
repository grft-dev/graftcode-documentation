---
title: "Type compatibility matrix"
description: "Portable baseline types, pair-specific types, types that require validation, and unsupported categories."
---

# Type compatibility matrix

Type support is a property of the whole **Receiver → Caller** path, not just the source type. Use the
groups below to design a contract, then generate and smoke-test the exact pair before depending on
richer types. The Graftcode Engine rejects framework types such as `DateTime`, `Guid`, and streams on
the public surface. User-defined classes and records, and a `T[]` of those models, are covered in the
groups below. Discovery of a type does not prove generation or runtime compatibility for every pair.

## Portable baseline

Expected to work across all currently supported runtime pairs. Prefer these for any cross-runtime
contract.

| Type | Notes |
| --- | --- |
| `string` | Also use for IDs and ISO-8601 timestamps. |
| `bool` / `boolean` | Supported. |
| 32-bit integer (`int`) | Within the safe range of the target's number type. |
| floating point (`double`) | Test precision-sensitive uses. |
| homogeneous arrays of portable values | Arrays of primitives and strings. For `T[]` of a class or record, see Pair-specific. |
| plain objects / models of supported values | Every public member must itself be portable. On .NET, a class or a record is a plain model when its members are. |

## Pair-specific

Supported for selected Receiver–Caller combinations. Confirm the exact pair.

| Type | Behavior | Recommendation |
| --- | --- | --- |
| arrays of complex types (`T[]` of a class or record) | Available for .NET, including a page DTO with `Items: T[]`. | Prefer `T[]` over `List<T>`. Validate any non-.NET pair before depending on it. |
| C# classes and records | Available for .NET as plain models. | Use either a class or a record. Keep every public member portable. |
| enums | Representation varies by pair. | Generate and smoke-test; a string or int is more portable. |
| nullable values | Handled by some pairs (for example a TS union with `null`). | Verify the pair; consider an explicit "empty" model. |
| nested models | Supported where every member is portable. | Keep nesting shallow and members simple. |

For a .NET Receiver called from a .NET Caller, prefer a typed graft method contract — primitives,
plain class or record models, and `T[]` — over JSON carried in a string.

## Requires validation

Behavior depends on precision, runtime library, or the generated package. Test before depending on
these.

| Type | Risk | Recommendation |
| --- | --- | --- |
| 64-bit integer (`long`) | Target number type may not represent every value. | Use `int` or a string for exact values. |
| `decimal` | No exact equivalent in some Callers. | Represent as a string for exactness. |
| `List<T>` of a complex type | Not the preferred shape for class or record elements. | Prefer `T[]` of the class or record. |
| maps / dictionaries / sets | Not a portable baseline. | Use explicit plain models or arrays. |
| inheritance / polymorphism | Constructor, dispatch, and serialization semantics vary. | Flatten to standalone facade types. |
| generics | Constraints, variance, and nesting are not universal. | Expose a concrete facade with closed types. |

## Unsupported (keep off the public surface)

| Type | Why | Instead |
| --- | --- | --- |
| framework date/time and ID types (`DateTime`, `Guid`, …) | Rejected / not portable. | ISO-8601 strings and string identifiers. |
| `Task` / `Task<T>` on a .NET public method | Rejected on the public surface. | Keep public methods synchronous; the generated Caller API may still be async. |
| streams, files, HTTP request/response objects | Not a transferable contract. | Keep internal; expose primitive/model results. |
| callbacks, delegates, events | No portable lifecycle across pairs/transports. | Redesign as explicit request/result calls. |
| remote object references as durable state | No durable lifetime guarantee. | Keep state behind explicit IDs. |

## Directional pairs to verify

Behavior can differ by direction. Confirm each pair your application uses with a generated-package
smoke test:

- **.NET Receiver → .NET Caller:** typed method contracts are available. Use a class or a record and
  `T[]` (including a page DTO with `Items: T[]`). Prefer that contract over JSON in a string, and
  prefer `T[]` over `List<T>` of a complex type. Keep framework `DateTime`, `Guid`, streams, and
  public `Task` / `Task<T>` off the surface.
- **.NET Receiver → Node Caller:** `long` and `decimal` are unsafe as JavaScript `number`; use `int`
  or strings. `Task<T>` is rejected on the .NET public surface; the generated Node call may still
  return a `Promise<T>`.
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
exact Receiver/Caller pair before depending on richer types. On .NET, a class and a record are both
plain models. For .NET-to-.NET calls, prefer the typed graft method contract over JSON in a string.

## Next steps

- [Type mapping](../core-concepts/type-mapping.md)
- [Expose code](../how-to-guides/expose-code-as-a-graftcode-receiver.md)
- [Errors and status](errors-and-status-reference.md)
- [Known limitations](known-limitations.md)
