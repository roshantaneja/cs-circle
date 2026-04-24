import importlib
import os
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _student():
    name = os.environ.get("STUDENT")
    if not name:
        pytest.exit(
            "STUDENT env var not set. Run: STUDENT=devarshi pytest   or   STUDENT=priansh pytest",
            returncode=2,
        )
    if name not in {"devarshi", "priansh"}:
        pytest.exit(f"Unknown STUDENT={name!r}. Must be 'devarshi' or 'priansh'.", returncode=2)
    return name


@pytest.fixture(scope="session")
def student():
    return _student()


@pytest.fixture
def hw1(student):
    module_name = f"{student}.homework1"
    if module_name in sys.modules:
        del sys.modules[module_name]
    return importlib.import_module(module_name)
