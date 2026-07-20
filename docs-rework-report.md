# Graftcode documentation rework report

## Summary

The documentation on `feature/rework-documentation` now starts with a verified cross-runtime call
instead of product positioning. It separates tutorials, concepts, task guides, language guides,
operations, reference, and troubleshooting. Existing URLs remain available as rewritten
compatibility pages because the documentation repository cannot configure portal redirects.

The rewritten corpus contains 97 Markdown pages, seven focused SVG diagrams, a complete
.NET-to-Node.js sample, a page-by-page audit, a visual-source audit, and repository-local validation.

## Problems addressed

- Replaced abstract and repetitive introductions with a concrete provider, Gateway, generated Graft,
  consumer, and result.
- Distinguished developer-written code, generated packages, package-time work, and runtime work.
- Explained that remote syntax can look local while latency, serialization, networking, partial
  failure, security, compatibility, and observability still apply.
- Consolidated terminology in one glossary and linked other pages to the canonical definitions.
- Split generic concepts from runtime-specific syntax and limitations.
- Replaced broad performance, security, privacy, compatibility, and production claims with scoped
  implementation evidence or explicit gaps.
- Preserved technically useful old routes while moving their main content to task-oriented pages.
- Replaced large presentation blueprints with seven single-purpose technical diagrams.

## New information architecture

1. Start here
2. Tutorials
3. Core concepts
4. How-to guides
5. Language guides
6. Operations
7. Reference
8. Troubleshooting

The human and machine-readable navigation are both maintained in `docs/README.md`.

## Principal files created

- `docs-rework-audit.md`
- `docs-visual-assets-audit.md`
- `scripts/validate-docs.py`
- `docs/tutorials/dotnet-to-nodejs.md`
- `docs/tutorials/dotnet-to-nodejs/provider/*`
- `docs/tutorials/dotnet-to-nodejs/consumer/*`
- `docs/core-concepts/index.md`
- `docs/core-concepts/glossary.md`
- `docs/core-concepts/callable-surface.md`
- `docs/core-concepts/invocation-lifecycle.md`
- `docs/core-concepts/execution-modes.md`
- `docs/core-concepts/static-and-instance-context.md`
- `docs/core-concepts/package-generation.md`
- `docs/core-concepts/configuration-resolution.md`
- `docs/core-concepts/type-mapping.md`
- `docs/core-concepts/contract-evolution.md`
- `docs/how-to-guides/*`
- `docs/language-guides/*`
- `docs/operations/*`
- `docs/reference/gateway-cli.md`
- `docs/reference/configuration-keys-precedence.md`
- `docs/reference/environment-variables.md`
- `docs/reference/supported-runtimes-package-managers.md`
- `docs/reference/type-matrix.md`
- `docs/reference/errors-status.md`
- `docs/reference/generated-package-structure.md`
- `docs/reference/ports-protocols.md`
- `docs/reference/known-limitations.md`
- `docs/troubleshooting/*`
- `assets/diagrams/*`

## Compatibility handling

No page was deleted. Existing introduction, architecture, integration, security, performance,
use-case, and `how-graftcode-works` paths were retained and reduced to evidence-bounded pages or
compatibility routes with links to canonical content.

The selected docs-only scope did not permit changes to the Next.js redirect configuration. True HTTP
redirects, canonical URL headers, and portal search-index migration require a separate portal change.

## Verified technical assumptions

- Gateway loads provider modules, analyzes their callable surface, uploads a Unified Graft Model, and
  prints package-manager installation instructions after successful publication.
- The free registry identifier is generated at runtime and can change when Gateway restarts.
- The canonical tutorial's live Gateway 1.3.6 run generated the npm package
  `@graft/nuget-billingservice`.
- The generated Node method was `BillingService.calculateMonthlyBill`; the .NET provider method was
  `BillingService.CalculateMonthlyBill`.
