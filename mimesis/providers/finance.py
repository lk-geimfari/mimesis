"""Business data provider."""

import typing as t

from mimesis.data import (
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
    """Class for generating finance data."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._datafile = "finance.json"
        self._load_datafile(self._datafile)

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "finance"

    def company(self) -> str:
        """Get a random company name.

        :return: Company name.
        """
        names: t.List[str] = self.extract(["company", "name"])

        return self.random.choice(names)

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.
        """
        key = "abbr" if abbr else "title"

        company_types: t.List[str] = self.extract(["company", "type", key])
        return self.random.choice(company_types)

    def currency_iso_code(self, allow_random: bool = False) -> str:
        """Get code of the currency for current locale.

        :param allow_random: Get a random ISO code.
        :return: Currency code.
        """
        code: str = self.extract(["currency-code"])

        if allow_random:
            return self.random.choice(CURRENCY_ISO_CODES)
        return code

    def cryptocurrency_iso_code(self) -> str:
        """Get symbol of random cryptocurrency.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_ISO_CODES)

    def currency_symbol(self) -> str:
        """Get a currency symbol for current locale.

        :return: Currency symbol.
        """
        return CURRENCY_SYMBOLS[self.locale]

    def cryptocurrency_symbol(self) -> str:
        """Get a cryptocurrency symbol.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

    def price(self, minimum: float = 500, maximum: float = 1500) -> float:
        """Generate random price.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price.
        """
        return self.random.uniform(
            minimum,
            maximum,
            precision=2,
        )

    def price_in_btc(self, minimum: float = 0, maximum: float = 2) -> float:
        """Generate random price in BTC.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price in BTC.
        """
        return self.random.uniform(
            minimum,
            maximum,
            precision=7,
        )

    def stock_ticker(self) -> str:
        """Returns random stock ticker.

        :return: Ticker.
        """
        return self.random.choice(STOCK_TICKERS)

    def stock_name(self) -> str:
        """Returns stock name.

        :return: Stock name.
        """
        return self.random.choice(STOCK_NAMES)

    def stock_exchange(self) -> str:
        """Returns stock exchange name.

        :return: Returns exchange name.
        """
        return self.random.choice(STOCK_EXCHANGES)
