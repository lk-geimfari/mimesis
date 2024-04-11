"""Address module.

This module contains provider Address() and other utils which represent
data related to location, such as street name, city etc.
"""

import typing as t

from mimesis.datasets import (
    CALLING_CODES,
    CONTINENT_CODES,
    COUNTRY_CODES,
    SHORTENED_ADDRESS_FMT,
)
from mimesis.enums import CountryCode
from mimesis.providers.base import BaseDataProvider

__all__ = ["Address"]


class Address(BaseDataProvider):
    """Class for generate fake address data.

    This object provides all the data related to
    geographical location.
    """

    class Meta:
        name = "address"
        datafile = f"{name}.json"

    @staticmethod
    def _dd_to_dms(num: float, _type: str) -> str:
        """Converts decimal number to DMS format.

        :param num: Decimal number.
        :param _type: Type of number.
        :return: Number in DMS format.
        """
        direction = ""
        if _type == "lg":
            direction = "W" if num < 0 else "E"
        elif _type == "lt":
            direction = "S" if num < 0 else "N"

        num = abs(num)
        degrees = int(num)
        part = num - degrees
        minutes = int(part * 60)
        seconds = 3600 * part - 60 * minutes
        seconds = round(seconds, 3)

        return f"{degrees}º{minutes}'{seconds:.3f}\"{direction}"

    def street_number(self, maximum: int = 1400) -> str:
        """Generates a random street number.

        :param maximum: Maximum value.
        :return: Street number.
        """
        return str(self.random.randint(1, maximum))

    def street_name(self) -> str:
        """Generates a random street name.

        :return: Street name.
        """
        street_names: list[str] = self._extract(["street", "name"])
        return self.random.choice(street_names)

    def street_suffix(self) -> str:
        """Generates a random street suffix.

        :return: Street suffix.
        """
        suffixes: list[str] = self._extract(["street", "suffix"])
        return self.random.choice(suffixes)

    def address(self) -> str:
        """Generates a random full address.

        :return: Full address.
        """
        fmt: str = self._extract(["address_fmt"])

        st_num = self.street_number()
        st_name = self.street_name()

        if self.locale in SHORTENED_ADDRESS_FMT:
            return fmt.format(
                st_num=st_num,
                st_name=st_name,
            )

        if self.locale == "ja":
            return fmt.format(
                self.random.choice(self._extract(["city"])),
                # Generate a list of random integers
                # in n of 3, from 1 to 100.
                *self.random.randints(n=3, a=1, b=100),
            )

        return fmt.format(
            st_num=st_num,
            st_name=st_name,
            st_sfx=self.street_suffix(),
        )

    def state(self, abbr: bool = False) -> str:
        """Generates a random administrative district of the country.

        :param abbr: Return ISO 3166-2 code.
        :return: Administrative district.
        """
        key = "abbr" if abbr else "name"
        states: list[str] = self._extract(["state", key])
        return self.random.choice(states)

    def region(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random region.

        An alias for :meth:`~.state()`.
        """
        return self.state(*args, **kwargs)

    def province(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random province.

        An alias for :meth:`~.state()`.
        """
        return self.state(*args, **kwargs)

    def federal_subject(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random federal_subject (Russia).

        An alias for :meth:`~.state()`.
        """
        return self.state(*args, **kwargs)

    def prefecture(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random prefecture.

        An alias for :meth:`~.state()`.
        """
        return self.state(*args, **kwargs)

    def postal_code(self) -> str:
        """Generates a postal code for current locale.

        :return: Postal code.
        """
        return self.random.generate_string_by_mask(self._extract(["postal_code_fmt"]))

    def zip_code(self) -> str:
        """Generates a zip code.

        An alias for :meth:`~.postal_code()`.

        :return: Zip code.
        """
        return self.postal_code()

    def country_code(self, code: CountryCode | None = CountryCode.A2) -> str:
        """Generates a random code of country.

        Default format is :attr:`~enums.CountryCode.A2` (ISO 3166-1-alpha2),
        you can change it by passing parameter ``fmt``.

        :param code: Country code.
        :return: Country code in selected format.
        :raises KeyError: if fmt is not supported.
        """
        key = self.validate_enum(code, CountryCode)
        return self.random.choice(COUNTRY_CODES[key])

    def country_emoji_flag(self) -> str:
        """Generates a randomly chosen country emoji flag.

        :example:
            🇹🇷

        :return: Flag emoji.
        """
        code = self.country_code(
            code=CountryCode.A2,
        )

        offset = ord("🇦") - ord("A")
        first = ord(code[0]) + offset
        second = ord(code[1]) + offset
        return chr(first) + chr(second)

    def default_country(self) -> str:
        """Returns the country associated with the current locale.

        :return: The country associated with current locale.
        """
        country: str = self._extract(["country", "current_locale"])
        return country

    def country(self) -> str:
        """Generates a random country.

        :return: The Country.
        """
        countries: list[str] = self._extract(["country", "name"])
        return self.random.choice(countries)

    def city(self) -> str:
        """Generates a random city.

        :return: City name.
        """
        cities: list[str] = self._extract(["city"])
        return self.random.choice(cities)

    def _get_fs(self, key: str, dms: bool = False) -> str | float:
        """Get float number.

        :param key: Key (`lt` or `lg`).
        :param dms: DMS format.
        :return: Float number
        """
        # The default range is a range of longitudes.
        rng = (-90, 90) if key == "lt" else (-180, 180)
        result = self.random.uniform(*rng, precision=6)

        if dms:
            return self._dd_to_dms(result, key)

        return result

    def latitude(self, dms: bool = False) -> str | float:
        """Generates a random value of latitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        return self._get_fs("lt", dms)

    def longitude(self, dms: bool = False) -> str | float:
        """Generates a random value of longitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        return self._get_fs("lg", dms)

    def coordinates(self, dms: bool = False) -> dict[str, str | float]:
        """Generates random geo coordinates.

        :param dms: DMS format.
        :return: Dict with coordinates.
        """
        return {
            "longitude": self._get_fs("lg", dms),
            "latitude": self._get_fs("lt", dms),
        }

    def continent(self, code: bool = False) -> str:
        """Returns a random continent name or continent code.

        :param code: Return code of a continent.
        :return: Continent name.
        """
        codes: list[str] = self._extract(["continent"])

        if code:
            codes = CONTINENT_CODES

        return self.random.choice(codes)

    def calling_code(self) -> str:
        """Generates a random calling code of random country.

        :return: Calling code.
        """
        return self.random.choice(CALLING_CODES)

    def isd_code(self) -> str:
        """Generates a random ISD code.

        An alias for :meth:`~Address.calling_code()`.
        """
        return self.calling_code()
