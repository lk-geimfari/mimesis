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

        ulocale = lambda: pull('personal.json', 'spoke')
        self.assertRaises(UnsupportedLocale, ulocale)

        # Fake file
        ffile = lambda: pull('something.json', 'en')
        self.assertRaises(FileNotFoundError, ffile)
