# -*- coding: utf-8 -*-

import elizabeth.data.common as common

from tests.test_data import DummyCase


class BusinessTestCase(DummyCase):
    def test_company_type(self):
        result = self.generic.business.company_type()
        self.assertIn(result,
                      self.generic.business.data['company']['type']['title'])

        result_2 = self.generic.business.company_type(abbr=True)
        self.assertIn(result_2,
                      self.generic.business.data['company']['type']['abbr'])

    def test_company(self):
        result = self.generic.business.company()
        self.assertIn(result, self.generic.business.data['company']['name'])

    def test_copyright(self):
        result = self.generic.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)
        self.assertTrue(len(result) > 4)

    def test_currency_sio(self):
        result = self.generic.business.currency_iso()
        self.assertIn(result, common.CURRENCY)
