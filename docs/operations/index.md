---
title: "Operations and deployment model"
description: "Operate Graftcode Gateway and provider modules as a standard application workload."
---

# Operations and deployment model

Gateway is the host process and network entry point for remote Graft calls. A deployment contains:

1. the provider module and its runtime dependencies;
2. a compatible Gateway binary;
3. selected listeners;
4. optional project identity for stable publication;
5. external process supervision, networking, TLS, secrets, and observability.

Package generation/publication and runtime invocation are different paths. Consumers install a
generated Graft first; normal calls then resolve configuration and invoke the provider through
Hypertube and Gateway. Graftcode cloud services are not proven to be in every runtime data path.

## Deployment choices

- Run Gateway beside the module on a host or VM.
- Package Gateway and the provider in one container.
- Replicate stateless Gateway/provider instances behind WebSocket-, TCP-, or HTTP/2-aware
  infrastructure.
- Keep stateful sessions pinned to one instance.

Pass the built module path explicitly, pin Gateway and generated-package versions, and obtain registry
and host values from current Gateway/Vision output.

## Operational gaps

No built-in orchestrator, universal readiness endpoint, metrics endpoint, zero-downtime reload
command, or stable cross-major compatibility guarantee is documented. Supply these controls through
the deployment platform and validate them for the installed release.

## Next steps

- [Gateway lifecycle](gateway-lifecycle.md)
- [Deployment with Docker](../how-to-guides/deploy-with-docker.md)
- [Networking and ports](networking-ports.md)
