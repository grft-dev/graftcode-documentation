---
title: "Enterprise self-hosted engine"
description: "Learn how enterprises can self-host the Graftcode grafting engine to meet security, compliance, and regulatory requirements without changing the execution model."
keywords: "enterprise graftcode, self-hosted engine, compliance, regulated environments, on-prem graftcode"
---

# Enterprise self-hosted engine

For many organizations, especially in regulated or security-sensitive environments, introducing a cloud dependency requires careful evaluation.

Graftcode is designed to support these environments by offering an **enterprise self-hosted grafting engine**, allowing organizations to retain full control over metadata, tooling, and integration workflows—without changing how systems execute at runtime.

This section explains what is self-hosted, what is not, and why this model exists.

---

## What the self-hosted engine is

The self-hosted engine is a deployable version of the **grafting engine and metadata services** that normally run in the Graftcode cloud.

When self-hosted, the organization operates:
- its own graft registry
- its own Unified Graft Model storage
- its own metadata processing services
- its own on-demand graft generation infrastructure

All of this runs inside the organization’s own cloud account or on-prem environment.

---

## What the self-hosted engine is not

The self-hosted engine does **not**:
- execute business logic
- proxy production traffic
- participate in runtime calls
- replace the Graftcode Gateway or Hypertube

Execution still happens entirely:
- inside application processes
- inside Gateways
- inside the organization’s networks

The self-hosted engine exists purely for **metadata and tooling**, not execution.

---

## Why enterprises need this option

Some organizations must satisfy requirements such as:
- data residency
- regulatory compliance
- internal security audits
- vendor risk assessments
- restricted outbound connectivity

Even though the Graftcode cloud does not process runtime data, these organizations may still require **full ownership of all supporting services**.

The self-hosted engine exists to meet these requirements without altering the architecture.

---

## No change to the execution model

A key design goal is that **nothing changes for developers**.

Whether the grafting engine is:
- hosted by Graftcode
- self-hosted in a private cloud
- deployed on-prem

the runtime model remains identical:
- Gateways behave the same
- Hypertube executes the same
- invocation intent flows the same way
- plugins and security behave the same

Only the destination of metadata exchange changes.

---

## Deployment and isolation

The self-hosted engine can be deployed:
- in a private cloud subscription
- in a dedicated tenant
- in an on-prem environment

It can be isolated:
- at the network level
- at the account or subscription level
- behind internal load balancers and firewalls

This allows organizations to align deployment with existing security zones and policies.

---

## Marketplace availability

For cloud-native enterprises, the self-hosted engine is designed to be available through:
- cloud marketplaces
- managed private offers
- enterprise licensing agreements

This simplifies procurement, billing, and internal approval processes.

---

## Auditing and compliance

Because the self-hosted engine runs inside the organization’s environment:
- traffic can be inspected
- logs can be retained internally
- access can be audited
- changes can be reviewed

This supports:
- SOC audits
- internal security reviews
- compliance reporting

The system behaves like any other internally operated platform service.

---

## Operational responsibility

With self-hosting comes operational responsibility.

Organizations manage:
- availability
- scaling
- backups
- upgrades

Graftcode provides:
- deployment artifacts
- upgrade paths
- operational guidance

but does not require any changes to application code.

---

## Gradual adoption path

Organizations do not need to start with a self-hosted engine.

A common adoption path is:
- start with the hosted Graftcode platform
- validate value and usage
- migrate to a self-hosted engine later if required

Because the execution model is unchanged, this transition is operational—not architectural.

---

## Trust through control

The enterprise self-hosted engine exists to reduce friction in high-trust environments.

It allows organizations to:
- keep control over all supporting services
- satisfy compliance requirements
- avoid unnecessary external dependencies

while preserving the developer experience and architectural benefits of Graftcode.

---

## Closing perspective

Graftcode does not require blind trust.

For organizations that need it, the self-hosted engine provides:
- ownership
- isolation
- compliance

without compromising on performance, execution semantics, or developer productivity.
