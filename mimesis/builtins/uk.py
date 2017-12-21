from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.helpers import validate_enum
from mimesis.utils import pull


class UkraineSpecProvider(BaseSpecProvider):
    def __init__(self):
        super().__init__()
        self._data = pull('builtin.json', 'uk')

    class Meta:
        name = 'ukraine_provider'

    def patronymic(self, gender: Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :type gender: str or int
        :return: Patronymic name.
        """
        gender = validate_enum(gender, Gender)
        patronymics = self._data['patronymic'][gender]
        return self.random.choice(patronymics)
