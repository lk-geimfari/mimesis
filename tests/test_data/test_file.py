# -*- coding: utf-8 -*-

import pytest

from mimesis import File
from mimesis.data import EXTENSIONS, MIME_TYPES


@pytest.fixture
def file():
    return File()


@pytest.mark.parametrize(
    'extension', [
        'audio',
        'compressed',
        'data',
        'executable',
        'image',
        'source',
        'text',
        'video',
    ],
)
def test_extension(file, extension):
    ext = file.extension(file_type=extension)

    assert ext in EXTENSIONS[extension]


@pytest.mark.parametrize(
    'mime_type', [
        'application',
        'audio',
        'image',
        'message',
        'text',
        'video',
    ],
)
def test_mime_type(file, mime_type):
    assert file.mime_type(type_t=mime_type) in MIME_TYPES[mime_type]

    with pytest.raises(ValueError):
        file.mime_type(type_t='nil')


@pytest.mark.parametrize(
    'file_type', [
        'audio',
        'compressed',
        'data',
        'executable',
        'image',
        'source',
        'text',
        'video',
    ],
)
def test_file_name(file, file_type):
    result = file.file_name(file_type=file_type)

    assert isinstance(result, str)
    assert result


def test_size(file):
    result = file.size(10, 10)
    size = result.split(' ')[0].strip()
    assert int(size) == 10
