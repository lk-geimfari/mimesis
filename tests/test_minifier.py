import sys

import pytest

from tasks.minifier import Minimizer, human_repr


def test_human_repr():
    assert human_repr(0) == "0.0B"
    assert human_repr(1) == "1.0B"
    assert human_repr(100.1) == "100.1B"
    assert human_repr(1024) == "1.0KB"
    assert human_repr(1024 * 100.1) == "100.1KB"
    assert human_repr(1024 ** 2) == "1.0MB"
    assert human_repr(1024 ** 2 * 100.1) == "100.1MB"


def test_human_repr_cant_handle_gigabytes():
    assert human_repr(1024 ** 3) == "1.0"


def test_minimizer_minifies_file(tmp_path):
    file = tmp_path / "spam.json"
    file.write_text('{\n    "spam": [\n        "eggs"\n    ]\n}')
    minifier = Minimizer(files=(file,))
    minifier.run()
    assert file.read_text() == '{"spam":["eggs"]}'


@pytest.fixture
def disable_colorama_codes(monkeypatch):
    from colorama import Fore, Style

    monkeypatch.setattr(Style, "RESET_ALL", "")
    for name in vars(Fore).keys():
        if name.upper() == name:
            monkeypatch.setattr(Fore, name, "")


@pytest.mark.skipif(sys.platform.startswith("win"), reason="windows")
@pytest.mark.usefixtures(disable_colorama_codes.__name__)
def test_minimizer_reports_to_stdout(capsys, tmp_path):
    file = tmp_path / "spam.json"
    file.write_text("{\n}")
    minifier = Minimizer(files=(file,))
    minifier.run()
    lines = capsys.readouterr().out.split("\n")
    assert lines[0].strip().endswith("3.0B    -> 2.0B")
    assert lines[2] == "Total: 3.0B -> 2.0B. Compressed: 1.0B"
