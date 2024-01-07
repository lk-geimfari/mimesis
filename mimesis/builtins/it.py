"""Specific data provider for Italy (it)."""

import string

from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed

__all__ = ["ItalySpecProvider"]


class ItalySpecProvider(BaseDataProvider):
    """Specific-provider of misc data for Italy."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.IT, seed=seed)

    class Meta:
        name = "italy_provider"
        datafile = "builtin.json"

    def fiscal_code(self, gender: Gender | None = None) -> str:
        """Return a random fiscal code.

        :param gender: Gender's enum object.
        :return: Fiscal code.

        Example:
            RSSMRA66R05D612U
        """
        code = "".join(self.random.choices(string.ascii_uppercase, k=6))

        code += self.random.generate_string_by_mask(mask="##")

        month_codes = self._extract(["fiscal_code", "month_codes"])
        code += self.random.choice(month_codes)

        birth_day = self.random.randint(101, 131)
        self.validate_enum(gender, Gender)
        if gender == Gender.FEMALE:
            birth_day += 40
        code += str(birth_day)[1:]

        city_letters = self._extract(["fiscal_code", "city_letters"])
        code += self.random.choice(city_letters)
        code += self.random.generate_string_by_mask(mask="###@")

        return code
