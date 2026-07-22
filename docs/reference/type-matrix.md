---
title: "Public contract type matrix"
description: "Portable public types, verified target mappings, and unsupported framework-type boundaries."
---

# Public contract type matrix

| Contract shape | .NET Receiver to generated packages | Node.js/TypeScript Receiver | Guidance |
| --- | --- | --- | --- |
| `string` | Portable baseline | Portable baseline | Use for IDs and ISO-8601 timestamps |
| `bool` / `boolean` | Portable baseline | Portable baseline | Supported |
| integer | `int` baseline | Maps to JavaScript `number` | Avoid values beyond safe target range |
| floating point | `double` baseline | `number` baseline | Test precision-sensitive uses |
| `decimal` | .NET baseline | No direct JS equivalent | Test exact caller pair |
| plain models | Simple members supported | Plain exported shapes supported | Every public member must be portable |
| homogeneous arrays | Verified baseline | Verified baseline | Prefer over framework collections |
| nullable values | Generator handlers exist | Union with `null` in TS output | Verify Receiver/Caller pair |
| async wrapper | .NET `Task`/`Task<T>` rejected on public surface | Receiver promises vary by path | Keep .NET Receiver methods synchronous |
| framework date/ID types | Rejected/unsupported | `Date` not portable baseline | Use strings |
| streams/files/HTTP objects | Unsupported public contract | Unsupported public contract | Keep internal |
| dictionaries/maps/sets | Not portable baseline | Not portable baseline | Use explicit plain models/arrays |
| callbacks/delegates | Not portable baseline | Not portable baseline | Redesign as explicit calls |
| inheritance/generics/enums | Not fully verified | Not fully verified | Generate and smoke-test |

The Graftcode Engine explicitly rejects complex framework types. Discovery does not prove
generation or runtime compatibility.

## Directional caveats (Receiver to Caller)

Type behavior depends on the **Receiver → Caller** pair, not just the source type. Verify these with a
generated-package smoke test:

- **.NET `long` / 64-bit integer → JavaScript/TypeScript Caller:** JavaScript `number` cannot safely
  represent every 64-bit value. Use `int` or a decimal string unless the exact pair is tested.
- **.NET `decimal` → JavaScript/TypeScript Caller:** no direct equivalent; represent as a string for
  exactness.
- **Framework date/time or ID types (any Receiver → any Caller):** not portable; use ISO-8601 strings
  and string identifiers.
- **`Task`/`Task<T>` on a .NET Receiver's public method:** rejected; keep public methods synchronous.
  The generated Caller API may still be asynchronous (see
  [Async, cancellation, and timeouts](../core-concepts/invocation-lifecycle.md#async-cancellation-and-timeouts)).
- **Nullable, enums, inheritance, generics:** behavior varies by pair; generate and smoke-test.

For the safest cross-runtime contract, use primitives, strings, and plain models, and always test the
exact Receiver/Caller pair before depending on richer types.

## Next steps

- [Expose code](../how-to-guides/expose-code.md)
- [Errors and status](errors-status.md)
- [Known limitations](known-limitations.md)
