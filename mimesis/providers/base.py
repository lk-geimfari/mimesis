from typing import Any, Optional

from mimesis.exceptions import NonEnumerableError
from mimesis.helpers import Random
from mimesis.utils import locale_info, setup_locale


class Boilerplate(object):
    """
    Boilerplate for builtins and usual providers.
    """

    @staticmethod
    def _validate_enum(item: Any, enum: Any) -> Any:
        """Validate enum parameter of method in subclasses of BaseProvider.

        :param item: Item of enum object.
        :param enum: Enum object.
        :return: Value of item.
        :raises NonEnumerableError: if ``item`` not in ``enum``.
        """

        if item is None:
            result = enum.get_random_item()
        elif item and isinstance(item, enum):
            result = item
        else:
            raise NonEnumerableError(enum)

        return result.value

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


class BaseProvider(Boilerplate):
    """This is a base class for all providers."""

    def __init__(self, locale: str = '',
                 seed: Optional[int] = None) -> None:
        """Base constructor for all providers.

        :param str locale: Current locale. Default is 'en'.
        :param int seed: Seed to all the random functions. Default is 'None'.
        """
        self.seed = seed
        self.random = Random()
        self.locale = setup_locale(locale)

        if seed is not None:
            self.random.seed(self.seed)
