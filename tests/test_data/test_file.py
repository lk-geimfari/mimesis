# -*- coding: utf-8 -*-

import pytest

from mimesis import File
from mimesis.enums import FileType, MimeType
from mimesis.exceptions import NonEnumerableError
from mimesis.data import EXTENSIONS, MIME_TYPES


@pytest.fixture
def file():
    return File()


@pytest.mark.parametrize(
    'extension', [
        FileType.AUDIO,
        FileType.COMPRESSED,
        FileType.DATA,
        FileType.EXECUTABLE,
        FileType.IMAGE,
        FileType.SOURCE,
        FileType.TEXT,
        FileType.VIDEO,
    ],
)
def test_extension(file, extension):
    ext = file.extension(file_type=extension)
    assert ext in EXTENSIONS[extension.value]


@pytest.mark.parametrize(
    'type_', [
        MimeType.APPLICATION,
        MimeType.AUDIO,
        MimeType.IMAGE,
        MimeType.MESSAGE,
        MimeType.TEXT,
        MimeType.VIDEO,
    ],
)
def test_mime_type(file, type_):
    result = file.mime_type(type_=type_)
    assert result in MIME_TYPES[type_.value]

    with pytest.raises(NonEnumerableError):
        file.mime_type(type_='nil')


@pytest.mark.parametrize(
    'file_type', [
        FileType.AUDIO,
        FileType.COMPRESSED,
        FileType.DATA,
        FileType.EXECUTABLE,
        FileType.IMAGE,
        FileType.SOURCE,
        FileType.TEXT,
        FileType.VIDEO,
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
