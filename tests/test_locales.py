import pytest
from mimesis.exceptions import LocaleError
from mimesis.locales import Locale, validate_locale


def test_locales_count():
    assert len(list(Locale)) == 34


def test_locale_in():
    assert Locale.EN in Locale
    assert Locale.RU in Locale


def test_validate_locale():
    with pytest.raises(ValueError):
        validate_locale(locale=None)

    assert validate_locale("en") == Locale.EN
    with pytest.raises(LocaleError):
        validate_locale(locale="nil")

    assert isinstance(validate_locale(Locale.EN), Locale)
