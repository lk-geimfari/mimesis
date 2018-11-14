"""Base data provider."""

import collections
import functools
import json

from os import path
from typing import Any, Optional, Mapping

from mimesis import locales
from mimesis.exceptions import NonEnumerableError, UnsupportedLocale
from mimesis.helpers import Random, get_random_item, random
from mimesis.typing import JSON, Seed

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
        self._data = {}
        self._datafile: Optional[str] = None
        self._setup_locale(locale)
        self._data_dir = path.abspath(
            path.join('mimesis', 'data'))

    def _setup_locale(self, locale: Optional[str] = None) -> None:
        """Set up locale after pre-check.

        :param str locale: Locale
        :raises UnsupportedLocale: When locale is not supported.
        :return: Nothing.
        """
        if not locale:
            locale = locales.DEFAULT_LOCALE

        locale = locale.lower()
        if locale not in locales.SUPPORTED_LOCALES:
            raise UnsupportedLocale(locale)

        self.locale = locale

    def _update_dict(self, initial: JSON, other: Mapping) -> JSON:
        """Recursively update a dictionary.

        :param initial: Dict to update.
        :param other: Dict to update from.
        :return: Updated dict.
        """
        for key, value in other.items():
            if isinstance(value, collections.Mapping):
                r = self._update_dict(initial.get(key, {}), value)
                initial[key] = r
            else:
                initial[key] = other[key]
        return initial

    @functools.lru_cache(maxsize=None)
    def pull(self, data_dir: Optional[str] = None,
             datafile: Optional[str] = None, locale: Optional[str] = None):
        """Pull the content from the JSON and memorize one.

        Opens JSON file ``file`` in the folder ``data/locale``
        and get content from the file and memorize ones using lru_cache.

        :param data_dir: Data directory.
        :param datafile: The name of file.
        :param locale: Locale.
        :return: The content of the file.
        :raises UnsupportedLocale: if locale is not supported.
        """

        if not data_dir:
            data_dir = self._data_dir

        if not datafile:
            datafile = self._datafile

        if not locale:
            locale = self.locale

        def get_data(locale_name: str) -> JSON:
            """Pull JSON data from file.

            :param locale_name: Locale name.
            :return: Content of JSON file as dict.
            """
            file_path = path.join(data_dir, locale_name, datafile)
            with open(file_path, 'r', encoding='utf8') as f:
                return json.load(f)

        locale = locale.lower()

        if locale not in locales.SUPPORTED_LOCALES:
            raise UnsupportedLocale(locale)

        master_locale = locale.split('-')[0]
        data = get_data(master_locale)

        # Handle sub-locales
        if '-' in locale:
            data = self._update_dict(data, get_data(locale))

        self._data = data

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
