# -*- coding: utf-8 -*-

import church._common as common

from . import DummyCase


class BusinessTestCase(DummyCase):
    def test_company_type(self):
        result = self.church.business.company_type()
        self.assertIn(result,
                      self.church.business.data['company']['type']['title'])

        result_2 = self.church.business.company_type(abbr=True)
        self.assertIn(result_2,
                      self.church.business.data['company']['type']['abbr'])

    def test_company(self):
        result = self.church.business.company()
        self.assertIn(result, self.church.business.data['company']['name'])

    def test_copyright(self):
        result = self.church.business.copyright()
        copyright_symbol = '©'
        self.assertIn(copyright_symbol, result)
        self.assertTrue(len(result) > 4)

    def test_currency_sio(self):
        result = self.church.business.currency_iso()
        self.assertIn(result, common.CURRENCY)
