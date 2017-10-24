# -*- coding: utf-8 -*-

import os
import sys

import pytest

from mimesis.exceptions import UnsupportedLocale, UnexpectedGender
from mimesis.utils import (check_gender, download_image, locale_info,
                           luhn_checksum, pull, update_dict)


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


def test_download_image(mocker):
    result = download_image(url=None)
    assert result is None

    url = 'https://github.com/lk-geimfari/mimesis/' \
          'raw/master/media/mimesis.png'

    def create_image(*args, **kwargs):
        image_name = 'mimesis.png'
        with open(image_name, 'w') as f:
            f.write('testing image')

    with mocker.patch('mimesis.utils.request.urlretrieve',
                      side_effect=create_image):
        verified = download_image(url=url)
        assert verified == 'mimesis.png'
        os.remove(verified)

        if sys.version_info.minor <= 3:
            with pytest.raises(NotImplementedError):
                download_image(url=None, unverified_ctx=True)
        else:
            unverified = download_image(url=None, unverified_ctx=True)
            assert unverified is None


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
    'abbr, gender',
    [
        ('0', ('male', 'female')),
        ('9', ('male', 'female')),
        ('1', 'male'),
        ('2', 'female'),
        ('f', 'female'),
        ('female', 'female'),
        ('m', 'male'),
        ('male', 'male'),
    ],
)
def test_check_gender(abbr, gender):
    result = check_gender(abbr)
    assert result == gender or result in gender


def test_check_gender_invalid_gender():
    with pytest.raises(UnexpectedGender):
        check_gender(gender='other')
