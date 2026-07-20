---
title: "Core-concepts glossary"
description: "Canonical terminology for Grafts, callable surfaces, Gateway hosting, configuration, and runtime invocation."
---

# Core-concepts glossary

**Callable surface**  
The types and members selected by a module analyzer and represented in the UGM.

**Caller**  
Code that initiates one Graft invocation.

**Configuration**  
Named runtime, host, module, stateless, plugin, and related values used to initialize a runtime context.

**Generated Graft**  
The generated package installed by a consumer. It contains target-language wrappers and configuration code derived from a UGM.

**Graftcode Gateway (`gg`)**  
The process that hosts modules and exposes enabled runtime-call transports; it can also host Vision.

**Hosted module**  
Producer code loaded for execution by a Gateway or runtime context. It is user-written code, not the generated Graft.

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

**Unified Graft Model (UGM)**  
The analyzer-produced model consumed by package-generation components. It represents callable types and members independently of a generated target package.

**Project key**  
Portal-issued JWT (or `env:jwt` form) passed to Gateway as `--projectKey` or `GC_PROJECT_KEY`. Authenticates Gateway to portal/project metadata services and stabilizes project-backed publication. It is **not** the consumer registry URL from Vision install commands.

**Registry URL**  
Package-manager feed or registry base URL emitted by a running Gateway for installing a generated Graft (for example an npm `--registry` or NuGet `-s` value). Copy it from Vision; do not infer it from the provider name.

**Vision**  
The Gateway-hosted web UI for inspecting loaded modules. Exact UI features are release-specific unless verified.

See the dedicated pages for qualification and evidence.
