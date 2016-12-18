# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.exceptions import (
    UnsupportedLocale
)
from elizabeth.utils import pull


class PullTestCase(TestCase):
    def test_pull(self):
        data = pull('personal.json', 'en')
        self.assertIsNotNone(data['views_on'])
        self.assertIsInstance(data['views_on'], list)
        self.assertRaises(UnsupportedLocale,
                          lambda: pull('personal.json', 'spoke'))
        self.assertRaises(FileNotFoundError,
                          lambda: pull('something.json', 'en'))
