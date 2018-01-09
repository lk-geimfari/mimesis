# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Business
from mimesis.data import (CRYPTOCURRENCY_ISO_CODES, CRYPTOCURRENCY_SYMBOLS,
                          CURRENCY_ISO_CODES, CURRENCY_SYMBOLS)

from . import _patterns as p


@pytest.fixture()
def _business():
    return Business()


def test_str(business):
    assert re.match(p.STR_REGEX, str(business))


def test_copyright(business):
    result = business.copyright()
    assert '©' in result


def test_currency_iso_code(_business):
    result = _business.currency_iso_code()
    assert result in CURRENCY_ISO_CODES


def test_cryptocurrency_iso_code(_business):
    result = _business.cryptocurrency_iso_code()
    assert result in CRYPTOCURRENCY_ISO_CODES


def test_currency_symbol(business):
    result = business.currency_symbol()
    assert result in CURRENCY_SYMBOLS.values()


def test_cryptocurrency_symbol(business):
    result = business.cryptocurrency_symbol()
    assert result in CRYPTOCURRENCY_SYMBOLS


@pytest.mark.parametrize(
    'abbr, key', [
        (False, 'title'),
        (True, 'abbr'),
    ],
)
def test_company_type(business, abbr, key):
    result = business.company_type(abbr=abbr)
    assert result in business._data['company']['type'][key]


def test_company(business):
    result = business.company()
    assert result in business._data['company']['name']


def test_price(business):
    result = business.price(minimum=100.00, maximum=1999.99)
    price, symbol = result.split(' ')
    assert isinstance(price, str)
    assert float(price) >= 100.00
    assert float(price) <= 1999.99
    assert symbol.strip() in CURRENCY_SYMBOLS[business.locale]


@pytest.mark.parametrize(
    'minimum, maximum', [
        (1, 2),
        (2, 4),
        (4, 16),
    ],
)
def test_price_in_btc(_business, minimum, maximum):
    result = _business.price_in_btc(minimum, maximum)
    price, symbol = result.split(' ')
    assert float(price) >= minimum
    assert float(price) <= maximum
    assert symbol == 'BTC'
