from random import Random

from elizabeth.utils import locale_info


class BaseProvider(object):
    """This is a base class for all providers."""

    def __init__(self, locale='en', seed=None):
        """Base constructor for all providers.

        :param locale: Current locale. Default is 'en'.
        :param seed: Seed to all the random functions. Default is 'None'.
        """
        self.locale = locale
        self.seed = seed
        self.random = Random()

        if seed is not None:
            self.random.seed(self.seed)

    def __str__(self):
        """
        Nice and pretty representation of a class.
        """
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale)
        )
