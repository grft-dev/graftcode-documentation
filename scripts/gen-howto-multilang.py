#!/usr/bin/env python3
"""Generate how-to guide stubs.

Two authoring patterns (see docs/README.md — How-to guides):

1. **Code-only runtime differences** — single `how-to-guides/<slug>.md` with fenced
   ` ```multi ` blocks (runtime tabs in the portal). Prose is shared; only code differs.

2. **Prose differs by runtime** — folder `how-to-guides/<slug>/` with one file per runtime
   (`dotnet.md`, `javascript.md`, …). The portal shows a page-level stack picker.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "how-to-guides"
LANGS = ["dotnet", "javascript", "python", "java", "php", "ruby"]

HOST_EXAMPLES = {
    "dotnet": (
        "dotnet build ./Pricing/Pricing.csproj\n"
        'gg --runtime netcore --modules ./Pricing/bin/Debug/net9.0/Pricing.dll '
        '--types Pricing.PriceService --methods Calculate'
    ),
    "javascript": (
        "npm ci && npm run build\n"
        "gg --runtime nodejs --modules ./dist/index.js --types PriceService --methods calculate"
    ),
    "python": "gg --runtime python --modules ./pricing/",
    "java": "mvn package\ngg --runtime jvm --modules ./target/pricing-1.0.0.jar",
    "php": "composer install\ngg --runtime php --modules ./src/",
    "ruby": "bundle install\ngg --runtime ruby --modules ./lib/",
}

FILTER_GUIDE = """---
title: "Filter the callable surface"
description: "Limit which types and methods Gateway hosts using --types and --methods."
articleTitle: "Filter the callable surface"
---

Narrow the **callable surface** before consumers install a Graft. Use Gateway flags plus an
intentional public API in source code.

## CLI filters

| Flag | Purpose |
| --- | --- |
| `--types` | Comma-separated type names to expose |
| `--methods` | Comma-separated method names to expose |

Example by runtime:

{host_multi}

Combine with `--GMA` when you need analyzer output without starting servers:

```bash
gg --graftOnly --runtime <runtime> --modules <module> --types <Type> --methods <Method>
```

Analyzer-level method filters also exist for some runtimes (wildcard patterns). See
[Callable surface](../core-concepts/callable-surface.md).

## Workflow

1. Start with the smallest public API in code (internal helpers stay non-public).
2. Add `--types` / `--methods` when Gateway would otherwise discover too much.
3. Open Vision and confirm only intended members appear.
4. Generate and smoke-test the consumer package.

## Next steps

- [Expose code](../expose-code)
- [Dependency injection facade](../dependency-injection)
- [Gateway CLI reference](../reference/gateway-cli.md)
"""

MCP_GUIDE = """---
title: "Expose provider methods for MCP"
description: "Host a module with MCP support and resolve tool calls with --mcpBaseClass."
articleTitle: "Expose provider methods for MCP"
---

Gateway can participate in MCP workflows when the deployment enables the relevant HTTP surfaces and
CORS settings. This is an **Alpha** area—verify behavior on your Gateway release.

## 1. Host the provider

{host_multi}

## 2. Set MCP base class

When MCP `tools/call` uses a bare method name and `params.class` is empty, Gateway can resolve the
declaring type from `--mcpBaseClass`:

```bash
gg --runtime <runtime> --modules <module> \\
  --mcpBaseClass <fully-qualified-type-name>
```

Use the UGM type name form for your runtime (for example `Pricing.PriceService`, `com.app.Util`,
`package.module`, `MyModule::MyClass`).

## 3. Configure CORS for MCP clients

Browser or edge MCP clients may require CORS headers such as `MCP-Protocol-Version` and
`Mcp-Session-Id`. Example `cors.config`:

```ini
allowedOrigins=http://localhost:3000
allowedMethods=GET,POST,PUT,PATCH,DELETE,OPTIONS
allowedHeaders=content-type,authorization,MCP-Protocol-Version,Mcp-Session-Id
exposedHeaders=Mcp-Session-Id,MCP-Protocol-Version
allowCredentials=false
```

Start Gateway with:

```bash
gg --modules <module> --corsConfig ./cors.config
```

## 4. Verify

Confirm types in Vision, exercise an MCP client against the Gateway HTTP surface, and treat
authorization as explicit application work.

**Gap:** no verified end-to-end MCP tutorial is maintained in this documentation set. See
[Known limitations](../reference/known-limitations.md) and
[When to use Graftcode](../introduction/when-to-use-graftcode.md).

## Next steps

