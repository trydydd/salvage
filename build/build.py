#!/usr/bin/env python3
"""
build.py — Render Salvage Electronics Markdown content to static HTML.

Usage:
    python build/build.py [--clean]

Options:
    --clean     Remove output/html/ before building.

On success:
    - output/html/ contains copied shared assets and rendered HTML pages
    - content paths are mirrored under output/html/ with .html extensions

Exits non-zero on missing content, missing shared assets, template errors, or
Markdown/frontmatter parse errors.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any

import mistune
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "output" / "html"
SHARED_DIR = REPO_ROOT / "shared"
OVERLAY_DIR = REPO_ROOT / "overlay"
MARKDOWN = mistune.create_markdown(
    renderer=mistune.HTMLRenderer(escape=False),
    plugins=["strikethrough", "table", "url", "task_lists"],
)
SECTION_DIRS = {
    "foundations": "foundations",
    "donor_guides": "donor-guides",
    "components": "components",
    "projects": "projects",
}


def asset_prefix(depth: int) -> str:
    """Return the relative prefix needed to reach output/html/ assets."""
    if depth < 0:
        raise ValueError("depth must be non-negative")
    return "../" * depth


def load_document(path: Path) -> tuple[dict[str, Any], str]:
    """Parse optional YAML frontmatter and return metadata plus body text."""
    text = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    body = text

    if text.startswith("---"):
        lines = text.splitlines(keepends=True)
        if lines and lines[0].strip() == "---":
            closing_index = None
            for index, line in enumerate(lines[1:], start=1):
                if line.strip() == "---":
                    closing_index = index
                    break
            if closing_index is None:
                raise ValueError(
                    f"{path}: frontmatter starts with '---' but has no closing delimiter"
                )

            raw_frontmatter = "".join(lines[1:closing_index])
            parsed = yaml.safe_load(raw_frontmatter) if raw_frontmatter.strip() else {}
            if parsed is None:
                parsed = {}
            if not isinstance(parsed, dict):
                raise ValueError(f"{path}: frontmatter must parse to a mapping")

            metadata = parsed
            body = "".join(lines[closing_index + 1 :])

    return metadata, body


def output_path_for(source_path: Path) -> Path:
    """Map a content/*.md file to its output/html/*.html path."""
    relative_path = source_path.relative_to(CONTENT_DIR)
    return OUTPUT_DIR / relative_path.with_suffix(".html")


def depth_for_output(output_path: Path) -> int:
    """Return the number of directory levels below output/html/."""
    relative_path = output_path.relative_to(OUTPUT_DIR)
    return len(relative_path.parts) - 1


def section_target(section_dir: str) -> str:
    """Return the first rendered page path for a section, or its future index."""
    content_section = CONTENT_DIR / section_dir
    if content_section.is_dir():
        for candidate in sorted(content_section.glob("*.md")):
            if candidate.name.startswith("_"):
                continue
            return candidate.relative_to(CONTENT_DIR).with_suffix(".html").as_posix()
    return f"{section_dir}/index.html"


def relative_link(prefix: str, target: str) -> str:
    """Prefix a site-relative output target for the current page depth."""
    return f"{prefix}{target}"


def navigation_context(prefix: str) -> dict[str, str]:
    """Build depth-relative navigation links for the shared header/footer."""
    return {
        "home": relative_link(prefix, "index.html"),
        "foundations": relative_link(prefix, section_target(SECTION_DIRS["foundations"])),
        "donor_guides": relative_link(prefix, section_target(SECTION_DIRS["donor_guides"])),
        "components": relative_link(prefix, section_target(SECTION_DIRS["components"])),
        "projects": relative_link(prefix, section_target(SECTION_DIRS["projects"])),
        "license_path": relative_link(prefix, "LICENSE.txt"),
        "attribution_path": relative_link(prefix, "ATTRIBUTION.md"),
    }


def validate_metadata(path: Path, metadata: dict[str, Any]) -> tuple[str, Any, Any, Any]:
    """Validate the required frontmatter fields."""
    title = metadata.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"{path}: missing required frontmatter field 'title'")

    hazard = metadata.get("hazard")
    if hazard is not None and hazard not in {1, 2, 3, 4}:
        raise ValueError(f"{path}: 'hazard' must be 1-4 or null")

    section = metadata.get("section")
    hazard_summary = metadata.get("hazard_summary")
    return title.strip(), section, hazard, hazard_summary


def ensure_required_inputs() -> None:
    """Check that the content tree and fetched shared assets exist."""
    if not CONTENT_DIR.is_dir():
        raise FileNotFoundError(f"Missing content directory: {CONTENT_DIR}")

    missing_assets = [name for name in ("css", "js", "fonts") if not (SHARED_DIR / name).is_dir()]
    if missing_assets:
        asset_list = ", ".join(f"shared/{name}/" for name in missing_assets)
        raise FileNotFoundError(
            f"Missing shared assets: {asset_list}. Run 'make fetch' first."
        )


def copy_tree(source: Path, destination: Path) -> None:
    """Copy a directory tree into the build output."""
    shutil.copytree(source, destination, dirs_exist_ok=True)


def copy_static_assets() -> None:
    """Copy shared and salvage-specific assets into output/html/."""
    copy_tree(SHARED_DIR / "css", OUTPUT_DIR / "css")
    copy_tree(SHARED_DIR / "js", OUTPUT_DIR / "js")
    copy_tree(SHARED_DIR / "fonts", OUTPUT_DIR / "fonts")
    copy_tree(OVERLAY_DIR / "icons", OUTPUT_DIR / "icons")

    salvage_css = OVERLAY_DIR / "css" / "salvage.css"
    if not salvage_css.is_file():
        raise FileNotFoundError(f"Missing salvage stylesheet: {salvage_css}")
    (OUTPUT_DIR / "css").mkdir(parents=True, exist_ok=True)
    shutil.copy2(salvage_css, OUTPUT_DIR / "css" / "salvage.css")

    for name in ("LICENSE.txt", "ATTRIBUTION.md"):
        source = REPO_ROOT / name
        if not source.is_file():
            raise FileNotFoundError(f"Missing required file: {source}")
        shutil.copy2(source, OUTPUT_DIR / name)


def render_pages() -> int:
    """Render all non-underscore Markdown files under content/."""
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
    )
    template = env.get_template("page.html")

    rendered_count = 0
    for source_path in sorted(CONTENT_DIR.rglob("*.md")):
        if source_path.name.startswith("_"):
            continue

        metadata, body_text = load_document(source_path)
        title, section, hazard, hazard_summary = validate_metadata(source_path, metadata)
        output_path = output_path_for(source_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        prefix = asset_prefix(depth_for_output(output_path))
        context = {
            "title": title,
            "section": section,
            "hazard": hazard,
            "hazard_summary": hazard_summary,
            "body": MARKDOWN(body_text),
            "css_shared": f"{prefix}css/open-circuits.css",
            "css_salvage": f"{prefix}css/salvage.css",
            "js_nav": f"{prefix}js/navigation.js",
            "icons_path": f"{prefix}icons/",
            **navigation_context(prefix),
        }

        output_path.write_text(template.render(**context), encoding="utf-8")
        rendered_count += 1

    return rendered_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove output/html/ before building",
    )
    args = parser.parse_args()

    try:
        ensure_required_inputs()

        if args.clean and OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        copy_static_assets()
        rendered_count = render_pages()
    except Exception as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Rendered {rendered_count} page(s) to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
