# -*- coding: utf-8 -*-

"""File data provider."""

import re
from pathlib import Path
from typing import Any, Optional

from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import (
    AudioFile,
    CompressedFile,
    DocumentFile,
    FileType,
    ImageFile,
    MimeType,
    VideoFile,
)
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text

__all__ = ["File", "Writable"]


class File(BaseProvider):
    """Class for generate data related to files."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.__text = Text("en", seed=self.seed)

    class Meta:
        """Class for metadata."""

        name = "file"

    def __sub(self, string: str = "") -> str:
        """Replace spaces in string.

        :param string: String.
        :return: String without spaces.
        """
        replacer = self.random.choice(["_", "-"])
        return re.sub(r"\s+", replacer, string.strip())

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
        unit = self.random.choice(["bytes", "kB", "MB", "GB", "TB"])

        return "{num} {unit}".format(
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

        return "{name}{ext}".format(
            name=self.__sub(name),
            ext=ext,
        )


class Writable(BaseProvider):
    """Class for generating data related to transports."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._data_dir = Path(__file__).parent.parent.joinpath("data", "int", "files")

    class Meta:
        """Class for metadata."""

        name = "writable"

    def _read_file(self, /, extension: Any, enum: Any) -> bytes:
        extension = self._validate_enum(extension, enum)
        file_path = self._data_dir.joinpath(f"sample.{extension}")

        with open(file_path, "rb") as file:
            return file.read()

    def video(self, *, extension: VideoFile = VideoFile.MP4) -> bytes:
        """Generates video file of given format.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension, VideoFile)

    def audio(self, *, extension: AudioFile = AudioFile.MP3) -> bytes:
        """

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension, AudioFile)

    def document(self, *, extension: DocumentFile = DocumentFile.PDF) -> bytes:
        """

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension, DocumentFile)

    def image(self, *, extension: ImageFile = ImageFile.PNG) -> bytes:
        """

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension, ImageFile)

    def compressed(self, *, extension: CompressedFile = CompressedFile.ZIP) -> bytes:
        """

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension, CompressedFile)
