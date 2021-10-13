# -*- coding: utf-8 -*-
import pytest
from mimesis import Choices


@pytest.fixture
def choices():
    return Choices()


@pytest.mark.parametrize(
    "items, weights, length",
    [
        (["a", "b", "c", "d", "e", "f", "g"], [1, 1, 1, 1, 1, 1, 1], 4),
        (["a", "b", "c", "d", "e", "f", "g"], [1, 1, 1, 1, 1, 1, 1], 5),
        (["a", "b", "c", "d", "e", "f", "g"], [1, 1, 1, 1, 1, 1, 1], 1),
        (("a", "b", "c", "d", "e", "f", "g"), [1, 1, 1, 1, 1, 1, 1], 4),
        (("a", "b", "c", "d", "e", "f", "g"), [1, 1, 1, 1, 1, 1, 1], 5),
        (("a", "b", "c", "d", "e", "f", "g"), [1, 1, 1, 1, 1, 1, 1], 1),
        ("abcdefg", [1, 1, 1, 1, 1, 1, 1], 4),
        ("abcdefg", [1, 1, 1, 1, 1, 1, 1], 5),
        ("abcdefg", [1, 1, 1, 1, 1, 1, 1], 1),
    ],
)
def test_choices(choices, weights, items, length):
    result = choices(items=items, weights=weights, length=length)
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
def test_choices_unique(choices, items):
    result = choices(items=items, length=4, unique=True)
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
def test_choices_one_element(choices, items):
    result = choices(items=items)
    assert type(result) is type(items)


@pytest.mark.parametrize("n", range(5))
def test_choices_seed(n):
    choices = Choices(seed=0xF1)
    items = ["a", "b", "c", "d", "e", "f", "g"]

    result = choices(items=items)
    assert result == ["e"]


def test_choices_non_sequence_items(choices):
    with pytest.raises(TypeError):
        choices(items=5)


def test_choices_empty_items(choices):
    with pytest.raises(ValueError):
        choices(items=[])


def test_choices_negative_length(choices):
    with pytest.raises(ValueError):
        choices(items=("a", "b"), length=-1)


def test_choices_insufficient_unique(choices):
    with pytest.raises(ValueError):
        choices(items=["a", "b"], length=3, unique=True)
