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

Start with [Support status](support-status.md) when selecting a runtime. Maintainers adding another
runtime should use the [language-guide template](template.md).

## One workflow, native APIs

1. Build a normal library or module. Public classes and methods form the contract.
2. Run Graftcode Gateway (`gg`) against the built module.
3. Confirm discovery in Gateway output or Graftcode Vision.
4. Select the consumer's package manager in Vision.
5. Copy the emitted installation command exactly. Registry identifiers and package coordinates are
   generated and can change; never construct them by hand.
6. Import the generated graft, set its remote host, and call it with the generated native API.

The guides distinguish evidence from recommendations. **Verified** means implementation or automated
test coverage was found in the inspected Graftcode source tree. **Gap** means the behavior was not
demonstrated by that evidence; Vision and the generated package remain authoritative.
