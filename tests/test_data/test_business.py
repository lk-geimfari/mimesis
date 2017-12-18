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


@pytest.fixture()
def _seeded_business():
    return Business(seed=42)


def test_str(business):
    assert re.match(p.STR_REGEX, str(business))


def test_copyright(business):
    result = business.copyright()
    assert '©' in result


def test_seeded_copyright(_seeded_business):
    result = _seeded_business.copyright()
    assert result == '© Briggs & Stratton, Corp.'
    result = _seeded_business.copyright()
    assert result == '© Interplay Entertainment, LLLP'


def test_currency_iso_code(_business):
    result = _business.currency_iso_code()
    assert result in CURRENCY_ISO_CODES
    result = _business.currency_iso_code(crypto=True)
    assert result in CRYPTOCURRENCY_ISO_CODES


def test_seeded_currency_iso_code(_seeded_business):
    result = _seeded_business.currency_iso_code(crypto=True)
    assert result == 'XZC'
    result = _seeded_business.currency_iso_code()
    assert result == 'CDF'
    result = _seeded_business.currency_iso_code()
    assert result == 'ARS'


def test_currency_symbol(business):
    result = business.currency_symbol()
    assert result in CURRENCY_SYMBOLS.values()
    result = business.currency_symbol(crypto=True)
    assert result in CRYPTOCURRENCY_SYMBOLS


def test_seeded_currency_symbol(_seeded_business):
    result = _seeded_business.currency_symbol(crypto=True)
    assert result == 'Ξ'
    result = _seeded_business.currency_symbol()
    assert result == '$'
    result = _seeded_business.currency_symbol()
    assert result == '$'


def test_company_type(business):
    result = business.company_type()
    assert result in business._data['company']['type']['title']

    result_2 = business.company_type(abbr=True)
    assert result_2 in business._data['company']['type']['abbr']


def test_seeded_company_type(_seeded_business):
    result = _seeded_business.company_type(abbr=True)
    assert result == 'Inc.'
    result = _seeded_business.company_type()
    assert result == 'Corporation'
    result = _seeded_business.company_type()
    assert result == 'Limited Liability Partnership'


def test_company(business):
    result = business.company()
    assert result in business._data['company']['name']


def test_seeded_company(_seeded_business):
    result = _seeded_business.company()
    assert result == 'Briggs & Stratton'
    result = _seeded_business.company()
    assert result == 'Agriprocessors'


def test_price(business):
    locale = business.get_current_locale()
    currencies = CURRENCY_SYMBOLS[locale]
    result = business.price(minimum=100.00, maximum=1999.99)
    price, symbol = result.split(' ')
    assert isinstance(price, str)
    assert float(price) >= 100.00
    assert float(price) <= 1999.99
    assert symbol in currencies

    business.locale = 'xx'
    assert CURRENCY_SYMBOLS['default'] in business.price()


def test_seeded_price(_seeded_business):
    result = _seeded_business.price(minimum=42, maximum=4200)
    assert result == '2700.74 $'
    result = _seeded_business.price()
    assert result == '34.76 $'
    result = _seeded_business.price()
    assert result == '282.28 $'


def test_price_in_btc(_business):
    result = _business.price_in_btc(minimum=0, maximum=2)
    price, symbol = result.split(' ')
    assert float(price) >= 0
    assert float(price) <= 2
    assert symbol == 'BTC'


def test_seeded_price_in_btc(_seeded_business):
    result = _seeded_business.price_in_btc(minimum=.42, maximum=42)
    assert result == '27.0073663 BTC'
    result = _seeded_business.price_in_btc()
    assert result == '0.0500215 BTC'
    result = _seeded_business.price_in_btc()
    assert result == '0.5500586 BTC'
