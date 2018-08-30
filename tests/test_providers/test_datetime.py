# -*- coding: utf-8 -*-
import datetime
import re

import pytest

from mimesis import Datetime
from mimesis.data import GMT_OFFSETS, TIMEZONES

from . import patterns


class TestDatetime(object):

    @pytest.fixture
    def _datetime(self):
        return Datetime()

    def test_str(self, dt):
        assert re.match(patterns.STR_REGEX, str(dt))

    def test_year(self, _datetime):
        result = _datetime.year(minimum=2000, maximum=2016)
        assert result >= 2000
        assert result <= 2016

    def test_gmt_offset(self, _datetime):
        result = _datetime.gmt_offset()
        assert result in GMT_OFFSETS

    def test_day_of_month(self, _datetime):
        result = _datetime.day_of_month()
        assert ((result >= 1) or (result <= 31))

    def test_date(self, dt):
        result = dt.date(start=1999, end=1999, fmt='%m/%d/%Y')

        result = datetime.datetime.strptime(result, '%m/%d/%Y')
        assert result.year == 1999  # check range was applied correctly

        date = dt.date(start=2018, end=2018)
        result_fmt = datetime.datetime.strptime(
            date, dt._data['formats']['date'],
        )
        assert result_fmt.year == 2018

    def test_time(self, dt):
        default = dt.time()
        default = datetime.datetime.strptime(
            default, dt._data['formats']['time'],
        )

        assert isinstance(default, datetime.datetime)

        result = dt.time(fmt='%H:%M')
        result = datetime.datetime.strptime(result, '%H:%M')
        assert isinstance(result, datetime.datetime)

    def test_century(self, _datetime):
        result = _datetime.century()
        assert result is not None
        assert isinstance(result, str)

    def test_day_of_week(self, dt):
        result = dt.day_of_week()
        assert result in dt._data['day']['name']

        result_abbr = dt.day_of_week(abbr=True)
        assert result_abbr in dt._data['day']['abbr']

    def test_month(self, dt):
        result = dt.month()
        assert result is not None

        result_abbr = dt.month(abbr=True)
        assert isinstance(result_abbr, str)

    def test_periodicity(self, dt):
        result = dt.periodicity()
        assert result in dt._data['periodicity']

    def test_timezone(self, _datetime):
        result = _datetime.timezone()

        assert result is not None
        assert isinstance(result, str)
        assert result in TIMEZONES

    @pytest.mark.parametrize(
        'posix, _type', [
            (False, str),
            (True, int),
        ],
    )
    def test_timestamp(self, _datetime, posix, _type):
        result = _datetime.timestamp(posix)
        assert result is not None
        assert isinstance(result, _type)

    @pytest.mark.parametrize(
        'start, end, humanized, timezone, _type', [
            (2018, 2018, False, 'Europe/Paris', datetime.datetime),
            (2018, 2018, True, '', str),
            (2018, 2018, False, '', datetime.datetime),
        ],
    )
    def test_datetime(self, _datetime, start, end, humanized, timezone, _type):
        dt = _datetime.datetime(start=start, end=end, humanized=humanized, timezone=timezone)
        
        assert dt is not None
        assert isinstance(dt, _type)

        if _type is str:
            year = int(dt.split(' ')[2])
            assert year == 2018

        if humanized:
            pass
        elif timezone is not '':
            assert dt.tzinfo is not None
        else:
            assert dt.tzinfo is None

    def test_week_date(self, _datetime):
        result = _datetime.week_date(start=2017, end=2018)
        result = result.replace('-', ' ').replace('W', '')
        year, week = result.split(' ')

        assert (int(year) >= 2017) and (int(year) <= 2018)
        assert int(week) <= 52


class TestSeededDatetime(object):

    @pytest.fixture
    def d1(self, seed):
        return Datetime(seed=seed)

    @pytest.fixture
    def d2(self, seed):
        return Datetime(seed=seed)

    def test_year(self, d1, d2):
        assert d1.year() == d2.year()
        assert d1.year(1942, 2048) == d2.year(1942, 2048)

    def test_gmt_offset(self, d1, d2):
        assert d1.gmt_offset() == d2.gmt_offset()

    def test_day_of_month(self, d1, d2):
        assert d1.day_of_month() == d2.day_of_month()

    def test_date(self, d1, d2):
        assert d1.date() == d2.date()
        assert d1.date(start=1024, end=2048, fmt='%m/%d/%Y') == \
            d2.date(start=1024, end=2048, fmt='%m/%d/%Y')

    def test_time(self, d1, d2):
        assert d1.time() == d2.time()
        assert d1.time(fmt='%H:%M') == d2.time(fmt='%H:%M')

    def test_century(self, d1, d2):
        assert d1.century() == d2.century()

    def test_day_of_week(self, d1, d2):
        assert d1.day_of_week() == d2.day_of_week()
        assert d1.day_of_week(abbr=True) == d2.day_of_week(abbr=True)

    def test_month(self, d1, d2):
        assert d1.month() == d2.month()
        assert d1.month(abbr=True) == d2.month(abbr=True)

    def test_periodicity(self, d1, d2):
        assert d1.periodicity() == d2.periodicity()

    def test_timezone(self, d1, d2):
        assert d1.timezone() == d2.timezone()

    def test_timestamp(self, d1, d2):
        assert d1.timestamp() == d2.timestamp()
        assert d1.timestamp(posix=False) == d2.timestamp(posix=False)

    def test_datetime(self, d1, d2):
        assert d1.datetime() == d2.datetime()
        assert d1.datetime(humanized=True) == d2.datetime(humanized=True)

    def test_week_date(self, d1, d2):
        assert d1.week_date() == d2.week_date()
        assert d1.week_date(start=2007, end=2018) == \
            d2.week_date(start=2007, end=2018)
