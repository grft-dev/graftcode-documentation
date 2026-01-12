---
title: "Gateway CLI"
description: "Complete reference for Graftcode Gateway command-line interface."
---

# Gateway CLI

## Command Line Interface

### `gcg.exe`

Main gateway executable for hosting services.

**Syntax:**
```bash
gcg.exe [options]
```

**Options:**

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `--projectKey` | string | Yes | - | Your unique project key |
| `--env` | string | No | DEV | Environment name (DEV, STAGING, PROD) |
| `--port` | number | No | 8080 | Port number for gateway |
| `--host` | string | No | 0.0.0.0 | Host address |
| `--config` | string | No | - | Path to configuration file |
| `--log-level` | string | No | INFO | Logging level (DEBUG, INFO, WARN, ERROR) |
| `--log-file` | string | No | - | Path to log file |

**Examples:**

```bash
# Basic usage
gcg.exe --projectKey abc123 --env DEV

# With custom port
gcg.exe --projectKey abc123 --env DEV --port 9090

# With configuration file
gcg.exe --projectKey abc123 --env DEV --config ./gateway.config.json

# Debug mode
gcg.exe --projectKey abc123 --env DEV --log-level DEBUG
```

## Common Commands

### Starting the Gateway

```bash
# Development environment
gcg.exe --projectKey YOUR_KEY --env DEV

# Production environment
gcg.exe --projectKey YOUR_KEY --env PROD --port 8080
```

### Configuration via File

```bash
gcg.exe --projectKey YOUR_KEY --config ./gateway.config.json
```

### Debugging

```bash
# Enable debug logging
gcg.exe --projectKey YOUR_KEY --env DEV --log-level DEBUG --log-file ./gateway.log
```
