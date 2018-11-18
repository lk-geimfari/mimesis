# -*- coding: utf-8 -*-

import os

import pytest

from mimesis import shortcuts


def test_luhn_checksum():
    assert shortcuts.luhn_checksum('7992739871') == '3'


@pytest.mark.parametrize(
    'ctx', [
        False,
        True,
    ],
)
def test_download_image(ctx):
    url_with_extinsion = 'https://raw.githubusercontent.com/lk-geimfari/' \
                         'mimesis/master/media/logo.png'

    verified = shortcuts.download_image(
        url=url_with_extinsion,
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
