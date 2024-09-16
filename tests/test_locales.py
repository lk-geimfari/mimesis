from enum import Enum

import pytest

from mimesis.exceptions import LocaleError
from mimesis.locales import Locale, validate_locale

SUPPORTED_LOCALES_COUNT = 44


def test_locale_enum():
    assert len(list(Locale)) == SUPPORTED_LOCALES_COUNT
    assert issubclass(Locale, Enum)


def test_validate_locale_missing_locale():
    with pytest.raises(TypeError):
        validate_locale()


def test_validate_locale_invalid_locale():
    with pytest.raises(LocaleError):
        validate_locale(locale=None)

    with pytest.raises(LocaleError):
        validate_locale(locale="nil")


def test_validate_locale():
    validated_locale = validate_locale("en")

    assert validated_locale == Locale.EN
    assert issubclass(validated_locale.__class__, Enum)
    assert isinstance(validate_locale(Locale.EN), Locale)
