# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.intd import EXTENSIONS, MIME_TYPES
from elizabeth.core.providers import File


@pytest.fixture
def file():
    return File()


def test_extension(file):
    text = file.extension(file_type='text')
    assert text in EXTENSIONS['text']

    source = file.extension(file_type='source')
    assert source in EXTENSIONS['source']


def test_mime_type(file):
    result = file.mime_type()
    assert result in MIME_TYPES
