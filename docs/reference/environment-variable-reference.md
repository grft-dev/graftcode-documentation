---
title: "Environment variable reference"
description: "Gateway, generated Graft configuration, Hypertube activation, embedded runtime paths, and diagnostic environment variables."
---

# Environment variable reference

Set variables in the **Caller process** before the first graft call. Hypertube caches runtime context
after initialization; restart the process after changes.

## Gateway

| Variable | Values / purpose | Precedence |
| --- | --- | --- |
| `GG_DEBUG` | `1` or `TRUE` logs incoming/outgoing byte traffic | Independent debug switch |
| `GSMU_ENDPOINT` | Legacy public variable name that overrides the Graftcode Engine endpoint | Overrides `--endpoint` |
| `GC_PROJECT_KEY` | Portal project JWT | Overrides `--projectKey` |

Treat `GC_PROJECT_KEY` as a secret. `GG_DEBUG` can expose invocation data and should remain off during
normal production operation.

## Generated Graft configuration sources

Generated packages resolve configuration from environment **pointers** and files. The environment
variable does not hold graft settings directly — it points to inline JSON/YAML, a file path, or a
connection string.

| Priority | Environment pointer | Typical file fallback |
| --- | --- | --- |
| 1 | `<graft-name>-config` | `<graft-name>-config.json` / `.yaml` / `.txt` |
| 2 | `graftcode-config` | `graftcode-config.json` / `.yaml` / `.txt` |

Keys inside the resolved configuration include `host`, `modules`, `runtime`, `stateless`, `licenseKey`,
and per-runtime `channel.runtimePath`. See [Configuration keys and precedence](configuration-keys-and-precedence.md).

Environment pointers outrank files, programmatic configuration, and generated defaults.

## Hypertube activation

| Variable | Purpose | Config file alternative |
| --- | --- | --- |
| `HYPERTUBE_KEY` | Hypertube license key for embedded in-memory runtimes | `licenseKey` in `graftcode-config.json` |

Resolution order: `licenseKey` from configuration file, then `HYPERTUBE_KEY` environment variable, then
license file on disk.

## Embedded Receiver runtime paths (in-memory)

When `host=inmemory` and the Caller technology differs from the Receiver technology, Hypertube must load
the Receiver's native runtime library on the local machine.

Resolution order for most Receiver runtimes:

1. `channel.runtimePath` in the Hypertube configuration file for that Receiver channel
2. Technology-specific environment variable (table below)
3. Platform defaults (`JAVA_HOME` for JVM; embedded PHP when `PHP_HOME` is unset)

| Variable | Receiver | Points to | Example value |
| --- | --- | --- | --- |
| `HYPERTUBE_RUBY_RUNTIME_PATH` | Ruby | Ruby shared library **file** | Windows: `C:\Ruby34-x64\bin\x64-ucrt-ruby340.dll`; Linux: `/usr/lib/libruby.so.3.4`; macOS: `/opt/homebrew/lib/libruby.3.4.dylib` |
| `HYPERTUBE_PYTHON_RUNTIME_PATH` | Python | Python shared library **file** | Windows: `C:\Python313\python313.dll`; Linux: `/usr/lib/x86_64-linux-gnu/libpython3.13.so` |
| `HYPERTUBE_PYTHON_VERSION` | Python | Version suffix used to build library name | `3.13` → `python3.13.dll` (Windows), `libpython3.13.so` (Linux) — prefer `HYPERTUBE_PYTHON_RUNTIME_PATH` when the file name does not match |
| `HYPERTUBE_PYTHON2_RUNTIME_PATH` | Python 2 (legacy) | Python 2 shared library **file** | `python27.dll`, `libpython2.7.so` |
| `HYPERTUBE_JVM_RUNTIME_PATH` | JVM | JVM shared library **file** or `JAVA_HOME` root | `C:\Program Files\Java\jdk-21\bin\server\jvm.dll` |
| `JAVA_HOME` | JVM | JDK/JRE root directory | `C:\Program Files\Java\jdk-21`; Hypertube searches `bin/server/jvm.dll` or `lib/server/libjvm.so` |
| `HYPERTUBE_NETCORE_RUNTIME_VERSION` | .NET | Target framework band | `net8.0`, `net9.0`, `net10.0` |
| `HT_NET_RUNTIME_CONFIG_PATH` | .NET | Full path to a `.runtimeconfig.json` file | `C:\app\MyApp.runtimeconfig.json` |
| `PHP_HOME` | PHP | PHP installation root (optional) | `C:\php`; when unset, Hypertube uses embedded PHP |

Node.js and Perl Receiver channels use runtimes bundled with the Hypertube package and do not expose
separate `HYPERTUBE_*_RUNTIME_PATH` variables in the native launchers.

## Hypertube diagnostics

| Variable | Scope | Values / purpose |
| --- | --- | --- |
| `HYPERTUBE_DEBUG` | Hypertube SDK (Python, JVM, PHP, Ruby, Node.js) | `true` enables SDK interpreter debug output |
| `HYPERTUBE_DEBUG_MODE` | Hypertube native launchers | `true` enables native launcher debug logging |
| `HYPERTUBE_LOGGING_LEVEL` | Hypertube native | `off`, `runtimeinfo` (default), `all` — overrides `loggingLevel` in config when set |
| `HYPERTUBE_INSTRUMENTATION_KEY` | Hypertube telemetry | Application Insights instrumentation key; optional |

