# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth import Code
from tests.test_data import DummyCase


class CodeBaseTestCase(TestCase):
    def setUp(self):
        self.code = Code('en')

    def tearDown(self):
        del self.code

    def test_custom_code(self):
        result = self.code.custom_code(
            mask="@###", char='@', digit='#')

        self.assertTrue(len(result) == 4)

    def test_custom_code_args(self):
        result = self.code.custom_code(
            mask="@@@-###-@@@").split('-')

        a, b, c = result
        self.assertTrue(
            a.isalpha() and c.isalpha() and b.isdigit())

    def test_ean(self):
        result = self.code.ean(fmt='ean-8')
        self.assertTrue(len(result) == 8)

        result = self.code.ean(fmt='ean-13')
        self.assertTrue(len(result) == 13)

    def test_imei(self):
        result = self.code.imei()
        self.assertTrue(len(result) <= 15)

    def test_pin(self):
        result = self.code.pin()
        self.assertTrue(len(result) == 4)

    def test_issn(self):
        result = self.code.issn()
        self.assertEqual(len(result), 9)


class CodeIntTestCase(DummyCase):
    def test_isbn(self):
        result = self.generic.code.isbn(fmt='isbn-10')
        self.assertTrue(len(result) >= 10)

        result = self.generic.code.isbn(fmt='isbn-13')
        self.assertTrue(len(result) >= 13)
