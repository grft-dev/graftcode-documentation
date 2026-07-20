# Graftcode visual assets audit

## Scope

This audit covers the five supplied blueprint PNGs under `C:\Users\PiotrChrzan\.cursor\projects\d-GRAFTCODE\assets`. The originals were inspected in place and were not copied, cropped, edited, or moved. The untracked `assets/infographics/` directory in the documentation repository was not touched.

The blueprints are presentation source material, not implementation evidence. Technical checks use the same implementation/test sources listed in `docs-rework-audit.md`.

## Decision summary

- Reuse as-is: **0**
- Crop for publication: **0**
- Split and redraw: **2** (`Graftcode_intro`, `Observability_and_configuration`)
- Discard the composite and redraw its useful concepts: **3** (`How_it_works`, `Code_deep_dive`, `Security`)

All five are 1024×724 presentation composites. At normal documentation width, most labels are too small to read. None is suitable as an accessible documentation image.

## Inventory

| Source file | Concept | Useful labels / flow | Claims shown or implied | Technically verified | Confidentiality / readability | Duplicate or conflict assessment | Recommended use | Required changes | Target documentation page |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `c__Users_PiotrChrzan_AppData_Roaming_Cursor_User_workspaceStorage_889ed09980123d25f6b5bf73b5ac8413_images_Graftcode_intro-29ff9438-43c9-4ec9-9701-0fe4301fe349.png` | Product overview: what Graftcode is, compatibility, five integration scenarios, and use cases. | “What is Graftcode”; “Compatibility”; programming languages, infrastructure, package ecosystems, operating systems; frontend-to-backend; backend-to-backend; backend-to-AI; public API integration; polyglot in-memory runtime; short- and long-term use cases. | Graftcode calls code across process/machine/language boundaries “as if” local; works with “any technology”; broad ecosystem/logo support; reduces integration complexity. | **Partial.** Gateway, analyzers, generators, and Hypertube support several runtimes and package paths. The repository does not establish universal or symmetric support, and current public-surface restrictions contradict “any technology.” | No credentials or personal data are visible. Vendor/logo grids can be mistaken for certified support. Most body text is unreadable at page width. Branding is reusable only as style inspiration, not as evidence. | Duplicates `what-is-graftcode`, `where-graftcode-fits`, integration-pattern, and use-case prose. Conflicts with Alpha type/runtime constraints and the lack of a release-qualified compatibility matrix. | **Split and redraw; do not crop.** | Create one small “provider → generated Graft → consumer → Gateway” overview and one text-based support matrix. Remove slogans, logo walls, infrastructure logos, and unsupported use cases. Label generated vs user-written components and runtime boundaries. | Rewritten landing page; “Supported runtimes and package managers”; “Choose an integration scenario.” |
| `c__Users_PiotrChrzan_AppData_Roaming_Cursor_User_workspaceStorage_889ed09980123d25f6b5bf73b5ac8413_images_How_it_works_-_more_technial-a5ccd143-f1dc-43b8-87f5-c49a4c75c1cb.png` | Composite architecture: caller/receiver execution, Hypertube, transport abstraction/selection, cloud Engine, and customer infrastructure. | Caller; receiver; Graft; Gateway; Hypertube; “transport agnostic execution”; “transport abstraction layer”; “transport selection matrix”; “what stays in your environment”; “what goes to Graftcode Engine”; “your infrastructure, your rules.” | Engine/cloud placement appears adjacent to the runtime path; arbitrary transport selection; clear separation of metadata and code/data; customer-controlled execution. | **Partial.** Direct in-memory/TCP/WebSocket configuration and Gateway-hosted execution are tested. UGM upload/publish paths exist. A general transport matrix, all cloud-data exclusions, and universal plugin semantics are not verified. | No obvious secrets. Dense lower panels are unreadable. The Engine placement is architecturally ambiguous and can incorrectly imply a production relay. | Conflicts with current docs that say the cloud is not in the runtime path. Overlaps three separate concepts: package generation, runtime invocation, and deployment/network ownership. | **Discard composite; redraw as separate Mermaid diagrams.** | Produce (1) package/discovery flow and (2) runtime sequence. Put Graftcode cloud in a separate trust boundary connected only by dashed metadata/package arrows. Use solid runtime-data arrows. Show in-memory, WebSocket, and TCP only where verified; put plugins in a separately scoped extension diagram. | “How Grafts are generated”; “Runtime invocation lifecycle”; “What data leaves your environment.” |
| `c__Users_PiotrChrzan_AppData_Roaming_Cursor_User_workspaceStorage_889ed09980123d25f6b5bf73b5ac8413_images_Code_deep_dive-39dc2145-51b2-4ed6-867e-b49c226f05a4.png` | Composite technical deep dive: client/server code, state model, REST/Graftcode topology, workflow, and CPU/memory/network charts. | Client side; server side; state management model; “REST & Graftcode”; workflow; average CPU usage; average memory usage; average network bytes. | Graftcode uses less CPU, memory, and network; simpler workflow; stateful and stateless behavior; architecture comparison. | **Low.** Public/static/instance analysis and runtime calls have source evidence, but the code cannot be audited from the bitmap. No checked-in raw data or complete methodology was found for the plotted benchmark values. | The code is unreadable and non-copyable. If enlarged, it may contain obsolete package names, hosts, or internal identifiers; it must be transcribed from verified source rather than cropped. No clearly readable secret was found. Charts lack legible units, versions, environment, sample size, percentiles, and source. | Duplicates all six performance pages and several runtime pages. Conflicts with claims that there is no serialization/protocol processing. The same comparison is presented elsewhere without reproducible data. | **Discard image and all embedded charts.** | Replace code panels with tested, syntax-highlighted source files. Replace workflow with a small sequence diagram. Publish performance visuals only from a versioned benchmark artifact with raw data and methodology; otherwise omit them. | Canonical quickstart; “Public callable surface”; “Runtime invocation lifecycle”; future benchmark report only. |
| `c__Users_PiotrChrzan_AppData_Roaming_Cursor_User_workspaceStorage_889ed09980123d25f6b5bf73b5ac8413_images_Observability_and_configuration-74dcab50-cc2c-4ca3-959e-c6fdd13df71f.png` | Four implementation-oriented topics: multiple Grafts, trace propagation, configuration precedence, exposed-type filtering, and an end-to-end trace timeline. | “Multiple grafts one application”; caller service; Graft client; Gateway receiver; OpenTelemetry/collector; `GraftConfig` precedence; filtering exposed types; end-to-end traceability. | Multiple independent Graft targets; automatic trace propagation; seven-level precedence; exposure filtering; complete trace continuity. | **Mixed.** Type filtering is tested in .NET and Node. W3C `traceparent` behavior is tested in .NET and Node. The precedence panel is **incorrect**: current .NET enum has six levels, not seven, and no `GraftSpecificDefault`. Universal all-runtime trace continuity is unverified. | No sensitive trace IDs, tenant data, or credentials are visible. Small text and timelines are unreadable. A production trace screenshot would require sanitization, but this appears synthetic. | The precedence panel conflicts directly with `ConfigPriority.cs`. The filtering panel conflicts with the Alpha page, which calls `--types` roadmap-only even though it is implemented/tested. Trace claims need runtime scope. | **Split and redraw; do not reuse bitmap.** | Create separate diagrams for configuration resolution, type filtering, and trace propagation. Generate priority names/order from source. Add .NET/Node scope to telemetry. Keep the trace waterfall optional and synthetic; include accessible text equivalents. | “Configuration resolution”; “Filter exposed types”; “OpenTelemetry and trace context.” |
| `c__Users_PiotrChrzan_AppData_Roaming_Cursor_User_workspaceStorage_889ed09980123d25f6b5bf73b5ac8413_images_Security-c78d572d-9508-4140-b8e3-815c2fe42663.png` | Security poster: encrypted communication, a four-layer security core, auth headers, registry trust, execution control, and runtime call validation. | “Communication”; “full end-to-end encryption”; TLS/WSS; auth headers; registry trust; execution control; caller app; receiver; execution; registry; JWT/API-key/OAuth-style icons. | Full end-to-end encryption; every call is authenticated/validated; registry controls what can be installed; execution control prevents unauthorized execution. | **Partial to contradicted.** A .NET JWT plugin and failures are tested, but authentication is optional and packaging/support status is unknown. Registry/project-key behavior exists for metadata/package publishing, not runtime authorization. Native Gateway TLS configuration was not established; TLS may terminate externally. | No credentials are visible. Security icons imply guarantees that the implementation does not enforce by default. The bitmap is too small for threat-boundary review. | Conflicts with “no plugin means no authentication,” with the Alpha page’s plugin status, and with transport docs that permit TLS termination before Gateway. Conflates package trust, transport encryption, identity, authorization, and execution. | **Discard composite; redraw only after security-owner review.** | Replace with (1) trust-boundary/data-flow diagram, (2) optional authentication sequence with dashed plugin steps, and (3) responsibility matrix for transport, identity, authorization, registry access, and business-method checks. Replace “end-to-end encryption” with deployment-specific transport wording. | “Security model and shared responsibility”; “Authentication and authorization”; “TLS/WSS deployment”; “What data leaves your environment.” |

