# -*- coding: utf-8 -*-

"""This module is provide internal util functions."""

from string import ascii_letters, digits, punctuation
from typing import Union

from mimesis.data import COMMON_LETTERS, ROMANIZATION_DICT
from mimesis.locales import Locale, validate_locale

__all__ = ["romanize", "luhn_checksum"]


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check = 0
    for i, s in enumerate(reversed(num)):
        sx = int(s)
        sx = sx * 2 if i % 2 == 0 else sx
        sx = sx - 9 if sx > 9 else sx
        check += sx
    return str(check * 9 % 10)


def romanize(string: str, locale: Union[Locale, str]) -> str:
    """Romanize a given string.

    Supported locales are:
        Locale.RU
        Locale.UK
        Locale.KK

    :param string: Cyrillic string.
    :param locale: Locale.
    :return: Romanized string.
    """
    locale = validate_locale(locale)

    if locale not in (Locale.RU, Locale.UK, Locale.KK):
        raise ValueError(f"Romanization is not available for: {locale}")

    # Cyrillic string can contain ascii symbols, digits and punctuation.
    alphabet = {s: s for s in ascii_letters + digits + punctuation}
    alphabet.update(
        {
            **ROMANIZATION_DICT[locale.value],
            **COMMON_LETTERS,
        }
    )

    return "".join([alphabet[i] for i in string if i in alphabet])
