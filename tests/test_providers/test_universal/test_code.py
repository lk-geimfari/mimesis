import re

import pytest

from mimesis import Code
from mimesis.datasets import LOCALE_CODES
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.exceptions import NonEnumerableError
from mimesis.locales import Locale

from .. import patterns


def _has_gs1_check_digit(code: str) -> bool:
    """Check the GS1 mod 10 relation, weighted from the left.

    Deliberately a different formulation from the implementation, which
    enumerates the digits in reverse, so that a transposed weighting cannot
    satisfy both. Note the weight depends on the distance from the right-hand
    end, so it is not simply "every other digit from the left".
    """
    digits = [int(char) for char in code]
    payload = digits[:-1]
    last = len(payload) - 1
    total = sum(
        digit * (3 if (last - index) % 2 == 0 else 1)
        for index, digit in enumerate(payload)
    )
    return digits[-1] == (10 - total) % 10


def _has_mod11_check_digit(code: str) -> bool:
    """Check the mod 11 relation, allowing ``X`` for a remainder of 10."""
    digits = [int(char) for char in code[:-1]]
    total = sum(d * (len(digits) + 1 - index) for index, d in enumerate(digits))
    expected = (11 - total) % 11
    return code[-1] == ("X" if expected == 10 else str(expected))


class TestCode:
    @pytest.fixture
    def code(self):
        return Code()

    def test_str(self, code):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(code))

    @pytest.mark.parametrize(
        "fmt, length",
        [
            (EANFormat.EAN8, 8),
            (EANFormat.EAN13, 13),
        ],
    )
    def test_ean(self, code, fmt, length):
        result = code.ean(fmt=fmt)
        assert len(result) == length

    def test_ean_non_enum(self, code):
        with pytest.raises(NonEnumerableError):
            code.ean(fmt="nil")

    def test_imei(self, code):
        result = code.imei()
        assert len(result) <= 15

    def test_pin(self, code):
        result = code.pin()
        assert len(result) == 4

    def test_issn(self, code):
        result = code.issn()
        assert len(result) == 9

    def test_issn_check_digit(self, code):
        for _ in range(50):
            assert _has_mod11_check_digit(code.issn().replace("-", ""))

    def test_ean_check_digit(self, code):
        for fmt in (EANFormat.EAN8, EANFormat.EAN13):
            for _ in range(50):
                assert _has_gs1_check_digit(code.ean(fmt=fmt))

    @pytest.mark.parametrize("fmt", [ISBNFormat.ISBN10, ISBNFormat.ISBN13])
    def test_isbn_check_digit(self, code, fmt):
        for _ in range(50):
            result = code.isbn(fmt=fmt, locale=Locale.EN).replace("-", "")
            if fmt == ISBNFormat.ISBN13:
                assert _has_gs1_check_digit(result)
            else:
                assert _has_mod11_check_digit(result)

    def test_locale_code(self, code):
        result = code.locale_code()
        assert result in LOCALE_CODES

    @pytest.mark.parametrize(
        "fmt, length",
        [
            (ISBNFormat.ISBN10, 10),
            (ISBNFormat.ISBN13, 13),
        ],
    )
    @pytest.mark.parametrize(
        "locale",
        list(Locale),
    )
    def test_isbn(self, code, fmt, length, locale):
        result = code.isbn(fmt=fmt, locale=locale)
        assert result is not None
        assert len(result) >= length

    def test_isbn_non_enum(self, code):
        with pytest.raises(NonEnumerableError):
            code.isbn(fmt="nil")


class TestSeededCode:
    @pytest.fixture
    def c1(self, seed):
        return Code(seed=seed)

    @pytest.fixture
    def c2(self, seed):
        return Code(seed=seed)

    def test_ean(self, c1, c2):
        assert c1.ean() == c2.ean()
        assert c1.ean(fmt=EANFormat.EAN13) == c2.ean(fmt=EANFormat.EAN13)

    def test_imei(self, c1, c2):
        assert c1.imei() == c2.imei()

    def test_pin(self, c1, c2):
        assert c1.pin() == c2.pin()
        assert c1.pin(mask="##") == c2.pin(mask="##")

    def test_issn(self, c1, c2):
        assert c1.issn() == c2.issn()
        assert c1.issn(mask="##") == c2.issn(mask="##")

    def test_locale_code(self, c1, c2):
        assert c1.locale_code() == c2.locale_code()

    def test_isbn(self, c1, c2):
        assert c1.isbn() == c2.isbn()
        assert c1.isbn(fmt=ISBNFormat.ISBN13) == c2.isbn(fmt=ISBNFormat.ISBN13)
