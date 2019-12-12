# -*- coding: utf-8 -*-
import datetime
import re

import pytest

from mimesis import FutureDatetime
from mimesis.data import GMT_OFFSETS, TIMEZONES

from . import patterns


class TestFutureDatetime(object):

    @pytest.fixture
    def _future_datetime(self):
        return FutureDatetime()

    def test_str(self, dt):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(dt))

    def test_week_date(self, _future_datetime):
        result = _future_datetime.week_date()
        result = result.replace('-', ' ').replace('W', '')
        year, week = result.split(' ')
        assert int(year) >= _future_datetime.future.year
        assert int(year) <= _future_datetime.future.year + 1
        assert int(week) <= 52

        with pytest.raises(ValueError):
            _future_datetime.week_date(end=datetime.MINYEAR)

    def test_year(self, _future_datetime):
        result = _future_datetime.year()
        assert result >= _future_datetime.future.year
        assert result <= _future_datetime.future.year + 65

        with pytest.raises(ValueError):
            _future_datetime.year(maximum=datetime.MINYEAR)

    def test_date(self, _future_datetime):
        date_object = _future_datetime.date()
        assert isinstance(date_object, datetime.date)
        assert date_object.year >= _future_datetime.future.year
        assert date_object.year <= _future_datetime.future.year + 19

        with pytest.raises(ValueError):
            _future_datetime.date(end=datetime.MINYEAR)

    @pytest.mark.parametrize(
        'end, timezone', [
            (datetime.MAXYEAR, 'Europe/Paris'),
            (datetime.MAXYEAR, None),
        ],
    )
    def test_datetime(self, _future_datetime, end, timezone):
        dt_obj = _future_datetime.datetime(end=end, timezone=timezone)

        assert _future_datetime.future.year <= dt_obj.year
        assert dt_obj.year <= datetime.MAXYEAR
        assert isinstance(dt_obj, datetime.datetime)

        with pytest.raises(ValueError):
            _future_datetime.datetime(end=datetime.MINYEAR)


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

    def test_datetime(self, d1, d2):
        assert d1.datetime() == d2.datetime()
        assert d1.datetime(end=datetime.MAXYEAR) == \
               d2.datetime(end=datetime.MAXYEAR)
