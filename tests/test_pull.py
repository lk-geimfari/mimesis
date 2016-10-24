# -*- coding: utf-8 -*-

from unittest import TestCase

from church.exceptions import (
    UnsupportedLocale
)
from church.utils import pull


class PullTestCase(TestCase):
    def test_pull(self):
        result = pull('views_on', 'en')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertRaises(
            UnsupportedLocale, lambda: pull('views_on', 'spoke'))
        self.assertRaises(
            FileNotFoundError, lambda: pull('something', 'en'))

