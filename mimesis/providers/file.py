"""File data provider."""

import re
import typing as t

from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text

__all__ = ["File"]


class File(BaseProvider):
    """Class for generate data related to files."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._text = Text(Locale.EN, seed=self.seed)

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "file"

    def __sub(self, string: str = "") -> str:
        """Replace spaces in string.

        :param string: String.
        :return: String without spaces.
        """
        replacer = self.random.choice(["_", "-"])
        return re.sub(r"\s+", replacer, string.strip())

    def extension(self, file_type: t.Optional[FileType] = None) -> str:
        """Get a random file extension from list.

        :param file_type: Enum object FileType.
        :return: Extension of the file.

        :Example:
            .py
        """
        key = self.validate_enum(item=file_type, enum=FileType)
        extensions = EXTENSIONS[key]
        return self.random.choice(extensions)

    def mime_type(self, type_: t.Optional[MimeType] = None) -> str:
        """Get a random mime type from list.

        :param type_: Enum object MimeType.
        :return: Mime type.
        """
        key = self.validate_enum(item=type_, enum=MimeType)
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
        unit = self.random.choice(["bytes", "kB", "MB", "GB", "TB"])
        return f"{num} {unit}"

    def file_name(self, file_type: t.Optional[FileType] = None) -> str:
        """Get a random file name with some extension.

        :param file_type: Enum object FileType
        :return: File name.

        :Example:
            legislative.txt
        """
        name = self.__sub(self._text.word())
        ext = self.extension(file_type)
        return f"{name}{ext}"
