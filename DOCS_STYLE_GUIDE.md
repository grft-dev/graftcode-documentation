# Graftcode documentation style guide

Internal, non-published guidance for contributors. This file lives at the repository root, outside
`docs/`, so it is never rendered on the public site. It defines canonical terminology and the writing
rules the external documentation must follow.

## Audience and tone

- The docs are for external developers evaluating or using Graftcode.
- Write like an experienced engineer for other engineers: concrete nouns, observable behavior,
  explicit constraints, short paragraphs, task-oriented headings.
- Do not read like an internal implementation audit.

## Canonical terminology

Use these terms consistently. After the first mention on a page, the short form in parentheses is
acceptable.

| Term | Meaning | Notes |
| --- | --- | --- |
| **Graftcode** | The product/platform as a whole | Not the name of every component |
| **Caller** | The app, service, frontend, AI client, or module that initiates a call through a Graft | Primary runtime-role term |
| **Receiver** | The app/service/module whose business logic is hosted through Gateway and receives the call | Primary runtime-role term |
| **Graft** | The generated, strongly typed package the Caller installs | "install/import/call through a Graft" |
| **Graftcode Gateway** (Gateway) | Runtime component deployed with the Receiver; hosts the runtime, exposes the callable surface, accepts Graft invocations, routes to Receiver code | Executable is `gg` / `gg.exe` |
| **Graftcode Engine** (Engine) | Setup/control-plane component that creates a Graft from public interface metadata | Unified external term; do not expose internal services behind it; not in the runtime data path |
| **Hypertube** | The runtime communication bridge between the Graft and Gateway | Describe via transport/execution behavior only |
| **Graftcode Vision** (Vision) | Developer UI for inspecting the callable surface and getting install/usage info | Document only current capabilities |
| **Public interface** | Types, methods, signatures, and metadata a Graft is created from | |
| **Callable surface** | The subset of public types/methods intentionally exposed by Gateway | Use for security, filtering, exposure, contract design |
| **Registry** | The package repository the Caller installs a Graft from | |
| **Project Key** | Credential associating Gateway with a project/Engine context | Not runtime-call authorization |
| **Runtime host** | The destination a Graft uses to reach Gateway during invocation | The `GraftConfig` host value; never the registry URL |
| **Invocation credentials** | Credentials/context authorizing an individual runtime call | Distinct from Project Key, registry, TLS |

Keep **Project Key**, **registry URL**, **runtime host**, and **invocation credentials** as four
separate concepts. See `docs/reference/identifiers-and-auth.md` for the canonical diagram and table.

## Role terms: Caller / Receiver

- Use **Caller** and **Receiver** as the primary role terms.
- Do not alternate randomly among provider, backend, server, target, hosted service, receiver.
- "Backend" is acceptable only in genuine frontend-to-backend scenario wording; the architectural
  role is still **Receiver**.
- When renaming prose: `provider` (role) -> `Receiver`; `consumer` (role) -> `Caller`.

## Setup vs runtime

Always keep these two flows visually and textually separate:

- **Setup / control plane:** Receiver exposes a callable surface; the Graftcode Engine uses the public
  interface metadata to create and publish a Graft; the Caller installs it.
- **Runtime / data plane:** Caller invokes through the Graft; Hypertube reaches Gateway over the
  selected execution mode/transport; Gateway validates the target is on the callable surface; Receiver
  executes; result/error returns. The Engine is not in this path.

## Preserve literal public identifiers

Do not rename literal identifiers developers must type, even if they contain historical acronyms:

- CLI flags (for example `--GMA`, `--projectKey`), executable names (`gg`),
- environment variables (for example `GSMU_ENDPOINT`, `GC_PROJECT_KEY`),
- package names, configuration keys, protocol values, public API members.

Use canonical Graftcode terminology in the surrounding prose, but keep the exact identifier in code
blocks and reference tables.

## Do not publish internal-facing language

Never include in published pages:

- internal service names, repository names, file paths, class/namespace names, test names,
- "verified in the repository", "confirmed by implementation", "we inspected the source", "evidence
  shows", or similar,
- historical implementation archaeology or descriptions of how internal services are organized.

Replace internal explanations with observable product behavior.

## Capability status labels

Use these consistently and keep them easy to find (Start here > Current status and limitations, plus
Reference):

- **Available** — reachable through a public product path and behaves as documented.
- **Alpha** / **Preview** — exists but incomplete or unstable.
- **Planned** — only partial foundations exist.
- **Unsupported** — not available.

Never turn uncertainty into a confident claim.

## Claims to avoid

Avoid unqualified: "exactly like local", "identical semantics", "zero boilerplate", "no serialization",
"any language/transport/type", "always up to date", "no version drift", "automatically secure",
"10x/20x/70%" without a documented, reproducible benchmark. Prefer scoped, precise wording (see the
external product explanation in `docs/introduction/what-is-graftcode.md`).

## Information architecture

Top-level sections: Start here, Core concepts, How-to guides, Operations, Reference, Troubleshooting.
There is no Language Guides section and no Tutorials section. Runtime-specific instructions live in
language tabs within How-to articles and in the Reference matrices.
