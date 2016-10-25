# -*- coding: utf-8 -*-

from unittest import TestCase

from church.church import Datetime
from tests import LANG


class DatetimeTestCase(TestCase):
    def setUp(self):
        self.datetime = Datetime(LANG)
        self.db = self.datetime.data

    def tearDown(self):
        del self.datetime

    def test_day_of_week(self):
        result = self.datetime.day_of_week()
        self.assertIn(result, self.db['day']['name'])

        result_abbr = self.datetime.day_of_week(abbr=True)
        self.assertIn(result_abbr, self.db['day']['abbr'])

    def test_month(self):
        result = self.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.datetime.year(from_=2000, to=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.datetime.periodicity()
        self.assertIn(result, self.db['periodicity'])

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.datetime.birthday()
        self.assertIsInstance(result, str)
