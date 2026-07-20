---
title: "Debug Graft invocations"
description: "Use GG_DEBUG, Vision, and structured checks to diagnose Gateway and Graft failures."
articleTitle: "Debug Graft invocations"
---

## 1. Enable byte-level Gateway logging

```bash
export GG_DEBUG=1
gg --runtime <runtime> --modules <module>
```

**Warning:** logs may contain sensitive payload bytes. Use only in controlled environments.

## 2. Verify the hosted surface

1. Confirm the intended runtime in Gateway output.
2. Open Vision on the configured HTTP port (default `81`).
3. Compare discovered types/methods with your source.
4. Re-copy the install command from this Gateway instance.

## 3. Verify consumer configuration

- Remote: `host`/`Host` set to `ws://` or `wss://` **before** the first call.
- In-memory: provider module locally resolvable.
- After config changes, restart the consumer process (context is cached).

## 4. Classify the failure

| Symptom | Likely cause |
| --- | --- |
| `FileNotFound` provider DLL | `inmemory` without local module |
| `422` package generation | unsupported public type |
| Connection timeout | wrong host, proxy, or TLS termination |
| Missing method | filters, stale package, or analyzer gap |

See [Troubleshooting index](../../troubleshooting/index.md).

## Provider example (JVM)

```bash
mvn package
gg --runtime jvm --modules ./target/pricing-1.0.0.jar
```

## Next steps

- [Vision mismatch](../../troubleshooting/vision-mismatch.md)
- [Connection and auth failures](../../troubleshooting/connection-timeouts-auth.md)
- [Observability](../../operations/observability.md)

## Source anchors

- `graftcode-gateway/README.md`, `GG_DEBUG`
