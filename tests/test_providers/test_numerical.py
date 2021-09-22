# -*- coding: utf-8 -*-
import decimal
import re

import pytest
from mimesis import Numerical
from mimesis.enums import NumType
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestNumbers(object):
    @pytest.fixture
    def numerical(self):
        return Numerical()

    def test_str(self, numerical):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(numerical))

    def test_incremental(self):
        numerical = Numerical()
        for i in range(1, 50):
            assert numerical.incremental() == i

    @pytest.mark.parametrize(
        "start, end",
        [
            (1.2, 10),
            (10.4, 20.0),
            (20.3, 30.8),
        ],
    )
    def test_floats(self, numerical, start, end):
        result = numerical.floats(start, end)
        assert max(result) <= end
        assert min(result) >= start
        assert len(result) == 10
        assert isinstance(result, list)

        result = numerical.floats(n=1000)
        assert len(result) == 1000

        result = numerical.floats(precision=4)
        for e in result:
            assert len(str(e).split(".")[1]) <= 4

    @pytest.mark.parametrize(
        "start, end",
        [
            (1, 10),
            (10, 20),
            (20, 30),
        ],
    )
    def test_integers(self, numerical, start, end):
        result = numerical.integers(start=start, end=end)

        assert max(result) <= end
        assert min(result) >= start
        assert isinstance(result, list)

        element = numerical.random.choice(result)
        assert isinstance(element, int)

    @pytest.mark.parametrize(
        "start, end",
        [
            (1, 10),
            (10, 20),
            (20, 30),
        ],
    )
    def test_decimals(self, numerical, start, end):
        result = numerical.decimals(start=start, end=end)

        assert max(result) <= end
        assert min(result) >= start
        assert isinstance(result, list)

        element = numerical.random.choice(result)
        assert isinstance(element, decimal.Decimal)

    @pytest.mark.parametrize(
        "start_real, end_real, start_imag, end_imag",
        [
            (1.2, 10, 1, 2.4),
            (10.4, 20.0, 2.3, 10),
            (20.3, 30.8, 2.4, 4.5),
        ],
    )
    def test_complexes(self, numerical, start_real, end_real, start_imag, end_imag):
        result = numerical.complexes(start_real, end_real, start_imag, end_imag)
        assert max(e.real for e in result) <= end_real
        assert min(e.real for e in result) >= start_real
        assert max(e.imag for e in result) <= end_imag
        assert min(e.imag for e in result) >= start_imag
        assert len(result) == 10
        assert isinstance(result, list)

        result = numerical.complexes(n=1000)
        assert len(result) == 1000

        result = numerical.complexes(precision_real=4, precision_imag=6)
        for e in result:
            assert len(str(e.real).split(".")[1]) <= 4
            assert len(str(e.imag).split(".")[1]) <= 6

    @pytest.mark.parametrize(
        "sr, er, si, ei, pr, pi",
        [
            (1.2, 10, 1, 2.4, 15, 15),
            (10.4, 20.0, 2.3, 10, 10, 10),
            (20.3, 30.8, 2.4, 4.5, 12, 12),
        ],
    )
    def test_complex_number(self, numerical, sr, er, si, ei, pr, pi):
        result = numerical.complex_number(
            start_real=sr,
            end_real=er,
            start_imag=si,
            end_imag=ei,
            precision_real=pr,
            precision_imag=pi,
        )
        assert isinstance(result, complex)
        assert len(str(result.real).split(".")[1]) <= pr
        assert len(str(result.imag).split(".")[1]) <= pi

    def test_matrix(self, numerical):
        # TODO: Rewrite it to cover all cases

        with pytest.raises(NonEnumerableError):
            numerical.matrix(num_type="int")

        result = numerical.matrix(precision=4)
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                assert isinstance(e, float)
                assert len(str(e).split(".")[1]) <= 4

        result = numerical.matrix(m=5, n=5, num_type=NumType.INTEGER, start=5)
        assert len(result) == 5
        for row in result:
            assert len(row) == 5
            assert min(row) >= 5
            for e in row:
                assert isinstance(e, int)

        precision_real, precision_imag = 4, 6
        result = numerical.matrix(
            num_type=NumType.COMPLEX,
            precision_real=precision_real,
            precision_imag=precision_imag,
        )
        result[0][0] = 0.0001 + 0.000001j
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                real_str = "{:.{}f}".format(e.real, precision_real)
                imag_str = "{:.{}f}".format(e.imag, precision_imag)
                assert float(real_str) == e.real
                assert float(imag_str) == e.imag
                assert len(real_str.split(".")[1]) <= precision_real
                assert len(imag_str.split(".")[1]) <= precision_imag

    def test_integer(self, numerical):
        result = numerical.integer_number(-100, 100)
        assert isinstance(result, int)
        assert -100 <= result <= 100

    def test_float(self, numerical):
        result = numerical.float_number(-100, 100, precision=15)
        assert isinstance(result, float)
        assert -100 <= result <= 100
        assert len(str(result).split(".")[1]) <= 15

    def test_decimal(self, numerical):
        result = numerical.decimal_number(-100, 100)
        assert -100 <= result <= 100
        assert isinstance(result, decimal.Decimal)


class TestSeededNumbers(object):
    @pytest.fixture
    def n1(self, seed):
        return Numerical(seed=seed)

    @pytest.fixture
    def n2(self, seed):
        return Numerical(seed=seed)

    def test_incremental(self, n1, n2):
        assert n1.incremental() == n2.incremental()

    def test_floats(self, n1, n2):
        assert n1.floats() == n2.floats()
        assert n1.floats(n=5) == n2.floats(n=5)

    def test_decimals(self, n1, n2):
        assert n1.decimals() == n2.decimals()
        assert n1.decimals(n=5) == n2.decimals(n=5)

    def test_integers(self, n1, n2):
        assert n1.integers() == n2.integers()
        assert n1.integers(start=-999, end=999, n=10) == n2.integers(
            start=-999, end=999, n=10
        )

    def test_complexes(self, n1, n2):
        assert n1.complexes() == n2.complexes()
        assert n1.complexes(n=5) == n2.complexes(n=5)

    def test_matrix(self, n1, n2):
        assert n1.matrix() == n2.matrix()
        assert n1.matrix(n=5) == n2.matrix(n=5)

    def test_integer(self, n1, n2):
        assert n1.integer_number() == n2.integer_number()

    def test_float(self, n1, n2):
        assert n1.float_number() == n2.float_number()

    def test_decimal(self, n1, n2):
        assert n1.decimal_number() == n2.decimal_number()

    def test_complex_number(self, n1, n2):
        assert n1.complex_number() == n2.complex_number()
