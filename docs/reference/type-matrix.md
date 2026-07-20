---
title: "Public contract type matrix"
description: "Portable public types, verified target mappings, and unsupported framework-type boundaries."
---

# Public contract type matrix

| Contract shape | .NET provider to generated packages | Node.js/TypeScript provider | Guidance |
| --- | --- | --- | --- |
| `string` | Portable baseline | Portable baseline | Use for IDs and ISO-8601 timestamps |
| `bool` / `boolean` | Portable baseline | Portable baseline | Supported |
| integer | `int` baseline | Maps to JavaScript `number` | Avoid values beyond safe target range |
| floating point | `double` baseline | `number` baseline | Test precision-sensitive uses |
| `decimal` | .NET baseline | No direct JS equivalent | Test exact caller pair |
| plain models | Simple members supported | Plain exported shapes supported | Every public member must be portable |
| homogeneous arrays | Verified baseline | Verified baseline | Prefer over framework collections |
| nullable values | Generator handlers exist | Union with `null` in TS output | Verify producer/consumer pair |
| async wrapper | .NET `Task`/`Task<T>` rejected on public surface | Provider promises vary by path | Keep .NET provider methods synchronous |
| framework date/ID types | Rejected/unsupported | `Date` not portable baseline | Use strings |
| streams/files/HTTP objects | Unsupported public contract | Unsupported public contract | Keep internal |
| dictionaries/maps/sets | Not portable baseline | Not portable baseline | Use explicit plain models/arrays |
| callbacks/delegates | Not portable baseline | Not portable baseline | Redesign as explicit calls |
| inheritance/generics/enums | Incomplete evidence | Incomplete evidence | Generate and smoke-test |

The package-generation engine explicitly rejects complex framework types. Discovery does not prove
generation or runtime compatibility.

Generated target mappings include numeric collapsing in TypeScript and narrower primitive mapping in
.NET; therefore support belongs to the complete producer-analyzer-generator-consumer path.

## Next steps

- [Expose code](../how-to-guides/expose-code.md)
- [Errors and status](errors-status.md)
- [Known limitations](known-limitations.md)
