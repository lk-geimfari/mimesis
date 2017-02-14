# -*- coding: utf-8 -*-

import pytest

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


def test_locale_information():
    result = locale_information(locale='ru')
    assert result == 'Russian'

    result_1 = locale_information(locale='is')
    assert result_1 == 'Icelandic'
    with pytest.raises(UnsupportedLocale):
        locale_information(locale='w')
