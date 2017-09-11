from mimesis.data import CALLING_CODES, CONTINENT_CODES, \
    COUNTRIES_ISO, SHORTENED_ADDRESS_FMT
from mimesis.providers import BaseProvider
from mimesis.utils import pull


class Address(BaseProvider):
    """Class for generate fake address data."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('address.json', self.locale)

    def street_number(self, maximum=1400):
        """Generate a random street number.

        :return: Street number.
        :Example:
            134.
        """
        number = self.random.randint(1, int(maximum))
        return '%s' % number

    def street_name(self):
        """Get a random street name.

        :return: Street name.
        :Example:
           Candlewood.
        """
        names = self.data['street']['name']
        return self.random.choice(names)

    def street_suffix(self):
        """Get a random street suffix.

        :return: Street suffix.
        :Example:
            Alley.
        """
        suffixes = self.data['street']['suffix']
        return self.random.choice(suffixes)

    def address(self):
        """Get a random full address (include Street number, suffix and name).

        :return: Full address.
        :Example:
            5 Central Sideline.
        """
        fmt = self.data['address_fmt']

        st_num = self.street_number()
        st_name = self.street_name()

        if self.locale in SHORTENED_ADDRESS_FMT:
            return fmt.format(
                st_num=st_num,
                st_name=st_name,
            )

        if self.locale == 'ja':
            cities = self.data['city']
            city = self.random.choice(cities)

            n, nn, nnn = self.random.randints(3, 1, 100)
            return fmt.format(city=city, n=n, nn=nn, nnn=nnn)

        return fmt.format(
            st_num=st_num,
            st_name=st_name,
            st_sfx=self.street_suffix(),

        )

    def state(self, abbr=False):
        """Get a random states or subject of country.

        :param abbr:
            If True then return ISO (ISO 3166-2)
            code of state/region/province/subject.
        :return: State of current country.
        :Example:
            Alabama (for locale `en`).
        """
        key = 'abbr' if abbr else 'name'
        states = self.data['state'][key]
        return self.random.choice(states)

    def postal_code(self):
        """Generate a postal code for current locale.

        :return: Postal code.
        :Example:
            389213
        """
        from mimesis.providers import Code

        mask = self.data['postal_code_fmt']
        return Code(self.locale).custom_code(mask)

    def country_iso(self, fmt='iso2'):
        """Get a random ISO code of country.

        :param fmt: Format of code (iso2, iso3, numeric).
        :return: ISO Code.
        :Example:
            DE
        """
        sup = ''.join(list(COUNTRIES_ISO.keys()))

        if fmt not in COUNTRIES_ISO:
            raise KeyError('Unsupported format. Use: {}'.format(sup))

        countries = COUNTRIES_ISO[fmt]
        return self.random.choice(countries)

    def country(self):
        """Get a random country.

        :return: The Country.
        :Example:
            Russia.
        """
        countries = self.data['country']['name']
        return self.random.choice(countries)

    def city(self):
        """Get a random city for current locale.

        :return: City name.
        :Example:
            Saint Petersburg.
        """
        cities = self.data['city']
        return self.random.choice(cities)

    def latitude(self):
        """Generate a random value of latitude (-90 to +90).

        :return: Value of longitude.
        :Example:
            -66.4214188124611
        """
        return self.random.uniform(-90, 90)

    def longitude(self):
        """Generate a random value of longitude (-180 to +180).

        :return: Value of longitude.
        :Example:
            112.18440260511943
        """
        return self.random.uniform(-180, 180)

    def coordinates(self):
        """Generate random geo coordinates.

        :return: Dict with coordinates.
        :rtype: dict
        :Example:
            {'latitude': 8.003968712834975, 'longitude': 36.02811153405548}
        """
        coord = {
            'longitude': self.longitude(),
            'latitude': self.latitude(),
        }
        return coord

    def continent(self, code=False):
        """Get a random continent name or continent
        code (code in international format).

        :return: Continent name.
        :Example:
            Africa (en)
        """
        if code:
            codes = CONTINENT_CODES
            return self.random.choice(codes)

        continents = self.data['continent']
        return self.random.choice(continents)

    def calling_code(self):
        """Get a random calling code of random country.

        :return: Calling code.
        :Example:
            +7
        """
        return self.random.choice(CALLING_CODES)
