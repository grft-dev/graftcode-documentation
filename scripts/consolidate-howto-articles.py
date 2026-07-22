#!/usr/bin/env python3
"""Consolidate how-to folders where only code differs into single .md files with ```multi fences."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "how-to-guides"
LANGS = ["dotnet", "javascript", "python", "java", "php", "ruby"]

HOST = {
    "dotnet": (
        "dotnet build ./Pricing/Pricing.csproj\n"
        "gg ./Pricing/bin/Debug/net9.0/Pricing.dll"
    ),
    "javascript": (
        "npm ci && npm run build\n"
        "gg ./dist/index.js"
    ),
    "python": "gg ./pricing/",
    "java": "mvn package\ngg ./target/pricing-1.0.0.jar",
    "php": "composer install\ngg ./src/",
    "ruby": "bundle install\ngg ./lib/",
}

INSTALL = {
    "dotnet": "dotnet add package <package-id> --version <version> -s <registry-from-vision>",
    "javascript": "npm install <package> --registry <registry-from-vision>",
    "python": "python -m pip install <package> --extra-index-url <url-from-vision>",
    "java": "# Copy the Maven dependency block from Vision",
    "php": "composer require <vendor/package>:<version> --repository <repo-from-vision>",
    "ruby": "gem install <name> --source <source-from-vision>",
}

CONFIG = {
    "dotnet": """using <generated_namespace>;

GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;""",
    "javascript": """import { GraftConfig } from "<package-copied-from-vision>";

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "python": """from <generated_package_path>.graft_config import GraftConfig

GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True""",
    "java": """import <generated_package>.GraftConfig;

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "php": """GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;""",
    "ruby": """GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true""",
}

CONTRACT = {
    "dotnet": """namespace Pricing;

public static class PriceService
{
    public static double Calculate(double amount, double discountPercent) =>
        amount * (1 - discountPercent / 100);
}""",
    "javascript": """export class PriceService {
  static calculate(amount: number, discountPercent: number): number {
    return amount * (1 - discountPercent / 100);
  }
}""",
    "python": """class PriceService:
    @staticmethod
    def calculate(amount: float, discount_percent: float) -> float:
        return amount * (1 - discount_percent / 100)""",
    "java": """public class PriceService {
    public static double calculate(double amount, double discountPercent) {
        return amount * (1 - discountPercent / 100);
    }
}""",
    "php": """class PriceService {
    public static function calculate(float $amount, float $discountPercent): float {
        return $amount * (1 - $discountPercent / 100);
    }
}""",
    "ruby": """class PriceService
  def self.calculate(amount, discount_percent)
    amount * (1 - discount_percent / 100.0)
  end
end""",
}

BUILD = {
    "dotnet": "dotnet build ./Pricing/Pricing.csproj",
    "javascript": "npm ci\nnpm run build",
    "python": "# Build or package the provider module per your project layout",
    "java": "mvn package",
    "php": "composer install",
    "ruby": "bundle install",
}

GG_START = {
    "dotnet": "gg ./Pricing/bin/Debug/net9.0/Pricing.dll",
    "javascript": "gg ./dist/index.js",
    "python": "gg ./pricing/",
    "java": "gg ./target/pricing-1.0.0.jar",
    "php": "gg ./src/",
    "ruby": "gg ./lib/",
}


def gg_command(lang: str) -> str:
    return HOST[lang].split("\n")[-1]


def with_project_key_cli(lang: str) -> str:
    return gg_command(lang).replace("gg ", 'gg --projectKey "dev:<jwt-copied-from-portal>" ', 1)


def multi_fence(codes: dict[str, str], lang_in_fence: bool = True) -> str:
    parts = []
    for lang in LANGS:
        if lang not in codes:
            continue
        body = codes[lang].strip()
        fence = lang if lang_in_fence else "bash"
        parts.append(f"```{fence}\n{body}\n```")
    return "```multi\n" + "\n".join(parts) + "\n```"


def write_article(slug: str, body: str, **frontmatter_fields: str) -> None:
    path = ROOT / f"{slug}.md"
    text = "---\n"
    for key, value in frontmatter_fields.items():
        text += f'{key}: "{value}"\n' if " " in str(value) else f"{key}: {value}\n"
    text += "---\n" + body.strip() + "\n"
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path.name}")


def remove_folder(slug: str) -> None:
    folder = ROOT / slug
    if folder.is_dir():
        shutil.rmtree(folder)
        print(f"removed {slug}/")


def project_key() -> None:
    body = f"""A **project key** authenticates Gateway to Graftcode portal and project metadata services. It is not
