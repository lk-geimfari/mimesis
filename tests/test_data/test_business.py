# -*- coding: utf-8 -*-

from unittest import TestCase

import church._common as common
from church.church import Business
from tests import LANG


class BusinessTestCase(TestCase):
    def setUp(self):
        self.business = Business(LANG)
        self.db = self.business.data

    def test_company_type(self):
        result = self.business.company_type()
        self.assertIn(result, self.db['company']['type']['title'])

        result_2 = self.business.company_type(abbr=True)
        self.assertIn(result_2, self.db['company']['type']['abbr'])

    def test_company(self):
        result = self.business.company()
        self.assertIn(result, self.db['company']['name'])

    def test_copyright(self):
        result = self.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)
        self.assertTrue(len(result) > 4)

    def test_currency_sio(self):
        result = self.business.currency_iso()
        self.assertIn(result, common.CURRENCY)