- [Filter the callable surface](filter-callable-surface.md)
- [Networking and ports](../operations/networking-ports.md)
"""

COEXIST_GUIDE = """---
title: "Use Graftcode alongside an existing REST API"
description: "Keep HTTP endpoints for external clients while adding Graftcode for typed internal integration."
articleTitle: "Use Graftcode alongside an existing REST API"
---

Graftcode and REST solve different integration problems. They can coexist in one product when each
boundary has a clear owner.

## When to keep REST

Keep REST (or OpenAPI) when:

- external clients require a public HTTP contract;
- partners integrate via webhooks or fixed URLs;
- consumers cannot install a generated Graft.

See [When to use Graftcode](../../introduction/when-to-use-graftcode.md).

## When to add Graftcode

Add Graftcode for **internal** or **controlled** callers that can install generated packages:

- service-to-service method calls across languages;
- sharing a provider library without hand-written HTTP clients;
- flipping between in-memory and remote execution with configuration alone.

## Typical layout

```text
┌─────────────────────────────────────┐
│  Monolith or API host               │
│  ├─ REST controllers (public)     │
│  └─ Provider module (Graftcode)    │──► Gateway ──► remote consumers
└─────────────────────────────────────┘
```

1. Extract callable business logic into a **plain module** (class library or package)—not controller
   types on the public Graft surface.
2. Keep REST controllers as thin adapters that call the same module internally if needed.
3. Host the module with Gateway for Graft consumers.
4. Do not expose database or HTTP framework types on the Graft contract.

## Consumer example ({lang_label})

After installing the Graft from Vision, configure remote execution before the first call. See
[Configure invocation](../configure-invocation).

REST traffic and Graft traffic use separate paths: HTTP routes for REST, generated Graft + Gateway
transport for Graftcode.

## Next steps

- [Expose code](../expose-code)
- [Caller and receiver](../../core-concepts/caller-and-receiver.md)
- [Authentication operations](../../operations/authentication-authorization.md)
"""

LANG_LABEL = {
    "dotnet": ".NET",
    "javascript": "Node.js",
    "python": "Python",
    "java": "JVM",
    "php": "PHP",
    "ruby": "Ruby",
}


def strip_fence(code: str) -> str:
    lines = code.strip().splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


def multi_fence(codes: dict[str, str]) -> str:
    parts = []
    for lang in LANGS:
        if lang not in codes:
            continue
        body = codes[lang]
        if body.strip().startswith("```"):
            body = strip_fence(body)
        parts.append(f"```{lang}\n{body.strip()}\n```")
    return "```multi\n" + "\n".join(parts) + "\n```"


def host_multi_fence() -> str:
    return multi_fence(HOST_EXAMPLES)


def write_code_only_guide(slug: str, template: str, **fmt):
    path = ROOT / f"{slug}.md"
    content = template.format(host_multi=host_multi_fence(), **fmt)
    path.write_text(content, encoding="utf-8")
    print(f"wrote {slug}.md (multi fences)")


def write_guide(folder: str, template: str, **fmt):
    d = ROOT / folder
    d.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        host = HOST_EXAMPLES[lang]
        content = template.format(host_example=host, lang_label=LANG_LABEL[lang], **fmt)
        (d / f"{lang}.md").write_text(content, encoding="utf-8")
    print(f"wrote {folder} x {len(LANGS)}")


if __name__ == "__main__":
    write_code_only_guide("filter-callable-surface", FILTER_GUIDE)
    write_code_only_guide("expose-mcp", MCP_GUIDE)
    write_guide("coexist-with-rest", COEXIST_GUIDE)

    AUTH = {
        "dotnet": """```csharp
using <generated_namespace>;

GraftConfig.Host = "wss://service.example/ws";
GraftConfig.Stateless = true;
GraftConfig.SetHeaders(new Dictionary<string, string> {
    ["Authorization"] = "Bearer <token>"
});

var result = PriceService.Calculate(100, 10);
```""",
        "javascript": """```typescript
import { GraftConfig, PriceService } from "<package-from-vision>";

GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders({ Authorization: "Bearer <token>" });

const result = await PriceService.calculate(100, 10);
```""",
        "python": """```python
from <generated_package_path>.graft_config import GraftConfig
from <generated_service_path> import PriceService

GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = True
# Header APIs vary by generated package; copy from Vision.

price = PriceService.calculate(100.0, 10.0)
```""",
        "java": """```java
import <generated_package>.GraftConfig;
import <generated_package>.PriceService;

GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders(java.util.Map.of("Authorization", "Bearer <token>"));

double price = PriceService.calculate(100, 10);
```""",
        "php": """```php
GraftConfig::$host = 'wss://service.example/ws';
GraftConfig::$stateless = true;
GraftConfig::setHeaders(['Authorization' => 'Bearer <token>']);

$price = PriceService::calculate(100, 10);
```""",
        "ruby": """```ruby
GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = true
# Copy header helper names from the generated gem.

price = PriceService.calculate(100, 10)
```""",
    }

    auth_tpl = """---
