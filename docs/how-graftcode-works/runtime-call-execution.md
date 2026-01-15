---
title: "Runtime call execution"
description: "Learn how method calls are executed at runtime in Graftcode, how invocation intent is processed, and how results, errors, and callbacks propagate across runtimes."
keywords: "graftcode runtime execution, method invocation, hypertube execution, distributed calls, strongly typed execution"
---
 
At its core, Graftcode is about executing **method calls**, not sending messages.
 
When a developer invokes a method on a Graft, they are expressing **programming intent**:
- call this method
- with these arguments
- and return a result or raise an error
 
This section explains how that intent is executed at runtime.
 
---
 
## From method call to execution
 
From the caller's point of view, a call looks completely ordinary:
 
- a method is invoked
- arguments are passed
- a result is returned
- or an exception is thrown
 
There is no explicit networking code, no serialization logic, and no protocol handling visible in application code.
 
Internally, however, the call follows a well-defined execution path.
 
---
 
## Capturing invocation intent
 
When a method on a Graft is invoked, the generated client does not execute business logic itself.
 
Instead, it:
- captures the invocation intent
- identifies the target method and arguments
- packages this intent into a binary runtime message
 
This message represents *what should be executed*, not *how* it should be transported.
 
---
 
## Intention Invocation Protocol (IIP)
 
Invocation intent is expressed using the **Intention Invocation Protocol (IIP)**.
 
IIP is a binary protocol designed to represent:
- method invocations
- argument values
- execution flow
- expected results
 
Unlike traditional RPC protocols, IIP does not model endpoints or payloads.  
It models **programming operations**.
 
The same protocol is used regardless of where execution happens.
 
---
 
## Dispatching the call
 
Once the invocation intent is created, it is passed to the **local Hypertube™**.
 
At this point, no decision has yet been made about *where* the call will execute.
The local Hypertube is responsible for deciding **how and where the invocation should be routed**.
 
This decision is made entirely on the caller side, based on Graft configuration.
 
---
 
## Configuration-driven routing
 
Hypertube determines the execution path using the **Graft Connection String** configuration.
 
This configuration can be provided in several ways, with a clear precedence order:
 
- **No configuration provided**  
  → the call is executed in memory by default
 
- **Configuration set in code**  
  → the last configured Graft Connection String is used
 
- **Configuration provided via a configuration file**  
  → overrides anything set in code
 
- **Configuration provided via environment variables**  
  → overrides both code and configuration files
 
This allows configuration to evolve naturally from development to production without changing application code.
 
---
 
## Global and per-Graft configuration
 
The Graft Connection String can be defined:
- globally, for all Grafts
- or per individual Graft
 
This makes it possible to:
- keep some calls local
- route others remotely
- and evolve architecture incrementally
 
Each Graft can be routed independently.
 
The purpose of this section is to describe how Graftcode and Hypertube cooperate to pass, store, and resolve runtime configurations.
 
The configuration system is designed to:
 
- support multiple runtimes,
- allow independent routing of individual Grafts,
- enable incremental architectural evolution,
- avoid central, monolithic configuration files.
 
### Definitions
 
#### Name
 
**Name** is a unique key within the user's application that corresponds to a single Graft.
 
- The value of Name is defined by the Graft itself (for example: `graft.nuget.sdncalculatorsimple`).
- It is later used by Hypertube to select the appropriate configuration when a runtime context is created.
 
#### Config
 
**Config** represents a complete definition required to start a runtime context inside Hypertube.
 
It is a class defined in Hypertube and contains the following logical fields:
 
- Runtime
- ConnectionData
- Modules (optional)
- Plugins (optional)
 
#### ConfigPriority
 
**ConfigPriority** defines the precedence order of configurations.
 
When multiple configurations with the same Name exist, the one with the highest priority is selected.
 
Priority order from highest to lowest:
 
1. RuntimeSpecificEnv
2. GlobalEnv
3. RuntimeSpecificFile
4. GlobalFile
5. User
6. DefaultLibrary
 
#### ConfigurationsCollection
 
**ConfigurationsCollection** is an internal structure inside Hypertube that stores all configurations added by all Grafts in the application.
 
