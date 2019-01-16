# -*- coding: utf-8 -*-

"""This module is provide internal util functions."""

import ssl
from os import path
from typing import Union
from urllib import request
from uuid import uuid4

__all__ = ['download_image', 'luhn_checksum']


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
        image_name = url.rsplit('/')[-1]

        splitted_name = image_name.rsplit('.')
        if len(splitted_name) < 2:
            image_name = '{}.jpg'.format(uuid4())
        else:
            image_name = '{}.{}'.format(uuid4(), splitted_name[-1])
        full_image_path = path.join(save_path, image_name)
        request.urlretrieve(url, full_image_path)
        return full_image_path
    return None
