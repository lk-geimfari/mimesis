# -*- coding: utf-8 -*-

"""Address module.

This module contains provider Address() and other utils which represents
data related to location, such as street name, city, country and etc.
"""

from typing import Optional, Union

from mimesis.data import (
    CALLING_CODES,
    CONTINENT_CODES,
    COUNTRY_CODES,
    SHORTENED_ADDRESS_FMT,
)
from mimesis.enums import CountryCode
from mimesis.providers.base import BaseDataProvider

__all__ = ['Address']


class Address(BaseDataProvider):
    """Class for generate fake address data.

    This object provides all the data related to
    geographical location.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'address.json'
        self._pull(self._datafile)

    class Meta:
        """Class for metadata."""

        name = 'address'

    @staticmethod
    def _dd_to_dms(num: float, _type: str) -> str:
        """Convert decimal number to DMS format.

        :param num: Decimal number.
        :param _type: Type of number.
        :return: Number in DMS format.
        """
        degrees = int(num)
        minutes = int((num - degrees) * 60)
        seconds = (num - degrees - minutes / 60) * 3600.00
        seconds = round(seconds, 3)
        result = [abs(i) for i in (degrees, minutes, seconds)]

        direction = ''
        if _type == 'lg':
            direction = 'W' if degrees < 0 else 'E'
        elif _type == 'lt':
            direction = 'S' if degrees < 0 else 'N'

        return ('{}º{}\'{:.3f}"' + direction).format(*result)

    def street_number(self, maximum: int = 1400) -> str:
        """Generate a random street number.

        :param maximum: Maximum value.
        :return: Street number.
        """
        return str(self.random.randint(1, maximum))

    def street_name(self) -> str:
        """Get a random street name.

        :return: Street name.
        """
        return self.random.choice(
            self._data['street']['name'])

    def street_suffix(self) -> str:
        """Get a random street suffix.

        :return: Street suffix.
        """
        return self.random.choice(
            self._data['street']['suffix'])

    def address(self) -> str:
        """Generate a random full address.

        :return: Full address.
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
                # Generate list of random integers
                # in amount of 3, from 1 to 100.
                *self.random.randints(amount=3, a=1, b=100),
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
        """
        return self.random.choice(
            self._data['state']['abbr' if abbr else 'name'])

    def region(self, *args, **kwargs) -> str:
        """Get a random region.

        An alias for :meth:`~Address.state()`.
        """
        return self.state(*args, **kwargs)

    def province(self, *args, **kwargs) -> str:
        """Get a random province.

        An alias for :meth:`~Address.state()`.
        """
        return self.state(*args, **kwargs)

    def federal_subject(self, *args, **kwargs) -> str:
        """Get a random region.

        An alias for :meth:`~Address.state()`.
        """
        return self.state(*args, **kwargs)

    def prefecture(self, *args, **kwargs) -> str:
        """Get a random prefecture.

        An alias for :meth:`~Address.state()`.
        """
        return self.state(*args, **kwargs)

    def postal_code(self) -> str:
        """Generate a postal code for current locale.

        :return: Postal code.
        """
        return self.random.custom_code(
            self._data['postal_code_fmt'])

    def zip_code(self) -> str:
        """Generate a zip code.

        An alias for :meth:`~Address.postal_code()`.

        :return: Zip code.
        """
        return self.postal_code()

    def country_code(self, fmt: Optional[CountryCode] = CountryCode.A2) -> str:
        """Get a random code of country.

        Default format is :attr:`~enums.CountryCode.A2` (ISO 3166-1-alpha2),
        you can change it by passing parameter ``fmt`` with enum object
        :class:`~enums.CountryCode`.

        :param fmt: Enum object CountryCode.
        :return: Country code in selected format.
        :raises KeyError: if fmt is not supported.
        """
        key = self._validate_enum(fmt, CountryCode)
        return self.random.choice(COUNTRY_CODES[key])

    def country(self, allow_random: bool = False) -> str:
        """Get the country of the current locale.

        :allow_random: Return a random country name.
        :return: The Country.
        """
        if allow_random:
            return self.random.choice(self._data['country']['name'])

        return self._data['country']['current_locale']

    def city(self) -> str:
        """Get a random city.

        :return: City name.
        """
        return self.random.choice(
            self._data['city'])

    def _get_fs(self, key: str, dms: bool = False) -> Union[str, float]:
        """Get float number.

        :param key: Key (`lt` or `lg`).
        :param dms: DMS format.
        :return: Float number
        """
        # Default range is a range of longitude.
        rng = (-90, 90) if key == 'lt' else (-180, 180)
        result = self.random.uniform(*rng, precision=6)

        if dms:
            return self._dd_to_dms(result, key)

        return result

    def latitude(self, dms: bool = False) -> Union[str, float]:
        """Generate a random value of latitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        return self._get_fs('lt', dms)

    def longitude(self, dms: bool = False) -> Union[str, float]:
        """Generate a random value of longitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        return self._get_fs('lg', dms)

    def coordinates(self, dms: bool = False) -> dict:
        """Generate random geo coordinates.

        :param dms: DMS format.
        :return: Dict with coordinates.
        """
        return {
            'longitude': self._get_fs('lg', dms),
            'latitude': self._get_fs('lt', dms),
        }

    def continent(self, code: bool = False) -> str:
        """Get a random continent name or continent code.

        :param code: Return code of continent.
        :return: Continent name.
        """
        codes = CONTINENT_CODES if \
            code else self._data['continent']

        return self.random.choice(codes)

    def calling_code(self) -> str:
        """Get a random calling code of random country.

        :return: Calling code.
        """
        return self.random.choice(CALLING_CODES)
