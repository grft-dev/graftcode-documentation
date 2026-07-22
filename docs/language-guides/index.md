---
title: "Language Guides"
description: "Build and consume Graftcode modules from supported application runtimes."
---

# Language guides

Choose the runtime in which you write or consume application code:

- [.NET](dotnet.md)
- [Node.js and TypeScript](nodejs-typescript.md)
- [Java and JVM](java-jvm.md)
- [Python](python.md)
- [PHP](php.md)
- [Ruby](ruby.md)

Start with [Support status](support-status.md) when selecting a runtime.

## One workflow, native APIs

1. Build a normal library or module. Public classes and methods form the contract.
2. Run Graftcode Gateway (`gg`) against the built module.
3. Confirm discovery in Gateway output or Graftcode Vision.
4. Select the consumer's package manager in Vision.
5. Copy the emitted installation command exactly. Registry identifiers and package coordinates are
   generated and can change; never construct them by hand.
6. Import the generated graft, set its remote host, and call it with the generated native API.

The guides distinguish what is supported from what is not. **Verified** means the behavior is
supported and covered by automated tests. **Gap** means it is not yet guaranteed; Vision and the
generated package remain authoritative.
