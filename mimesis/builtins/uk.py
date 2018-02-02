"""Specific data provider for Ukraine (uk)."""

from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.utils import pull

__all__ = ['UkraineSpecProvider']


class UkraineSpecProvider(BaseSpecProvider):
    """Class that provides special data for Ukraine (uk)."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes."""
        super().__init__(*args, **kwargs)
        self._data = pull('builtin.json', 'uk')

    class Meta:
        """The name of the provider."""

        name = 'ukraine_provider'

    def patronymic(self, gender: Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = self._validate_enum(gender, Gender)
        patronymics = self._data['patronymic'][gender]
        return self.random.choice(patronymics)