`GG_DEBUG` (Gateway / protocol layer) and `HYPERTUBE_DEBUG` (Hypertube SDK) are independent. Enable
diagnostic variables only in controlled environments; captured logs may contain payload or credential
data.

## Samples

### Windows (PowerShell) — Python Caller, Ruby Receiver, in-memory

```powershell
$env:HYPERTUBE_KEY = "<your-hypertube-license-key>"
$env:HYPERTUBE_RUBY_RUNTIME_PATH = "C:\Ruby34-x64\bin\x64-ucrt-ruby340.dll"

# Optional: point graftcode-config at a file instead of using cwd lookup
$env:graftcode-config = "C:\apps\my-caller\graftcode-config.json"

# Optional: protocol byte logging (redact before sharing)
$env:GG_DEBUG = "1"
$env:HYPERTUBE_DEBUG = "true"
```

`graftcode-config.json`:

```json
{
  "licenseKey": "<your-hypertube-license-key>",
  "loggingLevel": "runtimeinfo",
  "runtimes": {
    "ruby": {
      "name": "default",
      "modules": "C:/receivers/my-ruby-package",
      "channel": {
        "type": "inMemory",
        "runtimePath": "C:/Ruby34-x64/bin/x64-ucrt-ruby340.dll"
      }
    }
  }
}
```

### Linux / macOS (bash) — .NET Caller, Python Receiver, in-memory

```bash
export HYPERTUBE_KEY="<your-hypertube-license-key>"
export HYPERTUBE_PYTHON_RUNTIME_PATH="/usr/lib/x86_64-linux-gnu/libpython3.13.so"
# or: export HYPERTUBE_PYTHON_VERSION="3.13"

export graftcode-config="/opt/my-caller/graftcode-config.json"

export HYPERTUBE_LOGGING_LEVEL="runtimeinfo"
export HYPERTUBE_DEBUG_MODE="true"
```

### JVM Receiver — `JAVA_HOME` vs explicit JVM library path

```bash
# Option A: JDK/JRE root (searched for libjvm.so / jvm.dll)
export JAVA_HOME="/usr/lib/jvm/java-21-openjdk-amd64"

# Option B: direct path when JAVA_HOME layout is non-standard
export HYPERTUBE_JVM_RUNTIME_PATH="/usr/lib/jvm/java-21-openjdk-amd64/lib/server/libjvm.so"
```

### .NET Receiver — framework band and custom runtime config

```bash
export HYPERTUBE_NETCORE_RUNTIME_VERSION="net8.0"

# Use only when the default runtimeconfig.json does not match your installed runtime
export HT_NET_RUNTIME_CONFIG_PATH="/opt/receivers/MyReceiver.runtimeconfig.json"
```

### PHP Receiver — optional external PHP installation

```bash
export PHP_HOME="/usr/local/php"
# When unset, Hypertube uses embedded PHP
```

### Gateway (Docker)

```bash
export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name receiver receiver:1.0.0
```

### Remote execution (no embedded runtime paths)

When `host` is `ws://` or `wss://`, the Receiver runs in Gateway. Set host and module through
configuration or code; embedded `HYPERTUBE_*_RUNTIME_PATH` variables are not required on the Caller.

```python
from my_graft_package.graft_config import GraftConfig

GraftConfig.host = "wss://gateway.example.com/ws"
GraftConfig.stateless = True
```

Programmatic remote host (field names vary — copy from Vision):

```multi
```dotnet
GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
```
```javascript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```python
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
```
```java
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
```
```php
GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;
```
```ruby
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true
```
```

## Quick lookup

| Scenario | Variables to set |
| --- | --- |
| First in-memory call fails with `Hypertube not active` | `HYPERTUBE_KEY` or `licenseKey` in config |
| Python → Ruby graft | `HYPERTUBE_RUBY_RUNTIME_PATH` (or `runtimePath` in config) + `modules` |
| Any Caller → Python graft | `HYPERTUBE_PYTHON_RUNTIME_PATH` or `HYPERTUBE_PYTHON_VERSION` |
| Any Caller → Java graft | `JAVA_HOME` or `HYPERTUBE_JVM_RUNTIME_PATH` |
| Any Caller → .NET graft | `HYPERTUBE_NETCORE_RUNTIME_VERSION`; `HT_NET_RUNTIME_CONFIG_PATH` if needed |
| PHP graft with custom extensions | `PHP_HOME` |
| Diagnose protocol / launcher issues | `GG_DEBUG`, `HYPERTUBE_DEBUG`, `HYPERTUBE_DEBUG_MODE`, `HYPERTUBE_LOGGING_LEVEL` |
| Gateway publication to portal | `GC_PROJECT_KEY` |

## Next steps

- [Environment and configuration](../operations/environment-and-configuration.md)
- [Configuration keys and precedence](configuration-keys-and-precedence.md)
- [In-memory execution and Hypertube exceptions](../troubleshooting/in-memory-hypertube-exceptions.md)
