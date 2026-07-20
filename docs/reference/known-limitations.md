---
title: "Known limitations"
description: "Canonical link and operational summary for current Graftcode Alpha constraints."
---

# Known limitations

The maintained limitations page is:

- [Alpha limitations and known constraints](../how-graftcode-works/alpha-limitations-and-known-constraints.md)

Before production use, review at least:

- simple public-contract type restrictions;
- .NET synchronous public method requirement;
- unsupported framework wrappers such as date and GUID types;
- stateful remote-object affinity and restart behavior;
- no cross-major backward-compatibility guarantee;
- current package dependency gaps;
- explicit authentication/authorization responsibility;
- portal and collaboration limitations.

Where the limitations page conflicts with generated output or a tested current Gateway release,
record the release and treat the generated package plus reproducible test as the operational source
of truth. Do not silently broaden support claims.

## Next steps

- [Type matrix](type-matrix.md)
- [Version compatibility and upgrades](../operations/version-compatibility-upgrades.md)
- [Errors and status](errors-status.md)

## Source anchors

- [Alpha limitations and known constraints](../how-graftcode-works/alpha-limitations-and-known-constraints.md)
- `graftcode-gateway/README.md`
- `graftcode-e2e-tests/src/nodejs/grafting-agent-e2e-tests/tests/`
