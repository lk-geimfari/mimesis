from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.providers import BaseProvider


class File(BaseProvider):
    """Class for generate fake data for files."""

    def extension(self, file_type='text'):
        """Get a random file extension from list.

        :param file_type:
            File type (source, text, data, audio, video, image,
            executable, compressed).
        :return: Extension of a file.
        :Example:
            .py (file_type='source').
        """
        k = file_type.lower()
        return self.random.choice(EXTENSIONS[k])

    def mime_type(self, type_t='application'):
        """Get a random mime type from list.

        :return: Mime type.
        :param type_t:
            Type of media: (application, image, video, audio, text, message).
        :rtype: str
        """
        supported = ' '.join(MIME_TYPES.keys())

        if type_t not in list(MIME_TYPES.keys()):
            raise ValueError(
                'Unsupported mime type! Use: {}'.format(supported))

        mime_type = self.random.choice(MIME_TYPES[type_t])
        return mime_type
