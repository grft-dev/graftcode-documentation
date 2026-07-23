#!/usr/bin/env python3
"""Regenerate documentation SVG diagrams in blueprint visual style."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams"

BG = "#0B1B2E"
FG = "#FFFFFF"
MUTED = "#9BB0C4"
STROKE = 1.6


def wrap(title: str, desc: str, body: str, width: int, height: int) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0 0 L8 4 L0 8 Z" fill="{FG}"/>
    </marker>
    <marker id="arrowMuted" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0 0 L8 4 L0 8 Z" fill="{MUTED}"/>
    </marker>
  </defs>
  <rect width="{width}" height="{height}" fill="{BG}"/>
  <style>
    .title {{ font: 700 22px Georgia, "Times New Roman", serif; fill: {FG}; letter-spacing: 0.04em; }}
    .h {{ font: 600 15px Consolas, "Courier New", monospace; fill: {FG}; }}
    .small {{ font: 12px Consolas, "Courier New", monospace; fill: {MUTED}; }}
    .cap {{ font: 700 11px Consolas, "Courier New", monospace; fill: {MUTED}; letter-spacing: 0.08em; }}
    .mono {{ font: 600 13px Consolas, "Courier New", monospace; fill: {FG}; }}
    .edge {{ font: 11px Consolas, "Courier New", monospace; fill: {MUTED}; }}
    .box {{ fill: none; stroke: {FG}; stroke-width: {STROKE}; }}
    .boxMuted {{ fill: none; stroke: {MUTED}; stroke-width: 1.2; stroke-dasharray: 5 4; }}
    .flow {{ fill: none; stroke: {FG}; stroke-width: {STROKE}; marker-end: url(#arrow); }}
    .flowMuted {{ fill: none; stroke: {MUTED}; stroke-width: 1.4; stroke-dasharray: 6 5; marker-end: url(#arrowMuted); }}
    .track {{ fill: none; stroke: {MUTED}; stroke-width: 2; }}
  </style>
  {body}
</svg>
"""


def rounded_box(x: float, y: float, w: float, h: float, rx: float = 12) -> str:
    return f'<rect class="box" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'


def label(x: float, y: float, text: str, cls: str = "h", anchor: str = "middle") -> str:
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>'


def arrow(x1: float, y1: float, x2: float, y2: float, muted: bool = False) -> str:
    cls = "flowMuted" if muted else "flow"
    return f'<path class="{cls}" d="M{x1} {y1} H{x2}"/>' if y1 == y2 else f'<path class="{cls}" d="M{x1} {y1} V{y2}"/>'


def generated_vs_written() -> str:
    body = """
  <text class="title" x="380" y="34" text-anchor="middle">Generated vs user-written</text>
  """ + rounded_box(36, 70, 200, 96) + label(136, 108, "Receiver service") + label(136, 128, "USER-WRITTEN", "cap") + """
  """ + rounded_box(280, 70, 200, 96) + label(380, 104, "Graft package") + label(380, 124, "GENERATED", "cap") + label(380, 144, "wrappers + GraftConfig", "small") + """
  """ + rounded_box(524, 70, 200, 96) + label(624, 108, "Caller service") + label(624, 128, "USER-WRITTEN", "cap") + """
  <path class="flow" d="M236 118 H280"/><path class="flow" d="M480 118 H524"/>
  """ + rounded_box(280, 196, 200, 58) + label(380, 222, "GraftConfig", "h") + label(380, 240, "user-controlled", "small") + """
  <path class="flowMuted" d="M380 166 V196"/>
"""
    return wrap(
        "Generated and user-written boundaries",
        "User-written Receiver and Caller services connect through a generated Graft package; deployment configuration stays user-controlled.",
        body,
        760,
        280,
    )