title: "Authenticate Graft calls"
description: "Pass tokens to remote providers using headers or supported method parameters."
articleTitle: "Authenticate Graft calls"
---

Gateway `--projectKey` authenticates **publication**, not each invocation. Validate credentials inside
provider methods or through generated header APIs.

## Option 1: token as a method parameter

Pass `apiKey` or `bearerToken` as a supported primitive parameter and validate before side effects.
This works in every runtime and in browser clients.

## Option 2: generated headers

{auth_multi}

Configure `host` and headers **before** the first generated call. Browser WebSocket clients cannot
set arbitrary handshake headers; use the HTTP/2 configuration emitted by Vision when required.

## Provider-side validation

Default deny: reject missing or invalid tokens with a clear domain exception. Do not log secrets.

## Next steps

- [Authentication operations](../operations/authentication-authorization.md)
- [Configure invocation](configure-invocation)
"""

    write_code_only_guide(
        "authenticate-graft-calls",
        auth_tpl,
        auth_multi=multi_fence(AUTH),
    )

    STATE = {
        "dotnet": """```csharp
// Stateless static call — preferred for remote routing
GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;
var total = PriceService.Calculate(10, 5);

// Stateful instance — object identity may not survive Gateway restart
var svc = new PriceService();
var value = svc.Calculate(10, 5);
```""",
        "javascript": """```typescript
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
const total = await PriceService.calculate(10, 5);

// Instance methods create remote object identity; prefer static when possible
const svc = new PriceService();
const value = await svc.calculate(10, 5);
```""",
        "python": """```python
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True
price = PriceService.calculate(10.0, 5.0)
```""",
        "java": """```java
GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;
double price = PriceService.calculate(10, 5);
```""",
        "php": """```php
GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;
$price = PriceService::calculate(10, 5);
```""",
        "ruby": """```ruby
GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true
price = PriceService.calculate(10, 5)
```""",
    }

    state_tpl = """---
title: "Stateless vs stateful Graft calls"
description: "Choose static stateless calls or instance-bound remote objects and configure GraftConfig.stateless."
articleTitle: "Stateless vs stateful Graft calls"
---

## Concepts

| Mode | Meaning |
| --- | --- |
| **Static method** | Type-level call; no remote object handle |
| **Instance method** | Bound to remote object identity across calls |
| **`stateless = true`** | Generated/runtime hint for independently routable operations |
| **`stateless = false`** | Allows stateful remote object semantics |

`stateless` does not remove serialization or network failure modes for remote calls.

## Examples

{state_multi}

## When to use which

- Prefer **static + stateless** for idempotent reads and independent operations behind load balancers.
- Use **instances** when the domain model requires constructor inputs and follow-up calls on the same
  object—and accept affinity requirements.

See [Static and instance context](../core-concepts/static-and-instance-context.md).

## Next steps

- [Configure invocation](configure-invocation)
- [Scaling](../operations/scaling.md)
"""

    write_code_only_guide(
        "stateless-vs-stateful",
        state_tpl,
        state_multi=multi_fence(STATE),
    )

    INMEM = {
        "dotnet": """```csharp
GraftConfig.Host = "inmemory";
GraftConfig.Module = "Pricing.dll"; // copy exact module id from generated package / Vision
```""",
        "javascript": """```typescript
GraftConfig.host = "inmemory";
// Ensure the provider JS module is resolvable on disk; copy module path from Vision.
```""",
        "python": """```python
GraftConfig.host = "inmemory"
GraftConfig.module = "<module-path-from-generated-package>"
```""",
        "java": """```java
GraftConfig.host = "inmemory";
GraftConfig.module = "<module-path-from-generated-package>";
```""",
        "php": """```php
GraftConfig::$host = 'inmemory';
GraftConfig::$module = '<module-path-from-generated-package>';
```""",
        "ruby": """```ruby
GraftConfig.host = "inmemory"
GraftConfig.module = "<module-path-from-generated-package>"
```""",
    }

    inmem_tpl = """---
