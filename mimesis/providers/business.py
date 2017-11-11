from mimesis.data import CURRENCIES, CURRENCY_SYMBOLS
from mimesis.providers.base import BaseProvider
from mimesis.utils import pull


class Business(BaseProvider):
    """Class for generating data for business."""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('business.json', self.locale)

    def company_type(self, abbr: bool = False) -> str:
        """Get a random type of business entity.

        :param bool abbr: If True then return abbreviated company type.
        :return: Types of business entity.

        :Example:
            Incorporated.
        """
        key = 'abbr' if abbr else 'title'
        company_type = self.data['company'].get(
            'type').get(key)
        return self.random.choice(company_type)

    def company(self) -> str:
        """Get a random company name.

        :return: Company name.

        :Example:
            Gamma Systems.
        """
        companies = self.data['company'].get('name')
        return self.random.choice(companies)

    def copyright(self) -> str:
        """Generate a random copyright.

        :return: Dummy copyright of company.

        :Example:
            © 1990-2016 Komercia, Inc.
        """
        return '© {company}, {company_type}'.format(
            company=self.company(),
            company_type=self.company_type(
                abbr=True,
            ),
        )

    def currency_iso(self) -> str:
        """Get a currency code. ISO 4217 format.

        :return: Currency code.

        :Example:
            RUR.
        """
        return self.random.choice(CURRENCIES)

    def price(self, minimum: float = 10.00, maximum: float = 1000.00) -> str:
        """Generate a random price.

        :param float minimum: Max value of price.
        :param float maximum: Min value of price.
        :return: Price.

        :Example:
            599.99 $.
        """
        currencies = CURRENCY_SYMBOLS

        price = self.random.uniform(
            float(minimum),
            float(maximum),
        )

        fmt = '{0:.2f} {1}'

        if self.locale in currencies:
            return fmt.format(price, currencies[self.locale])

        return fmt.format(price, currencies['default'])
