# -*- coding: utf-8 -*-

"""Business data provider."""

from mimesis.data import (
    CRYPTOCURRENCY_ISO_CODES,
    CRYPTOCURRENCY_SYMBOLS,
    CURRENCY_ISO_CODES,
    CURRENCY_SYMBOLS,
)
from mimesis.providers.base import BaseDataProvider

__all__ = ['Business']


class Business(BaseDataProvider):
    """Class for generating data for business."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'business.json'
        self._pull(self._datafile)

    class Meta:
        """Class for metadata."""

        name = 'business'

    def company(self) -> str:
        """Get a random company name.

        :return: Company name.
        """
        return self.random.choice(self._data['company']['name'])

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.
        """
        key = 'abbr' if abbr else 'title'
        return self.random.choice(
            self._data['company']['type'][key],
        )

    def copyright(self) -> str:  # noqa: A003
        """Generate a random copyright.

        :return: Copyright of company.
        """
        return '© {}, {}'.format(
            self.company(),
            self.company_type(abbr=True),
        )

    def currency_iso_code(self, allow_random: bool = False) -> str:
        """Get code of the currency for current locale.

        :param allow_random: Get a random ISO code.
        :return: Currency code.
        """
        if allow_random:
            return self.random.choice(CURRENCY_ISO_CODES)
        return self._data['currency-code']

    def cryptocurrency_iso_code(self) -> str:
        """Get symbol of random cryptocurrency.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_ISO_CODES)

    def currency_symbol(self):
        """Get a currency symbol for current locale.

        :return: Currency symbol.
        """
        return CURRENCY_SYMBOLS[self.locale]

    def cryptocurrency_symbol(self) -> str:
        """Get a cryptocurrency symbol.

        :return: Symbol of cryptocurrency.
        """
        return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

    def price(self, minimum: float = 10.00,
              maximum: float = 1000.00) -> str:
        """Generate a random price.

        :param minimum: Max value of price.
        :param maximum: Min value of price.
        :return: Price.
        """
        price_format = self._data['price-format']
        numeric_frac_digits = self._data['numeric-frac-digits']
        delims = {
            '.': self._data['numeric-decimal'],
            ',': self._data['numeric-thousands'],
        }

        value = self.random.uniform(minimum, maximum)
        price = '{:,.{}f}'.format(value, numeric_frac_digits)

        price = ''.join(delims.get(char, char) for char in price)

        return price_format.replace('#', price)

    def price_in_btc(self, minimum: float = 0, maximum: float = 2) -> str:
        """Generate random price in BTC.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price in BTC.
        """
        return '{} BTC'.format(
            self.random.uniform(
                minimum,
                maximum,
                precision=7,
            ),
        )
