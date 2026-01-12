import re
from decimal import Decimal

import pytest

from mimesis import Finance
from mimesis.datasets import (
    CRYPTOCURRENCY_ISO_CODES,
    CRYPTOCURRENCY_SYMBOLS,
    CURRENCY_ISO_CODES,
    CURRENCY_SYMBOLS,
    STOCK_EXCHANGES,
    STOCK_NAMES,
    STOCK_TICKERS,
)

from .. import patterns


class TestFinance:
    @pytest.fixture()
    def _finance(self):
        return Finance()

    def test_str(self, finance):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(finance))

    def test_stock_ticker(self, finance):
        result = finance.stock_ticker()
        assert result in STOCK_TICKERS

    def test_stock_name(self, finance):
        result = finance.stock_name()
        assert result in STOCK_NAMES

    def test_stock_exchange(self, finance):
        result = finance.stock_exchange()
        assert result in STOCK_EXCHANGES

    def test_currency_iso_code(self, finance):
        result1 = finance.currency_iso_code()
        result2 = finance.currency_iso_code()
        assert result1 == result2

        result = finance.currency_iso_code(allow_random=True)
        assert result in CURRENCY_ISO_CODES

    def test_cryptocurrency_iso_code(self, _finance):
        result = _finance.cryptocurrency_iso_code()
        assert result in CRYPTOCURRENCY_ISO_CODES

    def test_currency_symbol(self, finance):
        result = finance.currency_symbol()
        assert result in CURRENCY_SYMBOLS.values()

    def test_cryptocurrency_symbol(self, finance):
        result = finance.cryptocurrency_symbol()
        assert result in CRYPTOCURRENCY_SYMBOLS

    @pytest.mark.parametrize(
        "abbr, key",
        [
            (False, "title"),
            (True, "abbr"),
        ],
    )
    def test_company_type(self, finance, abbr, key):
        result = finance.company_type(abbr=abbr)
        assert result in finance._dataset["company"]["type"][key]

    def test_bank(self, finance):
        result = finance.bank()
        assert result in finance._dataset["banks"]

    def test_company(self, finance):
        result = finance.company()
        assert result in finance._dataset["company"]["name"]

    def test_price(self, finance):
        result = finance.price(minimum=100.00, maximum=1999.99)
        assert isinstance(result, float)

    def test_price_as_decimal(self, finance):
        result = finance.price(minimum=100.00, maximum=1999.99, as_decimal=True)
        assert isinstance(result, Decimal)
        assert result >= Decimal("100.00")
        assert result <= Decimal("1999.99")

    @pytest.mark.parametrize(
        "minimum, maximum",
        [
            (1, 2),
            (2, 4),
            (4, 16),
        ],
    )
    def test_price_in_btc(self, _finance, minimum, maximum):
        price = _finance.price_in_btc(minimum, maximum)
        assert float(price) >= minimum
        assert float(price) <= maximum

    def test_price_in_btc_as_decimal(self, _finance):
        result = _finance.price_in_btc(minimum=0.5, maximum=1.5, as_decimal=True)
        assert isinstance(result, Decimal)
        assert result >= Decimal("0.5")
        assert result <= Decimal("1.5")

    def test_price_precision(self, _finance):
        result = _finance.price(minimum=10, maximum=100, precision=4, as_decimal=True)
        assert isinstance(result, Decimal)
        decimal_places = abs(result.as_tuple().exponent)
        assert decimal_places <= 4

    def test_price_in_btc_precision(self, _finance):
        result = _finance.price_in_btc(
            minimum=0, maximum=1, precision=4, as_decimal=True
        )
        assert isinstance(result, Decimal)
        decimal_places = abs(result.as_tuple().exponent)
        assert decimal_places <= 4


class TestSeededFinance:
    @pytest.fixture()
    def f1(self, seed):
        return Finance(seed=seed)

    @pytest.fixture()
    def f2(self, seed):
        return Finance(seed=seed)

    def test_stock_ticker(self, f1, f2):
        assert f1.stock_ticker() == f2.stock_ticker()

    def test_stock_name(self, f1, f2):
        assert f1.stock_name() == f2.stock_name()

    def test_stock_exchange(self, f1, f2):
        assert f1.stock_exchange() == f2.stock_exchange()

    def test_currency_iso_code(self, f1, f2):
        assert f1.currency_iso_code() == f2.currency_iso_code()

    def test_cryptocurrency_iso_code(self, f1, f2):
        assert f1.cryptocurrency_iso_code() == f2.cryptocurrency_iso_code()

    def test_currency_symbol(self, f1, f2):
        assert f1.currency_symbol() == f2.currency_symbol()

    def test_cryptocurrency_symbol(self, f1, f2):
        assert f1.cryptocurrency_symbol() == f2.cryptocurrency_symbol()

    def test_company_type(self, f1, f2):
        assert f1.company_type() == f2.company_type()
        assert f1.company_type(abbr=True) == f2.company_type(abbr=True)

    def test_company(self, f1, f2):
        assert f1.company() == f2.company()

    def test_price(self, f1, f2):
        assert f1.price() == f2.price()
        assert f1.price(1.11, 22.2) == f2.price(1.11, 22.2)

    def test_price_in_btc(self, f1, f2):
        assert f1.price_in_btc() == f2.price_in_btc()
        assert f1.price_in_btc(1.11, 22.2) == f2.price_in_btc(1.11, 22.2)

    def test_price_as_decimal(self, f1, f2):
        assert f1.price(as_decimal=True) == f2.price(as_decimal=True)

    def test_price_in_btc_as_decimal(self, f1, f2):
        assert f1.price_in_btc(as_decimal=True) == f2.price_in_btc(as_decimal=True)

    def test_bank(self, f1, f2):
        assert f1.bank() == f2.bank()
