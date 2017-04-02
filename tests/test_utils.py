# -*- coding: utf-8 -*-

import os
import pytest
import sys
import socket

from elizabeth.exceptions import UnsupportedLocale, WrongArgument
from elizabeth.utils import (
    pull, luhn_checksum,
    locale_information, download_image,
    update_dict,
    check_gender
)


def is_connected():
    try:
        host = socket.gethostbyname('https://github.com/')
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


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

    data = pull('address.json', 'en-gb')
    assert "city" in data
    assert "Aberystwyth" in data['city']
    assert "Addison" not in data['city']

    data = pull('address.json', 'en-au')
    assert "city" in data
    assert "Melbourne" in data['city']


def test_download_image():
    result = download_image(url=None)
    assert result is None

    url = "https://github.com/lk-geimfari/elizabeth/raw/master/other/elizabeth.png"

    if is_connected():
        verified = download_image(url=url)
        assert verified == "elizabeth.png"
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


def test_update_dict():
    first = {
        "animals": {
            "dogs": [
                'spaniel'
            ]
        }
    }
    second = {
        "animals": {
            "cats": [
                'maine coon'
            ]
        }
    }

    result = update_dict(first, second)

    assert "cats" in result['animals']
    assert "dogs" in result['animals']

    third = {
        "animals": {
            "dogs": [
                "golden retriever"
            ]
        }
    }

    result = update_dict(first, third)
    assert "spaniel" not in result['animals']['dogs']


def test_check_gender():
    for gender in ['male', 'female', 'Male', 'Female']:
        assert check_gender(gender) == gender.lower()

    seen_values = set()
    for _ in range(1000):
        seen_values.add(check_gender(None))
    assert seen_values == set(['male', 'female'])

    with pytest.raises(WrongArgument):
        check_gender('some other arg')
