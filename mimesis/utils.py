"""This module is provide internal util functions."""

import collections
import functools
import json
import ssl
from os import path
from typing import Mapping, Optional, Union
from urllib import request

from mimesis import config
from mimesis.exceptions import UnsupportedLocale
from mimesis.typing import JSON

__all__ = ['download_image', 'locale_info',
           'luhn_checksum', 'setup_locale', 'pull']

DATA_DIR = path.abspath(path.join(path.dirname(__file__), 'data'))


def locale_info(locale: str) -> str:
    """Check information about locale.

    :param locale: Locale abbreviation.
    :return: Locale name.
    :raises UnsupportedLocale: if locale is not supported.
    """
    locale = locale.lower()
    supported = config.SUPPORTED_LOCALES

    if locale not in supported:
        raise UnsupportedLocale(locale)

    return supported[locale]['name']


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check = 0
    for i, s in enumerate(reversed(num)):
        sx = int(s)
        sx = sx * 2 if i % 2 == 0 else sx
        sx = sx - 9 if sx > 9 else sx
        check += sx
    return str(check * 9 % 10)


def update_dict(initial: JSON, other: Mapping) -> JSON:
    """Recursively update a dictionary.

    :param initial: Dict to update.
    :type initial: dict or list
    :param other: Dict to update from.
    :type other: Mapping
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


@functools.lru_cache(maxsize=None)
def pull(file: str, locale: str = 'en') -> JSON:
    """Pull the content from the JSON and memorize one.

    Opens JSON file ``file`` in the folder ``data/locale``
    and get content from the file and memorize ones using lru_cache.

    :param file: The name of file.
    :param locale: Locale.
    :return: The content of the file.
    :rtype: dict
    :raises UnsupportedLocale: if locale is not supported.

    :Example:

        >>> from mimesis.utils import pull
        >>> en = pull(file='datetime.json', locale='en')
        >>> isinstance(en, dict)
        True
        >>> en['day']['abbr'][0]
        'Mon.'
    """
    def get_data(locale_name: str) -> JSON:
        """Pull JSON data from file.

        :param locale_name: Locale name.
        :return: Content of JSON file as dict.
        """
        file_path = path.join(DATA_DIR, locale_name, file)
        # Needs explicit encoding for Windows
        with open(file_path, 'r', encoding='utf8') as f:
            return json.load(f)

    locale = locale.lower()

    if locale not in config.SUPPORTED_LOCALES:
        raise UnsupportedLocale(locale)

    master_locale = locale.split('-')[0]
    data = get_data(master_locale)

    # Handle sub-locales
    if '-' in locale:
        data = update_dict(data, get_data(locale))

    return data


def download_image(url: str = '', save_path: str = '',
                   unverified_ctx: bool = False) -> Union[None, str]:
    """Download image and save in current directory on local machine.

    :param url: URL to image.
    :param save_path: Saving path.
    :param unverified_ctx: Create unverified context.
    :return: Image name.
    :rtype: str or None
    """
    if unverified_ctx:
        ssl._create_default_https_context = ssl._create_unverified_context

    if url:
        image_name = url.rsplit('/')[-1]
        request.urlretrieve(url, save_path + image_name)
        return image_name
    return None


def setup_locale(locale: Optional[str] = None) -> str:
    """Set up locale after pre-check.

    :param str locale: Locale
    :return: Locale in lowercase.
    :raises UnsupportedLocale: if locales is not supported.
    """
    if not locale:
        return config.DEFAULT_LOCALE

    locale = locale.lower()
    if locale not in config.SUPPORTED_LOCALES:
        raise UnsupportedLocale(locale)

    return locale
