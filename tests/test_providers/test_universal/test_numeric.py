import decimal
import re

import pytest

from mimesis import Numeric
from mimesis.enums import NumType
from mimesis.exceptions import NonEnumerableError

from .. import patterns


class TestNumbers:
    @pytest.fixture
    def numeric(self):
        return Numeric()

    def test_str(self, numeric):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(numeric))

    def test_incremental(self):
        numeric = Numeric()
        for i in range(1, 50 + 1):
            assert numeric.increment() == i

    def test_incremental_with_accumulator(self, numeric):
        for i in range(1, 50):
            for key in ("a", "b", "c"):
                assert numeric.increment(accumulator=key) == i

    @pytest.mark.parametrize(
        "start, end",
        [
            (1.2, 10),
            (10.4, 20.0),
            (20.3, 30.8),
        ],
    )
    def test_floats(self, numeric, start, end):
        result = numeric.floats(start, end)
        assert max(result) <= end
        assert min(result) >= start
        assert len(result) == 10
        assert isinstance(result, list)

        result = numeric.floats(n=1000)
        assert len(result) == 1000

        result = numeric.floats(precision=4)
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
    def test_integers(self, numeric, start, end):
        result = numeric.integers(start=start, end=end)

        assert max(result) <= end
        assert min(result) >= start
        assert isinstance(result, list)

        element = numeric.random.choice(result)
        assert isinstance(element, int)

    @pytest.mark.parametrize(
        "start, end",
        [
            (1, 10),
            (10, 20),
            (20, 30),
        ],
    )
    def test_decimals(self, numeric, start, end):
        result = numeric.decimals(start=start, end=end)

        assert max(result) <= end
        assert min(result) >= start
        assert isinstance(result, list)

        element = numeric.random.choice(result)
        assert isinstance(element, decimal.Decimal)

    @pytest.mark.parametrize(
        "start_real, end_real, start_imag, end_imag",
        [
            (1.2, 10, 1, 2.4),
            (10.4, 20.0, 2.3, 10),
            (20.3, 30.8, 2.4, 4.5),
        ],
    )
    def test_complexes(self, numeric, start_real, end_real, start_imag, end_imag):
        result = numeric.complexes(start_real, end_real, start_imag, end_imag)
        assert max(e.real for e in result) <= end_real
        assert min(e.real for e in result) >= start_real
        assert max(e.imag for e in result) <= end_imag
        assert min(e.imag for e in result) >= start_imag
        assert len(result) == 10
        assert isinstance(result, list)

        result = numeric.complexes(n=1000)
        assert len(result) == 1000

        result = numeric.complexes(precision_real=4, precision_imag=6)
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
    def test_complex_number(self, numeric, sr, er, si, ei, pr, pi):
        result = numeric.complex_number(
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

    def test_matrix(self, numeric):
        # TODO: Rewrite it to cover all cases

        with pytest.raises(NonEnumerableError):
            numeric.matrix(num_type="int")

        result = numeric.matrix(precision=4)
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                assert isinstance(e, float)
                assert len(str(e).split(".")[1]) <= 4

        result = numeric.matrix(m=5, n=5, num_type=NumType.INTEGER, start=5)
        assert len(result) == 5
        for row in result:
            assert len(row) == 5
            assert min(row) >= 5
            for e in row:
                assert isinstance(e, int)

        precision_real, precision_imag = 4, 6
        result = numeric.matrix(
            num_type=NumType.COMPLEX,
            precision_real=precision_real,
            precision_imag=precision_imag,
        )
        result[0][0] = 0.0001 + 0.000001j
        assert len(result) == 10
        for row in result:
            assert len(row) == 10
            for e in row:
                real_str = f"{e.real:.{precision_real}f}"
                imag_str = f"{e.imag:.{precision_imag}f}"
                assert float(real_str) == e.real
                assert float(imag_str) == e.imag
                assert len(real_str.split(".")[1]) <= precision_real
                assert len(imag_str.split(".")[1]) <= precision_imag

    def test_integer(self, numeric):
        result = numeric.integer_number(-100, 100)
        assert isinstance(result, int)
        assert -100 <= result <= 100

    def test_float(self, numeric):
        result = numeric.float_number(-100, 100, precision=15)
        assert isinstance(result, float)
        assert -100 <= result <= 100
        assert len(str(result).split(".")[1]) <= 15

    def test_decimal(self, numeric):
        result = numeric.decimal_number(-100, 100)
        assert -100 <= result <= 100
        assert isinstance(result, decimal.Decimal)


class TestSeededNumbers:
    @pytest.fixture
    def n1(self, seed):
        return Numeric(seed=seed)

    @pytest.fixture
    def n2(self, seed):
        return Numeric(seed=seed)

    def test_incremental(self, n1, n2):
        assert n1.increment() == n2.increment()

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
