from functools import lru_cache
from os.path import abspath, join, dirname

from .exceptions import UnsupportedLocale

PATH = abspath(join(dirname(__file__), 'data'))

__all__ = ['pull']

SUPPORTED_LOCALES = {
    "en": "English",
    "es": "Spanish",
    "de": "German",
    "fr": "French",
    "it": 'Italian',
    "ru": "Russian"
}


@lru_cache(maxsize=None)
def pull(filename, locale='en'):
    """
    Open file and get content from file. Memorize result using lru_cache.
    pull - is internal function, please do not use this function outside
    the module'church'.
    Args:
        filename: The name of file.
        locale:
           de - German  (data/de)
           en - English (data/en)
           ru - Russian (data/ru)
           fr - French  (data/fr)
           es - Spanish (data/es)
           it - Italian (data/it)
    Returns: The content of the file.
    """
    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s does not supported" % locale)

    with open(join(PATH + '/' + locale, filename), 'r') as f:
        data = f.readlines()

    return data