the same as the **registry URL** shown on the dashboard for installing a generated Graft.

## What each identifier is for

| Identifier | Used by | Purpose |
| --- | --- | --- |
| **Project key** (`--projectKey`, `GC_PROJECT_KEY`) | Gateway at startup | Portal/project identity, stable publication context |
| **Registry URL** (in Vision install commands) | Consumer package managers | Download a specific generated Graft package |

A Gateway without a project key can receive a **new registry identifier after restart**. Consumers must
copy install commands from the **currently running** Gateway or Vision—not from an old log line.

The project key does **not** authenticate individual Graft invocations. See
[Authenticate Graft calls](authenticate-graft-calls.md) and
[Authentication operations](../operations/authentication-authorization.md).

## Obtain a project key

1. Sign in to [Graftcode Portal](https://portal.graftcode.com/).
2. Open or create a project for the provider you host.
3. Copy the project key from the project settings or onboarding flow shown in the portal UI for your
   account.

The key is a JWT, often used in `env:jwt` form (for example `dev:eyJ...`) or as a bare token. Copy
the exact format the portal displays.

**Gap:** portal screen names and navigation can change between releases. Use the live portal UI as
authority.

## Configure Gateway

Prefer environment variables in deployment; they override CLI flags:

{multi_fence({lang: f'export GC_PROJECT_KEY="dev:<jwt-copied-from-portal>"\\n{HOST[lang]}' for lang in LANGS})}

Or pass on the command line (avoid in shared shells and images):

{multi_fence({lang: with_project_key_cli(lang) for lang in LANGS})}

For Docker, inject `GC_PROJECT_KEY` through the platform secret store—never bake it into the image.
See [Deploy with Docker](deploy-with-docker.md).

## Versioning interaction

With a project key, Gateway uses project-backed publication semantics. In standalone mode without a
key, versioning is disabled by default unless `--keepVersioning` is set. See
[Gateway versioning](gateway-no-versioning.md).

## Next steps

- [Obtain and install a Graft](obtain-install-graft.md)
- [Environment variables](../reference/environment-variables.md)
- [Core-concepts glossary — Project key](../core-concepts/glossary.md#project-key)
"""
    write_article(
        "project-key",
        body,
        title="Use a portal project key",
        description="Obtain a project key from the portal, configure Gateway, and understand how it differs from a registry URL.",
        articleTitle="Use a portal project key",
    )


def obtain_install_graft() -> None:
    body = f"""## 1. Wait for publication

Start Gateway against the built provider and wait for successful model upload in logs or Vision.

## 2. Open Vision

Default HTTP port is `81` (`http://localhost:81/GV` in local Docker workflows).

## 3. Copy the install command

For your runtime, copy the **complete** command from Vision, including registry, package name, and
version.

{multi_fence({lang: INSTALL[lang] for lang in LANGS})}

Never derive registry URLs from the provider assembly or module name. Use a [project key](project-key.md)
when stable publication identity is required.

## 4. Verify exports

Inspect generated namespaces, imports, and method names in the installed package.

## Next steps

- [Configure invocation](configure-invocation.md)
- [Generated package structure](../reference/generated-package-structure.md)
"""
    write_article(
        "obtain-install-graft",
        body,
        title="Obtain and install a Graft",
        description="Use Gateway or Vision output to install the generated package without guessing registry details.",
        articleTitle="Obtain and install a Graft",
    )


def configure_invocation() -> None:
    body = f"""Point an installed Graft at the intended provider.

## 1. Choose execution mode

- `inmemory` loads the provider module in the consumer process.
- `ws://` or `wss://` sends calls to a remote Gateway WebSocket endpoint.
- TCP and HTTP/2 are optional Gateway transports and must be explicitly enabled.

Many generated Grafts default to `inmemory`. Confirm the default for your package in Vision.

## 2. Configure before the first call

Set `host` and `stateless` programmatically **before** the first generated call. Copy imports and
field names from Vision—the generated runtime context is cached after initialization.

{multi_fence(CONFIG)}

## 3. Pick the state model deliberately

Prefer static methods and stateless calls for independently routable operations. Instance methods and
remote object identity are stateful; they require connection/session affinity and can be lost on
Gateway restart or scale-in.

## 4. Use another configuration source only when needed

Generated packages inspect multiple configuration source levels (environment, files, programmatic
settings, then library defaults). Earlier levels win in the inspected resolver.

## Next steps

- [Stateless vs stateful](stateless-vs-stateful.md)
- [Configuration keys and precedence](../reference/configuration-keys-precedence.md)
- [Networking and ports](../operations/networking-ports.md)
- [Scale Gateway instances](../operations/scaling.md)
"""
    write_article(
        "configure-invocation",
        body,
        title="Configure Graft invocation",
        description="Select in-memory or remote execution and configure generated GraftConfig before first use.",
        articleTitle="Configure Graft invocation",
    )


def coexist_with_rest() -> None:
    body = """Graftcode and REST solve different integration problems. They can coexist in one product when each
boundary has a clear owner.

## When to keep REST

Keep REST (or OpenAPI) when:

- external clients require a public HTTP contract;
- partners integrate via webhooks or fixed URLs;
- consumers cannot install a generated Graft.

See [When to use Graftcode](../introduction/when-to-use-graftcode.md).

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

## Consumer example

After installing the Graft from Vision, configure remote execution before the first call. See
[Configure invocation](configure-invocation.md).

REST traffic and Graft traffic use separate paths: HTTP routes for REST, generated Graft + Gateway
transport for Graftcode.

## Next steps

- [Expose code](expose-code.md)
- [Caller and receiver](../core-concepts/caller-and-receiver.md)
- [Authentication operations](../operations/authentication-authorization.md)
"""
    write_article(
        "coexist-with-rest",
        body,
        title="Use Graftcode alongside an existing REST API",
        description="Keep HTTP endpoints for external clients while adding Graftcode for typed internal integration.",
        articleTitle="Use Graftcode alongside an existing REST API",
    )


def debug_graft_invocations() -> None:
    body = f"""## 1. Enable byte-level Gateway logging

```bash
export GG_DEBUG=1
gg <module>
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

See [Troubleshooting index](../troubleshooting/index.md).

## Provider example

{multi_fence(HOST)}

## Next steps

- [Vision mismatch](../troubleshooting/vision-mismatch.md)
- [Connection and auth failures](../troubleshooting/connection-timeouts-auth.md)
- [Observability](../operations/observability.md)
"""
    write_article(
        "debug-graft-invocations",
        body,
        title="Debug Graft invocations",
        description="Use GG_DEBUG, Vision, and structured checks to diagnose Gateway and Graft failures.",
        articleTitle="Debug Graft invocations",
    )


def gateway_no_versioning() -> None:
    no_ver = {}
    for lang in LANGS:
        if "\n" in HOST[lang]:
            build, gg = HOST[lang].split("\n", 1)
            no_ver[lang] = f"{build}\n{gg} --noVersioning"
        else:
            no_ver[lang] = HOST[lang] + " --noVersioning"

    standalone = {lang: HOST[lang] for lang in LANGS}
    with_key = {
        lang: f'export GC_PROJECT_KEY="dev:<jwt-from-portal>"\n{gg_command(lang)}'
        for lang in LANGS
    }

    body = f"""Hosted-module versioning is separate from the version on a generated consumer package. Gateway
decides whether each publication of a provider surface is versioned in the service model.

## Default behavior

After CLI and environment parsing:

- Without `--projectKey` or `GC_PROJECT_KEY`, Gateway runs in **standalone mode** and **disables
  versioning by default**.
- `--keepVersioning` (default `true`) can re-enable versioning even without a project key.
- `--noVersioning` **explicitly disables** versioning regardless of project key.

A [portal project key](project-key.md) ties publication to stable project metadata and is the normal
production path.

## When to bump consumer package versions

Bump the generated package version shown in Vision when the **callable surface** changes in a way
that affects consumers: renamed members, signature changes, removed types, or unsupported type
introduction. See [Update a Receiver contract](update-receiver-contract.md) and
[Contract evolution](../core-concepts/contract-evolution.md).

Additive methods are safer but are not guaranteed compatible in every target language. Always
regenerate, reinstall, and smoke-test each consumer ecosystem.

## When to use --noVersioning

Use `--noVersioning` for local experiments where you do not want Gateway to track module versions in
the service model, or when a deployment policy requires a single unversioned hosted surface.

Do not use it to avoid republishing after a **breaking** contract change. Consumers still depend on
the generated package version you install.

## Examples

Disable versioning:

{multi_fence(no_ver)}

Standalone mode without a project key (versioning off by default):

{multi_fence(standalone)}

Re-enable versioning in standalone mode (.NET example):

```bash
gg ./Pricing/bin/Debug/net9.0/Pricing.dll --keepVersioning
```

With a project key (store the key in a secret, not in source):

{multi_fence(with_key)}

## Verify

After startup, confirm discovery and publication in Gateway logs and Vision. If consumers install an
old package while the hosted surface changed, failures appear at invocation time—not as an automatic
drift rejection unless your deployment verifies versions.

**Gap:** automatic rejection of a changed UGM registered under the same version is not established in
the inspected implementation.

## Next steps

- [Use a project key](project-key.md)
- [Gateway CLI reference](../reference/gateway-cli.md)
- [Version compatibility and upgrades](../operations/version-compatibility-upgrades.md)
"""
    write_article(
        "gateway-no-versioning",
        body,
        title="Gateway module versioning and --noVersioning",
        description="Understand hosted-module versioning, when to bump package versions, and how to control versioning with Gateway flags.",
        articleTitle="Gateway module versioning and --noVersioning",
    )


def expose_code() -> None:
    body = f"""Turn an existing library or module into a provider without adding HTTP route handlers, controllers,
or transport types on the public surface.

## 1. Choose the public surface

Expose only intentional public classes and methods. Keep database clients, HTTP objects, streams,
framework models, and implementation helpers internal.

Use a plain module with a small synchronous or async-free public API (per runtime rules):

{multi_fence(CONTRACT)}

Use primitives and plain models. For cross-runtime contracts, represent dates and identifiers as
strings. The .NET package-generation path rejects framework complex types on the public surface.

## 2. Build the provider

{multi_fence(BUILD)}

## 3. Start Gateway with the real module

{multi_fence({lang: GG_START[lang] for lang in LANGS})}

Adjust paths and runtime versions to the project. Do not copy package IDs, registry URLs, or project
keys from examples.

## 4. Verify discovery

Check Gateway output and Graftcode Vision for the expected type and methods. Treat the discovered
surface as a review gate: remove accidental public members before consumers install a Graft.

**Gap:** there is no verified universal type matrix. Generate and smoke-test every producer/consumer
language pair that uses types beyond the portable baseline.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Obtain and install a Graft](obtain-install-graft.md)
- [Type compatibility matrix](../reference/type-matrix.md)
"""
    write_article(
        "expose-code",
        body,
        title="Expose code as a Graftcode provider",
        description="Prepare a small public contract and verify that Gateway discovers it.",
        articleTitle="Expose code as a Graftcode provider",
    )


def deploy_with_docker() -> None:
    other_cmd = {
        "javascript": 'CMD ["gg", "./dist/index.js"]',
        "python": 'CMD ["gg", "./pricing/"]',
        "java": 'CMD ["gg", "./target/pricing-1.0.0.jar"]',
        "php": 'CMD ["gg", "./src/"]',
        "ruby": 'CMD ["gg", "./lib/"]',
    }
    body = f"""Host Gateway in a container with your provider artifacts and the Linux `gg` package from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases).

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
CMD ["gg", "Provider.dll"]
```

```bash
docker build -t provider:test .
docker run -d -p 80:80 -p 81:81 -e GC_PROJECT_KEY="$GC_PROJECT_KEY" --name provider provider:test
```

## Other runtimes (illustrative)

Use a base image that includes your runtime, install `gg`, copy provider artifacts, and expose ports
`80` and `81`. Host locally first with [Run Gateway locally](run-gateway-locally.md), then
containerize the same `gg` command line.

{multi_fence(other_cmd)}

**Gap:** verified multi-stage Dockerfiles for every runtime are not maintained in this documentation
set.

## Next steps

- [Run Gateway locally](run-gateway-locally.md)
- [Use a project key](project-key.md)
- [Networking and ports](../operations/networking-ports.md)
"""
    write_article(
        "deploy-with-docker",
        body,
        title="Deploy Gateway with Docker",
        description="Build a provider and Gateway into a container.",
        articleTitle="Deploy Gateway with Docker",
    )


def main() -> None:
    project_key()
    obtain_install_graft()
    configure_invocation()
    coexist_with_rest()
    debug_graft_invocations()
    gateway_no_versioning()
    expose_code()
    deploy_with_docker()

    for slug in [
        "project-key",
        "obtain-install-graft",
        "configure-invocation",
        "coexist-with-rest",
        "debug-graft-invocations",
        "gateway-no-versioning",
        "expose-code",
        "deploy-with-docker",
    ]:
        remove_folder(slug)


if __name__ == "__main__":
    main()