Characteristics:
 
- configurations are grouped by Name
- then grouped by ConfigPriority
- existing configurations are never overridden
 
### Global Graft Connection String
 
A global Graft Connection String defines the default runtime connectivity for the entire application.
 
It applies to all Grafts unless explicitly overridden by a per-Graft configuration.
 
#### Naming of Global Configuration
 
Global configuration is not associated with any specific Graft.
 
As a consequence:
 
- it does not use a Graft name as its Name
- it does not directly represent a single runtime context
- it acts as a shared baseline configuration
 
From Hypertube's perspective:
 
- global configurations are stored in the internal configuration collection
- they may define one or more configuration entries
- they are not directly selected when initializing a runtime context for a specific Graft
 
Global configuration defines the environment, not the Graft.
 
#### Purpose of Global Configuration
 
Global configuration is intended for:
 
- defining a common Hypertube endpoint for the whole application
- running all Grafts locally (for example in-memory) during development
- switching environments such as local, staging, and production
- avoiding repetitive configuration for every individual Graft
 
### Per-Graft Graft Connection String
 
A per-Graft Graft Connection String defines runtime connectivity for a single Graft and always has higher priority than global configuration.
 
#### Naming of Per-Graft Configuration
 
Each per-Graft configuration must use the Graft's name as its Name.
 
- The Name value must be exactly equal to the `graftName` defined by the Graft.
- This Name is later used when a runtime context is requested for that Graft.
 
#### Global vs Per-Graft Resolution Rules
 
Configuration resolution follows strict and predictable rules:
 
- each Graft is resolved independently
- per-Graft configuration always overrides global configuration
- global configuration is never selected if a per-Graft configuration exists
- configuration priority is resolved only within the same Name
 
This enables mixed execution models inside a single application.
 
Example scenarios:
 
- most Grafts running locally in-process
- selected Grafts routed to a remote Hypertube instance
- gradual migration from monolithic to distributed architecture
- isolated testing or rollout of a single Graft
 
### How Grafts Provide Configurations
 
Each Graft attempts to register configuration data during startup from multiple sources, including environment variables, files, and user-provided values.
 
Each Graft defines:
 
- its unique `graftName`
- runtime identity
- default module or artifact
- default host or execution target
 
Configurations are registered with different priorities and accumulated inside Hypertube.
 
#### Configuration Sources
 
Configuration may be supplied from:
 
- environment variables
- files
- plain text
 
Each source may contain one or more configurations.
 
Details of configuration formats are described in a separate document.
 
#### Configuration Load Order
 
At startup, each Graft attempts to add configuration data in the following order, from highest to lowest priority:
 
1. Graft-specific environment configuration
2. Global environment configuration
3. Graft-specific configuration file
4. Global configuration file
5. Configuration provided explicitly by the user in application code
6. Default configuration embedded in the Graft
 
Previously registered configurations are never overridden.
 
### Runtime Context Initialization
 
When a Graft is used for the first time, Hypertube initializes a runtime context for that Graft by selecting the configuration with:
 
- a matching Name
- the highest available priority
 
#### Internal Hypertube Behavior
 
When a configuration is added:
 
- the source is resolved
- its format is detected
- all configurations contained in the source are parsed
- configurations are added to the internal collection
 
When a runtime context is initialized:
 
- configurations are filtered by Name
- the highest-priority configuration is selected
- a RuntimeContext is created and returned
 
### Open Questions / To Be Implemented
 
- standard locations for configuration files
- logging and diagnostics
- user-visible exceptions for invalid configuration
 
---
 
## Deciding where the call goes
 
Based on the resolved configuration, the local Hypertube may route the call in several ways:
 
- **Within the same runtime**  
  Used when a Graft represents a module that is currently co-located and planned for extraction later.
 
- **To another runtime within the same process**  
  Used for polyglot scenarios where multiple runtimes are hosted side by side.
 
- **Over the network**  
  Sent via TCP/IP or WebSocket to a remote Hypertube hosted inside a Graftcode Gateway.
 
- **Through a transport plugin**  
  Routed via a configured channel such as a PaaS messaging or transport system, if a plugin is enabled.
 
