# -*- coding: utf-8 -*-

"""File data provider."""

import re
from typing import Optional

from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text

__all__ = ['File']


class File(BaseProvider):
    """Class for generate data related to files."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.__text = Text('en', seed=self.seed)

    class Meta:
        """Class for metadata."""

        name = 'file'

    def __sub(self, string: str = '') -> str:
        """Replace spaces in string.

        :param string: String.
        :return: String without spaces.
        """
        replacer = self.random.choice(['_', '-'])
        return re.sub(r'\s+', replacer, string.strip())

    def extension(self, file_type: Optional[FileType] = None) -> str:
        """Get a random file extension from list.

        :param file_type: Enum object FileType.
        :return: Extension of the file.

        :Example:
            .py
        """
        key = self._validate_enum(item=file_type, enum=FileType)
        extensions = EXTENSIONS[key]
        return self.random.choice(extensions)

    def mime_type(self, type_: Optional[MimeType] = None) -> str:
        """Get a random mime type from list.

        :param type_: Enum object MimeType.
        :return: Mime type.
        """
        key = self._validate_enum(item=type_, enum=MimeType)
        types = MIME_TYPES[key]
        return self.random.choice(types)

    def size(self, minimum: int = 1, maximum: int = 100) -> str:
        """Get size of file.

        :param minimum: Maximum value.
        :param maximum: Minimum value.
        :return: Size of file.

        :Example:
            56 kB
        """
        num = self.random.randint(minimum, maximum)
        unit = self.random.choice(
            ['bytes', 'kB', 'MB', 'GB', 'TB'])

        return '{num} {unit}'.format(
            num=num,
            unit=unit,
        )

    def file_name(self, file_type: Optional[FileType] = None) -> str:
        """Get a random file name with some extension.

        :param file_type: Enum object FileType
        :return: File name.

        :Example:
            legislative.txt
        """
        name = self.__text.word()
        ext = self.extension(file_type)

        return '{name}{ext}'.format(
            name=self.__sub(name),
            ext=ext,
        )
