# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Numbers
from mimesis.enums import NumTypes
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestNumbers(object):

    @pytest.fixture
    def numbers(self):
        return Numbers()

    def test_str(self, numbers):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(numbers))

    @pytest.mark.parametrize(
        'start, end', [
            (1.2, 10),
            (10.4, 20.0),
            (20.3, 30.8),
        ],
    )
    def test_floats(self, numbers, start, end):
        result = numbers.floats(start, end)
        assert max(result) <= end
        assert min(result) >= start
        assert len(result) == 10
        assert isinstance(result, list)

        result = numbers.floats(n=1000)
        assert len(result) == 1000

        result = numbers.floats(rounding=4)
        for e in result:
            assert len(str(e).split('.')[1]) <= 4

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

    @pytest.mark.parametrize(
        'start_real, end_real, start_imag, end_imag', [
            (1.2, 10, 1, 2.4),
            (10.4, 20.0, 2.3, 10),
            (20.3, 30.8, 2.4, 4.5),
        ],
    )
    def test_complexes(self, numbers,
                         start_real, end_real, start_imag, end_imag):
        result = numbers.complexes(start_real, end_real,
                                     start_imag, end_imag)
        assert max(e.real for e in result) <= end_real
        assert min(e.real for e in result) >= start_real
        assert max(e.imag for e in result) <= end_imag
        assert min(e.imag for e in result) >= start_imag
        assert len(result) == 10
        assert isinstance(result, list)

        result = numbers.complexes(n=1000)
        assert len(result) == 1000

        result = numbers.complexes(rounding_real=4, rounding_imag=6)
        for e in result:
            assert len(str(e.real).split('.')[1]) <= 4
            assert len(str(e.imag).split('.')[1]) <= 6

    def test_matrix(self, numbers):

        with pytest.raises(NonEnumerableError):
            numbers.matrix(num_type='int')

        result = numbers.matrix(rounding=4)
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                assert isinstance(e, float)
                assert len(str(e).split('.')[1]) <= 4

        result = numbers.matrix(m=5, n=5, num_type=NumTypes.INTEGERS, start=5)
        assert len(result) == 5
        for row in result:
            assert len(row) == 5
            assert min(row) >= 5
            for e in row:
                assert isinstance(e, int)

        result = numbers.matrix(
            num_type=NumTypes.COMPLEXES, rounding_real=4, rounding_imag=6)
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                assert len(str(e.real).split('.')[1]) <= 4
                assert len(str(e.imag).split('.')[1]) <= 6

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


class TestSeededNumbers(object):

    @pytest.fixture
    def n1(self, seed):
        return Numbers(seed=seed)

    @pytest.fixture
    def n2(self, seed):
        return Numbers(seed=seed)

    def test_floats(self, n1, n2):
        assert n1.floats() == n2.floats()
        assert n1.floats(n=5) == n2.floats(n=5)

    def test_integers(self, n1, n2):
        assert n1.integers() == n2.integers()
        assert n1.integers(start=-999, end=999, n=10) == \
            n2.integers(start=-999, end=999, n=10)

    def test_complexes(self, n1, n2):
        assert n1.complexes() == n2.complexes()
        assert n1.complexes(n=5) == n2.complexes(n=5)

    def test_matrix(self, n1, n2):
        assert n1.matrix() == n2.matrix()
        assert n1.matrix(n=5) == n2.matrix(n=5)

    def test_digit(self, n1, n2):
        assert n1.digit() == n2.digit()
        assert n1.digit(to_bin=True) == n2.digit(to_bin=True)

    def test_between(self, n1, n2):
        assert n1.between() == n2.between()
        assert n1.between(minimum=42, maximum=2048) == \
            n2.between(minimum=42, maximum=2048)

    @pytest.mark.skip(reason='Method refactoring needed.')
    def test_primes(self, n1, n2):
        assert n1.primes() == n2.primes()
