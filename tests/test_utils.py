# -*- coding: utf-8 -*-

import os
import pytest
import sys

from elizabeth.exceptions import UnsupportedLocale
from elizabeth.utils import (
    pull, luhn_checksum,
    locale_information, download_image
)


def test_luhn_checksum():
    assert luhn_checksum("7992739871") == "3"


def test_pull():
    data = pull('personal.json', 'en')

    assert data['views_on'] is not None
    assert isinstance(data['views_on'], list)
    with pytest.raises(UnsupportedLocale):
        pull('personal.json', 'w')
    with pytest.raises(FileNotFoundError):
        pull('something.json', 'en')


def test_download_image():
    result = download_image(url=None)
    assert result is None

    verified = download_image(
        url="https://github.com/lk-geimfari/elizabeth/raw/master/other/elizabeth_1.png",
    )
    assert verified == "elizabeth_1.png"
    os.remove(verified)

    if sys.version_info.minor <= 3:
        with pytest.raises(NotImplementedError):
            download_image(url=None, unverified_ctx=True)
    else:
        unverified = download_image(url=None, unverified_ctx=True)
        assert unverified is None


def test_locale_information():
    result = locale_information(locale='ru')
    assert result == 'Russian'

    result_1 = locale_information(locale='is')
    assert result_1 == 'Icelandic'
    with pytest.raises(UnsupportedLocale):
        locale_information(locale='w')
