"""Base data provider."""

from typing import Any, Optional

from mimesis.exceptions import NonEnumerableError
from mimesis.helpers import Random, get_random_item
from mimesis.typing import Seed
from mimesis.utils import locale_info, setup_locale

__all__ = ['BaseDataProvider', 'BaseProvider']


class BaseProvider(object):
    """This is a base class for all providers."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize attributes.

        :param seed: Seed for random.
        """
        self.seed = seed
        self.random = Random()

        if seed is not None:
            self.random.seed(self.seed)

    def _validate_enum(self, item: Any, enum: Any) -> Any:
        """Validate enum parameter of method in subclasses of BaseProvider.

        :param item: Item of enum object.
        :param enum: Enum object.
        :return: Value of item.
        :raises NonEnumerableError: if ``item`` not in ``enum``.
        """
        if item is None:
            result = get_random_item(enum, self.random)
        elif item and isinstance(item, enum):
            result = item
        else:
            raise NonEnumerableError(enum)

        return result.value


class StrMixin(object):
    """A mixin for showing information about the current locale."""

    def __str__(self) -> str:
        """Human-readable representation of locale."""
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
    """This is a base class for all data providers."""

    def __init__(self, locale: Optional[str] = None,
                 seed: Optional[Seed] = None) -> None:
        """Initialize attributes for data providers.

        :param locale: Current locale.
        :param seed: Seed to all the random functions.
        """
        super().__init__(seed=seed)
        self.locale = setup_locale(locale)

    def get_current_locale(self) -> str:
        """Get current locale.

        If locale is not defined then this method will always return ``en``,
        because ``en`` is default locale for all providers, excluding builtins.

        :return: Current locale.
        """
        return self.locale
