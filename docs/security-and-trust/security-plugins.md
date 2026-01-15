---
title: "Security plugins"
description: "Learn how Graftcode security plugins integrate with invocation intent, how authentication and transport plugins work, and how they enable side-car security and routing."
keywords: "graftcode plugins, security plugins, authentication plugins, transport plugins, iip interception"
---

# Security plugins

Security plugins are the mechanism through which authentication, authorization, and secure routing are applied in Graftcode.

They are deliberately designed as **runtime extensions**, not framework features.  
A plugin does not change how code is written. It changes **how invocation intent is handled** as it crosses runtime and network boundaries.

This makes security composable, inspectable, and independent from business logic.

---

## Plugins operate on invocation intent, not on code

At the core of Graftcode execution is the **Intention Invocation Protocol (IIP)**.

Every call—local or remote—is expressed as an invocation intent before it becomes a method call.  
Security plugins attach themselves **around this intent**, not around the method implementation itself.

This distinction is critical.

Plugins never:
- modify business logic
- intercept method execution mid-flight
- rewrite code paths

They only observe, enrich, validate, or reroute invocation intent *before execution begins*.

---

## Two categories of plugins

At a high level, Graftcode supports two categories of plugins:

- plugins that enrich or validate invocation intent  
- plugins that control how invocation intent is transported

Both operate at runtime and both are configured externally.

---

## Authentication and authorization plugins

Authentication plugins integrate at the point where invocation intent is about to leave one runtime or enter another.

On the caller side, a plugin can:
- inspect the target operation
- read execution context
- attach identity information to the IIP message

This identity can take any form required by the system: JWT tokens, API keys, signed claims, or custom credentials. Graftcode does not interpret these values—it merely transports them as part of the invocation context.

On the receiver side, the corresponding plugin:
- receives the IIP message
- extracts identity data
- validates it
- reconstructs identity claims

Only after this validation succeeds does execution continue.

If the plugin throws an authentication or authorization exception, execution stops immediately. No user code is executed and no side effects occur. Control returns to the caller with a native exception.

---

## Authorization as user-defined logic

Once identity has been validated, authorization decisions are made explicitly by user-defined logic.

Because plugins have access to:
- the method being invoked
- metadata about that method
- identity claims

authorization can be implemented in several ways:
- attributes or annotations on methods
- centralized authorization services
- policy-based evaluators

The plugin does not decide *what* is allowed.  
It provides the context in which the decision is made.

If authorization logic rejects the invocation, the plugin throws an exception and execution stops. If it does nothing, execution proceeds normally.

---

## JWT plugin as a concrete example (alpha version - to be evolved and change significantly)

The sample repository includes a working JWT plugin implemented in C#.

You will notice the `Javonet.*` namespaces in the code. That is a historical name used in the current plugin tooling and runtime packages. In Graftcode terminology, this is the same layer that today we refer to as **Hypertube™** and the plugin system around invocation intent.

What makes this example useful is that it shows the plugin model exactly where it matters: at the boundary where invocation intent is about to be sent, and right before it is executed on the receiving side.

On the caller side, the plugin runs just before Hypertube sends an invocation message. In the sample implementation, `JwtSendingPlugin` resolves a user-provided JWT implementation (`IJwtAuthorize`), loads plugin configuration, reads an ambient request context (stored with `AsyncLocal`), generates a token, and returns it as plugin payload:

```csharp
public IPluginPayload Execute()
{
    var jwtAuthorize = PluginImplementationRegistry
        .ResolvePluginTransientImplementation<IJwtAuthorize>();

    var config = PluginImplementationRegistry
        .GetPluginConfiguration<JwtGraftocodePluginSettings>();

    if (jwtAuthorize is null) throw new JwtPluginResolvingException($"Plugin not found: {nameof(IJwtAuthorize)}");

    if (config == null || string.IsNullOrWhiteSpace(config.Username) || string.IsNullOrWhiteSpace(config.SecretKey))
        throw new JwtPluginResolvingException($"Settings not found for: {nameof(IJwtAuthorize)}");

    PluginId = config.PluginId;

    JwtAuthContext? context = JwtPluginRequestContext.Current;

    var token = jwtAuthorize?.GenerateJwtToken(
        context?.UserId ?? string.Empty,
        context?.Role ?? string.Empty,
        config.SecretKey,
        context?.Parameters);

    return new { Token = token };
}
```

Two details in this snippet are worth calling out.

First, the plugin is not coupled to any HTTP construct. There are no headers and no web framework assumptions. The plugin participates at the intent level and simply returns a payload that will travel with the invocation.