In all cases, the invocation intent itself remains unchanged.
 
---
 
## Arriving at the receiver
 
Once routed, the invocation reaches:
- a Hypertube instance in another runtime within the same process,
- the same Hypertube instance (in-memory execution),
- or a remote Hypertube hosted inside a Graftcode Gateway.
 
From this point on, execution proceeds as described in the next section:  
**Executing business logic**.
 
---
 
## Executing business logic
 
Actual execution of business logic is performed by **Hypertube™**, not by the Graftcode Gateway itself.
 
The Gateway's role is to **host Hypertube and load runtimes**.  
Hypertube is the component that:
- dispatches invocation intent
- executes methods
- manages execution context
- propagates results, errors, and callbacks
 
This distinction is important, because execution semantics are identical regardless of whether a Gateway is present.
 
---
 
### Hypertube as the execution engine
 
Hypertube is responsible for executing calls inside the target runtime.
 
When an invocation arrives:
- Hypertube validates it against the Unified Graft Model
- resolves the target method
- executes it inside the appropriate runtime
- captures the result or exception
 
From the runtime's perspective, this is a normal method call.
 
There is no special execution sandbox, no artificial constraints, and no altered semantics.
 
---
 
### With or without a Gateway
 
The same execution model applies in all scenarios:
 
- **In-memory execution**  
  Hypertube runs inside a single process, loads runtimes directly, and executes calls without any network involvement.  
  No Graftcode Gateway process is required.
 
- **Local or remote execution with a Gateway**  
  Hypertube runs inside a Graftcode Gateway process, loads runtimes there, and executes calls received over TCP/IP or WebSocket.
 
In both cases:
- the same Hypertube code runs
- the same invocation model is used
- the same execution semantics apply
 
The presence of a Gateway does not change how business logic is executed—it only changes where Hypertube is hosted.
 
---
 
### Execution context and lifecycle
 
During execution, Hypertube:
- maintains execution context
- preserves call stacks where applicable
- manages object lifecycles for stateful interactions
- handles event subscriptions and callbacks
 
This allows long-lived, duplex interactions to behave consistently, regardless of deployment topology.
 
---
 
### Results and exceptions
 
After execution:
- return values are captured by Hypertube
- structured results are materialized
- exceptions are intercepted and propagated
 
On the caller side:
- results are reconstructed as native types
- exceptions are re-thrown as native exceptions
 
Error handling remains idiomatic and language-appropriate.
 
---
 
### Why this matters
 
By centralizing execution in Hypertube:
- execution behavior is consistent everywhere
- in-memory and remote execution behave the same
- architectural decisions do not leak into business code
 
This is what allows Graftcode to virtualize locality without virtualizing semantics.
 
---
 
### In short
 
Business logic is executed by **Hypertube™**.
 
The Graftcode Gateway:
- hosts Hypertube
- loads runtimes
- exposes interfaces
 
Whether execution happens:
- in memory
- in the same process
- or on a remote node
 
the same Hypertube engine performs the work.
 
---
 
## Threading and execution model
 
Threading is one of the most common concerns when execution crosses runtime boundaries.
 
Graftcode is designed so that the **threading model remains intuitive and predictable**, closely matching what developers already expect from in-process execution.
 
Hypertube takes responsibility for managing threads and execution contexts automatically.
 
---
 
### In-memory execution
 
In in-memory scenarios, execution behaves as if everything were running inside a single application.
 
For each thread on the caller side:
- Hypertube automatically creates a corresponding execution thread on the receiver side
- the lifetime of the receiver thread is tied to the caller thread
- execution context is preserved across runtime boundaries
 
This means that:
- thread-local state behaves as expected
- standard synchronization primitives work normally
- locking, monitors, and concurrency controls apply naturally
 
From the developer's perspective, this behaves like calling into another module—even if that module runs in a different runtime.
 
---
 
### Stateful remote execution
 
For **stateful remote calls**, the threading model is intentionally the same as in-memory execution.
 
When a stateful session is established:
- a logical execution context is created
- calls within that session are consistently routed
- the receiver-side thread lifecycle follows the caller-side lifecycle
 
