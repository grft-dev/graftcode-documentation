---
title: "What goes to the Graftcode cloud?"
description: "Current evidence boundaries for Gateway and cloud data flows."
keywords: "graftcode cloud, interface metadata, unified graft model, data flow"
---

# What goes to the Graftcode cloud?

The inspected implementation shows Gateway/uploader paths that build and submit Unified Graft Model data, with behavior that differs between anonymous and project-key flows. Package requests also necessarily identify requested package/version information.

That evidence is not a complete data inventory. It does not establish which metadata, dependency trees, logs, metrics, identifiers, request fields, or diagnostic data leave a particular deployed release, nor their retention and access policies.

Before approving a deployment, obtain a release-specific inventory covering:

- outbound destinations and schemas;
- anonymous and project-bound modes;
- UGM and dependency information;
- package-manager requests;
- telemetry and logging defaults;
- credentials, identifiers, retention, and operator access.

Do not use this compatibility page as a privacy, residency, or “no runtime data” guarantee. For the documented generation flow, see [Package generation](../core-concepts/package-generation.md).
