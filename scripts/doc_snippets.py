"""Shared multi-runtime snippet bodies for documentation (used by consolidate scripts)."""

LANGS = ["dotnet", "javascript", "python", "java", "php", "ruby"]

REMOTE_HOST_CONFIG = {
    "dotnet": """GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;""",
    "javascript": """GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "python": """GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True""",
    "java": """GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "php": """GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;""",
    "ruby": """GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true""",
}

REMOTE_HOST_CONFIG_WITH_IMPORTS = {
    "dotnet": """using <generated_namespace>;

GraftConfig.Host = "ws://localhost/ws";
GraftConfig.Stateless = true;""",
    "javascript": """import { GraftConfig } from "<package-from-vision>";

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "python": """from <generated_package_path>.graft_config import GraftConfig

GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = True""",
    "java": """import <generated_package>.GraftConfig;

GraftConfig.host = "ws://localhost/ws";
GraftConfig.stateless = true;""",
    "php": """GraftConfig::$host = 'ws://localhost/ws';
GraftConfig::$stateless = true;""",
    "ruby": """GraftConfig.host = "ws://localhost/ws"
GraftConfig.stateless = true""",
}

INSTALL_COMMANDS = {
    "dotnet": "dotnet add package <package-id> --version <version> -s <registry-from-vision>",
    "javascript": "npm install <package> --registry <registry-from-vision>",
    "python": "python -m pip install <package> --extra-index-url <url-from-vision>",
    "java": "# Copy the Maven or Gradle dependency block from Vision",
    "php": "composer require <vendor/package>:<version> --repository <repo-from-vision>",
    "ruby": "gem install <name> --source <source-from-vision>",
}

AUTH_HEADERS = {
    "dotnet": """GraftConfig.Host = "wss://service.example/ws";
GraftConfig.Stateless = true;
GraftConfig.SetHeaders(new Dictionary<string, string> {
    ["Authorization"] = "Bearer <token>"
});""",
    "javascript": """GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders({ Authorization: "Bearer <token>" });""",
    "python": """GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = True
# Copy header helper names from Vision.""",
    "java": """GraftConfig.host = "wss://service.example/ws";
GraftConfig.stateless = true;
GraftConfig.setHeaders(java.util.Map.of("Authorization", "Bearer <token>"));""",
    "php": """GraftConfig::$host = 'wss://service.example/ws';
GraftConfig::$stateless = true;
GraftConfig::setHeaders(['Authorization' => 'Bearer <token>']);""",
    "ruby": """GraftConfig.host = "wss://service.example/ws"
GraftConfig.stateless = true
# Copy header helper names from the generated gem.""",
}


def multi_fence(codes: dict[str, str]) -> str:
    parts = []
    for lang in LANGS:
        if lang not in codes:
            continue
        parts.append(f"```{lang}\n{codes[lang].strip()}\n```")
    return "```multi\n" + "\n".join(parts) + "\n```"
