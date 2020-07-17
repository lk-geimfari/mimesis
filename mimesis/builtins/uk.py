# -*- coding: utf-8 -*-

"""Specific data provider for Ukraine (uk)."""

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.typing import Seed

__all__ = ['UkraineSpecProvider']


class UkraineSpecProvider(BaseSpecProvider):
    """Class that provides special data for Ukraine (uk)."""

    def __init__(self, seed: Seed = None):
        """Initialize attributes."""
        super().__init__(locale='uk', seed=seed)
        self._pull(self._datafile)

    class Meta:
        """The name of the provider."""

        name = 'ukraine_provider'

    def patronymic(self, gender: Gender = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = self._validate_enum(gender, Gender)
        patronymics = self._data['patronymic'][gender]
        return self.random.choice(patronymics)
