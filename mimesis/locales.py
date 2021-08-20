# -*- coding: utf-8 -*-

"""This module provides constants for locale-dependent providers."""

from mimesis.enums import Locale
from mimesis.exceptions import LocaleError

__all__ = ["Locale"]


def validate_locale(locale: Locale) -> Locale:
    if not locale:
        locale = Locale.DEFAULT

    if isinstance(locale, str):
        if locale not in Locale.values():
            raise LocaleError(locale)

        locale = Locale(locale)

    if locale not in Locale:
        raise LocaleError(locale)

    return locale