## Extracted concepts worth preserving

| Concept | Preserve | Do not preserve |
| --- | --- | --- |
| One provider-to-consumer picture | Provider code, analyzed public surface, generated package, consumer call, Gateway execution, and response/error. | “Any technology,” “boundaries disappear,” or a logo wall. |
| Development-time vs runtime | Separate metadata/package generation from direct runtime invocation. | Engine/cloud drawn above or inline with the production channel. |
| Generated vs developer-written | Provider implementation and consumer application are developer-written; Graft and model/package artifacts are generated; Gateway/Hypertube are runtime infrastructure. | A single undifferentiated flow that makes generated code look like business logic. |
| Configuration resolution | Source precedence and one resolved target per Graft. | The obsolete seven-level list or “last configured always wins.” |
| Trace propagation | `traceparent` crossing tested .NET/Node invocation boundaries and integration with an existing observability stack. | “No broken traces” across all runtimes or automatic backend export with no setup. |
| Public-surface filtering | Type/method filters and resulting exposed model. | Treating every public member as automatically supported or the filter as merely planned. |
| Security boundaries | Customer runtime, metadata/package services, transport termination, optional identity hooks, and user authorization. | “Full end-to-end encryption,” “every call validated,” or registry trust as runtime authorization. |
| REST comparison | Equivalent responsibilities and distributed failure boundaries. | A winner/loser graphic or unqualified latency/resource claims. |

