# utils.py

import collections
import functools
import json
import os.path as path
import urllib.request as request

from elizabeth.exceptions import UnsupportedLocale
from elizabeth.settings import SUPPORTED_LOCALES

__all__ = ['pull', 'download_image', 'locale_info']

PATH = path.abspath(path.join(path.dirname(__file__), 'data'))


def locale_info(locale: str) -> str:
    """Return name (in english) or local name of the locale

    :param locale: Locale abbreviation.
    :type locale: str
    :returns: Locale name.
    :rtype: str
    :Example:

    >>> from elizabeth.utils import locale_info
    >>> locale_info('sv')
    'Swedish'
    """
    locale = locale.lower()

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s is not supported" % locale)

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
    """Open json file file and get content from file and memorize result using lru_cache.

    .. note:: pull - is internal function, please do not use this function outside
    the module 'elizabeth'.

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

    def get_data(locale_name):
        """
        Pull JSON data from file.
        :param locale_name: Name of locale to pull.
        :return: Dict of data from file
        """
        file_path = path.join(PATH + '/' + locale_name, file)
        # Needs explicit encoding for Windows
        with open(file_path, 'r', encoding='utf8') as f:
            return json.load(f)

    locale = locale.lower()

    if locale not in SUPPORTED_LOCALES:
        raise UnsupportedLocale("Locale %s is not supported" % locale)

    master_locale = locale.split("-")[0]
    data = get_data(master_locale)

    # Handle sub-locales
    if "-" in locale:
        data = update_dict(data, get_data(locale))

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


def update_dict(initial, other):
    """Recursively update a dictionary.

    :param initial: Dict to update.
    :param other: Dict to update from.
    :return: Updated dict.
    :rtype: dict
    """
    for key, value in other.items():
        if isinstance(value, collections.Mapping):
            r = update_dict(initial.get(key, {}), value)
            initial[key] = r
        else:
            initial[key] = other[key]
    return initial
