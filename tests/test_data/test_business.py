# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth import Business
import elizabeth.core.interdata as common
from tests.test_data import DummyCase


class BusinessBaseTest(TestCase):
    def setUp(self):
        self.business = Business()

    def tearDown(self):
        del self.business

    def test_copyright(self):
        result = self.business.copyright()
        self.assertIn('©', result)
        self.assertIsNotNone(result)

        result_1 = self.business.copyright(date=False)
        self.assertIn('©', result)
        self.assertIsNotNone(result_1)

        result_args = self.business.copyright(minimum=1999, maximum=2010)
        date = result_args.split()[1].split('-')
        self.assertTrue(int(date[0]) >= 1999 and int(date[1]) <= 2010)

    def test_currency_sio(self):
        result = self.business.currency_iso()
        self.assertIn(result, common.CURRENCY)


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

    def test_price(self):
        currencies = ('kr', '€', 'R$', '₽', '$', 'zł', '﷼', "£", 'Ft', '₩')
        result = self.generic.business.price(minimum=100.00, maximum=1999.99)
        price, symbol = result.split(' ')
        self.assertTrue((float(price) >= 100.00) and (float(price) <= 2000))
        self.assertIn(symbol, currencies)
