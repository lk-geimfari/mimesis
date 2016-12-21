# -*- coding: utf-8 -*-

import re

from tests.test_data import DummyCase


class CodeTestCase(DummyCase):

    def test_issn(self):
        result = self.generic.code.issn()
        self.assertEqual(len(result), 9)

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

    def test_custom_code(self):
        result = self.generic.code.custom_code(
            mask="@###", char='@', digit='#')

        self.assertTrue(len(result) == 4)

    def test_custom_code_args(self):
        result = self.generic.code.custom_code\
            (mask="@@@-###-@@@").split('-')

        a, b, c = result
        self.assertTrue(a.isalpha() and c.isalpha() and b.isdigit())

    def test_cpf(self):
        # test if the cpf has 14 digits with the mask
        cpf_with_mask = self.generic.code.cpf()
        self.assertEqual(len(cpf_with_mask), 14, cpf_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cpf_with_mask)
        self.assertEqual('..-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cpf_with_mask)),
                         11, cpf_with_mask)
        # test for the cpf without mask
        cpf_without_mask = self.generic.code.cpf(False)
        self.assertEqual(len(cpf_without_mask), 11, cpf_without_mask)
        non_numeric_digits = re.sub('\d', '', cpf_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)

    def test_cnpj(self):
        # test if the cnpj has 14 digits with the mask
        cnpj_with_mask = self.generic.code.cnpj()
        self.assertEqual(len(cnpj_with_mask), 18, cnpj_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cnpj_with_mask)
        self.assertEqual('../-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cnpj_with_mask)),
                         14, cnpj_with_mask)
        # test for the cnpj without mask
        cnpj_without_mask = self.generic.code.cnpj(False)
        self.assertEqual(len(cnpj_without_mask), 14, cnpj_without_mask)
        non_numeric_digits = re.sub('\d', '', cnpj_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)
