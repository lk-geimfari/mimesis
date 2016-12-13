# -*- coding: utf-8 -*-

from tests.test_data import DummyCase


class DatetimeTestCase(DummyCase):
    def test_day_of_week(self):
        result = self.generic.datetime.day_of_week()
        self.assertIn(result, self.generic.datetime.data['day']['name'])

        result_abbr = self.generic.datetime.day_of_week(abbr=True)
        self.assertIn(result_abbr, self.generic.datetime.data['day']['abbr'])

    def test_month(self):
        result = self.generic.datetime.month()
        self.assertIsNotNone(result)

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

        fmt_year = self.generic.datetime.birthday(minimum=2015, maximum=2025, readable=False, fmt='%Y')
        self.assertGreaterEqual(int(fmt_year), 2015)
        self.assertLessEqual(int(fmt_year), 2025)

    def test_date(self):
        # Default values: date(sep='-', start=2000, end=2035, with_time=False)
        result = self.generic.datetime.date()
        d, m, y = result.split('-')
        self.assertTrue(int(d) <= 31)
        self.assertTrue(int(m) <= 12)
        self.assertTrue(int(y) >= 2000)
        self.assertTrue(int(y) <= 2035)

        result = self.generic.datetime.date(with_time=True)
        hour, minutes = result.split(' ')[1].split(':')
        self.assertTrue(int(hour) <= 24)
        self.assertTrue(int(minutes) <= 60)


    def test_time(self):
        result = self.generic.datetime.time()
        hour, minutes = result.split(':')
        self.assertTrue(int(hour) <= 24)
        self.assertTrue(int(minutes) <= 60)
