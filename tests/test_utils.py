# -*- coding: utf-8 -*-

import unittest

from elizabeth.exceptions import UnsupportedLocale
from elizabeth.utils import (
    pull, luhn_checksum,
    locale_information, download_image
)


class UtilsTest(unittest.TestCase):
    def test_luhn_checksum(self):
        self.assertEqual(luhn_checksum("7992739871"), "3")

    def test_pull(self):
        data = pull('personal.json', 'en')

        self.assertIsNotNone(data['views_on'])
        self.assertIsInstance(data['views_on'], list)
        self.assertRaises(UnsupportedLocale,
                          lambda: pull('personal.json', 'w'))
        self.assertRaises(FileNotFoundError,
                          lambda: pull('something.json', 'en'))

    def test_download_image(self):
        result = download_image(url=None)
        self.assertIsNone(result)

    def test_locale_information(self):
        result = locale_information(locale='ru')
        self.assertEqual(result, 'Russian')

        result_1 = locale_information(locale='is')
        self.assertEqual(result_1, 'Icelandic')
        self.assertRaises(UnsupportedLocale,
                          lambda: locale_information(locale='w'))
