from functools import wraps
from string import (
    ascii_letters as letters,
    digits,
    punctuation,
)

from mimesis.data import COMMON_LETTERS, ROMANIZATION_DICT
from mimesis.exceptions import UnsupportedLocale


def romanized(locale):
    def romanized_deco(func):
        """Cyrillic letter to latin converter. Romanization of the Cyrillic
         alphabet is the process of transliterating the Cyrillic language from
         the Cyrillic script into the Latin alphabet.

        .. note:: At this moment it's work only for `ru`, `uk`, `kk`.

        :param func: Function.
        :return: Latinized text.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                alphabet = ROMANIZATION_DICT[locale]
                # Add common cyrillic common letters
                alphabet.update(COMMON_LETTERS)
                # String can contain ascii symbols, digits and
                # punctuation symbols.
                alphabet.update({s: s for s in
                                 letters + digits + punctuation})
            except KeyError:
                raise UnsupportedLocale(
                    'Locale {0} is not supported yet.'.format(locale),
                )
            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return wrapper

    return romanized_deco


def type_to(new_type, check_len=False):
    """Convert result of function to different type.

    :param new_type: New type.
    :param check_len: Check length of object.
    :return: Converted to new_type object.
    """

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result = new_type(result)

            if check_len and len(result) == 1:
                return result[0]
            return result

        return wrapper

    return inner
