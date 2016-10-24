# -*- coding: utf-8 -*-

from unittest import TestCase

from church.church import Datetime
from church.utils import pull

from tests import LANG


class DatetimeTestCase(TestCase):
    def setUp(self):
        self.datetime = Datetime(LANG)

    def tearDown(self):
        del self.datetime

    def test_day_of_week(self):
        result = self.datetime.day_of_week() + '\n'
        self.assertGreater(len(result), 4)

        result_abbr = self.datetime.day_of_week(abbr=True)
        self.assertTrue(len(result_abbr) < 6 or '.' in result_abbr)

    def test_month(self):
        result = self.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.datetime.year(from_=2000, to_=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.datetime.periodicity()
        parent_file = pull('periodicity', self.datetime.lang)
        self.assertIn(result + '\n', parent_file)

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.datetime.birthday()
        self.assertIsInstance(result, str)
