import re
from unittest import TestCase

from elizabeth.builtins import Brazil, USA, Russia


class BrazilTest(TestCase):
    def setUp(self):
        self.pt_br = Brazil()

    def tearDown(self):
        del self.pt_br

    def test_cpf(self):
        # test if the cpf has 14 digits with the mask
        cpf_with_mask = self.pt_br.cpf()
        self.assertEqual(len(cpf_with_mask), 14, cpf_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cpf_with_mask)
        self.assertEqual('..-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cpf_with_mask)),
                         11, cpf_with_mask)
        # test for the cpf without mask
        cpf_without_mask = self.pt_br.cpf(False)
        self.assertEqual(len(cpf_without_mask), 11, cpf_without_mask)
        non_numeric_digits = re.sub('\d', '', cpf_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)

    def test_cnpj(self):
        # test if the cnpj has 14 digits with the mask
        cnpj_with_mask = self.pt_br.cnpj()
        self.assertEqual(len(cnpj_with_mask), 18, cnpj_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cnpj_with_mask)
        self.assertEqual('../-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cnpj_with_mask)),
                         14, cnpj_with_mask)
        # test for the cnpj without mask
        cnpj_without_mask = self.pt_br.cnpj(False)
        self.assertEqual(len(cnpj_without_mask), 14, cnpj_without_mask)
        non_numeric_digits = re.sub('\d', '', cnpj_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)


class USATest(TestCase):
    def setUp(self):
        self.usa = USA()

    def tearDown(self):
        del self.usa

    def test_usps_tracking_number(self):
        result = self.usa.tracking_number(service='usps')
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 24 or len(result) == 17)

        result_1 = self.usa.tracking_number(service='fedex')
        self.assertIsNotNone(result_1)
        self.assertTrue(len(result_1) == 14 or len(result_1) == 18)

        result_2 = self.usa.tracking_number(service='ups')
        self.assertIsNotNone(result_2)
        self.assertTrue(len(result_2) == 18)


class RussiaTest(TestCase):
    def setUp(self):
        self.russia = Russia()

    def tearDown(self):
        del self.russia

    def test_passport_series(self):
        result = self.russia.passport_series()
        self.assertIsNotNone(result)
        result = result.split(' ')
        self.assertIsInstance(result, list)

        result = self.russia.passport_series(year=10)
        region, year = result.split(' ')
        self.assertTrue(int(year) == 10)

    def test_passport_number(self):
        result = self.russia.passport_number()
        self.assertTrue(len(result) == 6)

    def test_series_and_number(self):
        result = self.russia.series_and_number()
        self.assertIsNotNone(result)
