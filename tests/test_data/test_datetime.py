# -*- coding: utf-8 -*-

from tests.test_data import DummyCase


class DatetimeTestCase(DummyCase):
    def test_day_of_week(self):
        result = self.generic.datetime.day_of_week()
        self.assertIn(result, self.generic.datetime.data['day']['name'])

        result_abbr = self.generic.datetime.day_of_week(abbr=True)
        self.assertIn(result_abbr, self.generic.datetime.data['day']['abbr'])

    def test_month(self):
        result = self.generic.datetime.month() + '\n'
        self.assertGreater(len(result), 3)

        result_abbr = self.generic.datetime.month(abbr=True)
        self.assertIsInstance(result_abbr, str)

    def test_year(self):
        result = self.generic.datetime.year(minimum=2000, maximum=2016)
        self.assertTrue((result >= 2000) and (result <= 2016))

    def test_periodicity(self):
        result = self.generic.datetime.periodicity()
        self.assertIn(result, self.generic.datetime.data['periodicity'])

    def test_day_of_month(self):
        result = self.generic.datetime.day_of_month()
        self.assertTrue((result >= 1) or (result <= 31))

    def test_birthday(self):
        result = self.generic.datetime.birthday()
        self.assertIsInstance(result, str)

        not_readable = self.generic.datetime.birthday(readable=False)
        day, month, year = not_readable.split('-')
        self.assertTrue(int(day) <= 31)
        self.assertTrue(int(month) <= 12)
        self.assertTrue((int(year) >= 1980) and (int(year) <= 2000))

        fmt = self.generic.datetime.birthday(minimum=2015, maximum=2025, readable=False, fmt='%Y')
        self.assertTrue((int(year) >= 1980) and (int(year) <= 2000))
