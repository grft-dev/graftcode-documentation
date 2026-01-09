---
title: "Core Concepts"
order: 4
description: "Understand the fundamental concepts of Graftcode including Gateway, Graft, Vision Portal, and method signatures."
---

# Core Concepts

## Gateway

The Graftcode Gateway is a lightweight service that:
- Hosts your backend/service logic
- Automatically exposes all public classes and methods
- Provides Graftcode Vision portal for monitoring and management
- Handles cross-language communication

## Graft

A "Graft" is the generated client package that:
- Provides strongly-typed interfaces to remote services
- Auto-updates when target API evolves
- Works with your native package manager
- Requires no REST/gRPC/PaaS client code

## Vision Portal

Graftcode Vision is a web portal that allows you to:
- Monitor services exposed with Graftcode Gateway
- Track all hosted modules
- View Grafts used in projects
- Add private artifact feeds
- Manage configurations

## Method Signatures

Graftcode uses method signatures instead of integration-specific logic:
- Code communicates through target method signatures
- Independent from platforms, data buses, and cloud PaaS
- Architecture and integrations can evolve seamlessly
