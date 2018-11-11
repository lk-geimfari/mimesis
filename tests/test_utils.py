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
    url_with_extinsion = 'https://raw.githubusercontent.com/lk-geimfari/' \
                         'mimesis/master/media/logo.png'

    verified = utils.download_image(url=url_with_extinsion, unverified_ctx=ctx)
    assert verified == str(verified)[:-4] + '.png'
    os.remove(verified)

    url_without_extension = 'https://source.unsplash.com/300x300/?people'
    verified = utils.download_image(
        url=url_without_extension, unverified_ctx=ctx,
    )
    assert verified == str(verified)[:-4] + '.jpg'
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
