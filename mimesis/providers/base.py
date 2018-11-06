"""Base data provider."""

from typing import Any, Optional

from mimesis.exceptions import NonEnumerableError
from mimesis.helpers import Random, get_random_item, random
from mimesis.typing import Seed
from mimesis.utils import setup_locale

__all__ = ['BaseDataProvider', 'BaseProvider']


class BaseProvider(object):
    """This is a base class for all providers."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize attributes.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        """
        self.seed = seed
        self.random = random

        if seed is not None:
            self.reseed(seed)

    def reseed(self, seed: Optional[Seed] = None) -> None:
        """Reseed the internal random generator.

        In case we use the default seed, we need to create a per instance
        random generator, in this case two providers with the same seed
        will always return the same values.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        """
        if self.random is random:
            self.random = Random()

        self.seed = seed
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

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        return self.__class__.__name__


class BaseDataProvider(BaseProvider):
    """This is a base class for all data providers."""

    def __init__(self, locale: Optional[str] = None,
                 seed: Optional[Seed] = None) -> None:
        """Initialize attributes for data providers.

        :param locale: Current locale.
        :param seed: Seed to all the random functions.
        """
        super().__init__(seed=seed)
        self._data: dict
        self._datafile: str
        self.locale = setup_locale(locale)

    def get_current_locale(self) -> str:
        """Get current locale.

        If locale is not defined then this method will always return ``en``,
        because ``en`` is default locale for all providers, excluding builtins.

        :return: Current locale.
        """
        return self.locale

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        locale = getattr(self, 'locale', 'en')
        return '{} <{}>'.format(self.__class__.__name__, locale)
