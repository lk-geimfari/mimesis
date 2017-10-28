from mimesis.utils import pull
from mimesis.builtins.base import BaseSpecProvider


class GermanySpecProvider(BaseSpecProvider):
    def __init__(self):
        super().__init__()
        self._data = pull('builtin.json', 'de')

    class Meta:
        name = 'germany_provider'

    def noun(self, plural: bool = False) -> str:
        """Return a random noun in German.

        :param plural: Return noun in plural.
        :return: Noun.
        :rtype: str
        """

        key = 'plural' if \
            plural else 'noun'

        return self.random.choice(self._data[key])
