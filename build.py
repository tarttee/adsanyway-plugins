"""Build dist/adsanyway-chatgpt.zip: the ChatGPT plugin package.

The skills are shared with the Claude plugin (plugins/adsanyway/skills), so they live in one place.
usage: python build.py
"""
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "plugins" / "adsanyway" / "skills"
DIST = ROOT / "dist"


def main() -> Path:
    plugin = json.loads((ROOT / "chatgpt" / "plugin.json").read_text(encoding="utf-8"))
    claude = json.loads((ROOT / "plugins" / "adsanyway" / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert plugin["version"] == claude["version"], "bump both plugin versions together"
    ui = plugin["extensions"]["com.openai"]["interface"]
    assert len(ui["displayName"]) <= 30 and len(ui["shortDescription"]) <= 30
    assert len(ui["longDescription"]) <= 4000
    assert all(len(p) <= 128 for p in ui["defaultPrompt"]) and len(ui["defaultPrompt"]) <= 3
    review = plugin["extensions"]["com.openai"]["review"]["test_cases"]
    assert len(review["positive"]) >= 5 and len(review["negative"]) >= 3

    DIST.mkdir(exist_ok=True)
    out = DIST / "adsanyway-chatgpt.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(ROOT / "chatgpt" / "plugin.json", "plugin.json")
        z.write(ROOT / "chatgpt" / "mcp.json", "mcp.json")
        for name in ("icon.png", "composer-icon.png"):
            z.write(ROOT / "assets" / name, f"assets/{name}")
        for f in sorted(SKILLS.rglob("*")):
            if f.is_file():
                z.write(f, "skills/" + f.relative_to(SKILLS).as_posix())
    return out


if __name__ == "__main__":
    path = main()
    with zipfile.ZipFile(path) as z:
        print(path, *z.namelist(), sep="\n  ")
