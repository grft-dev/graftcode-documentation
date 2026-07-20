---
title: "Version compatibility and upgrades"
description: "Upgrade Gateway, providers, and generated packages as one tested compatibility set."
---

# Version compatibility and upgrades

Graftcode Alpha does not guarantee backward compatibility across major Gateway, protocol, SDK, and
generated-package releases.

## Inventory

Record:

- Gateway release and platform;
- provider artifact/version and runtime;
- generated package name/version in each consumer ecosystem;
- Hypertube runtime dependency version;
- enabled transports and configuration sources.

## Upgrade procedure

1. Read release notes and select an explicit Gateway release.
2. Rebuild the provider with its supported runtime.
3. Start the new Gateway in an isolated environment and verify discovery/publication.
4. Generate fresh packages for every consumer ecosystem from that Gateway.
5. Compile/type-check consumers and run representative in-memory and remote calls.
6. Test errors, auth, tracing, retries, proxies, and stateful behavior used by the workload.
7. Deploy a stateless canary; keep the previous set available for rollback.
8. Drain old instances before removal and upgrade stateful workloads in a maintenance window.

Never infer compatibility from a matching public method signature alone; generators and runtime
protocols also participate.

**Gap:** no published exhaustive compatibility table or automatic contract-drift rejection was found.
Vision and smoke tests from the deployed version are authoritative.

## Next steps

- [Update a provider contract](../how-to-guides/update-provider-contract.md)
- [Runtime and package-manager support](../reference/supported-runtimes-package-managers.md)
- [Known limitations](../how-graftcode-works/alpha-limitations-and-known-constraints.md)

## Source anchors

- `graftcode-gateway/README.md`, runtime requirements
- `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/`
- `graftcode-package-generation-engine/` and `graftcode-code-generator/`
- [Alpha limitations](../how-graftcode-works/alpha-limitations-and-known-constraints.md)
