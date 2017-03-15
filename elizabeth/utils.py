# utils.py

import functools
import json
import os.path as path
import urllib.request as request

from elizabeth.exceptions import UnsupportedLocale
from elizabeth.settings import SUPPORTED_LOCALES

__all__ = ['pull']

PATH = path.abspath(path.join(path.dirname(__file__), 'data'))


def locale_information(locale: str) -> str:
    """Return name (in english) or local name of the locale

    :param locale: Locale abbreviation.
    :type locale: str
    :returns: Locale name.
    :rtype: str
    :Example:

    >>> from elizabeth.utils import locale_information
    >>> locale_information('sv')
    'Swedish'
    """
    locale = locale.lower()

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s does not supported" % locale)

    return SUPPORTED_LOCALES[locale]['name']


def luhn_checksum(num) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    See: https://en.wikipedia.org/wiki/Luhn_algorithm
    :param num: The number to calculate a checksum for as a string
    :type num: str
    :returns: checksum for number
    :rtype: str
    :Example:

    >>> from elizabeth.utils import luhn_checksum
    >>> luhn_checksum("7992739871")
    '3'
    """
    check = 0
    for i, s in enumerate(reversed([x for x in num])):
        sx = int(s)
        sx = sx * 2 if i % 2 == 0 else sx
        sx = sx - 9 if sx > 9 else sx
        check += sx
    return str(check * 9 % 10)


@functools.lru_cache(maxsize=None)
def pull(file, locale='en') -> dict:
    """Open file and get content from file. Memorize result using lru_cache.

    pull - is internal function, please do not use this function outside
    the module 'elizabeth'.

    +------------------------------+--------------+
    | Locale Code                  | Folder       |
    +==============================+==============+
    | cs - Czech                   | (data/cs)    |
    +------------------------------+--------------+
    | da - Danish                  | (data/da)    |
    +------------------------------+--------------+
    | de - German                  | (data/de)    |
    +------------------------------+--------------+
    | de-at - Austrian german      | (data/de-at) |
    +------------------------------+--------------+
    | en - English                 | (data/en)    |
    +------------------------------+--------------+
    | en-au - Australian English   | (data/en-au) |
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
    | jp - Japanese                | (data/jp)    |
    +------------------------------+--------------+
    | ko - Korean                  | (data/ko)    |
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
    | tr - Turkish                 | (data/tr)    |
    +------------------------------+--------------+

    :param file: The name of file.
    :param locale: Locale.
    :returns: The content of the file.

    :Example:

        >>> from elizabeth.utils import pull
        >>> en = pull(file='datetime.json', locale='en')
        >>> isinstance(en, dict)
        True
        >>> en['day']['abbr'][0]
        'Mon.'
    """

    locale = locale.lower()

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s is not supported" % locale)

    master_locale = locale.split("-")[0]
    master_locale_path = path.join(PATH + '/' + master_locale, file)

    # Needs explicit encoding for Windows
    with open(master_locale_path, 'r', encoding='utf8') as f:
        data = json.load(f)

    # Handle sub-locales
    if "-" in locale:
        sub_locale_path = path.join(PATH + '/' + locale, file)
        with open(sub_locale_path, 'r', encoding='utf8') as f:
            data.update(json.load(f))

    return data


def download_image(url, save_path='', unverified_ctx=False):
    """Download image and save in current directory on local machine.

    :param url: URL to image.
    :param save_path: Saving path.
    :param unverified_ctx: Create unverified context. Use if you get CERTIFICATE_VERIFY_FAILED.
    :return: Image name.
    :rtype: str
    :Example:
        f88684c22086d4bb3983159fb1e95c22.png
    """
    if unverified_ctx:
        import ssl
        try:
            ssl._create_default_https_context = ssl._create_stdlib_context
        except AttributeError:
            raise NotImplementedError("unverified_ctx is only supported in Python 3.4+")

    if url is not None:
        image_name = url.rsplit('/')[-1]
        request.urlretrieve(url, save_path + image_name)
        return image_name
    return None