## Duplicate and conflict assessment

1. **The five posters are not five independent assets.** They repeat the same caller/Graft/Gateway/Hypertube path with different labels and maturity assumptions.
2. **`Graftcode_intro` and `How_it_works` overlap on architecture.** Replace both architecture sections with one canonical component vocabulary and two lifecycle diagrams.
3. **`How_it_works` and `Security` disagree on the cloud/runtime boundary.** The runtime diagram must keep metadata/package services out of the production invocation path unless implementation evidence proves otherwise.
4. **`Observability_and_configuration` conflicts with implementation on precedence.** Current .NET code has six priority levels: `RuntimeSpecificEnv`, `GlobalEnv`, `RuntimeSpecificFile`, `GlobalFile`, `User`, and `DefaultLibrary`.
5. **`Observability_and_configuration` conflicts with the Alpha page on filtering maturity.** Gateway lists `--types`, and .NET/Node tests cover filtering.
6. **`Security` conflicts with both security prose and implementation maturity.** Authentication is not automatic; a .NET JWT plugin exists in source/tests, while release and cross-runtime support remain unknown.
7. **`Code_deep_dive` duplicates the entire performance section.** No chart should survive unless its exact dataset and methodology are versioned and reproducible.
8. **No bitmap fragment is uniquely valuable enough to crop.** Reusing fragments would preserve unreadable typography, obsolete labels, and ambiguous arrows while losing editability and accessibility.

## Confidentiality assessment

| Asset | Assessment | Publication rule |
| --- | --- | --- |
| `Graftcode_intro` | No obvious personal data, credentials, tenant IDs, internal URLs, or environment identifiers. Vendor logos may create unsupported endorsement/support implications. | Do not publish the bitmap; use maintained text for compatibility. |
| `How_it_works` | No obvious secrets. Some lower-panel labels are too small to inspect reliably. | Do not publish; rebuild from reviewed component/data-flow inventory. |
| `Code_deep_dive` | No readable credential was found, but embedded code is too small for a reliable secret/internal-identifier review. | Never crop code from it. Recreate examples from reviewed repository source. |
| `Observability_and_configuration` | Appears synthetic; no real trace IDs or customer data are readable. | Use synthetic trace values only; never substitute a production trace without sanitization. |
| `Security` | No credentials or customer identifiers. Risk is misleading assurance, not visible secret leakage. | Publish only a security-reviewed replacement with explicit defaults and optional controls. |

## Canonical visual system

### Formats

