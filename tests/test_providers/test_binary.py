import tempfile

import pytest

from mimesis.enums import (
    AudioFile,
    CompressedFile,
    DocumentFile,
    ImageFile,
    VideoFile,
)
from mimesis.providers.binaryfile import BinaryFile


class TestBinaryFile:
    @pytest.fixture
    def binary(self):
        return BinaryFile()

    @pytest.mark.parametrize(
        "method_name, extensions",
        [
            ("video", (VideoFile.MP4, VideoFile.MOV)),
            ("audio", (AudioFile.MP3, AudioFile.AAC)),
            ("image", (ImageFile.PNG, ImageFile.JPG, ImageFile.GIF)),
            ("document", (DocumentFile.DOCX, DocumentFile.XLSX, DocumentFile.PDF)),
            ("compressed", (CompressedFile.ZIP, CompressedFile.GZIP)),
        ],
    )
    def test_all_methods(self, binary, method_name, extensions):
        method = getattr(binary, method_name)
        with pytest.raises(TypeError):
            for extension in extensions:
                method(extension)

        for extension in extensions:
            content = method(file_type=extension)
            assert isinstance(content, bytes)

            with tempfile.TemporaryFile() as f:
                f.write(content)
