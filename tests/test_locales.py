import pytest

from mimesis import locales
from mimesis.providers import Code, Cryptographic, Internet, Person


@pytest.mark.parametrize(
    'locale, new_locale', [
        ('en', 'ru'),

    ],
)
def test_override(locale, new_locale):
    provider = Person(locale)
    assert provider.locale == locale

    with locales.override(provider, locales.RU):
        assert 'Жен.' in provider._data['gender']
        assert provider.locale == new_locale

    assert provider.locale == locale
    assert 'Жен.' not in provider._data['gender']


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
