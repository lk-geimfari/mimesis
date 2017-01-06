# -*- coding: utf-8 -*-

import unittest

from elizabeth.exceptions import (
    UnsupportedLocale
)
from elizabeth.utils import pull, luhn_checksum


class UtilsTest(unittest.TestCase):

    def test_luhn_checksum(self):
        self.assertEqual(luhn_checksum("7992739871"), "3")

    def test_pull(self):
        f = ('personal.json', 'something.json')

        data = pull('personal.json', 'en')

        self.assertIsNotNone(data['views_on'])
        self.assertIsInstance(data['views_on'], list)
        self.assertRaises(UnsupportedLocale, lambda: pull(f[0], 'p0'))
        self.assertRaises(FileNotFoundError, lambda: pull(f[1], 'en'))
