"""Business data provider."""

from decimal import Decimal

from mimesis.datasets import (
    CRYPTOCURRENCY_ISO_CODES,
    CRYPTOCURRENCY_SYMBOLS,
    CURRENCY_ISO_CODES,
    CURRENCY_SYMBOLS,
    STOCK_EXCHANGES,
    STOCK_NAMES,
    STOCK_TICKERS,
)
from mimesis.providers.base import BaseDataProvider

__all__ = ["Finance"]


class Finance(BaseDataProvider):
    """Class to generate finance and business related data."""

    class Meta:
        name = "finance"
        datafile = f"{name}.json"

    def company(self) -> str:
        """Generates a random company name.

        :return: Company name.
        """
        names: list[str] = self._extract(["company", "name"])

        return self.random.choice(names)

    def company_type(self, abbr: bool = False) -> str:
        """Generates a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.
        """
        key = "abbr" if abbr else "title"

        company_types: list[str] = self._extract(["company", "type", key])
        return self.random.choice(company_types)

    def currency_iso_code(self, allow_random: bool = False) -> str:
        """Returns a currency code for current locale.

        :param allow_random: Get a random ISO code.
        :return: Currency code.
        """
        code: str = self._extract(["currency-code"])

        if allow_random:
            return self.random.choice(CURRENCY_ISO_CODES)
        return code

    def bank(self) -> str:
        """Generates a random bank name.

        :return: Bank name.
        """
        banks: list[str] = self._extract(["banks"])
        return self.random.choice(banks)

    def cryptocurrency_iso_code(self) -> str:
        """Generates a random cryptocurrency ISO code.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_ISO_CODES)

    def currency_symbol(self) -> str:
        """Returns a currency symbol for current locale.

        :return: Currency symbol.
        """
        return CURRENCY_SYMBOLS[self.locale]

    def cryptocurrency_symbol(self) -> str:
        """Get a cryptocurrency symbol.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

    def price(
        self,
        minimum: float = 500,
        maximum: float = 1500,
        precision: int = 2,
        as_decimal: bool = False,
    ) -> float | Decimal:
        """Generate a random price.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :param precision: Number of decimal places (default 2).
        :param as_decimal: If True, returns Decimal for high-precision.
        :return: Price as float or Decimal.
        """
        if as_decimal:
            factor = Decimal(10) ** precision
            min_units = int(Decimal(str(minimum)) * factor)
            max_units = int(Decimal(str(maximum)) * factor)
            units = self.random.randint(min_units, max_units)
            return Decimal(units) / factor
        return self.random.uniform(minimum, maximum, precision=precision)

    def price_in_btc(
        self,
        minimum: float = 0,
        maximum: float = 2,
        precision: int = 8,
        as_decimal: bool = False,
    ) -> float | Decimal:
        """Generates a random price in BTC.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :param precision: Number of decimal places (default 8 for satoshi).
        :param as_decimal: If True, returns Decimal for high-precision.
        :return: Price in BTC as float or Decimal.
        """
        if as_decimal:
            factor = Decimal(10) ** precision
            min_units = int(Decimal(str(minimum)) * factor)
            max_units = int(Decimal(str(maximum)) * factor)
            units = self.random.randint(min_units, max_units)
            return Decimal(units) / factor
        return self.random.uniform(minimum, maximum, precision=precision)

    def stock_ticker(self) -> str:
        """Generates a random stock ticker.

        :return: Ticker.
        """
        return self.random.choice(STOCK_TICKERS)

    def stock_name(self) -> str:
        """Generates a stock name.

        :return: Stock name.
        """
        return self.random.choice(STOCK_NAMES)

    def stock_exchange(self) -> str:
        """Generates a stock exchange name.

        :return: Returns exchange name.
        """
        return self.random.choice(STOCK_EXCHANGES)
