# -*- coding: utf-8 -*-

from tests.test_data import DummyCase


class CodeTestCase(DummyCase):
    def test_isbn(self):
        result = self.generic.code.isbn(fmt='isbn-10')
        self.assertTrue(len(result) >= 10)

        result = self.generic.code.isbn(fmt='isbn-13')
        self.assertTrue(len(result) >= 13)

    def test_ean(self):
        result = self.generic.code.ean(fmt='ean-8')
        self.assertTrue(len(result) == 8)

        result = self.generic.code.ean(fmt='ean-13')
        self.assertTrue(len(result) == 13)

    def test_imei(self):
        result = self.generic.code.imei()
        self.assertTrue(len(result) <= 15)

    def test_pin(self):
        result = self.generic.code.pin()
        self.assertTrue(len(result) == 4)
