"""This module provides constants for locale-dependent providers."""

from mimesis.enums import Locale
from mimesis.exceptions import LocaleError


__all__ = ["Locale", "validate_locale"]


def validate_locale(locale: Locale | str) -> Locale:
    """Validate and normalize a locale value.

    :param locale: Locale enum member or locale code string.
    :return: Validated :class:`~mimesis.enums.Locale` member.
    :raises LocaleError: If the locale is not supported.
    """
    if isinstance(locale, str):
        try:
            return Locale(locale)
        except ValueError as err:
            raise LocaleError(locale) from err

    if not isinstance(locale, Locale):
        raise LocaleError(locale)

    return locale
