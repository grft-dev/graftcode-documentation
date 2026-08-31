---
title: "In-memory execution and Hypertube exceptions"
description: "Diagnose in-memory Graft failures, embedded Receiver runtime setup, and Hypertube exception messages surfaced at the Caller."
keywords: "graftcode inmemory, HypertubeException, FileNotFound, module path, HYPERTUBE_RUBY_RUNTIME_PATH, launcher exception"
---

# In-memory execution and Hypertube exceptions

This article covers **runtime and environment failures** when `host=inmemory`. It assumes the installed
graft package is correct. For missing members, stale packages, or Vision mismatches, see
[Module, method, or type is missing](module-method-or-type-is-missing.md) and
[Installed package is stale](installed-package-is-stale.md).

## Symptoms

- The Caller defaults to `host=inmemory` but cannot load the Receiver module, embedded runtime, or native bridge.
- The first call fails with `HypertubeException`, `FileNotFound`, or native launcher exception codes.
- Receiver user-code exceptions (for example division by zero) appear wrapped in the Caller runtime.
- Configuration or environment changes appear to have no effect until the Caller process restarts.
- Transport errors (`WebSocket`, TLS, connection refused) appear even though you expected in-memory execution.

In-memory execution runs the Receiver inside the Caller process. Hypertube still marshals arguments and
results through its protocol. Failures covered here originate in Caller configuration, embedded runtime
bootstrap, module resolution, protocol/version mismatch, or Receiver user code — not in graft generation.

## Prerequisites for in-memory execution

Before interpreting Hypertube messages, confirm the Caller process can embed the Receiver runtime and
resolve the Receiver artifact.

### Generated Graft defaults

Generated packages default `host` / `Host` to `inmemory`. The installed package must include the Receiver
module for the target ecosystem, or you must configure a remote `ws://` / `wss://` host before the first
call. See [Set the module path for in-memory execution](../how-to-guides/set-the-module-path-for-in-memory-execution.md).

### Hypertube activation

In-memory mode embeds Hypertube native runtimes in the Caller process. Activation is required before the
first call.

| Source | Variable / key | Purpose |
| --- | --- | --- |
| Environment | `HYPERTUBE_KEY` | Hypertube license key |
| Configuration file | `licenseKey` in `graftcode-config.json` (or package-specific config) | Same license key, file-based setup |

If activation is missing or invalid, failures often appear as `Hypertube not active`, `License invalid`,
or native `Exception code 031` before any Receiver method runs.

### Embedded Receiver runtime paths

When the Caller technology differs from the Receiver technology (for example Python calling Ruby), Hypertube
must locate the Receiver's native runtime library on the machine. Set paths in the **Caller process**
before the first graft call.

Resolution order for most runtimes:

1. `runtimePath` in the Hypertube configuration file (`graftcode-config.json` or package config) for the
   Receiver channel
2. Technology-specific environment variable (below)
3. Platform defaults (for example `JAVA_HOME` for JVM)

| Receiver | Environment variable | Points to | Platform examples |
| --- | --- | --- | --- |
| Ruby | `HYPERTUBE_RUBY_RUNTIME_PATH` | Ruby shared library file | Windows: `x64-ucrt-ruby340.dll`; Linux: `libruby.so`; macOS: `libruby.dylib` |
| Python | `HYPERTUBE_PYTHON_RUNTIME_PATH` | Python shared library file | Windows: `python313.dll`; Linux/macOS: `libpython3.13.so` / `.dylib` |
| Python | `HYPERTUBE_PYTHON_VERSION` | Version suffix when auto-resolving library name | Example: `3.13` → `python3.13.dll` on Windows — prefer `HYPERTUBE_PYTHON_RUNTIME_PATH` for exact file path |
| Python 2 (legacy) | `HYPERTUBE_PYTHON2_RUNTIME_PATH` | Python 2 shared library | `python27.dll`, `libpython2.7.so` |
| JVM | `JAVA_HOME` | JDK/JRE root directory | Hypertube searches `bin/server/jvm.dll` or `lib/server/libjvm.so` under this path |
| JVM | `HYPERTUBE_JVM_RUNTIME_PATH` | Full path to JVM shared library **or** `JAVA_HOME` root | Overrides config when set; use when `JAVA_HOME` alone is insufficient |
| .NET | `HYPERTUBE_NETCORE_RUNTIME_VERSION` | Target framework band | `net8.0`, `net9.0`, `net10.0` |
| .NET | `HT_NET_RUNTIME_CONFIG_PATH` | Full path to a `.runtimeconfig.json` file | Use when the installed .NET runtime does not match the default config |
| PHP | `PHP_HOME` | PHP installation root (optional) | When unset, Hypertube uses embedded PHP; when set, uses that installation's `php.ini` and extensions |

Configuration file alternative — set `channel.runtimePath` per Receiver runtime in `graftcode-config.json`:

```json
{
  "licenseKey": "<your-hypertube-key>",
  "runtimes": {
    "ruby": {
      "name": "default",
      "modules": "<receiver-module-path>",
      "channel": {
        "type": "inMemory",
        "runtimePath": "C:/Ruby34-x64/bin/x64-ucrt-ruby340.dll"
      }
    }
  }
}
```

