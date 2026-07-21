---
title: "Obtain and install a Graft"
description: "Install a public Graft from the Graftcode registry or copy the install command from your own Gateway."
articleTitle: "Obtain and install a Graft"
---

A **Graft** is a generated consumer package. You do not write it by hand—you install it with your
normal package manager. There are two common paths.

## Install a public Graft

Grafts published to the **public Graftcode registry** can be installed without running your own
Gateway or copying coordinates from Vision. Point your package manager at the public feed and install
the documented package name and version.

| Consumer ecosystem | Public registry URL |
| --- | --- |
| npm / NuGet / Composer / RubyGems | `https://grft.dev/` |
| Maven / Gradle | `https://grft.dev/maven2/` |
| pip | `https://grft.dev/simple/` |

Maintained cross-runtime **sample** packages (useful for smoke-testing installs):

| Package | Versions used in tests |
| --- | --- |
| `grft-test-simple-car-e2e` | `0.2.1` (npm, NuGet, Maven), `0.2.3` (PyPI), `0.2.4` (Composer graft package) |
| `grft-test-simple-car-repository-e2e` | `0.2.1`–`0.2.2` (see [support status](../language-guides/support-status.md)) |

Example install commands (production registry):

```multi
```dotnet
dotnet add package graft.nuget.grft-test-simple-car-e2e --version 0.2.1 -s https://grft.dev/
```
```javascript
npm install @graft/npm-grft-test-simple-car-e2e@0.2.1 --registry https://grft.dev/
```
```python
python -m pip install graft-pypi-grft-test-simple-car-e2e==0.2.3 --extra-index-url https://grft.dev/simple/
```
```java
# Maven — groupId com.graftcode, artifactId grft-test-simple-car-e2e, version 0.2.1,
# repository https://grft.dev/maven2/
```
```php
composer require graft-packagist-sdn/test-simple-car:0.2.4 --repository '{"type":"composer","url":"https://grft.dev/"}'
```
```ruby
gem install graft-rubygems-sdn_test_simple_car -v 0.2.2 --source https://grft.dev/
```
```

Exact scopes, artifact IDs, and import paths come from the installed package and its generated
`GraftConfig`. After install, configure invocation per
[Configure invocation](configure-invocation.md)—remote Grafts need a WebSocket host; some public
packages default to in-memory execution when the provider module ships inside the package.

Source for the sample provider: [grft-test-simple-car](https://github.com/grft-dev/grft-test-simple-car).

## Install from your own Gateway

When **you** expose a module, Gateway publishes a **private** (per-Gateway) registry identifier.
Install coordinates change when Gateway restarts without a [project key](project-key.md).

### 1. Wait for publication

Start Gateway against the built provider and wait for successful model upload in logs or Vision.
Install Gateway first if needed: [Run Gateway locally](run-gateway-locally.md).

### 2. Open Vision

Default HTTP port is `81`. When Gateway runs in a container, map host port `81` to reach Vision
(for example `http://localhost:81/GV`). See [Deploy with Docker](deploy-with-docker.md).

### 3. Copy the install command

For your runtime, copy the **complete** command from Vision, including registry, package name, and
version.

```multi
```dotnet
dotnet add package <package-id> --version <version> -s <registry-from-vision>
```
```javascript
npm install <package> --registry <registry-from-vision>
```
```python
python -m pip install <package> --extra-index-url <url-from-vision>
```
```java
# Copy the Maven dependency block from Vision
```
```php
composer require <vendor/package>:<version> --repository <repo-from-vision>
```
```ruby
gem install <name> --source <source-from-vision>
```
```

Never derive registry URLs from the provider assembly or module name. Use a [project key](project-key.md)
when stable publication identity is required.

### 4. Verify exports

Inspect generated namespaces, imports, and method names in the installed package.

## Next steps

- [Configure invocation](configure-invocation.md)
- [Generated package structure](../reference/generated-package-structure.md)
