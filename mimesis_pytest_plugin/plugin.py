from typing import TYPE_CHECKING, Callable, TypeAlias  # pragma: no cover

if TYPE_CHECKING:
    from mimesis.locales import Locale
    from mimesis.schema import Field

try:  # pragma: no cover
    import pytest
except ImportError:  # pragma: no cover
    raise ImportError("pytest is required to use this plugin")


_CacheCallable: TypeAlias = "Callable[[Locale], Field]"  # pragma: no cover


@pytest.fixture(scope="session")
def _mimesis_cache() -> _CacheCallable:
    from mimesis.schema import Field

    cached_instances: "dict[Locale, Field]" = {}

    def factory(locale: "Locale") -> "Field":
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return factory


@pytest.fixture()
def mimesis_locale() -> "Locale":
    """Specifies which locale to use."""
    from mimesis.locales import Locale

    return Locale.DEFAULT


@pytest.fixture()
def mimesis(_mimesis_cache: _CacheCallable, mimesis_locale: "Locale") -> "Field":
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
