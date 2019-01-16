# -*- coding: utf-8 -*-

"""Decorators for the public API and for internal purpose."""

import functools
from string import ascii_letters as letters
from string import digits, punctuation
from typing import Callable

from mimesis import data
from mimesis.exceptions import UnsupportedLocale


def romanized(locale: str = '') -> Callable:
    """Romanize the Cyrillic text.

    Transliterate the Cyrillic language from the Cyrillic
    script into the Latin alphabet.

    .. note:: At this moment it works only for `ru`, `uk`, `kk`.

    :param locale: Locale code.
    :return: Latinized text.
    """
    def romanized_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # String can contain ascii symbols, digits and
                # punctuation symbols.
                alphabet = {s: s for s in
                            letters + digits + punctuation}
                alphabet.update(data.ROMANIZATION_DICT[locale])
                # Add common cyrillic letters
                alphabet.update(data.COMMON_LETTERS)
            except KeyError:
                raise UnsupportedLocale(locale)
            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return wrapper

    return romanized_deco
