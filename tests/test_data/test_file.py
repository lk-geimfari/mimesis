# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.providers import File
from elizabeth.data.int import (
    EXTENSIONS,
    MIME_TYPES
)


@pytest.fixture
def file():
    return File()


def test_extension(file):
    text = file.extension(file_type='text')
    assert text in EXTENSIONS['text']

    source = file.extension(file_type='source')
    assert source in EXTENSIONS['source']


def test_mime_type(file):
    application = file.mime_type(type_t='application')
    assert application in MIME_TYPES['application']

    audio = file.mime_type(type_t='audio')
    assert audio in MIME_TYPES['audio']

    image = file.mime_type(type_t='image')
    assert image in MIME_TYPES['image']

    message = file.mime_type(type_t='message')
    assert message in MIME_TYPES['message']

    text = file.mime_type(type_t='text')
    assert text in MIME_TYPES['text']

    video = file.mime_type(type_t='video')
    assert video in MIME_TYPES['video']

    with pytest.raises(ValueError):
        file.mime_type(type_t='blablabla')
