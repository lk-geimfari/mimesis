"""Specific data provider for Ukraine (uk)."""
import typing as t

from mimesis.builtins.base import CountrySpecificProvider
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.types import MissingSeed, Seed

__all__ = ["UkraineSpecProvider"]


class UkraineSpecProvider(CountrySpecificProvider):
    """Class that provides special data for Ukraine (uk)."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.UK, seed=seed)

    class Meta:
        name = "ukraine_provider"
        datafile = "builtin.json"

    def patronymic(self, gender: t.Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: t.List[str] = self.extract(["patronymic", str(gender)])
        return self.random.choice(patronymics)
