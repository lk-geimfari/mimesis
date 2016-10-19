from functools import lru_cache
from os.path import abspath, join, dirname

from .exceptions import UnsupportedLocale

PATH = abspath(join(dirname(__file__), 'data'))

__all__ = ['pull']

SUPPORTED_LOCALES = {
    'da': {
        'name': 'Danish',
        'name_local': 'Dansk',
    },
    'de': {
        'name': 'German',
        'name_local': 'Deutsch',
    },
    'en': {
        'name': 'English',
        'name_local': 'English',
    },
    'es': {
        'name': 'Spanish',
        'name_local': 'Español',
    },
    'fr': {
        'name': 'French',
        'name_local': 'Français',
    },
    'it': {
        'name': 'Italian',
        'name_local': 'Italiano',
    },
    'nl': {
        'name': 'Dutch',
        'name_local': 'Nederlands',
    },
    'no': {
        'name': 'Norwegian',
        'name_local': 'Norsk',
    },
    'pt': {
        'name': 'Portuguese',
        'name_local': 'Português',
    },
    'pt-br': {
        'name': 'Brazilian Portuguese',
        'name_local': 'Português Brasileiro',
    },
    'ru': {
        'name': 'Russian',
        'name_local': 'Русский',
    },
    'sv': {
        'name': 'Swedish',
        'name_local': 'Svenska',
    }
}


@lru_cache(maxsize=None)
def pull(filename, locale='en'):
    """
    Open file and get content from file. Memorize result using lru_cache.
    pull - is internal function, please do not use this function outside
    the module 'church'.
    Args:
        filename: The name of file.
        locale: Locale

           locale code                   folder
           _________________________________________
           da - Danish                   (data/da)
           de - German                   (data/de)
           en - English                  (data/en)
           ru - Russian                  (data/ru)
           fr - French                   (data/fr)
           es - Spanish                  (data/es)
           it - Italian                  (data/it)
           pt - Portuguese               (data/pt)
           no - Norwegian                (data/no)
           sv - Swedish                  (data/sv)
           pt-br - Brazilian Portuguese  (data/pt-br)

    :return: The content of the file.
    """
    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s does not supported" % locale)

    with open(join(PATH + '/' + locale, filename), 'r') as f:
        data = f.readlines()

    return data
