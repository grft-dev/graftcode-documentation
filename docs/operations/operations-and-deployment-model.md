---
title: "Operations and deployment model"
description: "Operate Graftcode Gateway and Receiver modules as a standard application workload."
---

# Operations and deployment model

Gateway is the host process and network entry point for remote Graft calls. A deployment contains:

1. the Receiver module and its runtime dependencies;
2. a compatible Gateway binary;
3. selected listeners;
4. optional project identity for stable publication;
5. external process supervision, networking, TLS, secrets, and observability.

Package generation/publication and runtime invocation are different paths. Callers install a
generated Graft first; normal calls then resolve configuration and invoke the Receiver through
Hypertube and Gateway. Graftcode cloud services are not proven to be in every runtime data path.

## Deployment choices

- Run [Gateway](../core-concepts/gateway-and-hosted-modules.md) beside the module on a host or VM
  ([Run Gateway locally](../how-to-guides/run-gateway-locally.md)).
- Package Gateway and the Receiver in one container you build
  ([Deploy with Docker](../how-to-guides/deploy-gateway-with-docker.md)—there is no official pre-built image).
- Replicate stateless Gateway/Receiver instances behind WebSocket-, TCP-, or HTTP/2-aware
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
- [Deployment with Docker](../how-to-guides/deploy-gateway-with-docker.md)
- [Networking and ports](networking-and-ports.md)
