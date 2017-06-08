# -*- coding: utf-8 -*-

import pytest

from elizabeth.data.int import (
    EXTENSIONS,
    MIME_TYPES
)
from elizabeth.providers import File


@pytest.fixture
def file():
    return File()


def test_extension(file):
    file_types = list(EXTENSIONS.keys())

    for typ in file_types:
        assert file.extension(file_type=typ) in EXTENSIONS[typ]


def test_mime_type(file):
    mime_types = list(MIME_TYPES.keys())

    for mime in mime_types:
        assert file.mime_type(type_t=mime) in MIME_TYPES[mime]

    with pytest.raises(ValueError):
        file.mime_type(type_t='nil')
