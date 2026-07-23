---
title: "Version compatibility and upgrades"
description: "Upgrade Gateway, Receivers, and generated packages as one tested compatibility set."
---

# Version compatibility and upgrades

Graftcode Alpha does not guarantee backward compatibility across major Gateway, protocol, SDK, and
generated-package releases.

## Inventory

Record:

- Gateway release and platform;
- Receiver artifact/version and runtime;
- generated package name/version in each Caller ecosystem;
- Hypertube runtime dependency version;
- enabled transports and configuration sources.

## Upgrade procedure

1. Read release notes and select an explicit Gateway release.
2. Rebuild the Receiver with its supported runtime.
3. Start the new Gateway in an isolated environment and verify discovery/publication.
4. Generate fresh packages for every Caller ecosystem from that Gateway.
5. Compile/type-check Callers and run representative in-memory and remote calls.
6. Test errors, auth, tracing, retries, proxies, and stateful behavior used by the workload.
7. Deploy a stateless canary; keep the previous set available for rollback.
8. Drain old instances before removal and upgrade stateful workloads in a maintenance window.

Never infer compatibility from a matching public method signature alone; the Graftcode Engine and runtime
protocols also participate.

There is no exhaustive compatibility table or automatic contract-drift rejection. Treat Vision and
smoke tests from the deployed version as authoritative.

## Next steps

- [Update a Receiver contract](../how-to-guides/update-a-receiver-contract.md)
- [Runtime and package-manager support](../reference/supported-runtimes-and-package-managers.md)
- [Known limitations](../reference/known-limitations.md)
