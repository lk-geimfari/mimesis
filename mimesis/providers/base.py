from typing import Any, Optional

from mimesis.helpers import Random, validate_enum
from mimesis.utils import locale_info, setup_locale


class BaseProvider(object):
    """This is a base class for all providers.
    """
    def __init__(self, seed: Optional[int] = None) -> None:
        self.seed = seed
        self.random = Random()

        if seed is not None:
            self.random.seed(self.seed)

    def _validate_enum(self, item: Any, enum: Any) -> Any:
        return validate_enum(item, enum, self.random)


class StrMixin(object):
    """
    A mixin for showing information about the current
    locale of the current data provider.
    """

    def __str__(self) -> str:
        if hasattr(self, 'locale'):
            locale = getattr(self, 'locale')
            return '{}:{}:{}'.format(
                self.__class__.__name__,
                locale,
                locale_info(locale),
            )
        return '{}'.format(
            self.__class__.__name__)


class BaseDataProvider(BaseProvider, StrMixin):
    """
    This is a base class for all data providers.
    """

    def __init__(self, locale: Optional[str] = None,
                 seed: Optional[int] = None) -> None:
        """Base constructor for all data providers.

        :param str locale: Current locale. Default is 'en'.
        :param int seed: Seed to all the random functions. Default is 'None'.
        """
        super().__init__(seed=seed)
        self.locale = setup_locale(locale)

    def get_current_locale(self) -> str:
        """Current locale of provider.

        ..Note: Default for all providers is locale ``en``.
        """
        return self.locale
