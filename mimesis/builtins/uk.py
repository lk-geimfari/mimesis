from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.utils import pull


class UkraineSpecProvider(BaseSpecProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = pull('builtin.json', 'uk')

    class Meta:
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
