from pathlib import Path

import pytest

import fetch_shared


def test_asset_member_path_css_file():
    assert fetch_shared.asset_member_path("open-circuits/css/open-circuits.css") == Path(
        "css/open-circuits.css"
    )


def test_asset_member_path_js_file():
    assert fetch_shared.asset_member_path("open-circuits/js/navigation.js") == Path(
        "js/navigation.js"
    )


def test_asset_member_path_fonts_file():
    assert fetch_shared.asset_member_path("open-circuits/fonts/Inter-Regular.woff2") == Path(
        "fonts/Inter-Regular.woff2"
    )


def test_asset_member_path_non_asset_dir_returns_none():
    assert fetch_shared.asset_member_path("open-circuits/html/index.html") is None


def test_asset_member_path_wrong_prefix_returns_none():
    assert fetch_shared.asset_member_path("other-project/css/styles.css") is None


def test_asset_member_path_too_short_returns_none():
    assert fetch_shared.asset_member_path("open-circuits") is None


def test_asset_member_path_traversal_rejected():
    with pytest.raises(ValueError, match="unsafe"):
        fetch_shared.asset_member_path("open-circuits/css/../../../etc/passwd")
