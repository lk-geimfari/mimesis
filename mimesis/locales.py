# -*- coding: utf-8 -*-

"""This module provides constants for locale-dependent providers."""

from typing import Optional, Union

from mimesis.enums import Locale
from mimesis.exceptions import LocaleError

__all__ = ["Locale", "validate_locale"]


# TODO: Refactor
def validate_locale(locale: Optional[Union[Locale, str]] = None) -> Locale:
    if not locale:
        raise ValueError(f"Invalid locale: {locale}")

    # Validates deprecated locale format.
    if isinstance(locale, str):
        try:
            return Locale(locale)
        except ValueError:
            raise LocaleError(locale)

    if not isinstance(locale, Locale):
        raise LocaleError(locale)

    return locale
