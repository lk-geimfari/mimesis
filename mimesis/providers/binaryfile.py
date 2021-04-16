# -*- coding: utf-8 -*-

"""Binary data provider."""

from pathlib import Path
from typing import Any, Union

from mimesis.enums import (
    AudioFile,
    CompressedFile,
    DocumentFile,
    ImageFile,
    VideoFile,
)
from mimesis.providers.base import BaseProvider

__all__ = ["BinaryFile"]


class BinaryFile(BaseProvider):
    """Class for generating binary data"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._data_dir = Path(__file__).parent.parent

    class Meta:
        """Class for metadata."""

        name = "binary_file"

    def _read_file(
        self,
        *,
        extension: Union[
            AudioFile,
            CompressedFile,
            DocumentFile,
            ImageFile,
            VideoFile,
        ],
    ) -> bytes:
        extension = self._validate_enum(extension, extension.__class__)
        file_path = self._data_dir.joinpath("data", "bin", f"sample.{extension}")

        with open(file_path, "rb") as file:
            return file.read()

    def video(self, *, extension: VideoFile = VideoFile.MP4) -> bytes:
        """Generates video file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension=extension)

    def audio(self, *, extension: AudioFile = AudioFile.MP3) -> bytes:
        """Generates audio file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension=extension)

    def document(self, *, extension: DocumentFile = DocumentFile.PDF) -> bytes:
        """Generates document of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension=extension)

    def image(self, *, extension: ImageFile = ImageFile.PNG) -> bytes:
        """Generates image of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension=extension)

    def compressed(self, *, extension: CompressedFile = CompressedFile.ZIP) -> bytes:
        """Generates compressed file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param extension: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(extension=extension)
