"""Tests for optional import fallbacks."""

from __future__ import annotations

import builtins
import importlib
import sys

import pytest


def test_compat_without_pytz(monkeypatch: pytest.MonkeyPatch) -> None:
    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):  # noqa: A002
        if name == "pytz" or name.startswith("pytz."):
            raise ImportError("blocked")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    sys.modules.pop("pytz", None)
    sys.modules.pop("mimesis.compat", None)

    compat = importlib.import_module("mimesis.compat")
    assert compat.pytz is None

    monkeypatch.undo()
    sys.modules.pop("mimesis.compat", None)
    importlib.import_module("mimesis.compat")


def test_factory_plugin_requires_factory_boy(monkeypatch: pytest.MonkeyPatch) -> None:
    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):  # noqa: A002
        if name == "factory" or name.startswith("factory."):
            raise ImportError("blocked")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    for key in list(sys.modules):
        if key == "factory" or key.startswith(("factory.", "mimesis.plugins.factory")):
            sys.modules.pop(key, None)

    with pytest.raises(ImportError, match="factory_boy"):
        importlib.import_module("mimesis.plugins.factory")

    monkeypatch.undo()
    for key in list(sys.modules):
        if key.startswith("mimesis.plugins.factory"):
            sys.modules.pop(key, None)
    importlib.import_module("mimesis.plugins.factory")