def one_picture_overview() -> str:
    body = """
  <text class="title" x="390" y="34" text-anchor="middle">One-picture overview</text>
  """ + rounded_box(30, 64, 140, 72) + label(100, 96, "Receiver") + label(100, 116, "USER-WRITTEN", "cap") + """
  """ + rounded_box(200, 64, 150, 72) + label(275, 96, "Callable surface") + label(275, 116, "analyzed", "small") + """
  """ + rounded_box(380, 64, 150, 72) + label(455, 96, "Graft") + label(455, 116, "GENERATED", "cap") + """
  """ + rounded_box(560, 64, 140, 72) + label(630, 96, "Caller") + label(630, 116, "USER-WRITTEN", "cap") + """
  <path class="flow" d="M170 100 H200"/><path class="flow" d="M350 100 H380"/><path class="flow" d="M530 100 H560"/>
  """ + rounded_box(380, 170, 150, 58) + label(455, 198, "GraftConfig.host", "h") + label(455, 216, "inmemory or ws/wss", "small") + """
  <path class="flow" d="M455 136 V170"/>
  """ + rounded_box(150, 250, 190, 44) + label(245, 276, "In-memory execution") + rounded_box(470, 250, 200, 44) + label(570, 276, "Remote via Gateway") + """
  <path class="flow" d="M420 228 L245 250"/><path class="flow" d="M490 228 L570 250"/>
"""
    return wrap(
        "Graftcode one-picture overview",
        "A user-written Receiver is analyzed into callable-surface metadata, a generated Graft is installed by the Caller, and GraftConfig selects in-memory or Gateway-hosted execution.",
        body,
        780,
        320,
    )


def graftcode_mental_model() -> str:
    cards = [
        (44, "1", "Your module", ["ordinary class", "or package"], "YOU WRITE"),
        (248, "2", "Generated Graft", ["typed package for", "the Caller"], "GENERATED"),
        (452, "3", "Gateway or", ["host module or install", "from public repository"], "OPERATED"),
        (656, "4", "Monolith or", ["in-memory or", "remote host"], "CONFIG"),
        (860, "5", "Still distributed", ["failures, security,", "retries apply"], "OPERATED"),
    ]
    parts = ['<text class="title" x="540" y="34" text-anchor="middle">Five things to remember</text>']
    for x, num, title, lines, cap in cards:
        parts.append(rounded_box(x, 68, 176, 148))
        parts.append(label(x + 88, 104, num, "mono"))
        parts.append(label(x + 88, 132, title))
        parts.append(label(x + 88, 154, lines[0], "small"))
        parts.append(label(x + 88, 170, lines[1], "small"))
        parts.append(label(x + 88, 198, cap, "cap"))
    for x in (220, 424, 628, 832):
        parts.append(f'<path class="flow" d="M{x} 142 H{x + 24}"/>')
    return wrap(
        "The Graftcode mental model in five steps",
        "Your module is user-written; the Graft is generated; you host with Gateway or install from the public repository; configuration selects monolith or microservice; remote calls remain distributed.",
        "\n  ".join(parts),
        1080,
        300,
    )


def mental_model_procedure() -> str:
    body = """
  <text class="title" x="600" y="34" text-anchor="middle">Setup once, then call at runtime</text>
  <text class="cap" x="470" y="58" text-anchor="middle">SETUP · ONCE</text>
  <text class="cap" x="1080" y="58" text-anchor="middle">RUNTIME · PER CALL</text>
  <line class="track" x1="940" y1="70" x2="940" y2="210"/>
  """ + rounded_box(32, 84, 176, 88) + label(120, 118, "Receiver module") + label(120, 140, "USER-WRITTEN", "cap") + """
  """ + rounded_box(272, 84, 176, 88) + label(360, 118, "Gateway discovers") + label(360, 140, "public surface", "small") + """
  """ + rounded_box(512, 84, 176, 88) + label(600, 118, "Graftcode Engine") + label(600, 140, "generates Graft", "small") + """
  """ + rounded_box(752, 84, 176, 88) + label(840, 112, "Caller installs") + label(840, 132, "& calls Graft", "h") + label(840, 152, "USER-WRITTEN", "cap") + """
  """ + rounded_box(992, 84, 176, 88) + label(1080, 118, "Gateway invokes") + label(1080, 140, "Receiver", "small") + """
  <path class="flow" d="M208 126 H272"/><path class="flow" d="M448 126 H512"/><path class="flowMuted" d="M688 126 H752"/><path class="flow" d="M928 126 H992"/>
  <path class="flowMuted" d="M1080 172 V200 H840 V172"/>
  <text class="edge" x="240" y="116">analyze</text><text class="edge" x="480" y="116">generate</text><text class="edge" x="720" y="116">install</text><text class="edge" x="960" y="224">result or error</text>
"""
    return wrap(
        "The Graftcode procedure: setup once, then call at runtime",
        "Setup analyzes the Receiver, generates a Graft, and the Caller installs it; runtime invokes the Receiver through Gateway and returns a result or error.",
        body,
        1200,
        250,
    )


