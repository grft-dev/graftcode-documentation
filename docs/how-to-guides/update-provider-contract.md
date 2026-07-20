---
title: "Update a provider contract"
description: "Change a public surface, regenerate packages, and upgrade consumers safely."
---

# Update a provider contract

## Goal

Publish a provider change without silently breaking installed Grafts.

## 1. Classify the change

Usually breaking changes include removing or renaming members, changing parameter order or type,
changing return type, switching static and instance methods, and introducing unsupported types.
Additive methods are safer but are not guaranteed compatible in every generated target language.

## 2. Rebuild and inspect discovery

Build the provider, run Gateway against the new artifact, and compare the discovered surface with the
previous package. Verify static/instance shape, names, parameters, returns, and model members.

## 3. Generate every consumer target

Obtain a new package through the active Gateway/Vision output for each supported consumer ecosystem.
Compile or type-check representative consumers and run both local and remote smoke tests where used.

## 4. Publish and roll out deliberately

Use the version emitted by the active publication workflow. Do not overwrite or infer package
versions. Keep the previous provider contract reachable while old consumers remain deployed when the
deployment can host versions side by side.

Upgrade consumers using the exact current package-manager command, review generated API differences,
then deploy them before removing old compatibility.

## 5. Plan Gateway upgrades separately

Alpha releases do not guarantee compatibility across major Gateway, protocol, and generated-package
versions. Pin deployed versions and test Gateway plus all installed Grafts together.

**Gap:** the inspected implementation does not prove automatic rejection of a changed UGM registered
under the same version. Do not rely on automatic drift detection.

## Next steps

- [Version compatibility and upgrades](../operations/version-compatibility-upgrades.md)
- [Obtain and install a Graft](obtain-install-graft.md)
- [Known limitations](../reference/known-limitations.md)

## Source anchors

- `graftcode-package-manager-gateway/` version and package request paths
- `graftcode-package-generation-engine/`
- `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/virtual-repos-smoke-tests/`
- [Contract evolution](../core-concepts/contract-evolution.md)
