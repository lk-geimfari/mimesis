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
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(dt))

    @pytest.mark.parametrize(
        'days, objects_count', [
            (7, 169),
            (14, 337),
            (28, 673),
        ],
    )
    def test_bulk_create_datetimes(self, _datetime, days, objects_count):
        date_start = datetime.datetime.now()
        date_end = date_start + datetime.timedelta(days=days)
        datetime_objects = _datetime.bulk_create_datetimes(
            date_start=date_start,
            date_end=date_end,
            minutes=60,
        )
        assert len(datetime_objects) == objects_count

    def test_bulk_create_datetimes_error(self, _datetime):
        date_start = datetime.datetime.now()
        date_end = date_start - datetime.timedelta(days=7)

        with pytest.raises(ValueError):
            _datetime.bulk_create_datetimes(date_start, date_end)

        with pytest.raises(ValueError):
            _datetime.bulk_create_datetimes(None, None)

    def test_year(self, _datetime):
        result = _datetime.year(minimum=2000, maximum=_datetime.CURRENT_YEAR)
        assert result >= 2000
        assert result <= _datetime.CURRENT_YEAR

    def test_gmt_offset(self, _datetime):
        result = _datetime.gmt_offset()
        assert result in GMT_OFFSETS

    def test_day_of_month(self, _datetime):
        result = _datetime.day_of_month()
        assert ((result >= 1) or (result <= 31))

    def test_date(self, dt):
        date_object = dt.date(start=dt.CURRENT_YEAR, end=dt.CURRENT_YEAR)
        assert isinstance(date_object, datetime.date)
        assert date_object.year == dt.CURRENT_YEAR

    def test_formatted_date(self, dt):
        fmt_date = dt.formatted_date('%Y', start=2000, end=2000)
        assert int(fmt_date) == 2000
        assert isinstance(fmt_date, str)

    def test_time(self, dt):
        default = dt.time()
        assert isinstance(default, datetime.time)

    def test_formatted_time(self, dt):
        default = dt.formatted_time()
        assert isinstance(default, str)

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
        'start, end, timezone', [
            (2014, 2019, 'Europe/Paris'),
            (2014, 2019, None),
        ],
    )
    def test_datetime(self, _datetime, start, end, timezone):
        dt_obj = _datetime.datetime(start=start, end=end, timezone=timezone)

        assert start <= dt_obj.year <= end
        assert isinstance(dt_obj, datetime.datetime)

        if timezone:
            assert dt_obj.tzinfo is not None
        else:
            assert dt_obj.tzinfo is None

    @pytest.mark.parametrize(
        'start, end', [
            (2018, 2018),
            (2019, 2019),
        ],
    )
    def test_formatted_datetime(self, _datetime, start, end):
        dt_str = _datetime.formatted_date(fmt='%Y', start=start, end=end)
        assert isinstance(dt_str, str)
        assert start <= int(dt_str) <= end

    def test_week_date(self, _datetime):
        result = _datetime.week_date(start=2017, end=_datetime.CURRENT_YEAR)
        result = result.replace('-', ' ').replace('W', '')
        year, week = result.split(' ')

        assert (int(year) >= 2017) and (int(year) <= _datetime.CURRENT_YEAR)
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
        assert d1.date(start=1024, end=2048) == \
               d2.date(start=1024, end=2048)

    def test_formatted_date(self, d1, d2):
        assert d1.formatted_date() == d2.formatted_date()
        assert d1.formatted_date(start=1024, end=2048) == \
               d2.formatted_date(start=1024, end=2048)

    def test_time(self, d1, d2):
        assert d1.time() == d2.time()

    def test_formatted_time(self, d1, d2):
        assert d1.formatted_time() == d2.formatted_time()

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

    def test_formatted_datetime(self, d1, d2):
        assert d1.formatted_date() == d2.formatted_date()

    def test_week_date(self, d1, d2):
        assert d1.week_date() == d2.week_date()
        assert d1.week_date(start=2007, end=2018) == \
               d2.week_date(start=2007, end=2018)

    def test_bulk_create_datetimes(self, d1, d2):
        date_start = datetime.datetime.now()
        date_end = date_start + datetime.timedelta(days=7)
        assert d1.bulk_create_datetimes(date_start, date_end, minutes=10) == \
               d2.bulk_create_datetimes(date_start, date_end, minutes=10)
