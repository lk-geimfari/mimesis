from typing import Callable, Any

try:
    import pytest
except ImportError:
    raise ImportError("pytest is required to use this plugin")

_CacheCallable = Callable[[Any], Any]


@pytest.fixture(scope="session")
def _mimesis_cache() -> _CacheCallable:
    from mimesis.locales import Locale
    from mimesis.schema import Field

    cached_instances: dict[Locale, Field] = {}

    def factory(locale: Locale) -> Field:
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return factory


@pytest.fixture()
def mimesis_locale(): # type: ignore
    """Specifies which locale to use."""
    from mimesis.locales import Locale
    return Locale.DEFAULT


@pytest.fixture()
def mimesis(_mimesis_cache: _CacheCallable, mimesis_locale): # type: ignore
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
