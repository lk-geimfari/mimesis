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

        >>> business = Business()
        >>> company = business.company()
        >>> company in business._data['company']['name']
        True
        """
        return self.random.choice(self._data['company']['name'])

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.

        :Example:

        >>> business = Business()
        >>> company_type = business.company_type()
        >>> company_type in business._data['company']['type']['title']
        True
        >>> company_type = business.company_type(abbr=True)
        >>> company_type in business._data['company']['type']['abbr']
        True
        """
        key = 'abbr' if abbr else 'title'
        return self.random.choice(
            self._data['company']['type'][key],
        )

    def copyright(self) -> str:  # noqa: A003
        """Generate a random copyright.

        :return: Copyright of company.

        :Example:

        >>> business = Business()
        >>> _copyright = business.copyright()
        >>> isinstance(_copyright, str)
        True
        """
        return '© {}, {}'.format(
            self.company(),
            self.company_type(abbr=True),
        )

    def currency_iso_code(self) -> str:
        """Get code of the currency.

        :return: Currency code.

        :Example:

        >>> business = Business()
        >>> code = business.currency_iso_code()
        >>> code in CURRENCY_ISO_CODES
        True
        """
        return self.random.choice(CURRENCY_ISO_CODES)

    def cryptocurrency_iso_code(self) -> str:
        """Get symbol of random cryptocurrency.

        :return: Symbol of cryptocurrency.

        :Example:

        >>> business = Business()
        >>> code = business.cryptocurrency_iso_code()
        >>> code in CRYPTOCURRENCY_ISO_CODES
        True
        """
        return self.random.choice(CRYPTOCURRENCY_ISO_CODES)

    def currency_symbol(self):
        """Get a currency symbol for current locale.

        :return: Currency symbol.

        :Example:

        >>> business = Business()
        >>> symbol = business.currency_symbol()
        >>> symbol in CURRENCY_SYMBOLS.values()
        True
        """
        return CURRENCY_SYMBOLS[self.locale]

    def cryptocurrency_symbol(self) -> str:
        """Get a cryptocurrency symbol.

        :return: Symbol of cryptocurrency.

        :Example:

        >>> business = Business()
        >>> symbol = business.cryptocurrency_symbol()
        >>> symbol in CRYPTOCURRENCY_SYMBOLS
        True
        """
        return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

    def price(self, minimum: float = 10.00,
              maximum: float = 1000.00) -> str:
        """Generate a random price.

        :param minimum: Max value of price.
        :param maximum: Min value of price.
        :return: Price.

        :Example:

        >>> business = Business()
        >>> price = business.price()
        >>> isinstance(price, str)
        True
        >>> '$' in price
        True
        """
        price = self.random.uniform(minimum, maximum, precision=2)
        return '{0} {1}'.format(price, self.currency_symbol())

    def price_in_btc(self, minimum: float = 0, maximum: float = 2) -> str:
        """Generate random price in BTC.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price in BTC.

        :Example:

        >>> business = Business()
        >>> price = business.price_in_btc()
        >>> isinstance(price, str)
        True
        """
        return '{} BTC'.format(
            self.random.uniform(
                minimum,
                maximum,
                precision=7,
            ),
        )
