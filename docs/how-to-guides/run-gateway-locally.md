---
title: Run Gateway locally
description: >-
  Start Graftcode Gateway against a built module and verify discovery and
  publication.
articleTitle: Run Gateway locally
---
## 1. Install Gateway

**Graftcode Gateway** is the native host process; its CLI command is **`gg`** (`gg.exe` on Windows).

Download a release for your OS from
[Gateway releases](https://github.com/grft-dev/graftcode-gateway/releases) and put `gg` on your
`PATH`, or run it from the install directory.

| Platform | Typical asset |
| --- | --- |
| Linux (amd64) | `gg_linux_amd64.deb` — install with `dpkg -i`, or unpack the binary |
| Windows (amd64) | `gg_windows_amd64.msi` — install, then run `gg.exe` from the install location |
| Windows (arm64) | `gg_windows_arm64.msi` |

On Debian/Ubuntu you can also use the
[documented apt repository](https://github.com/grft-dev/graftcode-gateway/tree/main/packaging/apt-get)
(`sudo apt install gg` after adding the repo).

Verify the install:

```bash
gg --help
```

To host Gateway in a container without a local install, [build your own image](deploy-with-docker.md).
There is no official pre-built Gateway image to pull.

## 2. Build and host

```multi
```dotnet
dotnet build ./Pricing/Pricing.csproj
gg ./Pricing/bin/Debug/net9.0/Pricing.dll --types Pricing.PriceService --methods Calculate
```
```javascript
npm ci && npm run build
gg ./dist/index.js --types PriceService --methods calculate
```
```python
gg ./pricing/
```
```java
mvn package
gg ./target/pricing-1.0.0.jar
```
```php
composer install
gg ./src/
```
```ruby
bundle install
gg ./lib/
```
```

Use `gg.exe` on Windows. Pass the built module path explicitly when auto-scan would pick the wrong artifact.

## 3. Custom ports

```bash
gg <module> --port 8080 --httpPort 8081
```

## 4. Verify

Check logs for enabled types and successful publication, then open Vision.

## Next steps

- [Obtain and install a Graft](obtain-install-graft.md)
- [Gateway CLI](../reference/gateway-cli.md)
