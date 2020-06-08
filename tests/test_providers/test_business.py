# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Business
from mimesis.data import (
    CRYPTOCURRENCY_ISO_CODES,
    CRYPTOCURRENCY_SYMBOLS,
    CURRENCY_ISO_CODES,
    CURRENCY_SYMBOLS,
)

from . import patterns


class TestBusiness(object):

    @pytest.fixture()
    def _business(self):
        return Business()

    def test_str(self, business):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(business))

    def test_copyright(self, business):
        result = business.copyright()
        assert '©' in result

    def test_currency_iso_code(self, business):
        result1 = business.currency_iso_code()
        result2 = business.currency_iso_code()
        assert result1 == result2

        result = business.currency_iso_code(allow_random=True)
        assert result in CURRENCY_ISO_CODES

    def test_cryptocurrency_iso_code(self, _business):
        result = _business.cryptocurrency_iso_code()
        assert result in CRYPTOCURRENCY_ISO_CODES

    def test_currency_symbol(self, business):
        result = business.currency_symbol()
        assert result in CURRENCY_SYMBOLS.values()

    def test_cryptocurrency_symbol(self, business):
        result = business.cryptocurrency_symbol()
        assert result in CRYPTOCURRENCY_SYMBOLS

    @pytest.mark.parametrize(
        'abbr, key', [
            (False, 'title'),
            (True, 'abbr'),
        ],
    )
    def test_company_type(self, business, abbr, key):
        result = business.company_type(abbr=abbr)
        assert result in business._data['company']['type'][key]

    def test_company(self, business):
        result = business.company()
        assert result in business._data['company']['name']

    def test_price(self, business):
        result = business.price(minimum=100.00, maximum=1999.99)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        'minimum, maximum', [
            (1, 2),
            (2, 4),
            (4, 16),
        ],
    )
    def test_price_in_btc(self, _business, minimum, maximum):
        result = _business.price_in_btc(minimum, maximum)
        price, symbol = result.split(' ')
        assert float(price) >= minimum
        assert float(price) <= maximum
        assert symbol == 'BTC'


class TestSeededBusiness(object):

    @pytest.fixture()
    def b1(self, seed):
        return Business(seed=seed)

    @pytest.fixture()
    def b2(self, seed):
        return Business(seed=seed)

    def test_copyright(self, b1, b2):
        assert b1.copyright() == b2.copyright()

    def test_currency_iso_code(self, b1, b2):
        assert b1.currency_iso_code() == b2.currency_iso_code()

    def test_cryptocurrency_iso_code(self, b1, b2):
        assert b1.cryptocurrency_iso_code() == b2.cryptocurrency_iso_code()

    def test_currency_symbol(self, b1, b2):
        assert b1.currency_symbol() == b2.currency_symbol()

    def test_cryptocurrency_symbol(self, b1, b2):
        assert b1.cryptocurrency_symbol() == b2.cryptocurrency_symbol()

    def test_company_type(self, b1, b2):
        assert b1.company_type() == b2.company_type()
        assert b1.company_type(abbr=True) == b2.company_type(abbr=True)

    def test_company(self, b1, b2):
        assert b1.company() == b2.company()

    def test_price(self, b1, b2):
        assert b1.price() == b2.price()
        assert b1.price_in_btc(1.11, 22.2) == \
            b2.price_in_btc(1.11, 22.2)

    def test_price_in_btc(self, b1, b2):
        assert b1.price_in_btc() == b2.price_in_btc()
