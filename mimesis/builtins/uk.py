"""Specific data provider for Ukraine (uk)."""
import typing as t

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.types import Seed

__all__ = ["UkraineSpecProvider"]


class UkraineSpecProvider(BaseSpecProvider):
    """Class that provides special data for Ukraine (uk)."""

    def __init__(self, seed: Seed = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.UK, seed=seed)
        self._load_datafile(self._datafile)

    class Meta:
        """The name of the provider."""

        name: t.Final[str] = "ukraine_provider"

    def patronymic(self, gender: t.Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: t.List[str] = self.extract(["patronymic", str(gender)])
        return self.random.choice(patronymics)
