from unittest import TestCase

from elizabeth.builtins import RussiaSpecProvider
from elizabeth.exceptions import JSONKeyError


class RussiaTest(TestCase):
    def setUp(self):
        self.russia = RussiaSpecProvider()

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

    def test_patronymic(self):
        patronymic = self.russia.patronymic

        self.assertIsInstance(patronymic(gender='female'), str)
        self.assertTrue(len(patronymic(gender='female')) >= 4)

        self.assertIsInstance(patronymic(gender='male'), str)
        self.assertTrue(len(patronymic(gender='male')) >= 4)

        self.assertRaises(JSONKeyError, lambda: patronymic(gender='nil'))

    def test_generate_sentence(self):
        result = self.russia.generate_sentence()
        self.assertTrue(len(result) >= 20)
        self.assertIsInstance(result, str)
