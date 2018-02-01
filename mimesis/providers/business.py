"""Business data provider."""

from mimesis.data import (CRYPTOCURRENCY_ISO_CODES, CRYPTOCURRENCY_SYMBOLS,
                          CURRENCY_ISO_CODES, CURRENCY_SYMBOLS)
from mimesis.providers.base import BaseDataProvider
from mimesis.utils import pull

__all__ = ['Business']


class Business(BaseDataProvider):
    """Class for generating data for business."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('business.json', self.locale)

    def company(self) -> str:
        """Get a random company name.

        :return: Company name.

        :Example:
            Gamma Systems.
        """
        return self.random.choice(
            self._data['company']['name'])

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.

        :Example:
            Incorporated.
        """
        return self.random.choice(
            self._data['company']['type'].get(
                'abbr' if abbr else 'title'),
        )

    def copyright(self) -> str:
        """Generate a random copyright.

        :return: Copyright of company.

        :Example:
            © Komercia, Inc.
        """
        return '© {}, {}'.format(
            self.company(),
            self.company_type(abbr=True),
        )

    def currency_iso_code(self) -> str:
        """Get code of the currency.

        :return: Currency code.

        :Example:
            RUR.
        """
        return self.random.choice(CURRENCY_ISO_CODES)

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

        :Example:
            Ƀ
        """
        return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

    def price(self, minimum: float = 10.00,
              maximum: float = 1000.00) -> str:
        """Generate a random price.

        :param minimum: Max value of price.
        :param maximum: Min value of price.
        :return: Price.

        :Example:
            599.99 $.
        """
        price = self.random.uniform(minimum, maximum, precision=2)
        return '{0} {1}'.format(price, self.currency_symbol())

    def price_in_btc(self, minimum: float = 0, maximum: float = 2) -> str:
        """Generate random price in BTC.

        :param minimum: Minimum value of price
        :param maximum: Maximum value of price.
        :return: Price in BTC.

        :Example:
            0.5885238 BTC
        """
        return '{} BTC'.format(
            self.random.uniform(
                minimum,
                maximum,
                precision=7,
            ),
        )
