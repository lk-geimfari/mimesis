# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.core.interdata import EXTENSIONS, MIME_TYPES
from elizabeth.core.providers import File


class FileTest(TestCase):
    def setUp(self):
        self.file = File()

    def tearDown(self):
        del self.file

    def test_extension(self):
        text = self.file.extension(file_type='text')
        self.assertIn(text, EXTENSIONS['text'])

        source = self.file.extension(file_type='source')
        self.assertIn(source, EXTENSIONS['source'])

    def test_mime_type(self):
        result = self.file.mime_type()
        self.assertIn(result, MIME_TYPES)
