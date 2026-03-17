academy/
├── introduction/
│   ├── what-is-graftcode.md
│   ├── what-problem-does-graftcode-solve.md
│   ├── where-graftcode-fits.md
│   └── when-to-use-graftcode.md
│
├── get-started/
│   ├── your-first-graft-in-5-minutes.md
│   ├── running-your-first-gateway.md
│   ├── installing-a-graft-as-dependency.md
│   └── calling-remote-methods-like-local.md
│
├── core-concepts/
│   ├── what-is-a-graft.md
│   ├── public-interface-vs-business-logic.md
│   ├── caller-and-receiver.md
│   ├── graftcode-gateway.md
│   ├── hypertube-runtime-bridge.md
│   └── graftcode-vision.md
│
├── how-graftcode-works/
│   ├── development-time-vs-production-time.md
│   ├── what-goes-to-graftcode-cloud.md
│   ├── how-grafts-are-generated.md
│   ├── runtime-call-execution.md
│   ├── local-remote-and-in-memory-execution.md
│   ├── observability-tracing-and-context-propagation.md
│   ├── scaling-load-balancers-and-proxies.md
│   ├── what-happens-when-interfaces-change.md
│
├── quickstarts/
│   ├── backend-to-backend-communication.md
│   ├── frontend-to-backend-edge-clients.md
│   ├── modular-monolith-quickstart.md
│   ├── replacing-rest-apis.md
│   └── replacing-grpc.md
│
├── integration-patterns/
│   ├── service-to-service-integration.md
│   ├── edge-clients-without-apis.md
│   ├── internal-business-apis.md
│   ├── mcp-hosting-and-ai-tools.md
│   ├── modular-monoliths.md
│   ├── microservices-without-contracts.md
│   └── event-driven-communication-preview.md
│
├── security-and-trust/
│   ├── security-model-overview.md
│   ├── authentication-and-authorization.md
│   ├── security-plugins.md
│   ├── transport-security-tls-wss.md
│   ├── network-boundaries-and-isolation.md
│   └── enterprise-self-hosted-engine.md
│
├── performance-and-efficiency/
│   ├── why-runtime-level-integration-is-faster.md
│   ├── rest-vs-grpc-vs-graftcode.md
│   ├── cpu-memory-and-network-usage.md
│   ├── cloud-cost-implications.md
│   └── when-performance-gains-matter.md
│
├── migration-guides/
│   ├── migrating-from-rest.md
│   ├── migrating-from-grpc.md
│   ├── incremental-adoption.md
│   └── coexisting-with-existing-integrations.md
│
├── faq-and-misconceptions/
│   ├── is-graftcode-a-cloud-proxy.md
│   ├── do-you-see-my-data.md
│   ├── is-this-vendor-lock-in.md
│   ├── what-if-graftcode-disappears.md
│   ├── is-this-production-ready.md
│   └── why-not-just-use-grpc.md
│
└── glossary/
    ├── graft.md
    ├── graftcode-gateway.md
    ├── hypertube.md
    ├── grafting-engine.md
    ├── vision.md
    ├── caller-and-receiver.md
    └── transport-channel.md

dorobic MANUAL
gdzie bedzie instrukcja uzycia Vision, GG, Portalu, Gateway z wszystkimi parametrami

manuals/
├── overview.md
│
├── graft-connection-and-configuration/
│   ├── graft-connection-string.md
│   ├── configuration-precedence.md
│   ├── per-graft-vs-global-configuration.md
│   ├── environment-variables.md
│   └── configuration-files.md
│
├── graftcode-gateway/
│   ├── installing-gateway.md
│   ├── running-gateway.md
│   ├── gateway-modes-standalone-vs-project.md
│   ├── gateway-startup-parameters.md
│   ├── hosting-options-local-docker-cloud.md
│   ├── loading-modules-and-runtimes.md
│   ├── gateway-health-checks.md
│   └── gateway-troubleshooting.md
│
├── hypertube-and-runtime/
│   ├── hypertube-execution-model.md
│   ├── thread-and-lifecycle-management.md
│   ├── stateful-vs-stateless-execution.md
│   ├── connection-lifecycle.md
│   └── runtime-failure-handling.md
│
├── vision/
│   ├── using-graftcode-vision.md
│   ├── try-it-and-live-invocations.md
│   ├── installation-snippets.md
│   ├── configuration-snippets.md
│   └── vision-security-model.md
│
├── platform-and-portal/
│   ├── projects-and-workspaces.md
│   ├── project-keys.md
│   ├── dashboard-and-metrics.md
│   ├── service-map.md
│   ├── graft-registry-and-versions.md
│   └── team-collaboration.md
│
├── plugins/
│   ├── plugin-system-overview.md
│   ├── authentication-plugins.md
│   ├── transport-channel-plugins.md
│   ├── plugin-lifecycle.md
│   └── contributing-plugins.md
│
├── testing-and-debugging/
│   ├── testing-with-grafts.md
│   ├── local-debugging.md
│   ├── distributed-debugging.md
│   ├── tracing-and-logs.md
│   └── common-debugging-scenarios.md
│
├── reliability-and-failures/
│   ├── timeouts.md
│   ├── retries-and-backoff.md
│   ├── reconnect-and-session-recovery.md
│   ├── channel-failures.md
│   └── graceful-degradation.md
│
├── health-and-operations/
│   ├── health-checks.md
│   ├── readiness-and-liveness.md
│   ├── scaling-behavior.md
│   └── rolling-updates.md
│
├── troubleshooting/
│   ├── common-issues.md
│   ├── gateway-startup-errors.md
│   ├── connection-problems.md
│   ├── versioning-problems.md
│   └── performance-issues.md
│
└── reference/
    ├── gateway-parameters-reference.md
    ├── configuration-reference.md
    ├── error-codes.md
    ├── plugin-interfaces.md
    └── supported-runtimes-and-languages.md


dorobic sekcje o testing i debugging

dodac info o obsludze bledow kanalu komunikacji timeout, retry, reconnect, disconnect itd...?

dodac info o health check

dac troubleshooting

poprawic reference

dodac diagramy, obrazki i screenshoty