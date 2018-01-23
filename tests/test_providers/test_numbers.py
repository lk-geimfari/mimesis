# -*- coding: utf-8 -*-
import pytest

from mimesis import Numbers


class TestNumbers(object):

    @pytest.fixture
    def numbers(self):
        return Numbers()

    def test_floats(self, numbers):
        result = numbers.floats()
        assert len(result) == 100
        assert isinstance(result, list)

        result = numbers.floats(n=3)
        assert len(result) == 1000
        assert isinstance(result, list)

    @pytest.mark.parametrize(
        'start, end', [
            (1, 10),
            (10, 20),
            (20, 30),
        ],
    )
    def test_integers(self, numbers, start, end):
        result = numbers.integers(start=start, end=end)

        assert max(result) <= end
        assert min(result) >= start
        assert isinstance(result, list)

        element = numbers.random.choice(result)
        assert isinstance(element, int)

    def test_primes(self, numbers):
        result = numbers.primes()
        assert len(result) == 168
        assert isinstance(result, list)

        result = numbers.primes(500, 500000)
        assert len(result) == 41443
        assert isinstance(result, list)

        result = numbers.primes(start=10, end=200)[1]
        assert result == 13

    def test_digit(self, numbers):
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

    def test_between(self, numbers):
        result = numbers.between(90, 100)
        assert result >= 90
        assert result <= 100

    def test_rating(self, numbers):
        result = numbers.rating(maximum=5.0)
        assert isinstance(result, float)
        assert (result >= 0) and (result <= 5.0)


class TestSeededNumbers(object):

    @pytest.fixture
    def n1(self, seed):
        return Numbers(seed=seed)

    @pytest.fixture
    def n2(self, seed):
        return Numbers(seed=seed)

    def test_floats(self, n1, n2):
        assert n1.floats() == n2.floats()

    def test_integers(self, n1, n2):
        assert n1.integers() == n2.integers()

    def test_digit(self, n1, n2):
        assert n1.digit() == n2.digit()

    def test_between(self, n1, n2):
        assert n1.between() == n2.between()

    def test_rating(self, n1, n2):
        assert n1.rating() == n2.rating()

    @pytest.mark.skip(reason='Method refactoring needed.')
    def test_primes(self, n1, n2):
        assert n1.primes() == n2.primes()
