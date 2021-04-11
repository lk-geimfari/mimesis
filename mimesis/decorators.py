# -*- coding: utf-8 -*-

"""Decorators for the public API and for internal purpose."""

import functools
from string import ascii_letters
from string import digits
from string import punctuation
from typing import Any
from typing import Callable
from typing import TypeVar
from typing import cast

from mimesis import data
from mimesis.exceptions import UnsupportedLocale

__all__ = ['romanize']

F = TypeVar('F', bound=Callable[..., Any])


def romanize(locale: str = '') -> Callable[[F], F]:
    """Romanize the cyrillic text.

    Transliterate the cyrillic script into the latin alphabet.

    .. note:: At this moment it works only for `ru`, `uk`, `kk`.

    :param locale: Locale code.
    :return: Romanized text.
    """

    def romanize_deco(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Cyrillic string can contain ascii
                # symbols, digits and punctuation.
                alphabet = {s: s for s in
                            ascii_letters + digits + punctuation}
                alphabet.update({
                    **data.ROMANIZATION_DICT[locale],
                    **data.COMMON_LETTERS,
                })
            except KeyError:
                raise UnsupportedLocale(locale)

            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return cast(F, wrapper)

    return romanize_deco


# For backward compatibility
romanized = romanize
