"""This module is provide internal util functions."""

import functools
import typing as t

from mimesis.data import COMMON_LETTERS, ROMANIZATION_DICT
from mimesis.locales import Locale, validate_locale

__all__ = ["romanize", "luhn_checksum"]


@functools.lru_cache(maxsize=None)
def _get_translation_table(locale: Locale) -> t.Dict[int, str]:
    return str.maketrans({**ROMANIZATION_DICT[locale.value], **COMMON_LETTERS})


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check = 0
    for i, s in enumerate(reversed(num)):
        sx = int(s)
        if i % 2 == 0:
            sx *= 2
        if sx > 9:
            sx -= 9
        check += sx
    return str(check * 9 % 10)


def romanize(string: str, locale: t.Union[Locale, str]) -> str:
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

    table = _get_translation_table(locale)

    return string.translate(table)
