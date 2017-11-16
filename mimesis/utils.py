"""This module is provide internal util functions for mimesis
"""

import string
import collections
import functools
import json
import ssl
from os import path
from random import randint, choice
from typing import Mapping, Union
from urllib import request

from mimesis.exceptions import (
    UnexpectedGender,
    UnsupportedLocale,
)
from mimesis import config
from mimesis.typing import JSON
from mimesis.enums import Gender

__all__ = ['pull', 'download_image', 'locale_info', 'check_gender']

PATH = path.abspath(path.join(path.dirname(__file__), 'data'))


def locale_info(locale: str) -> str:
    """Return name (in english) or local name of the locale

    :param str locale: Locale abbreviation.
    :return: Locale name.
    :raises UnsupportedLocale: if locale is not supported.
    """
    locale = locale.lower()
    supported = config.SUPPORTED_LOCALES

    if locale not in supported:
        raise UnsupportedLocale(
            'Locale {} is not supported'.format(locale))

    return supported[locale]['name']


def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    :param str num: The number to calculate a checksum for as a string.
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
    """Open json file file and get content from file and memorize result using
     lru_cache.

    :param str file: The name of file.
    :param str locale: Locale.
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

        :param locale_name: Name of locale to pull.
        :return: Dict of data from file
        """
        file_path = path.join(PATH + '/' + locale_name, file)
        # Needs explicit encoding for Windows
        with open(file_path, 'r', encoding='utf8') as f:
            return json.load(f)

    locale = locale.lower()

    if locale not in config.SUPPORTED_LOCALES:
        raise UnsupportedLocale('Locale %s is not supported' % locale)

    master_locale = locale.split('-')[0]
    data = get_data(master_locale)

    # Handle sub-locales
    if '-' in locale:
        data = update_dict(data, get_data(locale))

    return data


def download_image(url: str = '', save_path: str = '',
                   unverified_ctx: bool = False) -> Union[None, str]:
    """Download image and save in current directory on local machine.

    :param str url: URL to image.
    :param str save_path: Saving path.
    :param bool unverified_ctx: Create unverified context.
    :return: Image name.
    :rtype: str or None
    """
    if unverified_ctx:
        ssl._create_default_https_context = ssl._create_unverified_context

    if url is not None:
        image_name = url.rsplit('/')[-1]
        request.urlretrieve(url, save_path + image_name)
        return image_name
    return None


def setup_locale(locale: str = '') -> str:
    """Setup locale to BaseProvider.

    :param str locale: Locale
    :return: Locale in lowercase.
    """
    if not locale:
        return config.DEFAULT_LOCALE

    return locale.lower()


def custom_code(mask: str = '@###',
                char: str = '@', digit: str = '#') -> str:
    """Generate custom code using ascii uppercase and random integers.

    :param str mask: Mask of code.
    :param str char: Placeholder for characters.
    :param str digit: Placeholder for digits.
    :return: Custom code.

    :Example:
        5673-AGFR-SFSFF-1423-4/AD.
    """
    code = ''
    for p in mask:
        if p == char:
            code += choice(string.ascii_uppercase)
        elif p == digit:
            code += str(randint(0, 9))
        else:
            code += p

    return code


def check_gender(gender: Gender = Gender.RANDOM) -> Gender:
    """Check correctness of the gender.

    :param gender: Gender's enum object.
    :return: Gender.
    :raises UnexpectedGender: if gender has incorrect value.
    """
    if gender and gender in Gender:
        return gender
    else:
        raise UnexpectedGender(
            'You should use enum object "Gender" '
            'from the module mimesis.enums'
        )
