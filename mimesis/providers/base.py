from mimesis.helpers import Random
from mimesis.utils import locale_info
from mimesis.settings import DEFAULT_LOCALE


class BaseProvider(object):
    """This is a base class for all providers."""

    def __init__(self, locale=None, seed=None):
        """Base constructor for all providers.

        :param locale: Current locale. Default is 'en'.
        :param seed: Seed to all the random functions. Default is 'None'.
        """
        if not locale:
            self.locale = DEFAULT_LOCALE
        else:
            self.locale = locale

        self.seed = seed
        self.random = Random()

        if seed is not None:
            self.random.seed(self.seed)

    def __str__(self):
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale),
        )