This ensures that:
- object state is preserved
- callbacks and events execute in the expected context
- concurrency rules remain consistent
 
Stateful remote execution behaves like a distributed extension of in-memory execution.
 
---
 
### Stateless remote execution
 
For **stateless calls**, the model matches what developers already know from traditional request-based systems.
 
In this case:
- each invocation is handled independently
- a new execution thread is created per request
- the thread exists only for the duration of the call
 
This is equivalent to how REST-style request processing typically works, but without exposing transport or protocol concerns to application code.
 
---
 
### Concurrency and safety
 
Hypertube manages concurrency explicitly so that:
- access to shared state is protected
- standard locking mechanisms prevent concurrent access to the same value
- deadlock prevention and execution ordering are handled consistently
 
Because execution semantics remain aligned with the runtime's native threading model, developers can rely on:
- existing concurrency patterns
- familiar synchronization primitives
- proven debugging techniques
 
No special concurrency model needs to be learned.
 
---
 
### Why this matters
 
By preserving intuitive threading behavior:
- local and remote execution feel the same
- concurrency bugs are easier to reason about
- existing mental models remain valid
 
Developers do not need to redesign their code to "fit" distributed execution.
 
Hypertube adapts execution to distribution—not the other way around.
 
---
 
### In short
 
Hypertube manages threading automatically:
 
- in-memory calls mirror local execution
- stateful remote calls preserve execution context
- stateless calls use a request-per-thread model
- standard concurrency mechanisms work out of the box
 
This allows developers to think in terms of code, not threads across machines.
 
---
 
## Returning results
 
When execution completes:
- return values are captured
- structured results are materialized
- execution context is preserved
 
The result is sent back through Hypertube using the same IIP-based mechanism.
 
On the caller side:
- the result is reconstructed
- native types are restored
- control returns to application code
 
The call completes exactly as if it were local.
 
---
 
## Error handling and exceptions
 
Graftcode does not use status codes to represent errors.
 
If a method throws an exception:
- the exception is captured
- error information is propagated
- the exception is re-thrown on the caller side
 
Exceptions are mapped to the native exception type of the caller's runtime.
 
For custom business exceptions:
- the exception type is preserved conceptually
- the generated client maps it to an equivalent exception hierarchy
- error handling remains idiomatic
 
From application code, errors are handled using normal `try/catch` patterns.
 
---
 
## Synchronous and asynchronous execution
 
Execution semantics are defined by the public interface.
 
If a method is:
- synchronous → the caller blocks until completion
- asynchronous → the caller receives a promise, task, or future
 
Hypertube virtualizes execution so that:
- synchronous calls can run over asynchronous channels
- asynchronous calls can run over stateful connections
 
The chosen transport does not leak into application code.
 
---
 
## Callbacks, delegates, and events
 
Graftcode supports bidirectional execution.
 
If a public interface:
- accepts a callback
- exposes events
- allows subscription
 
Hypertube establishes a session that supports **reverse invocation**.
 
When the receiver:
- raises an event
- invokes a delegate
- calls back into the caller
 
The invocation travels back through the same runtime session.
 
From both sides, this still appears as normal method invocation.
 
---
 
## Execution context and call chains
 
A single invocation may trigger:
- nested method calls
- chained operations
- callbacks and event handlers
 
IIP supports representing such execution graphs explicitly.
 
This allows complex execution flows to be carried across runtimes without flattening them into request–response exchanges.
 
---
 
## What runtime call execution is not
 
Runtime execution in Graftcode:
- is not message passing
- is not endpoint-based
- is not tied to HTTP semantics
- does not require manual serialization
 
It is a continuation of normal programming semantics across runtime boundaries.
 
---
 
## In short
 
At runtime, Graftcode:
- captures method invocation intent
- executes it in the target runtime
- propagates results and errors natively
- preserves synchronous, asynchronous, and bidirectional semantics
 
From the developer's perspective, code behaves the same—regardless of where it runs.
 
---
 
Next, we'll look at **where execution happens**, and how the same execution model applies to **local, remote, and in-memory** scenarios.
