from functools import wraps

from elizabeth.data.int.decorator import *
from elizabeth.exceptions import UnsupportedLocale


def romanized(locale):
    def romanized_deco(func):
        """Cyrillic letter to latin converter. Romanization of the Cyrillic alphabet
        is the process of transliterating the Cyrillic language from the Cyrillic script
        into the Latin alphabet.

        .. note:: At this moment it's work only for Russian and Ukrainian,
        but in future we can add support for all slavic languages or for all Cyrillic languages.

        :param func: Function.
        :return: Latinized text.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                alphabet = ROMANIZATION_ALPHABETS[locale]
            except KeyError:
                raise UnsupportedLocale('Locale {0} is not supported yet.'.format(locale))
            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return wrapper

    return romanized_deco
