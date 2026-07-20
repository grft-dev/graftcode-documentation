---
title: "Generated package structure"
description: "Stable responsibilities and intentionally variable details in generated Graft packages."
---

# Generated package structure

A generated Graft package contains consumer-side code, not the provider implementation.

## Verified responsibilities

- generated classes/models matching the accepted UGM surface;
- generated method wrappers that invoke Hypertube;
- `GraftConfig` and its generated defaults;
- target package metadata;
- target runtime dependencies or references;
- declarations/types required by the consumer ecosystem.

Every generated consumer package includes a `GraftConfig` (or equivalent) type. Field naming follows
the target language—PascalCase static fields in .NET, lower-case fields in Node.js, class attributes in
Python, and analogous patterns elsewhere. Copy the exact shape from Vision.

```multi
```dotnet
GraftConfig.Host = "inmemory";
GraftConfig.Stateless = false;
```
```javascript
GraftConfig.host = "inmemory";
GraftConfig.stateless = false;
```
```python
GraftConfig.host = "inmemory"
GraftConfig.stateless = False
```
```java
GraftConfig.host = "inmemory";
GraftConfig.stateless = false;
```
```php
GraftConfig::$host = 'inmemory';
GraftConfig::$stateless = false;
```
```ruby
GraftConfig.host = "inmemory"
GraftConfig.stateless = false
```
```

## Not stable enough to infer

- package name and scope;
- registry/feed/repository URL;
- package version;
- generated namespace/import path;
- source-to-target method casing;
- exact file layout;
- whether runtime dependencies are transitive in the current Alpha.

Read these values from current Gateway/Vision output and the installed artifact. Do not edit generated
files as the source of truth; change the provider contract or generator and regenerate.

Normal runtime calls do not regenerate the package. They use installed wrappers and resolved
configuration to invoke the provider.

**Gap:** this reference describes responsibilities shared by inspected generators, not an ABI or file
layout guarantee across releases.

## Next steps

- [Obtain and install a Graft](../how-to-guides/obtain-install-graft.md)
- [Update a provider contract](../how-to-guides/update-provider-contract.md)