1. Use Mermaid for sequences, lifecycle flows, configuration resolution, and simple topology comparisons.
2. Use documentation-native SVG only for trust boundaries, generated-vs-written distinctions, or trace waterfalls that Mermaid cannot express clearly.
3. Do not use code screenshots. Use tested source blocks with file names and expected output.
4. Do not use benchmark charts without checked-in data and reproduction instructions.

### Semantics

- Solid arrow: runtime invocation/result data.
- Dashed arrow: metadata, package generation, configuration, or installation.
- Dotted arrow: optional/preview integration.
- Boundary boxes: `Consumer environment`, `Provider environment`, `Graftcode metadata/package services`, and `Third-party infrastructure`.
- Component shape must be stable across pages:
  - rounded rectangle: developer-owned application/module;
  - package shape: generated Graft;
  - process box: Gateway/runtime;
  - cloud box: metadata/package service only;
  - cylinder: registry/storage.
- Every diagram must label `developer-written`, `generated`, or `runtime infrastructure` where relevant.
- Color cannot carry meaning alone. Arrow style, labels, and a legend must remain sufficient in grayscale.

### Accessibility and maintenance

- One primary question per diagram.
- No more than seven primary nodes in an overview.
- Minimum 14 px rendered label size at normal desktop width.
- Mobile-safe vertical fallback or a text sequence immediately below the visual.
- Useful alt text that states the conclusion, not “architecture diagram.”
- A one-sentence takeaway, runtime/release scope, and source/test links beside each diagram.
- Keep editable Mermaid/SVG source in the documentation repository; do not use exported presentation screenshots as source.

## Minimum replacement diagram set

| Diagram | Format | Required content | Evidence gate |
| --- | --- | --- | --- |
| Graftcode in one picture | SVG or small Mermaid flowchart | Provider public method → analyzed callable surface → generated Graft package → consumer installation/call → Gateway/provider execution. Distinguish generation from runtime. | MA, package generation, GG, and one E2E sample. |
| Package generation and installation | Mermaid flowchart | Compiled module → analyzer/UGM → metadata/package service → ecosystem-specific generated package → package manager → consumer. | SMU and package-generation/package-manager tests; install command copied from real Gateway output. |
| Runtime invocation lifecycle | Mermaid sequence | Consumer → generated Graft → resolved configuration → Hypertube transport → Gateway/runtime → provider method → result/error. Cloud absent from runtime path unless evidence changes. | HT configuration/runtime tests and one remote E2E test. |
| Local vs remote execution | Mermaid comparison | Same consumer API; local module prerequisite; remote Gateway/transport; changed latency/failure/operations. | Generated package defaults plus local and remote integration tests. |
| Configuration resolution | Mermaid flowchart | Six current priority levels and first-wins behavior at equal priority; per-runtime parity notes. | `ConfigPriority.cs` and resolver tests. |
| Public surface and filters | Mermaid flowchart | Public/exported candidates → type filter → method filter → supported-type validation → UGM. | .NET/Node analyzer filter tests and validation behavior. |
| Trace propagation | Mermaid sequence | Existing parent span → Graft invocation → `traceparent` → receiver span → application telemetry export. Scope to .NET/Node until expanded. | HT telemetry unit tests and OpenTelemetry demo. |
| Security and trust boundaries | Reviewed SVG | Customer environments, metadata/package service, runtime data path, transport termination point, optional auth hooks, and owner responsibilities. | Security review, cloud data inventory, TLS deployment recipe, auth support statement. |
| REST and Graftcode responsibilities | Mermaid side-by-side flow | Show equivalent consumer, network, provider, errors, security, observability, and partial-failure responsibilities without performance ranking. | Architecture review; no benchmark claims. |

## Asset-by-asset final decision

| Asset prefix | Final decision | Reason |
| --- | --- | --- |
| `Graftcode_intro` | **Use only as inspiration; split and redraw.** | Useful high-level concepts, but universal compatibility and logo support are unverified and the text is unreadable. |
| `How_it_works` | **Discard composite; redraw two lifecycle diagrams.** | Conflates generation, runtime, transport selection, and cloud boundaries; Engine placement is misleading. |
| `Code_deep_dive` | **Discard.** | Code cannot be reviewed or copied; charts are not reproducible; too many concepts share one canvas. |
| `Observability_and_configuration` | **Use only as inspiration; split and redraw.** | Strongest implementation basis, but precedence is wrong and telemetry needs runtime scope. |
| `Security` | **Discard; redraw after owner review.** | Conflates security controls and implies encryption/authentication guarantees not enabled by default. |
