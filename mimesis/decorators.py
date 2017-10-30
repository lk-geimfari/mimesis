from typing import Any, Callable, TypeVar, Generator, Iterable, cast
U = TypeVar('U', covariant=True)

from string import (
    ascii_letters as letters,
    digits,
    punctuation,
)

from mimesis import data
from mimesis.exceptions import UnsupportedLocale

import functools


def romanized(locale: str ='') -> Callable:
    """Romanization of the Cyrillic alphabet (transliterating the Cyrillic language
    from the Cyrillic script into the Latin alphabet).

    .. note:: At this moment it works only for `ru`, `uk`, `kk`.

    :param locale: Function.
    :return: Latinized text.
    :rtype: types.Callable
    """

    def romanized_deco(func: Callable[..., U]) -> U:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                alphabet = data.ROMANIZATION_DICT[locale]
                # Add common cyrillic common letters
                alphabet.update(data.COMMON_LETTERS)
                # String can contain ascii symbols, digits and
                # punctuation symbols.
                alphabet.update({s: s for s in
                                 letters + digits + punctuation})
            except KeyError:
                raise UnsupportedLocale(
                    'Locale {0} is not supported yet.'.format(locale),
                )
            result = func(*args, **kwargs)
            txt = ''.join(cast(Iterable, (alphabet[i] for i in result if i in alphabet)))
            return txt

        return wrapper

    return romanized_deco


def type_to(new_type: Callable,
            check_len: bool =False) -> Callable:
    """Convert result of function to different type. This is
    internal function.

    :param new_type: New type.
    :param check_len: Check length of object.
    :return: Converted to new_type object.
    :rtype: types.Callable
    """

    def inner(func: Callable[..., U]) -> U:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> U:
            result = func(*args, **kwargs)
            result = new_type(result)

            if check_len and len(result) == 1:
                return result[0]
            return result

        return cast(U, wrapper)

    return inner
