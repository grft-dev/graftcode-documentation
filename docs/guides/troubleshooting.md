---
title: "Troubleshooting"
description: "Common issues and solutions for debugging Graftcode Gateway and client SDK problems."
---

## Common Issues

### Gateway Not Starting

**Problem**: Gateway fails to start.

**Solutions**:
- Check if port is already in use: `netstat -an | findstr :8080`
- Verify project key is correct
- Check firewall settings
- Review gateway logs: `./logs/gateway.log`

### Client Connection Failed

**Problem**: Client cannot connect to gateway.

**Solutions**:
- Verify gateway is running: `curl http://localhost:8080/health`
- Check endpoint configuration
- Verify network connectivity
- Check CORS settings if calling from browser

### Type Errors

**Problem**: TypeScript/IDE shows type errors.

**Solutions**:
- Regenerate graft: `npm install @graftcode/service-name --force`
- Restart IDE/TypeScript server
- Clear node_modules and reinstall
- Check gateway is exposing correct method signatures

### Method Not Found

**Problem**: Method not available on client.

**Solutions**:
- Verify method is public in backend service
- Check gateway has scanned the service
- Regenerate graft package
- Review gateway logs for scanning errors

### Performance Issues

**Problem**: Slow response times.

**Solutions**:
- Check network latency
- Verify gateway resources (CPU, memory)
- Review method implementation efficiency
- Consider caching frequently called methods
- Check for connection pooling issues

## Debugging

### Enable Debug Logging

```bash
# Gateway
gcg.exe --projectKey YOUR_KEY --env DEV --log-level DEBUG

# Client (environment variable)
export GRAFTCODE_DEBUG=true
```

### Debug Mode in Code

```typescript
import { ServiceName } from '@graftcode/service-name';

const service = new ServiceName({
  debug: true,
  logLevel: 'DEBUG'
});
```

### Common Debug Commands

```bash
# Check gateway status
curl http://localhost:8080/health

# List exposed services
curl http://localhost:8080/services

# View service methods
curl http://localhost:8080/services/user-service/methods
```

## Getting Help

- **Documentation**: Check Graftcode Vision portal
- **Community**: Join Discord server
- **GitHub**: Report issues on GitHub
- **Support**: Contact support through Vision portal
