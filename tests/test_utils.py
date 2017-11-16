# -*- coding: utf-8 -*-

import os
import socket

import pytest

from mimesis.enums import Gender
from mimesis.exceptions import UnsupportedLocale, UnexpectedGender
from mimesis.utils import (
    check_gender,
    custom_code,
    download_image,
    locale_info,
    luhn_checksum,
    pull,
    update_dict,
    setup_locale,
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
    assert luhn_checksum('7992739871') == '3'


def test_pull():
    data = pull('personal.json', 'en')

    assert data['views_on'] is not None
    assert isinstance(data['views_on'], list)
    with pytest.raises(UnsupportedLocale):
        pull('personal.json', 'w')
    with pytest.raises(FileNotFoundError):
        pull('something.json', 'en')

    data = pull('address.json', 'en-gb')
    assert 'city' in data
    assert 'Aberystwyth' in data['city']
    assert 'Addison' not in data['city']

    data = pull('address.json', 'en-au')
    assert 'city' in data
    assert 'Melbourne' in data['city']


@pytest.mark.parametrize(
    'ctx', [
        False,
        True,
    ],
)
def test_download_image(ctx):
    url = 'https://github.com/lk-geimfari/mimesis/' \
          'raw/master/media/mimesis.png'

    if is_connected():
        verified = download_image(url=url, unverified_ctx=ctx)
        assert verified == 'mimesis.png'
        os.remove(verified)


def test_locale_information():
    result = locale_info(locale='ru')
    assert result == 'Russian'

    result_1 = locale_info(locale='is')
    assert result_1 == 'Icelandic'
    with pytest.raises(UnsupportedLocale):
        locale_info(locale='w')


def test_update_dict():
    first = {
        'animals': {
            'dogs': [
                'spaniel',
            ],
        },
    }
    second = {
        'animals': {
            'cats': [
                'maine coon',
            ],
        },
    }

    result = update_dict(first, second)

    assert 'cats' in result['animals']
    assert 'dogs' in result['animals']

    third = {
        'animals': {
            'dogs': [
                'golden retriever',
            ],
        },
    }

    result = update_dict(first, third)
    assert 'spaniel' not in result['animals']['dogs']


@pytest.mark.parametrize(
    'inp, out', [
        ('EN', 'en'),
        ('DE', 'de'),
        ('RU', 'ru'),
    ],
)
def test_setup_locale(inp, out):
    result = setup_locale(inp)
    assert result == out


def test_custom_code():
    result = custom_code(mask='@@@-###-@@@', char='@', digit='#')
    assert len(result) == 11

    a, b, c = result.split('-')
    assert a.isalpha()
    assert b.isdigit()
    assert c.isalpha()


@pytest.mark.parametrize(
    'gender, excepted', [
        (Gender.F, 'female'),
        (Gender.M, 'male'),
        (Gender.MALE, 'male'),
        (Gender.FEMALE, 'female'),
        (Gender.RANDOM, ['female', 'male']),
    ],
)
def test_check_gender(gender, excepted):
    result = check_gender(gender).value
    assert (result == excepted) or (result in excepted)
    assert gender in Gender

    with pytest.raises(UnexpectedGender):
        check_gender(gender=None)
