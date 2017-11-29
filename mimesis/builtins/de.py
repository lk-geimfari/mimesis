from mimesis.builtins.base import BaseSpecProvider
from mimesis.utils import pull


class GermanySpecProvider(BaseSpecProvider):
    """
    Specific-provider of misc data for Deutschland.
    """

    def __init__(self):
        super().__init__()
        self._data = pull('builtin.json', 'de')

    class Meta:
        name = 'germany_provider'

    def noun(self, plural: bool = False) -> str:
        """Return a random noun in German.

        :param bool plural: Return noun in plural.
        :return: Noun.
        """

        key = 'plural' if \
            plural else 'noun'

        return self.random.choice(self._data[key])
