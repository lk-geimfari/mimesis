# -*- coding: utf-8 -*-
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
            _future_datetime.week_date(end=1950)


class TestSeededFutureDatetime(object):

    @pytest.fixture
    def d1(self, seed):
        return FutureDatetime(seed=seed)

    @pytest.fixture
    def d2(self, seed):
        return FutureDatetime(seed=seed)

    def test_week_date(self, d1, d2):
        assert d1.week_date() == d2.week_date()
        assert d1.week_date() == d2.week_date()
