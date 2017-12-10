# -*- coding: utf-8 -*-

import pytest

from mimesis import File
from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.exceptions import NonEnumerableError


@pytest.fixture
def file():
    return File()


@pytest.fixture
def _seeded_file():
    return File(seed=42)


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


def test_seeded_extension(_seeded_file):
    result = _seeded_file.extension(file_type=FileType.SOURCE)
    assert result == '.pl'
    result = _seeded_file.extension()
    assert result == '.html'
    result = _seeded_file.extension()
    assert result == '.mp3'


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


def test_seeded_mime_type(_seeded_file):
    result = _seeded_file.mime_type(type_=MimeType.APPLICATION)
    assert result == 'application/reputon+json'
    result = _seeded_file.mime_type()
    assert result == 'application/vnd.ims.lis.v2.result+json'
    result = _seeded_file.mime_type()
    assert result == 'audio/GSM-EFR'


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


def test_seeded_file_name(_seeded_file):
    result = _seeded_file.file_name(file_type=FileType.EXECUTABLE)
    assert result == 'superior.exe'
    result = _seeded_file.file_name()
    assert result == 'checking.html'
    result = _seeded_file.file_name()
    assert result == 'amd.mp3'


def test_size(file):
    result = file.size(10, 10)
    size = result.split(' ')[0].strip()
    assert int(size) == 10


def test_seeded_size(_seeded_file):
    result = _seeded_file.size(42, 142)
    assert result == '123 bytes'
    result = _seeded_file.size()
    assert result == '4 MB'
    result = _seeded_file.size()
    assert result == '32 kB'
