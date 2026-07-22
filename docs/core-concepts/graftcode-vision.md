---
title: "Graftcode Vision"
description: "What is verified about the Gateway-hosted Vision interface, with unverified UI behavior clearly marked."
---

# Graftcode Vision

**Graftcode Vision** is a web UI that the Gateway can host for inspecting loaded modules. The Gateway README describes it as a web UI and a graph view for loaded modules.

## What Vision provides

- Vision hosting is enabled by the Gateway `--GV` option, on by default.
- The Vision HTTP port defaults to `81` and can be changed with `--httpPort`.
- Vision reflects the callable surface of the modules loaded by that Gateway process.

## Use the running Gateway as the source

Module selection, runtime detection, filters, and startup success determine what a Gateway actually hosts. Check Gateway output and the Vision instance for that process rather than inferring package names, versions, ports, or registry paths.

## Features requiring release-specific verification

The exact Vision UI features depend on your Gateway release. The following are **not guaranteed by this page**:

- exact package-install commands or supported package ecosystems shown in the UI;
- interactive method execution;
- generated code samples;
- configuration snippets;
- immediate UI refresh after contract changes;
- security equivalence between Vision and runtime-call transports.

If a release displays one of these features, treat that running release as confirmation of the feature and copy values exactly. Do not generalize it to other versions without release documentation.
