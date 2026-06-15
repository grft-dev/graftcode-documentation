# Graftcode Context Libraries

Graftcode Context provides a standardized way to access request context (headers and metadata) during Graftcode invocations. The library is available for multiple platforms and programming languages.

## Overview

The `RequestContext` class provides a thread-safe (or context-aware) singleton that allows you to retrieve headers and custom metadata anywhere in your code during the request lifecycle.

> **Note:** Headers are automatically set by Graftcode Gateway server which hosts your code

This is essential for accessing authentication tokens, correlation IDs, tenant information, and other request-scoped data propagated through Graftcode service calls.

---

## Available Libraries

| Technology | Package Name | Package URL |
|------------|--------------|-------------|
| Node.js | `graftcode-context` | [npmjs.com/package/graftcode-context](https://www.npmjs.com/package/graftcode-context) |
| .NET | `Graftcode.Context` | [nuget.org/packages/Graftcode.Context](https://www.nuget.org/packages/Graftcode.Context) |
| Java | `com.graftcode:graftcode-context` | [central.sonatype.com/artifact/com.graftcode/graftcode-context](https://central.sonatype.com/artifact/com.graftcode/graftcode-context) |
| Python | `graftcode-context` | [pypi.org/project/graftcode-context](https://pypi.org/project/graftcode-context/) |
| PHP | `graftcode/graftcode-context` | [packagist.org/packages/graftcode/graftcode-context](https://packagist.org/packages/graftcode/graftcode-context) |
| Ruby | `graftcode-context` | [rubygems.org/gems/graftcode-context](https://rubygems.org/gems/graftcode-context) |

---

## Node.js / TypeScript

### Installation

```bash
npm install graftcode-context
```

**Requirements:** Node.js >= 22.0.0

### Usage

```typescript
import { RequestContext } from 'graftcode-context';

const headers = RequestContext.current.getHeaders();

const authToken = headers['Authorization'];
const correlationId = headers['X-Correlation-Id'];
const tenantId = headers['X-Tenant-Id'];
```

---

## .NET

### Installation

```bash
dotnet add package Graftcode.Context
```

Or via Package Manager Console:

```powershell
Install-Package Graftcode.Context
```

**Target Frameworks:** .NET Standard 2.1, .NET 8.0

### Usage

```csharp
using Graftcode.Context;

var headers = RequestContext.Current.GetHeaders();

var authToken = headers["Authorization"];
var correlationId = headers["X-Correlation-Id"];
var tenantId = headers["X-Tenant-Id"];
```

> **Note:** The `RequestContext.Current` property uses `[ThreadStatic]` attribute to ensure thread safety in multi-threaded applications.

---

## Java / JVM

### Installation (Maven)

Add to your `pom.xml`:

```xml
<dependency>
    <groupId>com.graftcode</groupId>
    <artifactId>graftcode-context</artifactId>
    <version>1.0.0</version>
</dependency>
```

### Installation (Gradle)

```groovy
implementation 'com.graftcode:graftcode-context:1.0.0'
```

**Requirements:** Java 8+

### Usage

```java
import com.graftcode.context.RequestContext;
import java.util.Map;

Map<String, String> headers = RequestContext.current().getHeaders();

String authToken = headers.get("Authorization");
String correlationId = headers.get("X-Correlation-Id");
String tenantId = headers.get("X-Tenant-Id");
```

> **Note:** The implementation uses `ThreadLocal` to ensure thread safety.

---

## Python

### Installation

```bash
pip install graftcode-context
```

**Requirements:** Python >= 3.9

### Usage

```python
from graftcode.context import RequestContext

headers = RequestContext.current().get_headers()

auth_token = headers.get('Authorization')
correlation_id = headers.get('X-Correlation-Id')
tenant_id = headers.get('X-Tenant-Id')
```

> **Note:** The Python implementation uses `contextvars.ContextVar` for async-safe context propagation, making it compatible with asyncio and other async frameworks.

---

## PHP

### Installation

```bash
composer require graftcode/graftcode-context
```

**Requirements:** PHP >= 7.4 or PHP >= 8.0

### Usage

```php
<?php

use Graftcode\Context\RequestContext;

$headers = RequestContext::current()->getHeaders();

$authToken = $headers['Authorization'] ?? null;
$correlationId = $headers['X-Correlation-Id'] ?? null;
$tenantId = $headers['X-Tenant-Id'] ?? null;
```

---

## Ruby

### Installation

Add to your `Gemfile`:

```ruby
gem 'graftcode-context'
```

Then run:

```bash
bundle install
```

Or install directly:

```bash
gem install graftcode-context
```

**Requirements:** Ruby >= 3.1.0

### Usage

```ruby
require 'graftcode/context'

headers = Graftcode::Context::RequestContext.current.get_headers

auth_token = headers['Authorization']
correlation_id = headers['X-Correlation-Id']
tenant_id = headers['X-Tenant-Id']
```
---