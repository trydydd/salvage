import importlib.util
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent


def _load(name, rel_path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, _ROOT / rel_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)


_load("build_pipeline", "build/build.py")
_load("fetch_shared", "build/fetch_shared.py")
