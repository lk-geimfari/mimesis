# -*- coding: utf-8 -*-

import os

import pytest

from mimesis import utils
from mimesis.exceptions import UnsupportedLocale


def test_luhn_checksum():
    assert utils.luhn_checksum('7992739871') == '3'


def test_pull():
    data = utils.pull('person.json', 'en')

    assert data['views_on'] is not None
    assert isinstance(data['views_on'], list)
    with pytest.raises(UnsupportedLocale):
        utils.pull('personal.json', 'w')
    with pytest.raises(FileNotFoundError):
        utils.pull('something.json', 'en')

    data = utils.pull('address.json', 'en-gb')
    assert 'city' in data
    assert 'Aberystwyth' in data['city']
    assert 'Addison' not in data['city']

    data = utils.pull('address.json', 'en-au')
    assert 'city' in data
    assert 'Melbourne' in data['city']


@pytest.mark.parametrize(
    'ctx', [
        False,
        True,
    ],
)
def test_download_image(ctx):
    url = 'https://raw.githubusercontent.com/lk-geimfari/' \
          'mimesis/master/media/logo.png'

    verified = utils.download_image(url=url, unverified_ctx=ctx)
    assert verified == 'logo.png'
    os.remove(verified)

    result = utils.download_image('', unverified_ctx=ctx)
    assert result is None


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

    result = utils.update_dict(first, second)

    assert 'cats' in result['animals']
    assert 'dogs' in result['animals']

    third = {
        'animals': {
            'dogs': [
                'golden retriever',
            ],
        },
    }

    result = utils.update_dict(first, third)
    assert 'spaniel' not in result['animals']['dogs']


@pytest.mark.parametrize(
    'inp, out', [
        ('EN', 'en'),
        ('DE', 'de'),
        ('RU', 'ru'),
    ],
)
def test_setup_locale(inp, out):
    result = utils.setup_locale(inp)
    assert result == out


def test_setup_locale_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        utils.setup_locale('nil')
