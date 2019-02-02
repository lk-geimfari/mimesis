# -*- coding: utf-8 -*-

import os

import pytest

from mimesis import shortcuts


@pytest.mark.parametrize(
    'number, check_sum', [
        ('5563455651', '2'),
        ('7992739871', '3'),
        ('5161675549', '5'),
    ],
)
def test_luhn_checksum(number, check_sum):
    assert shortcuts.luhn_checksum(number) == check_sum


@pytest.mark.parametrize(
    'ctx', [
        False,
        True,
    ],
)
def test_download_image(ctx):
    url = 'https://raw.githubusercontent.com/' \
          'lk-geimfari/mimesis/master/media/readme-logo.png'

    verified = shortcuts.download_image(
        url=url,
        unverified_ctx=ctx,
    )
    assert verified == str(verified)[:-4] + '.png'
    os.remove(verified)

    url_without_extension = 'https://source.unsplash.com/300x300/?people'
    verified = shortcuts.download_image(
        url=url_without_extension, unverified_ctx=ctx,
    )
    assert verified == str(verified)[:-4] + '.jpg'
    os.remove(verified)

    result = shortcuts.download_image('', unverified_ctx=ctx)
    assert result is None
