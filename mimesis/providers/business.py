from mimesis.data import CURRENCIES, CURRENCY_SYMBOLS
from mimesis.providers import BaseProvider
from mimesis.utils import pull


class Business(BaseProvider):
    """Class for generating data for business."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('business.json', self.locale)

    def company_type(self, abbr=False):
        """Get a random type of business entity.

        :param abbr: If True then return abbreviated company type.
        :return: Types of business entity.
        :Example:
            Incorporated.
        """
        key = 'abbr' if abbr else 'title'
        company_type = self.data['company']['type'][key]
        return self.random.choice(company_type)

    def company(self):
        """Get a random company name.

        :return: Company name.
        :Example:
            Gamma Systems.
        """
        companies = self.data['company']['name']
        return self.random.choice(companies)

    def copyright(self):
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

    def currency_iso(self):
        """Get a currency code. ISO 4217 format.

        :return: Currency code.
        :Example:
            RUR.
        """
        return self.random.choice(CURRENCIES)

    def price(self, minimum=10.00, maximum=1000.00):
        """Generate a random price.

        :param minimum: Max value of price.
        :param maximum: Min value of price.
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
