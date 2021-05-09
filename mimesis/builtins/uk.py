# -*- coding: utf-8 -*-

"""Specific data provider for Ukraine (uk)."""
from typing import List, Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.typing import Seed

__all__ = ["UkraineSpecProvider"]


class UkraineSpecProvider(BaseSpecProvider):
    """Class that provides special data for Ukraine (uk)."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.UK, seed=seed)
        self._pull(self._datafile)

    class Meta:
        """The name of the provider."""

        name = "ukraine_provider"

    def patronymic(self, gender: Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: List[str] = self._data["patronymic"][gender]
        return self.random.choice(patronymics)
