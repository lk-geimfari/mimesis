from typing import Callable

from mimesis.locales import Locale
from mimesis.schema import Field

try:
    import pytest
except ImportError:
    raise ImportError("pytest is required to use this plugin")

_CacheCallable = Callable[[Locale], Field]


@pytest.fixture(scope="session")
def _mimesis_cache() -> _CacheCallable:
    cached_instances: dict[Locale, Field] = {}

    def factory(locale: Locale) -> Field:
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return factory


@pytest.fixture()
def mimesis_locale() -> Locale:
    """Specifies which locale to use."""
    return Locale.DEFAULT


@pytest.fixture()
def mimesis(_mimesis_cache: _CacheCallable, mimesis_locale: Locale) -> Field:
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
