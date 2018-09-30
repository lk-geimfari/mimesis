"""This module is provide internal util functions."""

import collections
import functools
import json
import ssl
from os import path
from typing import List, Mapping, Optional, Union
from urllib import request
from uuid import uuid4

from mimesis import config
from mimesis.exceptions import UnsupportedLocale
from mimesis.typing import JSON

__all__: List[str] = [
    'pull',
    'setup_locale',
    'luhn_checksum',
    'download_image',
]

DATA_DIR: str = path.abspath(path.join(path.dirname(__file__), 'data'))


def luhn_checksum(num: str = '') -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    check: int = 0
    for i, s in enumerate(reversed(num)):
        sx: int = int(s)
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
            r: JSON = update_dict(
                initial.get(key, {}), value)
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
        file_path: str = path.join(DATA_DIR, locale_name, file)
        with open(file_path, 'r', encoding='utf8') as f:
            return json.load(f)

    locale = locale.lower()

    if locale not in config.SUPPORTED_LOCALES:
        raise UnsupportedLocale(locale)

    master_locale: str = locale.split('-')[0]
    data: JSON = get_data(master_locale)

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
    :return: Path to downloaded image.
    :rtype: str or None
    """
    if unverified_ctx:
        ssl._create_default_https_context = ssl._create_unverified_context

    if url:
        image_name: str = url.rsplit('/')[-1]

        splitted_name: List[str] = image_name.rsplit('.')
        if len(splitted_name) < 2:
            image_name = '{}.jpg'.format(uuid4())
        else:
            image_name = '{}.{}'.format(uuid4(), splitted_name[-1])
        full_image_path: str = path.join(save_path, image_name)
        request.urlretrieve(url, full_image_path)
        return full_image_path
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
