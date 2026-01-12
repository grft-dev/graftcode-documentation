---
title: "Installation"
description: "Install Graftcode Gateway and set up client packages to start connecting your services."
---

# Installation

## Prerequisites

- Node.js (for npm-based installations)
- Package manager of your choice (npm, pip, composer, etc.)
- Access to Graftcode Gateway

## Installing Graftcode Gateway

```bash
npm install -g graftcode-gateway
```

## Running the Gateway

```bash
gcg.exe --projectKey [yourKey] --env DEV
```

**Parameters:**
- `--projectKey`: Your unique project key (required)
- `--env`: Environment (DEV, STAGING, PROD)

## Installing Client Packages

After running the gateway, use the generated package manager command to install the client:

```bash
# Example for npm
npm install @graftcode/[service-name]

# Example for pip
pip install graftcode-[service-name]

# Example for composer
composer require graftcode/[service-name]
```
