# -*- coding: utf-8 -*-
import datetime
import re

import pytest

from mimesis import FutureDatetime
from mimesis.data import GMT_OFFSETS, TIMEZONES

from . import patterns


class TestFutureDatetime(object):

    @pytest.fixture
    def future_dt(self):
        return FutureDatetime()

    def test_str(self, dt):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(dt))

    def test_week_date(self, future_dt):
        result = future_dt.week_date()
        result = result.replace('-', ' ').replace('W', '')
        year, week = result.split(' ')
        assert int(year) >= future_dt.future.year
        assert int(year) <= future_dt.future.year + 1
        assert int(week) <= 52

        with pytest.raises(ValueError):
            future_dt.week_date(end=datetime.MINYEAR)

    def test_year(self, future_dt):
        result = future_dt.year()
        assert result >= future_dt.future.year
        assert result <= future_dt.future.year + 65

        with pytest.raises(ValueError):
            future_dt.year(maximum=datetime.MINYEAR)

    def test_date(self, future_dt):
        date_object = future_dt.date()
        assert isinstance(date_object, datetime.date)
        assert date_object.year >= future_dt.future.year
        assert date_object.year <= future_dt.future.year + 19

        with pytest.raises(ValueError):
            future_dt.date(end=datetime.MINYEAR)

    def test_formatted_date(self, future_dt):
        fmt_date = future_dt.formatted_date('%Y', end=datetime.MAXYEAR)
        assert int(fmt_date) >= future_dt.future.year
        assert isinstance(fmt_date, str)

    @pytest.mark.parametrize(
        'end, timezone', [
            (datetime.MAXYEAR, 'Europe/Paris'),
            (datetime.MAXYEAR, None),
        ],
    )
    def test_datetime(self, future_dt, end, timezone):
        dt_obj = future_dt.datetime(end=end, timezone=timezone)

        assert future_dt.future.year <= dt_obj.year <= datetime.MAXYEAR
        assert isinstance(dt_obj, datetime.datetime)

        with pytest.raises(ValueError):
            future_dt.datetime(end=datetime.MINYEAR)

    def test_formatted_datetime(self, future_dt):
        dt_obj = future_dt.formatted_datetime('%Y', end=datetime.MAXYEAR)
        assert int(dt_obj) >= future_dt.future.year
        assert isinstance(dt_obj, str)

    def test_timestamp(self, future_dt):
        result = future_dt.timestamp(end=datetime.MAXYEAR)
        assert result is not None
        assert isinstance(result, int)
        year = datetime.datetime.fromtimestamp(int(result)).year
        assert year >= future_dt.future.year

        result = future_dt.timestamp(posix=False, end=datetime.MAXYEAR)
        assert isinstance(result, str)


class TestSeededFutureDatetime(object):

    @pytest.fixture
    def d1(self, seed):
        return FutureDatetime(seed=seed)

    @pytest.fixture
    def d2(self, seed):
        return FutureDatetime(seed=seed)

    def test_week_date(self, d1, d2):
        assert d1.week_date() == d2.week_date()
        assert d1.week_date(end=datetime.MAXYEAR) == \
               d2.week_date(end=datetime.MAXYEAR)

    def test_year(self, d1, d2):
        assert d1.year() == d2.year()
        assert d1.year(maximum=datetime.MAXYEAR) == \
               d2.year(maximum=datetime.MAXYEAR)

    def test_date(self, d1, d2):
        assert d1.date() == d2.date()
        assert d1.date(end=datetime.MAXYEAR) == d2.date(end=datetime.MAXYEAR)

    def test_formatted_date(self, d1, d2):
        assert d1.formatted_date() == d2.formatted_date()

    def test_datetime(self, d1, d2):
        assert d1.datetime() == d2.datetime()
        assert d1.datetime(end=datetime.MAXYEAR) == \
               d2.datetime(end=datetime.MAXYEAR)

    def test_formatted_datetime(self, d1, d2):
        assert d1.formatted_datetime() == d2.formatted_datetime()

    def test_timestamp(self, d1, d2):
        assert d1.timestamp() == d2.timestamp()
        assert d1.timestamp(posix=False) == d2.timestamp(posix=False)