On Linux or macOS, use the corresponding `.so` or `.dylib` path. Prefer absolute paths in CI, containers,
and multi-user hosts where the runtime is not on the default search path.

See [Environment variable reference](../reference/environment-variable-reference.md) for the full
variable list and copy-paste samples per platform.

Restart the Caller after changing host, module path, `runtimePath`, or environment variables. Generated
runtime context is cached after first initialization.

## Diagnostics

1. **Confirm execution mode.** Read the resolved `host`. `inmemory` / `in-memory` selects in-process
   execution. `ws://`, `wss://`, `tcp://`, or HTTP/2 hosts select network transport instead.
2. **Verify module path and package contents.** For in-memory mode, the Receiver artifact must be
   resolvable from the generated `GraftConfig.module` / `modules` setting or the installed graft package
   layout.
3. **Check configuration precedence.** Environment variables override files and generated defaults.
   A stale higher-priority value can keep the Caller on the wrong host or module path.
4. **Capture the first complete exception.** Preserve the outer Caller type (for example
   `HypertubeException` in Python) and the inner Receiver message. Hypertube rehydrates callee exceptions
   on the Caller side.
5. **Identify the bootstrap stage.** Note whether the failure happened during activation, embedded runtime
   load, `loadLibrary`, `getType`, or result serialization.
6. **Enable diagnostics only in controlled environments.**

| Variable | Scope | Effect |
| --- | --- | --- |
| `GG_DEBUG=1` | Graft / protocol | Logs incoming and outgoing protocol bytes; may expose payload data |
| `HYPERTUBE_DEBUG=true` | Hypertube SDK | Enables SDK-level debug output where supported |
| `HYPERTUBE_DEBUG_MODE` | Hypertube native | Enables native launcher debug logging |
| `HYPERTUBE_LOGGING_LEVEL` | Hypertube native | Adjusts native log verbosity |

```bash
export GG_DEBUG=1
export HYPERTUBE_RUBY_RUNTIME_PATH=/opt/ruby/lib/libruby.so
export HYPERTUBE_KEY=<your-key>
```

Redact captured logs before sharing. Disable debug switches after diagnosis.

## Hypertube exception catalog (in-memory)

The table lists runtime and environment messages when `host=inmemory`. Exact wording can vary slightly
by Caller runtime. Inner types are shown for Python; other SDKs map the same protocol codes to native
types.

### Configuration and bootstrap

| Message pattern | Typical cause | Fix |
| --- | --- | --- |
| `Config cannot be null` | `GraftConfig` not initialized before first call | Call `GraftConfig.init()` / equivalent before use |
| `Unknown connection type` | Invalid `host` format | Use `inmemory`, `ws://…`, `wss://…`, `tcp://…`, or documented HTTP/2 form |
| `FileNotFound` / `Library not found` / `File not found: {path}` | Receiver module path wrong or artifact missing from deployment | Set `module` / `modules`; verify the Receiver file exists on disk |
| `Hypertube not active` / `Runtime not initialized` / `Hypertube not active. Activate Hypertube before first use` / native `Exception code 031` | Missing or invalid `HYPERTUBE_KEY` / activation | Provide activation key; restart Caller |
| `License file not found` / `License key not found` / `License key not found in configuration source` | Activation configuration incomplete | Fix license source for embedded runtime |
| `License invalid` | Activation rejected or expired | Renew or replace license key |
| `Cannot load module: Library not found: {path}` (Node.js Caller) | Receiver module path wrong | Fix `module` path; verify artifact is deployed |
| `Ruby Launcher: Exception code 004` / `Cannot find Ruby installed on this machine` | Ruby shared library not found | Set `HYPERTUBE_RUBY_RUNTIME_PATH` or `runtimePath` in config |
| `Python Launcher: Exception code 006` / `Cannot find Python installed on this machine` | Python shared library not found | Set `HYPERTUBE_PYTHON_RUNTIME_PATH` or `HYPERTUBE_PYTHON_VERSION` |
| `JVM Launcher: Exception code 001` / `Set JAVA_HOME environment variable` | JVM not located | Set `JAVA_HOME` or `HYPERTUBE_JVM_RUNTIME_PATH` |
| `JVM Launcher: Exception code 002` | `JAVA_HOME` set but `jvm.dll` / `libjvm.so` not found under expected paths | Point `HYPERTUBE_JVM_RUNTIME_PATH` at the JVM shared library |
| `.NET Launcher: Exception code 007` | `HT_NET_RUNTIME_CONFIG_PATH` points at invalid `.runtimeconfig.json` | Fix path or clear variable to use default runtime selection |
| `Ruby Launcher: Exception code 001` / `Receiver file not found` | Receiver module path wrong | Set `modules` / `GraftConfig.module` to the Receiver artifact |
| `Python syntax error in file` / `Ruby syntax error in file` / `PHP syntax error` | Receiver source on disk is invalid or incomplete | Fix Receiver build output; point module path at the built artifact |
| `currentCommand is undefined in InvocationContext execute method` | Internal SDK state error after partial failure | Restart Caller; capture full stack; report if reproducible |

