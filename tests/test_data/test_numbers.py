# -*- coding: utf-8 -*-
import pytest

from mimesis import Numbers


@pytest.fixture
def numbers():
    return Numbers()


def test_floats(numbers):
    result = numbers.floats()
    assert len(result) == 100
    assert isinstance(result, list)

    result = numbers.floats(n=3)
    assert len(result) == 1000
    assert isinstance(result, list)


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


def test_between(numbers):
    result = numbers.between(90, 100)
    assert result >= 90
    assert result <= 100


def test_rating(numbers):
    result = numbers.rating(maximum=5.0)
    assert isinstance(result, float)
    assert (result >= 0) and (result <= 5.0)
