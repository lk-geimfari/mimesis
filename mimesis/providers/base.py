"""Base data provider."""

import contextlib
import functools
import json
import operator
import typing as t
from functools import reduce
from pathlib import Path

from mimesis.exceptions import NonEnumerableError
from mimesis.locales import Locale, validate_locale
from mimesis.random import Random, get_random_item
from mimesis.types import JSON, Seed

__all__ = ["BaseDataProvider", "BaseProvider"]


class BaseProvider:
    """This is a base class for all providers."""

    def __init__(self, *, seed: Seed = None, **kwargs: t.Any) -> None:
        """Initialize attributes.

        Keep in mind, that locale-independent data providers will work
        only with keyword-only arguments since version 5.0.0.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        """
        self.seed = seed
        self.random = Random()
        self.reseed(seed)

    def reseed(self, seed: Seed = None) -> None:
        """Reseed the internal random generator.

        In case we use the default seed, we need to create a per instance
        random generator, in this case two providers with the same seed
        will always return the same values.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        """
        self.seed = seed
        self.random.seed(seed)

    def validate_enum(self, item: t.Any, enum: t.Any) -> t.Any:
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

    _LOCALE_SEPARATOR = "-"

    def __init__(self, locale: Locale = Locale.DEFAULT, seed: Seed = None) -> None:
        """Initialize attributes for data providers.

        :param locale: Current locale.
        :param seed: Seed to all the random functions.
        """
        super().__init__(seed=seed)
        self._data: JSON = {}
        self._datafile = ""
        self._setup_locale(locale)
        self._data_dir = Path(__file__).parent.parent.joinpath("data")

    def _setup_locale(self, locale: Locale = Locale.DEFAULT) -> None:
        """Set up locale after pre-check.

        :param str locale: Locale
        :raises UnsupportedLocale: When locale not supported.
        :return: Nothing.
        """

        locale_obj = validate_locale(locale)
        self.locale = locale_obj.value

    def extract(self, keys: t.List[str], default: t.Optional[t.Any] = None) -> t.Any:
        """Extracts nested values from JSON file by list of keys.

        :param keys: List of keys (order extremely matters).
        :param default: Default value.
        :return: Data.
        """

        if not keys:
            raise ValueError("List of keys cannot be empty.")

        try:
            if len(keys) == 1:
                return self._data[keys[0]]
            return reduce(operator.getitem, keys, self._data)
        except (TypeError, KeyError):
            return default

    def _update_dict(self, initial: JSON, other: JSON) -> JSON:
        """Recursively update a dictionary.

        :param initial: Dict to update.
        :param other: Dict to update from.
        :return: Updated dict.
        """
        for key, value in other.items():
            if isinstance(value, dict):
                r = self._update_dict(initial.get(key, {}), value)
                initial[key] = r
            else:
                initial[key] = other[key]
        return initial

    @functools.lru_cache(maxsize=None)
    def _load_datafile(self, datafile: str = "") -> None:
        """Pull the content from the JSON and memorize one.

        Opens JSON file ``file`` in the folder ``data/locale``
        and get content from the file and memorize ones using lru_cache.

        :param datafile: The name of file.
        :return: The content of the file.
        :raises UnsupportedLocale: Raises if locale is unsupported.
        """
        locale = self.locale
        data_dir = self._data_dir

        if not datafile:
            datafile = self._datafile

        def get_data(locale_name: str) -> t.Any:
            """Pull JSON data from file.

            :param locale_name: Locale name.
            :return: Content of JSON file as dict.
            """
            file_path = Path(data_dir).joinpath(locale_name, datafile)
            with open(file_path, encoding="utf8") as f:
                return json.load(f)

        master_locale = locale.split(self._LOCALE_SEPARATOR).pop(0)
        data = get_data(master_locale)

        if self._LOCALE_SEPARATOR in locale:
            data = self._update_dict(data, get_data(locale))

        self._data = data

    def get_current_locale(self) -> str:
        """Get current locale.

        If locale is not defined then this method will always return ``en``,
        because ``en`` is default locale for all providers, excluding builtins.

        :return: Current locale.
        """
        return self.locale

    def _override_locale(self, locale: Locale = Locale.DEFAULT) -> None:
        """Overrides current locale with passed and pull data for new locale.

        :param locale: Locale
        :return: Nothing.
        """
        self._setup_locale(locale)
        self._load_datafile.cache_clear()
        self._load_datafile()

    @contextlib.contextmanager
    def override_locale(
        self,
        locale: Locale,
    ) -> t.Generator["BaseDataProvider", None, None]:
        """Context manager which allows overriding current locale.

        Temporarily overrides current locale for
        locale-dependent providers.

        :param locale: Locale.
        :return: Provider with overridden locale.
        """
        try:
            origin_locale = Locale(self.locale)
            self._override_locale(locale)
            try:
                yield self
            finally:
                self._override_locale(origin_locale)
        except AttributeError:
            raise ValueError(f"«{self.__class__.__name__}» has not locale dependent")

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        locale = Locale(getattr(self, "locale", Locale.DEFAULT))
        return f"{self.__class__.__name__} <{locale}>"