title: "Set the module path for in-memory execution"
description: "Configure modules and GraftConfig.module when host is inmemory."
articleTitle: "Set the module path for in-memory execution"
---

`host=inmemory` loads the provider in the consumer process. The consumer must resolve the provider
artifact locally.

## Configuration file example

`graftcode-config.json`:

```json
{{
  "configurations": {{
    "default": {{
      "name": "default",
      "runtime": "<runtime>",
      "modules": "<provider-artifact-path>",
      "host": "inmemory",
      "stateless": true
    }}
  }}
}}
```

## Programmatic configuration

{inmem_multi}

If you see `FileNotFound` for the provider module, the client remained in `inmemory` without a
resolvable module path. See [Errors reference](../reference/errors-status.md).

## Next steps

- [Configure invocation](configure-invocation)
- [Execution modes](../core-concepts/execution-modes.md)
"""

    write_code_only_guide(
        "inmemory-module-path",
        inmem_tpl,
        inmem_multi=multi_fence(INMEM),
    )

    debug_tpl = """---
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

## Provider example ({lang_label})

```bash
{host_example}
```

## Next steps

- [Vision mismatch](../../troubleshooting/vision-mismatch.md)
- [Connection and auth failures](../../troubleshooting/connection-timeouts-auth.md)
- [Observability](../../operations/observability.md)
"""

    for lang in LANGS:
        d = ROOT / "debug-graft-invocations"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{lang}.md").write_text(
            debug_tpl.format(
                host_example=HOST_EXAMPLES[lang],
                lang_label=LANG_LABEL[lang],
            ),
            encoding="utf-8",
        )
    print("wrote debug-graft-invocations x 6")

    INSTALL = {
        "dotnet": "dotnet add package <package-id> --version <version> -s <registry-from-vision>",
        "javascript": "npm install <package> --registry <registry-from-vision>",
        "python": "python -m pip install <package> --extra-index-url <url-from-vision>",
        "java": "# Copy Maven dependency block from Vision",
        "php": "composer require <vendor/package>:<version> --repository <repo-from-vision>",
        "ruby": "gem install <name> --source <source-from-vision>",
    }

    install_tpl = """---
title: "Obtain and install a Graft"
description: "Use Gateway or Vision output to install the generated package without guessing registry details."
articleTitle: "Obtain and install a Graft"
---

## 1. Wait for publication

Start Gateway against the built provider and wait for successful model upload in logs or Vision.

## 2. Open Vision

Default HTTP port is `81` (`http://localhost:81/GV` in local Docker workflows).

## 3. Copy the install command

For {lang_label} consumers, copy the **complete** command from Vision, including registry, package
name, and version.

```bash
{install_cmd}
```

Never derive registry URLs from the provider assembly name. Use a [project key](../project-key) when
stable publication identity is required.

## 4. Verify exports

Inspect generated namespaces, imports, and method names in the installed package.

## Next steps

- [Configure invocation](../configure-invocation)
- [Generated package structure](../../reference/generated-package-structure.md)
"""

    for lang in LANGS:
        d = ROOT / "obtain-install-graft"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{lang}.md").write_text(
            install_tpl.format(install_cmd=INSTALL[lang], lang_label=LANG_LABEL[lang]),
            encoding="utf-8",
        )
    print("wrote obtain-install-graft x 6")

    RUN_GW = """---
title: "Run Gateway locally"
description: "Start Graftcode Gateway against a built module and verify discovery and publication."
articleTitle: "Run Gateway locally"
---

## 1. Install Gateway

