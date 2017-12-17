# -*- coding: utf-8 -*-
import pytest

from mimesis import Numbers


@pytest.fixture
def numbers():
    return Numbers()


@pytest.fixture
def _seeded_numbers():
    return Numbers(seed=42)


def test_floats(numbers):
    result = numbers.floats()
    assert len(result) == 100
    assert isinstance(result, list)

    result = numbers.floats(n=3)
    assert len(result) == 1000
    assert isinstance(result, list)


def test_seeded_floats(_seeded_numbers):
    result = _seeded_numbers.floats(n=1)
    assert result[0] == 0.6394267984578837
    result = _seeded_numbers.floats()
    assert result[0] == 0.21863797480360336
    result = _seeded_numbers.floats()
    assert result[0] == 0.8758529403781941


def test_primes(numbers):
    result = numbers.primes()
    assert len(result) == 168
    assert isinstance(result, list)

    result = numbers.primes(500, 500000)
    assert len(result) == 41443
    assert isinstance(result, list)

    result = numbers.primes(start=10, end=200)[1]
    assert result == 13


def test_digit(numbers):
    digits = (
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,
        9,
    )
    result = numbers.digit()
    assert result in digits

    result = numbers.digit(to_bin=True)
    assert isinstance(result, str)


def test_seeded_digit(_seeded_numbers):
    result = _seeded_numbers.digit(to_bin=True)
    assert result == '0b1'
    result = _seeded_numbers.digit()
    assert result == 0
    result = _seeded_numbers.digit()
    assert result == 4


def test_between(numbers):
    result = numbers.between(90, 100)
    assert result >= 90
    assert result <= 100


def test_seeded_between(_seeded_numbers):
    result = _seeded_numbers.between(90, 100)
    assert result == 100
    result = _seeded_numbers.between()
    assert result == 115
    result = _seeded_numbers.between()
    assert result == 26


def test_rating(numbers):
    result = numbers.rating(maximum=5.0)
    assert isinstance(result, float)
    assert (result >= 0) and (result <= 5.0)


def test_seeded_rating(_seeded_numbers):
    result = _seeded_numbers.rating(maximum=10.0)
    assert result == 6.4
    result = _seeded_numbers.rating()
    assert result == 0.1
    result = _seeded_numbers.rating()
    assert result == 1.4
