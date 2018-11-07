# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import File
from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestFile(object):

    @pytest.fixture
    def file(self):
        return File()

    def test_str(self, file):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(file))

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
    def test_extension(self, file, extension):
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
    def test_mime_type(self, file, type_):
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
    def test_file_name(self, file, file_type):
        result = file.file_name(file_type=file_type)

        assert isinstance(result, str)
        assert result

    def test_size(self, file):
        result = file.size(10, 10)
        size = result.split(' ')[0].strip()
        assert int(size) == 10


class TestSeededFile(object):

    @pytest.fixture
    def f1(self, seed):
        return File(seed=seed)

    @pytest.fixture
    def f2(self, seed):
        return File(seed=seed)

    def test_extension(self, f1, f2):
        assert f1.extension() == f2.extension()
        assert f1.extension(file_type=FileType.AUDIO) == \
            f2.extension(file_type=FileType.AUDIO)

    def test_mime_type(self, f1, f2):
        assert f1.mime_type() == f2.mime_type()
        assert f1.mime_type(type_=MimeType.IMAGE) == \
            f2.mime_type(type_=MimeType.IMAGE)

    def test_file_name(self, f1, f2):
        assert f1.file_name() == f2.file_name()
        assert f1.file_name(file_type=FileType.SOURCE) == \
            f2.file_name(file_type=FileType.SOURCE)

    def test_size(self, f1, f2):
        assert f1.size() == f2.size()
        assert f1.size(minimum=8, maximum=1024) == \
            f2.size(minimum=8, maximum=1024)