Second, the user identity is taken from an ambient request context (JwtPluginRequestContext.Current), which is implemented using AsyncLocal. This mirrors how identity often flows through modern runtimes: the business code remains clean, while the context is carried along the execution path.

On the receiving side, JwtReceivingPlugin runs before the invocation is translated into a method call. It deserializes the plugin payload, extracts the token, validates it through IJwtAuthorize.Validate(...), and then performs authorization checks before execution is allowed to proceed:

```csharp
var pluginPayloadDict = JsonSerializer.Deserialize<Dictionary<string, object>>((string)commandPayload);

var pluginPayload = pluginPayloadDict?.GetValueOrDefault(PluginId)?.ToString() ?? string.Empty;

var token = JsonSerializer.Deserialize<TokenResponse>(pluginPayload)?.Token ?? string.Empty;

var (username, role) = jwtAuthorize.Validate(token);

var className = pluginPayloadDict?.GetValueOrDefault("className")?.ToString() ?? string.Empty;
var methodName = pluginPayloadDict?.GetValueOrDefault("methodName")?.ToString() ?? string.Empty;

if (string.IsNullOrWhiteSpace(username)
    || string.IsNullOrWhiteSpace(role))
    throw new JwtPluginValidationException($"Jwt Plugin authorization for token: {token}");

CheckAttributes(className, methodName, role, out string? reason);

if (!string.IsNullOrWhiteSpace(reason))
    throw new JwtAttributeException(reason);

return new AuthContext(username, role);
```

This is the enforcement point that matters for security reviews: if the plugin throws, the call is rejected before any business logic runs. There is no partial execution and no “best effort” behavior.

The example also demonstrates one practical authorization strategy: attribute-based access rules on methods. The receiving plugin reflects the target method and checks a JwtAuthorizeAttribute before allowing execution. The relevant part of CheckAttributes(...) looks like this:

```csharp
var authAttr = method.GetCustomAttribute<JwtAuthorizeAttribute>();

// TODO: add config switch: when user wants to restrict all methods and attribute is necessary
if (authAttr == null && !strictMode)
    return;

if (string.Equals(authAttr.Role, role, StringComparison.OrdinalIgnoreCase)
    || authAttr.Roles.Contains(role, StringComparer.OrdinalIgnoreCase))
{
    return;
}

reason = $"{authAttr.Reason} Required role: '{authAttr.Role}', but received: '{role ?? "none"}'.";
```
This is intentionally transparent. Graftcode does not define what “authorized” means. It gives the plugin the method identity and the claims context, and your code decides.

That transparency is what enables a side-car security model: teams can add authentication and authorization later, purely through configuration, by attaching a sending plugin that injects credentials and a receiving plugin that validates and authorizes them—without changing business logic or the public interface.

---

## Transport plugins and routing control

The second category of plugins operates at the transport layer.

Instead of enriching invocation intent, these plugins decide **how the intent is delivered**.

A transport plugin can:
- replace direct TCP/IP or WebSocket delivery
- route invocation intent through a message broker
- enqueue requests
- publish them to topics
- apply buffering, retries, or transactional guarantees

From the application’s point of view, nothing changes.  
The same method call produces the same invocation intent.

The only difference is **where and how that intent is delivered**.

---

## Execution remains unchanged

Even when transport plugins are used, execution semantics do not change.

On the receiving side:
- invocation intent arrives
- identity is validated
- authorization is enforced
- business logic executes normally

Results and exceptions are returned through the configured return channel.

Transport plugins change routing, not execution.

---

## Composability and late binding

One of the most important properties of the plugin system is that plugins can be added **after the fact**.

A system can start:
- fully in memory
- without authentication
- without transport indirection

As architecture evolves, plugins can be introduced purely through configuration:
- to add authentication between services
- to introduce secure routing
- to integrate with external infrastructure

No integration code needs to be rewritten.

---

## Transparency and auditability

Plugins run inside the same environment as the Gateway and Hypertube.

They are:
- visible
- inspectable
- auditable

This allows teams to:
- review security behavior
- perform penetration testing
- reason about failure modes

There is no hidden execution path.

---

## Source availability and extensibility

Security plugins are designed to be:
- open
- extensible
- community-contributed

Teams can:
- use provided plugins
- customize them
- write their own

The plugin system is intentionally minimal so that behavior remains understandable and controllable.

---

## Closing perspective

Security plugins are not an abstraction layer on top of Graftcode.

They are **hooks into the execution pipeline**, allowing identity and routing concerns to be handled exactly where they belong—at the boundary between intent and execution.

This enables secure systems to evolve naturally, without forcing security decisions into business code or freezing architectural choices too early.
