# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Code
from mimesis.data import LOCALE_CODES
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.exceptions import NonEnumerableError

from . import _patterns as p


@pytest.fixture
def code():
    return Code()


def test_str(code):
    assert re.match(p.STR_REGEX, str(code))


@pytest.mark.parametrize(
    'fmt, length', [
        (EANFormat.EAN8, 8),
        (EANFormat.EAN13, 13),
    ],
)
def test_ean(code, fmt, length):
    result = code.ean(fmt=fmt)
    assert len(result) == length


def test_ean_non_enum(code):
    with pytest.raises(NonEnumerableError):
        code.ean(fmt='nil')


def test_imei(code):
    result = code.imei()
    assert len(result) <= 15


def test_pin(code):
    result = code.pin()
    assert len(result) == 4


def test_issn(code):
    result = code.issn()
    assert len(result) == 9


def test_locale_code(code):
    result = code.locale_code()
    assert result in LOCALE_CODES


@pytest.mark.parametrize(
    'fmt, length', [
        (ISBNFormat.ISBN10, 10),
        (ISBNFormat.ISBN13, 13),
    ],
)
def test_isbn(code, fmt, length):
    result = code.isbn(fmt=fmt)
    assert result is not None
    assert len(result) >= length


def test_isbn_non_enum(code):
    with pytest.raises(NonEnumerableError):
        code.isbn(fmt='nil')
