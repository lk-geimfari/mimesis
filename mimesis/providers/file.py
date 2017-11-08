import re

from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text


class File(BaseProvider):
    """Class for generate fake data for files."""

    def __init__(self):
        super().__init__()
        self.__text = Text('en')

    def __sub(self, string: str = '') -> str:
        """Replace spaces in string.

        :param str string: String.
        :return: String without spaces.
        :rtype: str
        """
        replacer = self.random.choice(['_', '-'])
        return re.sub('\s+', replacer, string.strip())

    def extension(self, file_type: str = 'text') -> str:
        """Get a random file extension from list.

        :param str file_type:
            File type (source, text, data, audio, video, image,
            executable, compressed).
        :return: Extension of a file.
        :rtype: str

        :Example:
            .py (file_type='source').
        """
        key = file_type.lower()
        return self.random.choice(EXTENSIONS[key])

    def mime_type(self, type_t: str = 'application') -> str:
        """Get a random mime type from list.

        :param str type_t:
            Type of media: (application, image, video, audio, text, message).
        :return: Mime type.
        :rtype: str
        :raises ValueError: if type_t is not supported.
        """
        supported = ' '.join(MIME_TYPES.keys())

        if type_t not in list(MIME_TYPES.keys()):
            raise ValueError(
                'Unsupported mime type! Use: {}'.format(supported))

        mime_type = self.random.choice(MIME_TYPES[type_t])
        return mime_type

    def size(self, minimum: int = 1, maximum: int = 100) -> str:
        """Get size of file.

        :param int minimum: Maximum value.
        :param int maximum: Minimum value.
        :return: Size of file.
        :rtype: str

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

    def file_name(self, file_type: str = 'data') -> str:
        """Get a random file name with some extension.

        :param str file_type:
            File type (source, text, data, audio, video,
            image, executable, compressed)
        :return: File name.
        :rtype: str

        :Example:
            legislative.txt
        """
        name = self.__text.word()
        ext = self.extension(file_type)

        return '{name}{ext}'.format(
            name=self.__sub(name),
            ext=ext,
        )
