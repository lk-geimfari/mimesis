import json
import re
import unicodedata
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest


DATASETS_DIR = Path(__file__).parent.parent / "mimesis" / "datasets"

# Scripts with letters that look alike. A word that mixes them almost
# always holds a letter typed on the wrong keyboard layout.
LOOKALIKE_SCRIPTS = ("LATIN", "CYRILLIC", "GREEK")

WORD_PATTERN = re.compile(r"[^\W\d_]+")


def _script(char: str) -> str | None:
    name = unicodedata.name(char, "")
    for script in LOOKALIKE_SCRIPTS:
        if name.startswith(script + " "):
            return script
    return None


def _strings(data: Any) -> Iterator[str]:
    if isinstance(data, str):
        yield data
    elif isinstance(data, list):
        for item in data:
            yield from _strings(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            yield from _strings(key)
            yield from _strings(value)


@pytest.mark.parametrize(
    "path",
    sorted(DATASETS_DIR.rglob("*.json")),
    ids=lambda path: str(path.relative_to(DATASETS_DIR)),
)
def test_dataset_words_do_not_mix_lookalike_scripts(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    mixed = sorted(
        {
            word
            for string in _strings(data)
            for word in WORD_PATTERN.findall(string)
            if len({_script(char) for char in word} - {None}) > 1
        }
    )
    assert mixed == []
