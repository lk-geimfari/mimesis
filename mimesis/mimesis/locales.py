"""This module provides constants for locale-dependent providers."""

from mimesis.enums import Locale
from mimesis.exceptions import LocaleError

__all__ = ["Locale", "validate_locale"]


def validate_locale(locale: Locale | str) -> Locale:
    if isinstance(locale, str):
        try:
            return Locale(locale)
        except ValueError:
            raise LocaleError(locale)

    if not isinstance(locale, Locale):
        raise LocaleError(locale)

    return locale
