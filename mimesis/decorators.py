from functools import wraps

from mimesis.data import ROMANIZATION_ALPHABETS
from mimesis.exceptions import UnsupportedLocale


def romanized(locale):
    def romanized_deco(func):
        """Cyrillic letter to latin converter. Romanization of the Cyrillic
         alphabet is the process of transliterating the Cyrillic language from
         the Cyrillic script into the Latin alphabet.

        .. note:: At this moment it's work only for Russian and Ukrainian,
        but in future we can add support for all slavic languages or for all
        Cyrillic languages.

        :param func: Function.
        :return: Latinized text.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                alphabet = ROMANIZATION_ALPHABETS[locale]
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
    """Convert result of function to different type

    :param new_type: New type.
    :param check_len: Check lenght of object.
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
