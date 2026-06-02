import re
from pathlib import Path

import pytest

import build_pipeline as build

_CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
_EXTERNAL_IMG_RE = re.compile(r'<img\b[^>]*\bsrc=["\']https?://', re.IGNORECASE)


def _content_pages():
    return sorted(
        p for p in _CONTENT_DIR.rglob("*.md") if not p.name.startswith("_")
    )


def _page_id(path):
    return path.relative_to(_CONTENT_DIR).as_posix()


@pytest.mark.parametrize("path", _content_pages(), ids=_page_id)
def test_content_page_parses(path):
    build.load_document(path)


@pytest.mark.parametrize("path", _content_pages(), ids=_page_id)
def test_content_page_metadata_valid(path):
    meta, _ = build.load_document(path)
    build.validate_metadata(path, meta)


@pytest.mark.parametrize("path", _content_pages(), ids=_page_id)
def test_no_stale_exper1_links(path):
    text = path.read_text(encoding="utf-8")
    assert "EXPER_1.html" not in text, "stale EXPER_1.html link (path never existed)"


@pytest.mark.parametrize("path", _content_pages(), ids=_page_id)
def test_no_exp1_intro_links(path):
    text = path.read_text(encoding="utf-8")
    assert "EXP_1.html" not in text, "EXP_1.html is the intro landing page — do not link to it"


@pytest.mark.parametrize("path", _content_pages(), ids=_page_id)
def test_no_external_image_urls(path):
    text = path.read_text(encoding="utf-8")
    match = _EXTERNAL_IMG_RE.search(text)
    assert match is None, (
        f"{path.name}: external image URL found ({match.group()!r}) — "
        "all images must be local (offline-first)"
    )