Download from [Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

## 2. Build and host

{host_multi}

Use `gg.exe` on Windows. Prefer explicit `--runtime` and `--modules` over auto-scan in crowded directories.

## 3. Custom ports

```bash
gg <module> --port 8080 --httpPort 8081
```

## 4. Verify

Check logs for enabled types and successful publication, then open Vision.

## Next steps

- [Obtain and install a Graft](obtain-install-graft)
- [Gateway CLI](../reference/gateway-cli.md)
"""

    write_code_only_guide("run-gateway-locally", RUN_GW)

    DOCKER_DOTNET = """---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---

## Verified .NET workflow

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0
WORKDIR /usr/app
COPY . /usr/app/
RUN dotnet build && dotnet publish -c Release -o /usr/app/
RUN apt-get update && apt-get install -y wget \\
 && wget -O /usr/app/gg.deb https://github.com/grft-dev/graftcode-gateway/releases/latest/download/gg_linux_amd64.deb \\
 && dpkg -i /usr/app/gg.deb && rm /usr/app/gg.deb \\
 && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 80 81
CMD ["gg", "--modules", "Provider.dll"]
```

```bash
docker build -t provider:test .
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name provider provider:test
```

**Gap:** Docker recipes for every runtime are not verified in this documentation set.
"""

    DOCKER_OTHER = """---
title: "Deploy Gateway with Docker"
description: "Build a provider and Gateway into a container."
articleTitle: "Deploy Gateway with Docker"
---

Use a base image that includes the {lang_label} runtime and install the Linux `gg` package from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

```dockerfile
# Illustrative — pin Gateway version and base image for production
# COPY provider artifacts, install gg.deb, EXPOSE 80 81
CMD ["gg", "--runtime", "<runtime>", "--modules", "<module-path>"]
```

Host locally first with [Run Gateway locally](../run-gateway-locally), then containerize the same
`gg` command line.

**Gap:** no verified multi-stage Dockerfile for {lang_label} is maintained here.
"""

    d = ROOT / "deploy-with-docker"
    d.mkdir(parents=True, exist_ok=True)
    (d / "dotnet.md").write_text(DOCKER_DOTNET, encoding="utf-8")
    for lang in [x for x in LANGS if x != "dotnet"]:
        runtime = "nodejs" if lang == "javascript" else ("jvm" if lang == "java" else lang)
        (d / f"{lang}.md").write_text(
            DOCKER_OTHER.format(lang_label=LANG_LABEL[lang]).replace("<runtime>", runtime),
            encoding="utf-8",
        )
    print("wrote deploy-with-docker x 6")

    ERRORS = """---
title: "Handle provider and transport errors"
description: "Keep provider failures actionable and add retries only where repeat execution is safe."
articleTitle: "Handle provider and transport errors"
---

## Provider boundary

Validate inputs and throw domain exceptions with safe messages—no secrets in exception text.

## Classify before retry

- Domain errors: do not retry.
- Transient upstream `5xx` inside provider: bounded retry if idempotent.
- Transport failures: retry only idempotent operations; stateful identity may be lost.
- Package `422`: fix the public contract.

## Host example

{host_multi}

See [Timeouts and retries](../operations/timeouts-retries.md) and
[Errors reference](../reference/errors-status.md).
"""

    write_code_only_guide("handle-provider-errors", ERRORS)

    UPDATE = """---
title: "Update a provider contract"
description: "Change a public surface, regenerate packages, and upgrade consumers safely."
articleTitle: "Update a provider contract"
---

1. Classify breaking vs additive changes ([Contract evolution](../core-concepts/contract-evolution.md)).
2. Rebuild and host:

{host_multi}

3. Regenerate every consumer package from Vision.
4. Upgrade consumers with the new install command before removing old compatibility.

See [Version compatibility](../operations/version-compatibility-upgrades.md).
"""

    write_code_only_guide("update-provider-contract", UPDATE)

    DI_DOTNET = Path(__file__).resolve().parents[1] / "docs" / "how-to-guides" / "dependency-injection-dotnet.md"
    di_body = ""
    if DI_DOTNET.exists():
        di_body = DI_DOTNET.read_text(encoding="utf-8").split("---", 2)[-1].strip()
        di_body = di_body.replace("# Dependency injection in C#/.NET with stateless facades\n\n", "")

    DI_OTHER = """---
title: "Dependency injection with stateless facades"
description: "Keep containers internal while exposing a small Graftcode-compatible surface."
articleTitle: "Dependency injection with stateless facades"
---

This guide is verified for **.NET** in [Dependency injection — .NET](dotnet.md).

For {lang_label}, keep framework containers and infrastructure types off the public callable surface.
Expose a small facade with primitive or plain-model parameters. Wire dependencies inside the facade
method or through internal modules.

See the [{lang_label} language guide](../../language-guides/index.md).
"""

    d = ROOT / "dependency-injection"
    d.mkdir(parents=True, exist_ok=True)
    (d / "dotnet.md").write_text(
        "---\ntitle: \"Dependency injection with stateless facades\"\ndescription: \"Keep dependency injection internal while exposing a small Graftcode-compatible facade.\"\narticleTitle: \"Dependency injection with stateless facades\"\n---\n\n"
        + di_body,
        encoding="utf-8",
    )
    for lang in [x for x in LANGS if x != "dotnet"]:
        (d / f"{lang}.md").write_text(
            DI_OTHER.format(lang_label=LANG_LABEL[lang]), encoding="utf-8"
        )
    print("wrote dependency-injection x 6")
