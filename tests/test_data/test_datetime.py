# -*- coding: utf-8 -*-
import datetime
import re

from tests.test_data import dt, generic
from ._patterns import STR_REGEX


def test_str(dt):
    assert re.match(STR_REGEX, str(dt))


def test_year(dt):
    result = dt.year(minimum=2000, maximum=2016)
    assert result >= 2000
    assert result <= 2016


def test_day_of_month(dt):
    result = dt.day_of_month()
    assert ((result >= 1) or (result <= 31))


def test_date(dt):
    result = dt.date(start=1999, end=1999, fmt="%m/%d/%Y")

    result = datetime.datetime.strptime(result, "%m/%d/%Y")
    assert result.year == 1999  # check range was applied correctly


def test_time(dt):
    result = dt.time(fmt="%H:%M")

    result = datetime.datetime.strptime(result, "%H:%M")
    assert isinstance(result, datetime.datetime)


def test_century(dt):
    result = dt.century()
    assert result is not None
    assert isinstance(result, str)


def test_day_of_week(generic):
    result = generic.datetime.day_of_week()
    assert result in generic.datetime.data['day']['name']

    result_abbr = generic.datetime.day_of_week(abbr=True)
    assert result_abbr in generic.datetime.data['day']['abbr']


def test_month(generic):
    result = generic.datetime.month()
    assert result is not None

    result_abbr = generic.datetime.month(abbr=True)
    assert isinstance(result_abbr, str)


def test_periodicity(generic):
    result = generic.datetime.periodicity()
    assert result in generic.datetime.data['periodicity']
