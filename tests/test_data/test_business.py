# -*- coding: utf-8 -*-
import re

from mimesis.data import CURRENCIES, CURRENCY_SYMBOLS

from . import _patterns as p


def test_str(business):
    assert re.match(p.STR_REGEX, str(business))


def test_copyright(business):
    result = business.copyright()
    assert '©' in result


def test_currency_sio(business):
    result = business.currency_iso()
    assert result in CURRENCIES


def test_company_type(generic):
    result = generic.business.company_type()
    assert result in generic.business.data['company']['type']['title']

    result_2 = generic.business.company_type(abbr=True)
    assert result_2 in generic.business.data['company']['type']['abbr']


def test_company(generic):
    result = generic.business.company()
    assert result in generic.business.data['company']['name']


def test_price(generic):
    currencies = CURRENCY_SYMBOLS[generic.business.locale]
    result = generic.business.price(minimum=100.00, maximum=1999.99)
    price, symbol = result.split(' ')
    assert isinstance(price, str)
    assert float(price) >= 100.00
    assert float(price) <= 1999.99
    assert symbol in currencies

    # invalid locale should use default
    business = generic.business
    business.locale = 'xx'
    assert CURRENCY_SYMBOLS['default'] in business.price()
