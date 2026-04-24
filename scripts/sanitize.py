"""
Sanitize projects.raw.json -> projects.json

Drops local filesystem paths, filters out external clones (keeps only projects
I've authored/own on GitHub), attaches the canonical repo_url for each entry,
and produces a clean machine-readable index that matches the README.

Run: python3 scripts/sanitize.py
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "projects.raw.json"
DST = ROOT / "projects.json"

# name (as it appears in the raw catalog) -> canonical GitHub repo slug
OWNED = {
    "Claude_Hackathon": "Claude_Hackathon",
    "ML_Project_M_Spring26": "ResumeForge",
    "Clap_OpsPilot": "Clap_OpsPilot",
    "DeskFlow Native": "deskflow-native",
    "pradyotbathuri-website": "pradyotbathuri-website",
    "Quantitative-Modeling_Practice": "Quantitative-Modeling_Practice",
    "NCAA": "Kory_The_Cat-NCAA",
    # research / books
    "BOOK:LLM?": "abstraction-dictionary-book",
}

CATEGORY_REMAP = {
    "AI & ML": "ML systems & tooling",
    "Trading & Finance": "Capital markets & trading",
    "Tools & Utilities": "Tools",
    "Systems & HPC": "Quant & HPC research",
    "Hardware & Robotics": "Hardware & robotics",
    "Web & Backend": "Web & backend",
    "Education & Practice": "Education & practice",
    "Portfolio & Professional": "Portfolio",
    "Research & Documentation": "Research",
}


def main() -> None:
    raw = json.loads(SRC.read_text())
    out = {
        "meta": {
            "generated": raw["meta"]["generated"],
            "note": "Curated index of authored projects. External clones filtered out.",
            "owner": "pbathuri",
            "profile": "https://github.com/pbathuri",
        },
        "projects": [],
    }

    for p in raw["projects"]:
        if p["name"] not in OWNED:
            continue
        slug = OWNED[p["name"]]
        out["projects"].append({
            "name": p["name"],
            "repo": slug,
            "repo_url": f"https://github.com/pbathuri/{slug}",
            "category": CATEGORY_REMAP.get(p["category"], p["category"]),
            "languages": p.get("languages", []),
            "frameworks": p.get("frameworks", []),
            "tech_stack": p.get("tech_stack", []),
            "status": p.get("status"),
            "summary": p.get("summary", ""),
        })

    out["meta"]["count"] = len(out["projects"])
    DST.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {DST.relative_to(ROOT)} with {out['meta']['count']} projects")


if __name__ == "__main__":
    main()
