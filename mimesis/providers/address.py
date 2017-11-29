from typing import Optional

from mimesis.data import (CALLING_CODES, CONTINENT_CODES, COUNTRIES_ISO,
                          SHORTENED_ADDRESS_FMT)
from mimesis.enums import CountryCode
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider
from mimesis.utils import custom_code, pull


class Address(BaseProvider):
    """Class for generate fake address data."""

    def __init__(self, *args, **kwargs):
        """
        :param str locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('address.json', self.locale)

    def street_number(self, maximum: int = 1400) -> str:
        """Generate a random street number.

        :param int maximum: Maximum value.
        :return: Street number.

        :Example:
            134.
        """
        number = self.random.randint(1, int(maximum))
        return '{}'.format(number)

    def street_name(self) -> str:
        """Get a random street name.

        :return: Street name.

        :Example:
           Candlewood.
        """
        names = self.data['street'].get('name')
        return self.random.choice(names)

    def street_suffix(self) -> str:
        """Get a random street suffix.

        :return: Street suffix.

        :Example:
            Alley.
        """
        suffixes = self.data['street'].get('suffix')
        return self.random.choice(suffixes)

    def address(self) -> str:
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

    def state(self, abbr: bool = False) -> str:
        """Get a random administrative district of country.

        :param bool abbr: Return ISO 3166-2 code.
        :return: Administrative district.

        :Example:
            Alabama (for locale `en`).
        """
        key = 'abbr' if abbr else 'name'
        states = self.data['state'].get(key)
        return self.random.choice(states)

    def region(self, abbr: bool = False) -> str:
        """Get a random region.

        :param bool abbr: Return ISO 3166-2 code.
        :return: State.
        """
        return self.state(abbr)

    def province(self, abbr: bool = False) -> str:
        """Get a random province.

        :param bool abbr: Return ISO 3166-2 code.
        :return: Province.
        """
        return self.state(abbr)

    def federal_subject(self, abbr: bool = False) -> str:
        """Get a random region.

        :param bool abbr: Return ISO 3166-2 code.
        :return: Federal subject.
        """
        return self.state(abbr)

    def postal_code(self) -> str:
        """Generate a postal code for current locale.

        :return: Postal code.

        :Example:
            389213
        """

        mask = self.data['postal_code_fmt']
        return custom_code(mask=mask)

    def country_iso_code(self, fmt: Optional[CountryCode] = None) -> str:
        """Get a random ISO code of country.

        :param fmt: Enum object CountryCode.
        :return: ISO Code.
        :raises KeyError: if fmt is not supported.

        :Example:
            DE
        """
        if fmt is None:
            fmt = CountryCode.get_random_item()

        if fmt and fmt in CountryCode:
            codes = COUNTRIES_ISO[fmt.value]
            return self.random.choice(codes)
        else:
            raise NonEnumerableError(CountryCode)

    def country(self) -> str:
        """Get a random country.

        :return: The Country.

        :Example:
            Russia.
        """
        countries = self.data['country'].get('name')
        return self.random.choice(countries)

    def city(self) -> str:
        """Get a random city for current locale.

        :return: City name.

        :Example:
            Saint Petersburg.
        """
        cities = self.data['city']
        return self.random.choice(cities)

    def latitude(self) -> float:
        """Generate a random value of latitude (-90 to +90).

        :return: Value of longitude.

        :Example:
            -66.4214188124611
        """
        return self.random.uniform(-90, 90)

    def longitude(self) -> float:
        """Generate a random value of longitude (-180 to +180).

        :return: Value of longitude.

        :Example:
            112.18440260511943
        """
        return self.random.uniform(-180, 180)

    def coordinates(self) -> dict:
        """Generate random geo coordinates.

        :return: Dict with coordinates.

        :Example:
            {'latitude': 8.003968712834975,
            'longitude': 36.02811153405548}
        """
        coord = {
            'longitude': self.longitude(),
            'latitude': self.latitude(),
        }
        return coord

    def continent(self, code: bool = False) -> str:
        """Get a random continent name or continent
        code (code in international format).

        :param bool code: Return code of continent.
        :return: Continent name.

        :Example:
            Africa (en)
        """
        if code:
            return self.random.choice(
                CONTINENT_CODES)

        continents = self.data['continent']
        return self.random.choice(continents)

    def calling_code(self) -> str:
        """Get a random calling code of random country.

        :return: Calling code.

        :Example:
            +7
        """
        return self.random.choice(CALLING_CODES)
