#!/usr/bin/env python3
"""
fetch_shared.py — Fetch shared Open Circuits assets from a pinned release.

Usage:
    python build/fetch_shared.py [--force] [--version TAG]

Options:
    --force         Re-download even if shared assets are already populated.
    --version TAG   Override the pinned release tag for this fetch.

On success:
    - shared/css/, shared/js/, and shared/fonts/ are populated
    - shared/SHARED-VERSION.txt records the fetched release and date

Exits non-zero on download, extraction, or validation failure.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tarfile
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path, PurePosixPath

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = REPO_ROOT / "shared"
VERSION_FILE = SHARED_DIR / "SHARED-VERSION.txt"
ASSET_DIRS = ("css", "js", "fonts")
SHARED_VERSION = "v1.0.0"
RELEASE_URL_TEMPLATE = (
    "https://github.com/trydydd/open-circuits/releases/download/"
    "{version}/open-circuits-{version}.tar.gz"
)


def progress_hook(block_num: int, block_size: int, total_size: int) -> None:
    """Render a simple progress bar while downloading the release tarball."""
    if total_size <= 0:
        return
    downloaded = min(block_num * block_size, total_size)
    pct = downloaded * 100 / total_size
    bar = "#" * int(pct // 2)
    print(f"\r  [{bar:<50}] {pct:5.1f}%", end="", flush=True)


def requested_version(args: argparse.Namespace) -> str:
    """Return the requested version, defaulting to the pinned release."""
    return args.version or SHARED_VERSION


def read_existing_version() -> str | None:
    """Read the currently fetched shared version, if recorded."""
    if not VERSION_FILE.is_file():
        return None

    for line in VERSION_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith("VERSION="):
            return line.partition("=")[2].strip()
        if line.startswith("SOURCE_URL="):
            source_url = line.partition("=")[2].strip()
            tarball = source_url.rsplit("/", 1)[-1]
            prefix = "open-circuits-"
            suffix = ".tar.gz"
            if tarball.startswith(prefix) and tarball.endswith(suffix):
                return tarball[len(prefix) : -len(suffix)]
    return None


def assets_present() -> bool:
    """Return True when all required shared asset directories exist."""
    return all((SHARED_DIR / name).is_dir() for name in ASSET_DIRS)


def should_skip_fetch(version: str, force: bool, explicit_version: bool) -> bool:
    """Decide whether an existing shared asset checkout can be reused."""
    if force or not assets_present():
        return False

    current_version = read_existing_version()
    if current_version and current_version != version:
        print(
            f"shared assets are populated for {current_version}, not {version}; refetching."
        )
        return False
    if explicit_version and current_version is None:
        print("shared assets are populated but their version is unknown; refetching.")
        return False

    print("shared assets already populated. Skipping download.")
    print("Use --force to re-download.")
    return True


def cleanup_existing_assets() -> None:
    """Remove previously fetched shared asset directories before extraction."""
    SHARED_DIR.mkdir(parents=True, exist_ok=True)
    for name in ASSET_DIRS:
        shutil.rmtree(SHARED_DIR / name, ignore_errors=True)


def release_url(version: str) -> str:
    """Return the GitHub release tarball URL for the requested version."""
    return RELEASE_URL_TEMPLATE.format(version=version)


def tarball_name(version: str) -> str:
    """Return the expected tarball filename for the requested version."""
    return f"open-circuits-{version}.tar.gz"


def asset_member_path(name: str) -> Path | None:
    """Map a tar member name to a shared/ relative path, if it is an asset."""
    parts = PurePosixPath(name).parts
    if len(parts) < 2 or parts[0] != "open-circuits" or parts[1] not in ASSET_DIRS:
        return None

    relative_parts = parts[1:]
    if any(part in {"", ".", ".."} for part in relative_parts):
        raise ValueError(f"unsafe tarball member path: {name}")

    return Path(*relative_parts)


def download_tarball(source_url: str, destination: Path) -> None:
    """Download the shared asset tarball into the repository."""
    print(f"Downloading {source_url} ...")
    destination.parent.mkdir(parents=True, exist_ok=True)

    try:
        urllib.request.urlretrieve(source_url, destination, reporthook=progress_hook)
        print()
    except urllib.error.HTTPError as exc:
        print(f"\nDownload failed: {exc.code} {exc.reason}", file=sys.stderr)
        destination.unlink(missing_ok=True)
        sys.exit(1)
    except Exception as exc:
        print(f"\nDownload failed: {exc}", file=sys.stderr)
        destination.unlink(missing_ok=True)
        sys.exit(1)

    print(f"Download complete: {destination}")


def extract_assets(tarball: Path) -> None:
    """Extract only css/, js/, and fonts/ from the Open Circuits release."""
    cleanup_existing_assets()

    try:
        with tarfile.open(tarball) as archive:
            for member in archive.getmembers():
                relative_path = asset_member_path(member.name)
                if relative_path is None:
                    continue

                destination = SHARED_DIR / relative_path
                if member.isdir():
                    destination.mkdir(parents=True, exist_ok=True)
                    continue

                if not member.isfile():
                    continue

                destination.parent.mkdir(parents=True, exist_ok=True)
                extracted = archive.extractfile(member)
                if extracted is None:
                    raise RuntimeError(f"Could not read tarball member: {member.name}")
                with extracted, destination.open("wb") as handle:
                    shutil.copyfileobj(extracted, handle)
    except Exception as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        sys.exit(1)


def validate_assets() -> None:
    """Ensure the extracted shared asset directories exist."""
    missing = [name for name in ASSET_DIRS if not (SHARED_DIR / name).is_dir()]
    if missing:
        missing_paths = ", ".join(f"shared/{name}/" for name in missing)
        print(f"Extraction failed: missing expected assets: {missing_paths}", file=sys.stderr)
        sys.exit(1)


def write_version_file(version: str, source_url: str) -> None:
    """Record the fetched Open Circuits release in version-file format."""
    VERSION_FILE.write_text(
        "# Shared Asset Version\n"
        "# Written by build/fetch_shared.py — do not edit manually.\n\n"
        f"SOURCE_URL={source_url}\n"
        f"SNAPSHOT_DATE={date.today().isoformat()}\n"
        f"TARBALL={tarball_name(version)}\n"
        f"VERSION={version}\n",
        encoding="utf-8",
    )
    print(f"Updated {VERSION_FILE} (version: {version})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even if shared assets are already populated",
    )
    parser.add_argument(
        "--version",
        help="Override the pinned open-circuits release tag",
    )
    args = parser.parse_args()

    version = requested_version(args)
    if should_skip_fetch(version, args.force, explicit_version=args.version is not None):
        return

    source_url = release_url(version)
    tarball = SHARED_DIR / tarball_name(version)

    download_tarball(source_url, tarball)
    extract_assets(tarball)
    validate_assets()
    write_version_file(version, source_url)
    tarball.unlink(missing_ok=True)
    print("Removed tarball.")
    print(f"Done. shared/ contents: {sorted(path.name for path in SHARED_DIR.iterdir())}")


if __name__ == "__main__":
    main()
