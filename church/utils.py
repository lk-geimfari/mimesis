from functools import lru_cache
from os.path import abspath, join, dirname

from .exceptions import LocaleDoesNotSupport

PATH = abspath(join(dirname(__file__), 'data'))

SUPPORTED_LOCALES = {
    "en": "English",
    "es": "Spanish",
    "de": "German",
    "fr": "French",
    "ru": "Russian"
}


@lru_cache(maxsize=None)
def pull(filename, locale='en'):
    """
    Open file and get content from file. Memorize result using lru_cache.
    Args:
        filename: The name of file.
        locale:
           de - German  (data/de)
           en - English (data/en)
           ru - Russian (data/ru)
           fr - French  (data/fr)
           es - Spanish (data/es)
    Returns: The content of the file.
    """
    if locale not in SUPPORTED_LOCALES:
        raise LocaleDoesNotSupport("Locale %s does not exist" % locale)

    with open(join(PATH + '/' + locale, filename), 'r') as f:
        data = f.readlines()

    return data
