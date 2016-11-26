import functools
import json
from os.path import abspath, join, dirname

from elizabeth.exceptions import UnsupportedLocale

PATH = abspath(join(dirname(__file__), 'data'))

__all__ = ['pull']

SUPPORTED_LOCALES = {
    "da": {
        "name": "Danish",
        "name_local": "Dansk"
    },
    "de": {
        "name": "German",
        "name_local": "Deutsch"
    },
    "en": {
        "name": "English",
        "name_local": "English"
    },
    "es": {
        "name": "Spanish",
        "name_local": "Español"
    },
    "fi": {
        "name": "Finnish",
        "name_local": "Suomi"
    },
    "fr": {
        "name": "French",
        "name_local": "Français"
    },
    'is': {
        'name': 'Icelandic',
        'name_local': 'Íslenska',
    },
    "it": {
        "name": "Italian",
        "name_local": "Italiano"
    },
    'nl': {
        'name': 'Dutch',
        'name_local': 'Nederlands'
    },
    "no": {
        "name": "Norwegian",
        "name_local": "Norsk"
    },
    "pl": {
        'name': "Polish",
        'name_local': "Polski",
    },
    "pt": {
        "name": "Portuguese",
        "name_local": "Português"
    },
    "pt-br": {
        "name": "Brazilian Portuguese",
        "name_local": "Português Brasileiro"
    },
    "ru": {
        "name": "Russian",
        "name_local": "Русский"
    },
    "sv": {
        "name": "Swedish",
        "name_local": "Svenska"
    },
    "etc": "Int."
}


@functools.lru_cache(maxsize=None)
def pull(file, locale='en'):
    """
    Open file and get content from file. Memorize result using lru_cache.
    pull - is internal function, please do not use this function outside
    the module 'elizabeth'.

    +------------------------------+--------------+
    | Locale Code                  | Folder       |
    +==============================+==============+
    | da - Danish                  | (data/da)    |
    +------------------------------+--------------+
    | de - German                  | (data/de)    |
    +------------------------------+--------------+
    | en - English                 | (data/en)    |
    +------------------------------+--------------+
    | ru - Russian                 | (data/ru)    |
    +------------------------------+--------------+
    | fi - Finnish                 | (data/fi)    |
    +------------------------------+--------------+
    | fr - French                  | (data/fr)    |
    +------------------------------+--------------+
    | es - Spanish                 | (data/es)    |
    +------------------------------+--------------+
    | it - Italian                 | (data/it)    |
    +------------------------------+--------------+
    | is - Icelandic               | (data/is)    |
    +------------------------------+--------------+
    | pl - Polish                  | (data/pl)    |
    +------------------------------+--------------+
    | pt - Portuguese              | (data/pt)    |
    +------------------------------+--------------+
    | nl - Dutch                   | (data/nl)    |
    +------------------------------+--------------+
    | no - Norwegian               | (data/no)    |
    +------------------------------+--------------+
    | pt-br - Brazilian Portuguese | (data/pt-br) |
    +------------------------------+--------------+
    | sv - Swedish                 | (data/sv)    |
    +------------------------------+--------------+

    :param file: The name of file.
    :param locale: Locale.
    :returns: The content of the file.
    """

    locale = locale.lower()

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s does not supported" % locale)

    with open(join(PATH + '/' + locale, file), 'r') as f:
        data = json.load(f)

    return data


# TODO: Refactoring
def __push(**kwargs):
    """
    Dict to json file.
    :param kwargs: Kwargs
    :return: None
    """
    skeleton = {
        'key': {
            'key': 'value',
        }
    }

    locale = kwargs.get('locale', 'en')
    file = kwargs.get('file', 'test.json')
    data = kwargs.get('data', skeleton)

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s does not supported" % locale)

    with open(join(PATH + '/' + locale, file), 'w') as f:
        json.dump(data, f)
