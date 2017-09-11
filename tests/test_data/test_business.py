# -*- coding: utf-8 -*-
import re

import pytest

import mimesis
from mimesis.data import CURRENCIES, CURRENCY_SYMBOLS

from . import _patterns as p


@pytest.fixture()
def _business():
    return mimesis.Business()


def test_str(business):
    assert re.match(p.STR_REGEX, str(business))


def test_copyright(business):
    result = business.copyright()
    assert '©' in result


def test_currency_iso(_business):
    result = _business.currency_iso()
    assert result in CURRENCIES


def test_company_type(business):
    result = business.company_type()
    assert result in business.data['company']['type']['title']

    result_2 = business.company_type(abbr=True)
    assert result_2 in business.data['company']['type']['abbr']


def test_company(business):
    result = business.company()
    assert result in business.data['company']['name']


def test_price(business):
    currencies = CURRENCY_SYMBOLS[business.locale]
    result = business.price(minimum=100.00, maximum=1999.99)
    price, symbol = result.split(' ')
    assert isinstance(price, str)
    assert float(price) >= 100.00
    assert float(price) <= 1999.99
    assert symbol in currencies

    business.locale = 'xx'
    assert CURRENCY_SYMBOLS['default'] in business.price()
