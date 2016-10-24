# -*- coding: utf-8 -*-

from unittest import TestCase

import church._common as common
from church.church import Business
from church.utils import pull

from tests import LANG


class BusinessTestCase(TestCase):
    def setUp(self):
        self.business = Business(LANG)

    def test_company_type(self):
        result = self.business.company_type()
        self.assertTrue(len(result) > 8)

    def test_company(self):
        result = self.business.company()
        parent_file = pull('company', self.business.lang)
        self.assertIn(result + '\n', parent_file)

    def test_copyright(self):
        result = self.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)
        self.assertTrue(len(result) > 4)

    def test_currency_sio(self):
        result = self.business.currency_iso()
        self.assertIn(result, common.CURRENCY)