def identifiers_and_auth() -> str:
    cards = [
        (32, "Project Key", "Gateway startup", "--projectKey", "Registers Gateway in a project"),
        (282, "Registry URL", "Caller package manager", "https://grft.dev", "Installs the Graft"),
        (532, "Runtime host", "GraftConfig.host", "ws://host/ws · inmemory", "Executes methods"),
        (782, "Call credential", "Header or parameter", "Authorization: Bearer", "Authorizes one call"),
    ]
    parts = [
        '<text class="title" x="520" y="34" text-anchor="middle">Four different things — do not conflate them</text>'
    ]
    for x, title, where, example, purpose in cards:
        parts += [
            rounded_box(x, 72, 226, 150),
            label(x + 16, 100, title, "h", "start"),
            label(x + 16, 124, "SET ON / USED BY", "cap", "start"),
            label(x + 16, 142, where, "small", "start"),
            label(x + 16, 162, example, "mono", "start"),
            label(x + 16, 186, "PURPOSE", "cap", "start"),
            label(x + 16, 204, purpose, "small", "start"),
        ]
    return wrap(
        "Project Key, registry URL, runtime host, and call credential are four different things",
        "Project Key registers Gateway; registry URL installs the Graft; runtime host executes methods; call credential authorizes a specific call.",
        "\n  ".join(parts),
        1040,
        300,
    )


def contract_evolution_timeline() -> str:
    steps = [
        (80, "Change", "Receiver surface", True),
        (230, "Analyze", "public API", False),
        (380, "Generate", "packages", True),
        (530, "Compile", "Callers", False),
        (680, "Smoke test", "in-memory + remote", True),
        (830, "Publish", "new version", False),
        (980, "Keep old", "side by side", True),
    ]
    parts = [
        '<text class="title" x="530" y="34" text-anchor="middle">Safe contract evolution</text>',
        '<line class="track" x1="80" y1="150" x2="980" y2="150"/>',
    ]
    for x, title, sub, above in steps:
        cy = 150
        parts.append(f'<circle class="box" cx="{x}" cy="{cy}" r="16"/>')
        parts.append(label(x, cy + 5, str(steps.index((x, title, sub, above)) + 1), "mono"))
        ty = 94 if above else 196
        parts.append(label(x, ty, title))
        parts.append(label(x, ty + 18, sub, "small"))
    parts.append(
        label(
            530,
            262,
            "Additive changes are usually safe; renames and signature changes are usually breaking.",
            "small",
        )
    )
    return wrap(
        "Safe contract-evolution workflow",
        "Seven stages from changing the Receiver surface through publish, with old versions kept side by side while Callers migrate.",
        "\n  ".join(parts),
        1060,
        290,
    )


def type_mapping_path() -> str:
    body = """
  <text class="title" x="520" y="34" text-anchor="middle">Type mapping across three stages</text>
  """ + rounded_box(36, 72, 196, 96) + label(134, 104, "Receiver type") + label(134, 128, "long", "mono") + """
  """ + rounded_box(288, 72, 196, 96) + label(386, 104, "Interface metadata") + label(386, 128, "64-bit integer", "mono") + """
  """ + rounded_box(540, 72, 196, 96) + label(638, 110, "Target generator") + label(638, 132, "per Caller ecosystem", "small") + """
  """ + rounded_box(792, 72, 212, 96) + label(898, 104, "Caller type") + label(898, 128, "number", "mono") + """
  <path class="flow" d="M232 120 H288"/><path class="flow" d="M484 120 H540"/><path class="flow" d="M736 120 H792"/>
  """ + rounded_box(540, 214, 464, 66) + label(560, 240, "NOT PORTABLE", "cap", "start") + label(560, 260, "Framework complex type → rejected at generation", "h", "start") + """
  <path class="flowMuted" d="M638 168 V214"/>
  """ + label(230, 248, "Every stage must support the type", "small") + """
"""
    return wrap(
        "Type mapping across Receiver, interface metadata, and target generator",
        "A Receiver type becomes language-neutral interface metadata and maps to a Caller type; unsupported framework types are rejected during package generation.",
        body,
        1040,
        310,
    )


