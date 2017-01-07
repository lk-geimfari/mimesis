import functools
import json

from os.path import (
    abspath,
    dirname,
    join
)

from elizabeth.exceptions import UnsupportedLocale

__all__ = ['pull']

PATH = abspath(join(dirname(__file__), 'data'))

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
    "en-gb": {
        "name": "British English",
        "name_local": "British English"
    },
    "es": {
        "name": "Spanish",
        "name_local": "Español"
    },
    "fa": {
        "name": "Farsi",
        "name_local": "فارسی"
    },
    "fi": {
        "name": "Finnish",
        "name_local": "Suomi"
    },
    "fr": {
        "name": "French",
        "name_local": "Français"
    },
    "hu": {
        'name': 'Hungarian',
        'name_local': 'Magyar'
    },
    "is": {
        'name': 'Icelandic',
        'name_local': 'Íslenska'
    },
    "it": {
        "name": "Italian",
        "name_local": "Italiano"
    },
    "ko": {
        'name': 'Korean',
        'name_local': '한국어'
    },
    "nl": {
        'name': 'Dutch',
        'name_local': 'Nederlands'
    },
    "no": {
        "name": "Norwegian",
        "name_local": "Norsk"
    },
    "pl": {
        'name': "Polish",
        'name_local': "Polski"
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
    }
}


def luhn_checksum(num):
    """
    Calculate a checksum for num using the Luhn algorithm.

    See: https://en.wikipedia.org/wiki/Luhn_algorithm
    :param num: The number to calculate a checksum for as a string
    :type num: str
    :returns: checksum for number
    :rtype: str
    :Example:

    >>> from elizabeth.utils import luhn_checksum
    >>> luhn_checksum("7992739871")
    3
    """
    check = 0
    for i, s in enumerate(reversed([x for x in num])):
        sx = int(s)
        sx = sx * 2 if i % 2 == 0 else sx
        sx = sx - 9 if sx > 9 else sx
        check += sx
    return str(check * 9 % 10)


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
    | en-gb - British English      | (data/en-gb) |
    +------------------------------+--------------+
    | ru - Russian                 | (data/ru)    |
    +------------------------------+--------------+
    | fa - Farsi                   | (data/fa)    |
    +------------------------------+--------------+
    | fi - Finnish                 | (data/fi)    |
    +------------------------------+--------------+
    | fr - French                  | (data/fr)    |
    +------------------------------+--------------+
    | es - Spanish                 | (data/es)    |
    +------------------------------+--------------+
    | hu - Hungarian               | (data/hu)    |
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

    # Needs explicit encoding for Windows
    with open(join(PATH + '/' + locale, file), 'r', encoding='utf8') as f:
        data = json.load(f)

    return data
