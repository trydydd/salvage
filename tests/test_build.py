from pathlib import Path

import pytest

import build_pipeline as build

_FAKE = Path("fake.md")


# ── asset_prefix ──────────────────────────────────────────────────────────────


def test_asset_prefix_root():
    assert build.asset_prefix(0) == ""


def test_asset_prefix_one_level():
    assert build.asset_prefix(1) == "../"


def test_asset_prefix_two_levels():
    assert build.asset_prefix(2) == "../../"


def test_asset_prefix_negative_raises():
    with pytest.raises(ValueError):
        build.asset_prefix(-1)


# ── load_document ─────────────────────────────────────────────────────────────


def test_load_document_no_frontmatter(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("# Hello\n\nSome content.\n")
    meta, body = build.load_document(f)
    assert meta == {}
    assert "Hello" in body


def test_load_document_with_frontmatter(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("---\ntitle: My Page\nsection: foundations\n---\n\nBody text.\n")
    meta, body = build.load_document(f)
    assert meta["title"] == "My Page"
    assert meta["section"] == "foundations"
    assert "Body text." in body


def test_load_document_empty_frontmatter(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("---\n---\n\nBody.\n")
    meta, body = build.load_document(f)
    assert meta == {}
    assert "Body." in body


def test_load_document_unclosed_frontmatter_raises(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("---\ntitle: Oops\n\nNo closing delimiter.\n")
    with pytest.raises(ValueError, match="no closing delimiter"):
        build.load_document(f)


def test_load_document_non_dict_frontmatter_raises(tmp_path):
    f = tmp_path / "page.md"
    f.write_text("---\n- item one\n- item two\n---\n\nBody.\n")
    with pytest.raises(ValueError, match="must parse to a mapping"):
        build.load_document(f)


# ── validate_metadata ─────────────────────────────────────────────────────────


def test_validate_metadata_returns_correct_fields():
    title, section, hazard, summary = build.validate_metadata(
        _FAKE,
        {"title": "Good Page", "section": "components", "hazard": 2, "hazard_summary": "Watch out"},
    )
    assert title == "Good Page"
    assert section == "components"
    assert hazard == 2
    assert summary == "Watch out"


def test_validate_metadata_missing_title_raises():
    with pytest.raises(ValueError, match="missing required frontmatter field 'title'"):
        build.validate_metadata(_FAKE, {"section": "foundations"})


def test_validate_metadata_whitespace_title_raises():
    with pytest.raises(ValueError, match="missing required frontmatter field 'title'"):
        build.validate_metadata(_FAKE, {"title": "   "})


def test_validate_metadata_hazard_zero_raises():
    with pytest.raises(ValueError, match="hazard.*must be 1-4"):
        build.validate_metadata(_FAKE, {"title": "Page", "hazard": 0})


def test_validate_metadata_hazard_five_raises():
    with pytest.raises(ValueError, match="hazard.*must be 1-4"):
        build.validate_metadata(_FAKE, {"title": "Page", "hazard": 5})


def test_validate_metadata_hazard_four_passes():
    _, _, hazard, _ = build.validate_metadata(_FAKE, {"title": "Page", "hazard": 4})
    assert hazard == 4


def test_validate_metadata_null_hazard_passes():
    _, _, hazard, _ = build.validate_metadata(_FAKE, {"title": "Page"})
    assert hazard is None


# ── output_path_for / depth_for_output ────────────────────────────────────────


def test_output_path_for_root_index():
    result = build.output_path_for(build.CONTENT_DIR / "index.md")
    assert result == build.OUTPUT_DIR / "index.html"


def test_output_path_for_section_page():
    result = build.output_path_for(build.CONTENT_DIR / "components" / "01-resistors.md")
    assert result == build.OUTPUT_DIR / "components" / "01-resistors.html"


def test_depth_for_output_root():
    assert build.depth_for_output(build.OUTPUT_DIR / "index.html") == 0


def test_depth_for_output_one_level():
    assert build.depth_for_output(build.OUTPUT_DIR / "components" / "01-resistors.html") == 1


# ── section_target ────────────────────────────────────────────────────────────


def test_section_target_prefers_index_md(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "CONTENT_DIR", tmp_path)
    section = tmp_path / "components"
    section.mkdir()
    (section / "index.md").touch()
    (section / "01-resistors.md").touch()
    assert build.section_target("components") == "components/index.html"


def test_section_target_falls_back_to_first_page(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "CONTENT_DIR", tmp_path)
    section = tmp_path / "foundations"
    section.mkdir()
    (section / "01-why-salvage.md").touch()
    (section / "02-safety.md").touch()
    assert build.section_target("foundations") == "foundations/01-why-salvage.html"


def test_section_target_skips_underscore_files(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "CONTENT_DIR", tmp_path)
    section = tmp_path / "donor-guides"
    section.mkdir()
    (section / "_template.md").touch()
    (section / "01-battery-devices.md").touch()
    assert build.section_target("donor-guides") == "donor-guides/01-battery-devices.html"


def test_section_target_nonexistent_dir_returns_fallback(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "CONTENT_DIR", tmp_path)
    assert build.section_target("missing") == "missing/index.html"
