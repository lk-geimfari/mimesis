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


@pytest.fixture
def _seeded_code():
    return Code(seed=42)


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


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_ean(_seeded_code):
    result = _seeded_code.ean(fmt=EANFormat.EAN13)
    assert result == '1043321819600'
    result = _seeded_code.ean()
    assert result == '33890838'
    result = _seeded_code.ean()
    assert result == '3794026542351'


def test_ean_non_enum(code):
    with pytest.raises(NonEnumerableError):
        code.ean(fmt='nil')


def test_imei(code):
    result = code.imei()
    assert len(result) <= 15


def test_seeded_imei(_seeded_code):
    result = _seeded_code.imei()
    assert result == '353160041043329'
    result = _seeded_code.imei()
    assert result == '353327051819605'


def test_pin(code):
    result = code.pin()
    assert len(result) == 4


def test_seeded_pin(_seeded_code):
    result = _seeded_code.pin(mask='#######')
    assert result == '1043321'
    result = _seeded_code.pin()
    assert result == '8196'
    result = _seeded_code.pin()
    assert result == '0013'


def test_issn(code):
    result = code.issn()
    assert len(result) == 9


def test_seeded_issn(_seeded_code):
    result = _seeded_code.issn(mask='##_##-##')
    assert result == '10_43-32'
    result = _seeded_code.issn()
    assert result == '1819-6001'
    result = _seeded_code.issn()
    assert result == '3389-0838'


def test_locale_code(code):
    result = code.locale_code()
    assert result in LOCALE_CODES


def test_seeded_locale_code(_seeded_code):
    result = _seeded_code.locale_code()
    assert result == 'ko'
    result = _seeded_code.locale_code()
    assert result == 'ar-sy'


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


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_isbn(_seeded_code):
    result = _seeded_code.isbn(fmt=ISBNFormat.ISBN13)
    assert result == '104-1-33218-196-0'
    result = _seeded_code.isbn()
    assert result == '133-1-89083-863-7'
    result = _seeded_code.isbn()
    assert result == '1-02654-235-1'


def test_isbn_non_enum(code):
    with pytest.raises(NonEnumerableError):
        code.isbn(fmt='nil')
