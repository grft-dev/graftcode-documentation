---
title: "Language Guide Template"
description: "Required structure and evidence rules for Graftcode language guides."
---

# `<Language / runtime>`

> Copy this file for a new runtime. Replace every placeholder and delete authoring notes. Never turn
> an unverified assumption into an example.

## Support status and direction

State provider support, consumer support, maturity, and the evidence used. Separate Gateway hosting
from module analysis, package generation, publication, installation, and invocation.

## Prerequisites

List the minimum runtime, build tools, Gateway, and platform constraints supported by evidence.

## Provider support

Describe the artifact/module passed to `gg`, the public discovery boundary, build command, and exact
Gateway invocation. If flags or module paths vary, tell the reader how to obtain them.

## Consumer support

Name the generated package ecosystem and whether calls are synchronous or asynchronous. State that
generated names and signatures are authoritative.

## Package manager

Name the package manager and registry mechanism. Do not put a real-looking placeholder identifier in
a copyable command.

## Minimal provider example

Use the smallest portable public contract. Keep framework, transport, stream, database, and runtime
context types out of the public interface.

## Minimal consumer example

Use only generated APIs verified in generator source or tests. Put placeholders in angle brackets.
If exact imports or calls cannot be verified, say so and link the implementation source instead of
inventing syntax.

## Installation

1. Run Gateway and wait for successful module discovery/publication.
2. Open Vision or the package-manager route emitted by that running Gateway.
3. Select this consumer runtime.
4. Copy and execute the complete emitted command unchanged.
5. Record the generated import/namespace snippet.

Explain that dynamic registry IDs, package names, versions, repository paths, and project IDs must
never be guessed.

## Configuration

Document the exact generated `GraftConfig` API, its default in-memory behavior, remote host format,
and stateless mode. Mark optional headers/config APIs only when verified.

## Supported types

Separate:

- a test-backed portable baseline;
- types explicitly rejected;
- types that merely lack evidence.

Prefer primitives, strings, plain data objects, and homogeneous arrays/lists. Treat dates, maps,
unions, optional values, framework types, streams, callbacks, and runtime handles as unsupported
until verified.

## Runtime-specific limitations

Include naming, async, packaging, browser, native-binary, stateful-object, and version constraints.

## Troubleshooting

Give symptom-to-cause-to-fix entries that are specific to this runtime.

## Verified samples and tests

Link public Quick Starts and samples. Cite inspected test and implementation paths. Clearly label
private or local-only evidence that readers may not be able to open.

## Known gaps

List every requested area that could not be verified. Prefer an explicit gap over plausible syntax.
