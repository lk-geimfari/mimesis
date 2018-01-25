"""Address data provider."""

from typing import Optional

from mimesis.data import (CALLING_CODES, CONTINENT_CODES, COORDINATE_RANGE,
                          COUNTRIES_ISO, SHORTENED_ADDRESS_FMT)
from mimesis.enums import CountryCode
from mimesis.providers.base import BaseDataProvider
from mimesis.utils import pull


class Address(BaseDataProvider):
    """Class for generate fake address data."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('address.json', self.locale)

    def street_number(self, maximum: int = 1400) -> str:
        """Generate a random street number.

        :param maximum: Maximum value.
        :return: Street number.

        :Example:
            134.
        """
        return str(self.random.randint(1, maximum))

    def street_name(self) -> str:
        """Get a random street name.

        :return: Street name.

        :Example:
           Candlewood.
        """
        return self.random.choice(
            self._data['street']['name'])

    def street_suffix(self) -> str:
        """Get a random street suffix.

        :return: Street suffix.

        :Example:
            Alley.
        """
        return self.random.choice(
            self._data['street']['suffix'])

    def address(self) -> str:
        """Generate a random full address.

        :return: Full address.

        :Example:
            5 Central Sideline.
        """
        fmt = self._data['address_fmt']

        st_num = self.street_number()
        st_name = self.street_name()

        if self.locale in SHORTENED_ADDRESS_FMT:
            return fmt.format(
                st_num=st_num,
                st_name=st_name,
            )

        if self.locale == 'ja':
            return fmt.format(
                self.random.choice(self._data['city']),
                *self.random.randints(3, 1, 100),
            )

        return fmt.format(
            st_num=st_num,
            st_name=st_name,
            st_sfx=self.street_suffix(),

        )

    def state(self, abbr: bool = False) -> str:
        """Get a random administrative district of country.

        :param abbr: Return ISO 3166-2 code.
        :return: Administrative district.

        :Example:
            Alabama.
        """
        return self.random.choice(
            self._data['state']['abbr' if abbr else 'name'])

    def region(self, *args, **kwargs) -> str:
        """Get a random region.

        :param bool abbr: Return ISO 3166-2 code.
        :return: State.
        """
        return self.state(*args, **kwargs)

    def province(self, *args, **kwargs) -> str:
        """Get a random province.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        :return: Province.
        """
        return self.state(*args, **kwargs)

    def federal_subject(self, *args, **kwargs) -> str:
        """Get a random region.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        :return: Federal subject.
        """
        return self.state(*args, **kwargs)

    def prefecture(self, *args, **kwargs) -> str:
        """Get a random prefecture.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        :return: Prefecture.
        """
        return self.state(*args, **kwargs)

    def postal_code(self) -> str:
        """Generate a postal code for current locale.

        :return: Postal code.

        :Example:
            389213
        """
        return self.random.custom_code(
            self._data['postal_code_fmt'])

    def country_iso_code(self, fmt: Optional[CountryCode] = None) -> str:
        """Get a random ISO code of country.

        :param fmt: Enum object CountryCode.
        :return: ISO Code.
        :raises KeyError: if fmt is not supported.

        :Example:
            DE
        """
        key = self._validate_enum(fmt, CountryCode)
        return self.random.choice(COUNTRIES_ISO[key])

    def country(self) -> str:
        """Get a random country.

        :return: The Country.

        :Example:
            Russia.
        """
        return self.random.choice(
            self._data['country']['name'])

    def city(self) -> str:
        """Get a random city.

        :return: City name.

        :Example:
            Saint Petersburg.
        """
        return self.random.choice(
            self._data['city'])

    def _get_from_range(self, key: Optional[str] = None,
                        code: Optional[str] = None) -> float:
        """Get range of latitude or longitude.

        This function returns coordinates for current locale by default,
        but you can change this behavior passed parameter ``country_code``
        which represent country code ISO 3166-1 alpha-2.

        :param key: Key (``lat`` or ``long``).
        :param code: Country code (ISO 3166-1 alpha-2).
        :return: Float number.
        """
        if code:
            code = code.lower()
            if code in COORDINATE_RANGE.keys():
                range_seq = COORDINATE_RANGE[code][key]
            else:
                raise ValueError('Country code must be "default" '
                                 'or ISO 3166-1 alpha-2 code string.')
        else:
            # Default is coordinates range for current locale.
            range_seq = self._data['coordinates'].get(key)

        result = self.random.uniform(*range_seq)
        return float('{:.6f}'.format(result))

    def latitude(self, country_code: Optional[str] = None) -> float:
        """Generate a random value of latitude.

        :return: Value of longitude.

        :Example:
            -66.421418
        """
        return self._get_from_range('lat', country_code)

    def longitude(self, country_code: Optional[str] = None) -> float:
        """Generate a random value of longitude.

        :return: Value of longitude.

        :Example:
            112.184402
        """
        return self._get_from_range('long', country_code)

    def coordinates(self, *args, **kwargs) -> dict:
        """Generate random geo coordinates.

        :return: Dict with coordinates.

        :Example:
            {'latitude': 8.003968,
            'longitude': 36.028111}
        """
        coordinates = dict(
            longitude=self.longitude(*args, **kwargs),
            latitude=self.latitude(*args, **kwargs),
        )
        return coordinates

    def continent(self, code: bool = False) -> str:
        """Get a random continent name or continent code.

        :param code: Return code of continent.
        :return: Continent name.

        :Example:
            Africa (en)
        """
        codes = CONTINENT_CODES if \
            code else self._data['continent']

        return self.random.choice(codes)

    def calling_code(self) -> str:
        """Get a random calling code of random country.

        :return: Calling code.

        :Example:
            +7
        """
        return self.random.choice(CALLING_CODES)
