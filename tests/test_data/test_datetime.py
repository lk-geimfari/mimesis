# -*- coding: utf-8 -*-

import re
import datetime

from unittest import TestCase

from elizabeth import Datetime
from tests.test_data import DummyCase
from ._patterns import STR_REGEX


class DatetimeBaseTest(TestCase):
    def setUp(self):
        self.datetime = Datetime()

    def tearDown(self):
        del self.datetime

    def test_str(self):
        self.assertTrue(re.match(STR_REGEX, self.datetime.__str__()))

    def test_year(self):
        result = self.datetime.year(minimum=2000, maximum=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_day_of_month(self):
        result = self.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_date(self):
        result = self.datetime.date(start=1999, end=1999, fmt="%m/%d/%Y")

        try:  # check if is valid date in correct format
            result = datetime.datetime.strptime(result, "%m/%d/%Y")
        except ValueError:
            self.fail("date() returned value in incorrect format or invalid date")
        else:
            self.assertTrue(result.year == 1999)  # check range was applied correctly

    def test_time(self):
        result = self.datetime.time(fmt="%H:%M")

        try:  # check if is valid time in correct format
            datetime.datetime.strptime(result, "%H:%M")
        except ValueError:
            self.fail("time() returned value in incorrect format or invalid date")

    def test_century(self):
        result = self.datetime.century()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


class DatetimeTestCase(DummyCase):
    def test_day_of_week(self):
        result = self.generic.datetime.day_of_week()
        self.assertIn(result,
                      self.generic.datetime.data['day']['name'])

        result_abbr = self.generic.datetime.day_of_week(abbr=True)
        self.assertIn(result_abbr,
                      self.generic.datetime.data['day']['abbr'])

    def test_month(self):
        result = self.generic.datetime.month()
        self.assertIsNotNone(result)

        result_abbr = self.generic.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_periodicity(self):
        result = self.generic.datetime.periodicity()
        self.assertIn(result, self.generic.datetime.data['periodicity'])
