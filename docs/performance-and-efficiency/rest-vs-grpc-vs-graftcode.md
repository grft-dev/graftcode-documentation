---
title: "REST vs gRPC vs Graftcode"
description: "A neutral responsibility comparison without unsupported benchmark claims."
keywords: "rest vs grpc vs graftcode, integration comparison"
---

# REST vs gRPC vs Graftcode

Choose an integration model by requirements, not by an unverified ranking.

- **REST** fits resource-oriented HTTP interfaces, broad client interoperability, caches, and conventional HTTP infrastructure.
- **gRPC** fits schema-first RPC, supported streaming patterns, and ecosystems that can use protobuf and HTTP/2.
- **Graftcode** derives a callable contract from selected code and supplies generated packages for supported runtime pairs.

All remote options still require authentication, authorization, versioning, observability, timeouts, retries, idempotency, deployment, and failure handling. Graftcode also serializes an invocation representation; it should not be described as having no protocol or decoding work.

Performance depends on the actual workload and implementation. See [Compare performance](compare-performance.md) before publishing comparative results, and [What is a Graft?](../core-concepts/what-is-a-graft.md) for the current programming model.
