# -*- coding: utf-8 -*-
import datetime
import re

import pytest

from mimesis import PastDatetime
from mimesis.data import GMT_OFFSETS, TIMEZONES

from . import patterns


class TestPastDatetime(object):

    @pytest.fixture
    def past_dt(self):
        return PastDatetime()

    def test_str(self, dt):
        assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(dt))

    def test_date(self, past_dt):
        date_object = past_dt.date()
        assert isinstance(date_object, datetime.date)
        assert date_object.year >= past_dt.past.year - 19
        assert date_object.year <= past_dt.past.year

        with pytest.raises(ValueError):
            past_dt.date(start=datetime.MAXYEAR)

    def test_formatted_date(self, past_dt):
        fmt_date = past_dt.formatted_date('%Y', start=datetime.MINYEAR)
        assert int(fmt_date) >= past_dt.past.year
        assert isinstance(fmt_date, str)

    @pytest.mark.parametrize(
        'start, timezone', [
            (datetime.MINYEAR, 'Europe/Paris'),
            (datetime.MINYEAR, None),
        ],
    )
    def test_datetime(self, past_dt, start, timezone):
        dt_obj = past_dt.datetime(start=start, timezone=timezone)

        assert datetime.MINYEAR <= dt_obj.year <= past_dt.past.year
        assert isinstance(dt_obj, datetime.datetime)

        with pytest.raises(ValueError):
            past_dt.datetime(start=datetime.MAXYEAR)

    def test_formatted_datetime(self, past_dt):
        dt_obj = past_dt.formatted_datetime('%Y', start=datetime.MINYEAR)
        assert int(dt_obj) <= past_dt.past.year
        assert isinstance(dt_obj, str)

    def test_timestamp(self, past_dt):
        result = past_dt.timestamp(start=datetime.MINYEAR)
        assert result is not None
        assert isinstance(result, int)
        year = datetime.datetime.fromtimestamp(int(result)).year
        assert year <= past_dt.past.year

        result = past_dt.timestamp(posix=False, start=datetime.MINYEAR)
        assert isinstance(result, str)


class TestSeededPastDatetime(object):

    @pytest.fixture
    def d1(self, seed):
        return PastDatetime(seed=seed)

    @pytest.fixture
    def d2(self, seed):
        return PastDatetime(seed=seed)

    def test_date(self, d1, d2):
        assert d1.date() == d2.date()
        assert d1.date(start=datetime.MINYEAR) == \
               d2.date(start=datetime.MINYEAR)

    def test_formatted_date(self, d1, d2):
        assert d1.formatted_date() == d2.formatted_date()

    def test_datetime(self, d1, d2):
        assert d1.datetime() == d2.datetime()
        assert d1.datetime(start=datetime.MINYEAR) == \
               d2.datetime(start=datetime.MINYEAR)

    def test_formatted_datetime(self, d1, d2):
        assert d1.formatted_datetime() == d2.formatted_datetime()

    def test_timestamp(self, d1, d2):
        assert d1.timestamp() == d2.timestamp()
        assert d1.timestamp(posix=False) == d2.timestamp(posix=False)
