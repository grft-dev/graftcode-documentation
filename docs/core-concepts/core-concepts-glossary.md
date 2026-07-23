---
title: "Core-concepts glossary"
description: "Canonical terminology for Grafts, callable surfaces, Gateway hosting, configuration, and runtime invocation."
---

# Core-concepts glossary

**Callable surface**  
The types and members intentionally exposed through Gateway for Graft generation.

**Caller**  
Code that initiates one Graft invocation.

**Configuration**  
Named runtime, host, module, stateless, plugin, and related values used to initialize a runtime context.

**Generated Graft**  
The generated package installed by a Caller. It contains target-language wrappers and configuration code derived from the Receiver's callable surface.

**Graftcode Engine**  
The Graftcode service that uses metadata from the Receiver's selected callable surface to generate the target-language Graft package. It runs at setup/publication time and is not in the runtime call path.

**Graftcode Gateway (`gg`)**  
The process that hosts modules and exposes enabled runtime-call transports; it can also host Vision.

**Hosted module**  
Receiver code loaded for execution by a Gateway or runtime context. It is user-written code, not the generated Graft.

**Hypertube**  
The runtime bridge that serializes commands, selects a configured execution path, dispatches operations, and returns responses.

**In-memory execution**  
Execution selected by `inmemory` or `in-memory` connection data. It still uses generated/runtime machinery; it is not synonymous with direct source-level method dispatch.

**Local**  
Ambiguous on its own. Say **same process**, **same machine**, or **local Gateway**.

**Receiver**  
The runtime side that handles a command and executes the target member.

**Remote execution**  
Execution through a configured network transport such as WebSocket, HTTP/2, or TCP.

**Runtime context**  
The initialized Hypertube context selected by a named resolved configuration.

**Project key**  
Portal-issued JWT (or `env:jwt` form) passed to Gateway as `--projectKey` or `GC_PROJECT_KEY`. Authenticates Gateway to portal/project metadata services and stabilizes project-backed publication. It is **not** the Caller registry URL, the runtime host, or a call credential. See [Project Key, registry, host, and credentials](../reference/project-key-registry-host-and-credentials.md).

**Registry URL**  
Package-manager feed or registry base URL emitted by a running Gateway for installing a generated Graft (for example an npm `--registry` or NuGet `-s` value). Copy it from Vision; do not infer it from the Receiver name. It is separate from the runtime host — see [Project Key, registry, host, and credentials](../reference/project-key-registry-host-and-credentials.md).

**Runtime host**  
The `GraftConfig` host value that selects where calls execute (`inmemory` or a Gateway endpoint such as `ws://host/ws`). It executes methods; it is never the registry URL.

**Call credential**  
A token or key passed as a method parameter or generated header to authorize one specific invocation. Validated by the Receiver; distinct from the Project Key and transport TLS.

**Vision**  
The Gateway-hosted web UI for inspecting the callable surface and obtaining install and configuration details. Exact UI features are release-specific.

See the dedicated pages for detail.
