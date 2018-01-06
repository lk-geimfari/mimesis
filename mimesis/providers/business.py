from mimesis.data import (CRYPTOCURRENCY_ISO_CODES, CRYPTOCURRENCY_SYMBOLS,
                          CURRENCY_ISO_CODES, CURRENCY_SYMBOLS)
from mimesis.providers.base import BaseDataProvider
from mimesis.utils import pull


class Business(BaseDataProvider):
    """Class for generating data for business."""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('business.json', self.locale)

    def company(self) -> str:
        """Get a random company name.

        :return: Company name.

        :Example:
            Gamma Systems.
        """
        companies = self._data['company']['name']
        return self.random.choice(companies)

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param bool abbr: Abbreviated company type.
        :return: Types of business entity.

        :Example:
            Incorporated.
        """
        key = 'abbr' if abbr else 'title'
        company_type = self._data['company']['type']
        return self.random.choice(
            company_type.get(key),
        )

    def copyright(self) -> str:
        """Generate a random copyright.

        :return: Copyright of company.

        :Example:
            © Komercia, Inc.
        """
        return '© {}, {}'.format(
            self.company(),
            self.company_type(True),
        )

    def currency_iso_code(self, crypto: bool = False) -> str:
        """Get a currency code. ISO 4217 format.

        :param crypto: Return ISO code of cryptocurrency.
        :return: Currency code.

        :Example:
            RUR.
        """
        if crypto:
            return self.random.choice(
                CRYPTOCURRENCY_ISO_CODES)

        return self.random.choice(CURRENCY_ISO_CODES)

    def currency_symbol(self, crypto: bool = False):
        """Get a currency symbol for current locale.

        :param crypto: Return symbol of cryptocurrency.
        :return: Currency symbol.

        :Example:
            Ƀ
        """
        if crypto:
            return self.random.choice(CRYPTOCURRENCY_SYMBOLS)

        return CURRENCY_SYMBOLS[self.locale]

    def price(self, minimum: float = 10.00,
              maximum: float = 1000.00) -> str:
        """Generate a random price.

        :param float minimum: Max value of price.
        :param float maximum: Min value of price.
        :return: Price.

        :Example:
            599.99 $.
        """
        currencies = CURRENCY_SYMBOLS
        price = self.random.uniform(minimum, maximum)

        fmt = '{0:.2f} {1}'

        if self.locale in currencies:
            return fmt.format(price, currencies[self.locale])

        return fmt.format(price, currencies['default'])

    def price_in_btc(self, minimum: float = 0, maximum: float = 2) -> str:
        """Generate random price in BTC.

        :param minimum: Minimum value of price
        :param maximum: Maximum value of price.
        :return: Price in BTC.

        :Example:
            0.5885238 BTC
        """
        return '{:.7f} BTC'.format(
            self.random.uniform(
                minimum,
                maximum,
            ),
        )
