from typing import Any, Optional

from mimesis.exceptions import NonEnumerableError
from mimesis.helpers import Random
from mimesis.utils import locale_info, setup_locale


class ValidateEnumMixin(object):
    """
    A mixin which helps validate enums.
    """

    # TODO: pass seed and init random field in ValidateEnumMixin class?
    @staticmethod
    def _validate_enum(item: Any, enum: Any,
                       rnd: Optional[Random] = Random()) -> Any:
        """Validate enum parameter of method in subclasses of BaseProvider.

        :param item: Item of enum object.
        :param enum: Enum object.
        :param rnd: Custom random object.
        :return: Value of item.
        :raises NonEnumerableError: if ``item`` not in ``enum``.
        """

        if item is None:
            result = enum.get_random_item(rnd=rnd)
        elif item and isinstance(item, enum):
            result = item
        else:
            raise NonEnumerableError(enum)

        return result.value


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


class BaseProvider(ValidateEnumMixin, StrMixin):
    """
    This is a base class for all data providers.
    """

    def __init__(self, locale: Optional[str] = None,
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

    def get_current_locale(self) -> str:
        """Current locale of provider.

        ..Note: Default for all providers is locale ``en``.
        """
        return self.locale
