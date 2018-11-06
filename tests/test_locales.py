import pytest

from mimesis import locales
from mimesis.providers import (Address, Business, Code, Cryptographic,
                               Datetime, Food, Internet, Person, Science, Text)


@pytest.mark.parametrize(
    'provider, locale, new_locale', [
        (Address, 'en', 'ru'),
        (Business, 'en', 'ru'),
        (Datetime, 'en', 'ru'),
        (Food, 'en', 'ru'),
        (Person, 'en', 'ru'),
        (Science, 'en', 'ru'),
        (Text, 'en', 'ru'),

    ],
)
def test_override(provider, locale, new_locale):
    provider = provider(locale)
    assert provider.locale == locale

    with locales.override(provider, locales.RU):
        assert provider.locale == new_locale

    assert provider.locale == locale


@pytest.mark.parametrize(
    'provider', [
        Code,
        Cryptographic,
        Internet,
    ],
)
def test_override_locale_independent(provider):
    with pytest.raises(ValueError):
        with locales.override(provider, locales.RU):
            pass
