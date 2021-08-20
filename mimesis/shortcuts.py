# -*- coding: utf-8 -*-

"""This module is provide internal util functions."""

__all__ = ["luhn_checksum"]

from string import ascii_letters, digits, punctuation
from typing import Optional

from mimesis import data
from mimesis.locales import Locale, validate_locale


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


def romanize(string: str, locale: Optional[Locale] = None) -> str:
    """Romanize given string.

    Supported locales are:
        Locale.RU
        Locale.UK
        Locale.KK

    :param string: Cyrillic string.
    :param locale: Locale.
    :return: Romanized string.
    """
    locale = validate_locale(locale)

    # Cyrillic string can contain ascii
    # symbols, digits and punctuation.
    alphabet = {s: s for s in ascii_letters + digits + punctuation}
    alphabet.update(
        {
            **data.ROMANIZATION_DICT[locale.value],
            **data.COMMON_LETTERS,
        }
    )

    return "".join([alphabet[i] for i in string if i in alphabet])
