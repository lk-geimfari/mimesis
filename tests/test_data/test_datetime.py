# -*- coding: utf-8 -*-
import datetime
import re

import pytest

import mimesis
from mimesis.data import GMT_OFFSETS, TIMEZONES

from ._patterns import STR_REGEX


@pytest.fixture
def _datetime():
    return mimesis.Datetime()


def test_str(dt):
    assert re.match(STR_REGEX, str(dt))


def test_year(_datetime):
    result = _datetime.year(minimum=2000, maximum=2016)
    assert result >= 2000
    assert result <= 2016


def test_gmt_offset(_datetime):
    result = _datetime.gmt_offset()
    assert result in GMT_OFFSETS


def test_day_of_month(_datetime):
    result = _datetime.day_of_month()
    assert ((result >= 1) or (result <= 31))


def test_date(dt):
    result = dt.date(start=1999, end=1999, fmt='%m/%d/%Y')

    result = datetime.datetime.strptime(result, '%m/%d/%Y')
    assert result.year == 1999  # check range was applied correctly

    date = dt.date(start=2018, end=2018)
    result_fmt = datetime.datetime.strptime(date, dt._data['formats']['date'])
    assert result_fmt.year == 2018


def test_time(dt):
    default = dt.time()
    default = datetime.datetime.strptime(default, dt._data['formats']['time'])

    assert isinstance(default, datetime.datetime)

    result = dt.time(fmt='%H:%M')
    result = datetime.datetime.strptime(result, '%H:%M')
    assert isinstance(result, datetime.datetime)


def test_century(_datetime):
    result = _datetime.century()
    assert result is not None
    assert isinstance(result, str)


def test_day_of_week(dt):
    result = dt.day_of_week()
    assert result in dt._data['day']['name']

    result_abbr = dt.day_of_week(abbr=True)
    assert result_abbr in dt._data['day']['abbr']


def test_month(dt):
    result = dt.month()
    assert result is not None

    result_abbr = dt.month(abbr=True)
    assert isinstance(result_abbr, str)


def test_periodicity(dt):
    result = dt.periodicity()
    assert result in dt._data['periodicity']


def test_timezone(_datetime):
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
def test_timestamp(_datetime, posix, _type):
    result = _datetime.timestamp(posix)
    assert result is not None
    assert isinstance(result, _type)


@pytest.mark.parametrize(
    'start, end, humanized, _type', [
        (2018, 2018, False, datetime.datetime),
        (2018, 2018, True, str),
    ],
)
def test_datetime(_datetime, start, end, humanized, _type):
    dt = _datetime.datetime(start=start, end=end, humanized=humanized)

    assert dt is not None
    assert isinstance(dt, _type)

    if _type is str:
        year = int(dt.split(' ')[2])
        assert year == 2018


def test_week_date(_datetime):
    result = _datetime.week_date(start=2017, end=2018)
    result = result.replace('-', ' ').replace('W', '')
    year, week = result.split(' ')

    assert (int(year) >= 2017) and (int(year) <= 2018)
    assert int(week) <= 52