### Module and type loading (`loadLibrary` / `getType`)

These messages mean Hypertube could not load the Receiver module or resolve a type from the deployed
artifact — not that the graft API surface is wrong.

| Message pattern | Typical cause | Fix |
| --- | --- | --- |
| `Type {name} not found` | Receiver module not loaded or type missing from deployed artifact | Verify `modules` path; confirm Receiver was built and published |
| `No module named '{name}'` (Python Receiver) | Python import path does not include the Receiver package | Fix `modules` path and `PYTHONPATH` / working directory |
| `Type {name} not found in .NET assemblies` / `not found in classpath` | Assembly/JAR not on the load path or dependency missing | Deploy all Receiver dependencies alongside the primary artifact |
| `Class not found: {name}` / `Type: {name} not found in include path` (PHP) | PHP autoload cannot reach the Receiver class file | Fix `modules` path and Receiver deployment layout |

### Callee exceptions propagated through Hypertube

Receiver **user code** exceptions are serialized and re-thrown on the Caller. This is expected behavior
when the Receiver logic fails at runtime.

| Receiver technology | Example inner cause | Caller sees (Python) |
| --- | --- | --- |
| Python | `ZeroDivisionError: division by zero` | `HypertubeException` with inner traceback |
| Ruby | `ZeroDivisionError: divided by 0` | `HypertubeException` |
| Node.js | `Error: ZeroDivisionException` | `HypertubeException` |
| JVM | `java.lang.ArithmeticException` | `HypertubeException` |
| .NET | `System.DivideByZeroException` | `HypertubeException` |
| PHP | `DivisionByZeroError` | `HypertubeException` |

Do not retry domain failures (validation, divide by zero, business rule violations). Fix Receiver logic
or Caller inputs.

### Protocol, version, and serialization

| Message pattern | Typical cause | Fix |
| --- | --- | --- |
| `Type {type} is not supported for serialization.` | Payload type not supported by the Hypertube protocol version in use | Align Caller and Receiver Hypertube versions |
| `Unsupported payload item type: {type}` | Protocol/version mismatch between Caller SDK and embedded runtime | Align Hypertube package versions; upgrade Caller dependencies |
| `Array index list must not be empty` / `Array index must be an integer` | Protocol command malformed — often version skew | Align Caller and Receiver Hypertube versions |

### When the error is not in-memory specific

| Message pattern | Likely mode mismatch |
| --- | --- |
| `WebSocket connection … failed` / `requires 'ws' or 'wss'` | Caller uses remote WebSocket, not `inmemory` |
| `HTTP/2 send … failed` / `requires 'http' or 'https'` | Caller uses HTTP/2 transport |
| `could not connect to {host}:{port}` | TCP/network path selected |
| Authentication or TLS errors | Remote Gateway path; see connection troubleshooting |

If you expected in-memory execution but see transport errors, inspect resolved `host` and environment
overrides.

## Fixes

- **Missing embedded runtime:** set `HYPERTUBE_*_RUNTIME_PATH` (or `JAVA_HOME` / `PHP_HOME`) in the same
  process that runs the Caller, then restart. On Windows, point at the `.dll`; on Linux/macOS, at the
  `.so` / `.dylib`.
- **Missing activation:** set `HYPERTUBE_KEY` or `licenseKey` in `graftcode-config.json`, then restart.
- **Wrong module for in-memory:** configure `GraftConfig.module` / `modules` and verify the Receiver
  artifact exists at that path. See
  [Set the module path for in-memory execution](../how-to-guides/set-the-module-path-for-in-memory-execution.md).
- **Accidental remote host:** set `host` to `inmemory` before first call, or configure the intended
  `ws://` Gateway URL explicitly.
- **Hypertube version skew:** align Caller SDK, embedded native binaries, and Receiver-side Hypertube
  versions from the same release.

## Data to collect before reporting

1. Resolved `host`, `module` / `modules`, and configuration source (env, file, code).
2. Caller runtime and Hypertube dependency versions.
3. Receiver runtime version and deployed artifact paths.
4. Full outer and inner exception text (redact secrets).
5. Bootstrap stage: activation, runtime load, `loadLibrary`, `getType`, or serialization.
6. Values set for `HYPERTUBE_KEY`, `HYPERTUBE_*_RUNTIME_PATH`, `JAVA_HOME`, and `runtimePath` in config.
7. OS and architecture (Windows/Linux/macOS, x64/arm64).

## Next steps

- [Connection, timeout, or authentication failure](connection-timeout-or-authentication-failure.md) —
  when the resolved host is remote, not `inmemory`
- [Module, method, or type is missing](module-method-or-type-is-missing.md) — graft surface or discovery
  issues (outside this article's scope)
- [Debug Graft invocations](../how-to-guides/debug-graft-invocations.md) — `GG_DEBUG`, Vision, and staged
  checks
- [Environment variable reference](../reference/environment-variable-reference.md) — activation, runtime
  paths, and diagnostic variables
- [In-memory, same-machine, and remote execution](../core-concepts/in-memory-same-machine-and-remote-execution.md) —
  execution-mode terminology