def production_deployment() -> str:
    body = """
  <text class="title" x="560" y="34" text-anchor="middle">Production deployment topology</text>
  """ + rounded_box(28, 148, 150, 60) + label(103, 174, "Caller") + label(103, 194, "installed Graft", "small") + """
  """ + rounded_box(210, 148, 140, 60) + label(280, 174, "TLS/WSS ingress") + """
  """ + rounded_box(382, 148, 150, 60) + label(457, 170, "Load balancer") + label(457, 190, "affinity if stateful", "small") + """
  <rect class="boxMuted" x="564" y="60" width="380" height="300" rx="14"/>
  <text class="cap" x="580" y="82">RECEIVER ENVIRONMENT</text>
  """ + rounded_box(584, 96, 200, 42) + label(684, 122, "Gateway (gg)") + rounded_box(584, 144, 200, 42) + label(684, 170, "Receiver") + """
  """ + rounded_box(820, 120, 104, 46) + label(872, 146, "dependencies", "small") + """
  """ + rounded_box(584, 238, 200, 42) + label(684, 264, "Gateway (gg)") + rounded_box(584, 286, 200, 42) + label(684, 312, "Receiver") + """
  """ + rounded_box(820, 262, 104, 46) + label(872, 288, "dependencies", "small") + """
  <path class="flow" d="M178 178 H210"/><path class="flow" d="M350 178 H382"/><path class="flow" d="M532 178 C556 178 556 117 584 117"/><path class="flow" d="M532 178 C556 178 556 259 584 259"/>
  <path class="flow" d="M784 165 H820"/><path class="flow" d="M784 307 H820"/>
  <text class="cap" x="44" y="292">CONTROL PLANE (not runtime data path)</text>
  """ + rounded_box(28, 304, 240, 52) + label(148, 326, "Registry") + label(148, 344, "install-time", "small") + """
  """ + rounded_box(288, 304, 240, 52) + label(408, 326, "Graftcode Engine") + label(408, 344, "setup-time generation", "small") + """
  <path class="flowMuted" d="M103 208 V304"/><text class="edge" x="118" y="248">install time</text>
"""
    return wrap(
        "Graftcode production deployment topology",
        "Caller traffic flows through ingress and a load balancer to Gateway plus Receiver replicas; registry and Graftcode Engine sit on a separate control plane.",
        body,
        1120,
        440,
    )


def public_surface_vs_implementation() -> str:
    body = """
  <text class="title" x="400" y="34" text-anchor="middle">Public surface vs implementation</text>
  <text class="cap" x="200" y="70" text-anchor="middle">YOUR ENVIRONMENT</text>
  <text class="cap" x="620" y="70" text-anchor="middle">GRAFTCODE ENGINE</text>
  """ + rounded_box(40, 90, 320, 150) + label(200, 130, "Business logic · Gateway · secrets") + label(200, 152, "CI/CD · tests · infrastructure", "small") + """
  """ + rounded_box(440, 90, 320, 150) + label(600, 124, "Stores public method signatures") + label(600, 146, "Creates Grafts from interfaces", "small") + """
  <path class="flow" d="M360 165 H440"/><text class="edge" x="400" y="156">publish public interface</text>
  <path class="flowMuted" d="M440 190 H360"/><text class="edge" x="400" y="206">use generated Grafts</text>
"""
    return wrap(
        "Public surface vs implementation boundary",
        "Implementation stays in your environment; Graftcode Engine stores public method signatures and creates Grafts from public interfaces.",
        body,
        800,
        280,
    )


GENERATORS = {
    "generated-vs-written.svg": generated_vs_written,
    "one-picture-overview.svg": one_picture_overview,
    "graftcode-mental-model.svg": graftcode_mental_model,
    "mental-model-procedure.svg": mental_model_procedure,
    "identifiers-and-auth.svg": identifiers_and_auth,
    "contract-evolution-timeline.svg": contract_evolution_timeline,
    "type-mapping-path.svg": type_mapping_path,
    "production-deployment.svg": production_deployment,
    "public-surface-vs-implementation.svg": public_surface_vs_implementation,
}


def main() -> None:
    for name, generator in GENERATORS.items():
        path = OUT / name
        path.write_text(generator(), encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
