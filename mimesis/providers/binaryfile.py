"""Binary data provider."""

import typing as t

from mimesis.constants import DATADIR
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

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)

    class Meta:
        name = "binaryfile"

    def _read_file(
        self,
        *,
        file_type: AudioFile | CompressedFile | DocumentFile | ImageFile | VideoFile,
    ) -> bytes:
        file_type = self.validate_enum(file_type, file_type.__class__)
        file_path = DATADIR / "bin" / f"sample.{file_type}"

        with open(file_path, "rb") as file:
            return file.read()

    def video(self, *, file_type: VideoFile = VideoFile.MP4) -> bytes:
        """Generates video file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def audio(self, *, file_type: AudioFile = AudioFile.MP3) -> bytes:
        """Generates an audio file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def document(self, *, file_type: DocumentFile = DocumentFile.PDF) -> bytes:
        """Generates a document of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def image(self, *, file_type: ImageFile = ImageFile.PNG) -> bytes:
        """Generates an image of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def compressed(self, *, file_type: CompressedFile = CompressedFile.ZIP) -> bytes:
        """Generates a compressed file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)
