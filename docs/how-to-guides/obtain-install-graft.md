---
title: "Obtain and install a Graft"
description: "Use Gateway or Vision output to install the generated package without guessing registry details."
articleTitle: "Obtain and install a Graft"
---
## 1. Wait for publication

Start Gateway against the built provider and wait for successful model upload in logs or Vision.

## 2. Open Vision

Default HTTP port is `81` (`http://localhost:81/GV` in local Docker workflows).

## 3. Copy the install command

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

## 4. Verify exports

Inspect generated namespaces, imports, and method names in the installed package.

## Next steps

- [Configure invocation](configure-invocation.md)
- [Generated package structure](../reference/generated-package-structure.md)

## Source anchors

- `graftcode-package-manager-gateway/`
