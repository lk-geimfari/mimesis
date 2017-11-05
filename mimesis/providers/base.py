from typing import Optional

from mimesis.helpers import Random
from mimesis.utils import locale_info, setup_locale


class BaseProvider(object):
    """This is a base class for all providers."""

    def __init__(self, locale: str = '',
                 seed: Optional[int] = None) -> None:
        """Base constructor for all providers.

        :param locale: Current locale. Default is 'en'.
        :param seed: Seed to all the random functions. Default is 'None'.
        """
        self.seed = seed
        self.random = Random()
        self.locale = setup_locale(locale)

        if seed is not None:
            self.random.seed(self.seed)

    def __str__(self) -> str:
        return '{}:{}:{}'.format(
            self.__class__.__name__,
            self.locale,
            locale_info(self.locale),
        )
