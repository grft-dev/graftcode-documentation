---
title: "What happens when interfaces change"
description: "Compatibility route for the canonical contract-evolution guidance."
keywords: "graftcode interface changes, contract evolution, compatibility"
---

# What happens when interfaces change

This topic moved to [Contract evolution](../core-concepts/contract-evolution.md).

Treat the analyzer-selected callable surface and its UGM type information as a contract. Removing or renaming members, changing mapped types or parameter order, switching static and instance shape, and introducing unsupported types can break generated consumers.

Before publishing a change:

1. compare the new UGM with the previous model;
2. generate every supported consumer package;
3. compile or type-check representative consumers;
4. run applicable in-memory and remote smoke tests;
5. publish according to the target package ecosystem's version policy.

The current implementation evidence does not establish automatic breaking-change rejection, universal retention of old packages, or compatibility between an old Graft and a changed provider. Do not rely on those behaviors without release-specific end-to-end tests.