- A live remote call returned `Monthly bill: 50`.
- Generated configuration defaults to in-memory execution; remote consumers must configure the host
  before the first generated invocation.
- Configuration resolution has six inspected priority levels.
- Framework complex types rejected by package generation map to HTTP 422 in the inspected error
  protocol.
- Gateway source defines WebSocket, HTTP, optional TCP, and optional HTTP/2 surfaces. Transport
  availability still depends on startup flags and the runtime package.
- .NET, Node.js, Java/JVM, Python, PHP, and Ruby have repository evidence for provider and/or consumer
  paths. Each language guide scopes direction and confidence separately.
- Perl appears in runtime-hosting code, but the embedded analyzer does not establish an equivalent
  Graft publication path.

## Unresolved documentation gaps

The following topics need engineering or product confirmation before stronger claims are published:

- a release-versioned provider/consumer/type matrix for every runtime;
- Vision's supported feature set and canonical public port;
- cross-runtime authentication plugin packaging and support policy;
- Graftcode Context APIs and concurrency semantics by runtime;
- package retention, compatibility, and old-Graft/new-provider behavior;
- universal timeout, retry, circuit-breaker, and failover behavior;
- supported operating-system, CPU architecture, proxy, ingress, and load-balancer combinations;
- field-level cloud data handling, retention, telemetry, and privacy behavior;
- reproducible performance and cost benchmark methodology;
- health-check contract and production deployment recipes;
- support status for enterprise self-hosting and event-driven transports.

Recommended reviewers:

- Gateway owners: CLI, ports, Vision, lifecycle, runtime hosting, and deployment.
- Module analyzer and code-generator owners: callable surface, names, generated APIs, and type mapping.
- Package-generation and registry owners: package naming, versioning, retention, and installation.
- Hypertube owners: configuration, transport behavior, context, errors, retries, and telemetry.
- Security owners: authentication, authorization, TLS termination, cloud data, and threat boundaries.
- Runtime maintainers: every language guide and support-direction statement.

## Validation results

Passed:

```text
python scripts/validate-docs.py
Validated 97 Markdown files.
0 error(s), 0 warning(s).
```

The validator checks frontmatter, navigation/file parity, internal links and assets, duplicate titles,
forbidden marketing phrases, and fenced-code metadata.

Also passed:

- `git diff --check`
- XML parsing for all seven files in `assets/diagrams`
- IDE lint diagnostics for the documentation repository
- `dotnet build -c Release` for the tutorial provider: zero warnings and zero errors
- `node --check index.js` for the tutorial consumer
- live Docker-hosted Gateway 1.3.6 module discovery and publication
- live npm Graft installation from the emitted registry command
- live remote Node.js-to-.NET call returning `Monthly bill: 50`
- `npm run lint:docs`
- `npm run type-check:docs`
- `npm run build:docs`

Portal build caveat: the portal build loaded its existing `main` cache with 39 sections, fetched on
2026-06-02. It proves that the current renderer builds, but it does not prove that every page on this
unpublished feature branch renders correctly. Rendering the branch through the portal requires either
publishing the branch for the fetch pipeline or adding local-content support to the portal, which was
outside the selected docs-only scope.

Not completed:

- live validation of every external URL;
- automated desktop and mobile screenshot comparison for the feature-branch content;
- exhaustive execution of every language snippet;
- compatibility testing across Gateway and Graft versions.

These are recorded as follow-up work rather than reported as passing.

## Recommended follow-up work

1. Have the listed engineering owners review the pages in their area.
2. Publish the feature branch to a test documentation source and run the portal against that branch.
3. Add the repository validator to CI.
4. Add a link checker with an allowlist for authenticated and dynamic registry URLs.
5. Add executable sample projects for each language direction represented in the support matrix.
6. Add portal redirects and canonical URLs after the new structure is approved.
7. Add screenshot-based desktop and mobile checks for diagrams, tables, and code blocks.
