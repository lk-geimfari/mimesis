import json
import os
import subprocess
import sys

import pytest

from mimesis import Choice


@pytest.fixture
def choice():
    return Choice()


@pytest.mark.parametrize(
    "items, length",
    [
        (["a", "b", "c", "d", "e", "f", "g"], 4),
        (["a", "b", "c", "d", "e", "f", "g"], 5),
        (["a", "b", "c", "d", "e", "f", "g"], 1),
        (("a", "b", "c", "d", "e", "f", "g"), 4),
        (("a", "b", "c", "d", "e", "f", "g"), 5),
        (("a", "b", "c", "d", "e", "f", "g"), 1),
        ("abcdefg", 4),
        ("abcdefg", 5),
        ("abcdefg", 1),
    ],
)
def test_choice(choice, items, length):
    result = choice(items=items, length=length)
    assert len(result) == length
    assert type(result) is type(items)


@pytest.mark.parametrize(
    "items",
    [
        ["a", "b", "c", "d", "c", "b", "a"],
        ("a", "b", "c", "d", "c", "b", "a"),
        "abcdcba",
    ],
)
def test_choice_unique(choice, items):
    result = choice(items=items, length=4, unique=True)
    assert len(result) == len(set(result))
    assert type(result) is type(items)


@pytest.mark.parametrize(
    "items",
    [
        ["a", "b", "c", "d", "e"],
        ("a", "b", "c", "d", "e"),
        "abcde",
    ],
)
def test_choice_one_element(choice, items):
    result = choice(items=items)
    assert isinstance(result, str)


@pytest.mark.parametrize("n", range(5))
def test_choice_seed(n):
    choice = Choice(seed=0xF1)
    items = ["a", "b", "c", "d", "e", "f", "g"]

    result = choice(items=items)
    assert result == "f"


def test_choice_non_sequence_items(choice):
    with pytest.raises(TypeError):
        choice(items=5)


def test_choice_empty_items(choice):
    with pytest.raises(ValueError):
        choice(items=[])


def test_choice_negative_length(choice):
    with pytest.raises(ValueError):
        choice(items=("a", "b"), length=-1)


def test_choice_insufficient_unique(choice):
    with pytest.raises(ValueError):
        choice(items=["a", "b"], length=3, unique=True)


@pytest.mark.parametrize(
    "items",
    [
        ["alpha", "beta", "alpha", "gamma", "delta", "epsilon"],
        ("alpha", "beta", "alpha", "gamma", "delta", "epsilon"),
        "abacde",
    ],
)
def test_unique_choice_seed_independent_of_hash_seed(items):
    code = (
        "import json; from mimesis import Choice; "
        f"print(json.dumps(Choice(seed=42)({items!r}, length=4, unique=True)))"
    )
    results = []
    for hash_seed in ("1", "2", "3"):
        result = subprocess.run(  # noqa: S603 - fixed Python command for the test
            [sys.executable, "-c", code],
            env={**os.environ, "PYTHONHASHSEED": hash_seed},
            capture_output=True,
            check=True,
            text=True,
        )
        results.append(json.loads(result.stdout))
    assert results[0] == results[1] == results[2]


@pytest.mark.parametrize(
    "items",
    [
        ["alpha", "beta", "alpha", "gamma"],
        ("alpha", "beta", "alpha", "gamma"),
        "abac",
    ],
)
def test_unique_choice_removes_duplicates(choice, items):
    result = choice(items, length=3, unique=True)
    assert len(result) == len(set(result)) == 3
    assert set(result) == set(items)
    assert type(result) is type(items)
