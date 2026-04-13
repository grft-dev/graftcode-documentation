---
title: "Quick Reference"
description: "Quick reference guide with common commands, configuration snippets, and troubleshooting tips for Graftcode."
---

## Installation

```bash
# Run Graftcode Gateway
gg.exe --runtime <your_runtime> --modules <your_backend_library>

# Install a Graft (command from Graftcode Vision)
npm install graft.npm.EnergyPrice --registry=http://grft.dev/<project-id>__graftcode
```

## Basic Usage

```typescript
import { EnergyService } from "@graft/npm.EnergyPrice";

const energy = new EnergyService();

const price = await energy.getCurrentPrice("DE");
```

## Configuration

### GraftConfig (code)

```typescript
import { GraftConfig } from "@graft/npm.EnergyPrice";

GraftConfig.host = "tcp://energy-service:9000";
```

### Graft Connection String

```typescript
GraftConfig.setConfig("name=graft.nuget.EnergyPrice;runtime=netcore;host=ws://localhost:8004/ws");
```

### Environment Variables

Configuration can also be supplied via environment variables or config files, applied per Graft or globally. See [Configuring a Graft](../core-concepts/what-is-a-graft.md#configuring-a-graft) for details.

## Integration Scenarios

### Frontend <-> Backend

```typescript
import { BackendService } from "@graft/npm.Backend";

const backend = new BackendService();
const data = await backend.getData();
```

### AI <-> Backend (MCP)

Services hosted on Graftcode Gateway can be exposed as MCP tools for AI clients without rewriting APIs. See [MCP Hosting and AI Tools](../integration-patterns/mcp-hosting-and-ai-tools.md).

### Monolith <-> Microservice

Switching between in-memory and remote execution is a configuration change, not a code change. Point `GraftConfig.host` at a remote Gateway or leave it unset for in-memory execution.

## Error Handling

```typescript
try {
  const result = await service.method(params);
} catch (error) {
  // Exceptions from the target runtime are propagated
  // as strongly typed errors in the calling language
}
```

## Testing

### Unit Test

```typescript
const service = new EnergyService();
const price = await service.getCurrentPrice("DE");
expect(price).toBeDefined();
```

### Mock Service

```typescript
jest.mock("@graft/npm.EnergyPrice", () => ({
  EnergyService: jest.fn().mockImplementation(() => ({
    getCurrentPrice: jest.fn().mockResolvedValue(0.32),
  })),
}));
```

## Common Commands

```bash
# Start Graftcode Gateway
gg.exe --runtime <your_runtime> --modules <your_backend_library>
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Gateway won't start | Check port availability and runtime path |
| Connection failed | Verify `GraftConfig.host` value |
| Type errors | Regenerate Graft package |
| Method not found | Check that the method is public |

## Links

- **Graftcode Vision**: hosted by the running Gateway (default: `http://localhost:<port>/vision`)
- **Graftcode Portal**: [https://graftcode.com](https://graftcode.com)
- **Graftcode Performance Lab**: [Performance Lab](https://gc-d-ca-polc-demo-perf-lab-01.blackgrass-d2c29aae.polandcentral.azurecontainerapps.io/)
