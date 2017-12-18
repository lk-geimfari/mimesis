# -*- coding: utf-8 -*-
import datetime
import re

import pytest

from mimesis import Datetime
from mimesis.data import GMT_OFFSETS, TIMEZONES

from ._patterns import STR_REGEX


@pytest.fixture
def _datetime():
    return Datetime()


@pytest.fixture
def _seeded_datetime():
    return Datetime(seed=42)


def test_str(dt):
    assert re.match(STR_REGEX, str(dt))


def test_year(_datetime):
    result = _datetime.year(minimum=2000, maximum=2016)
    assert result >= 2000
    assert result <= 2016


def test_seeded_year(_seeded_datetime):
    result = _seeded_datetime.year(minimum=42, maximum=1942)
    assert result == 1351
    result = _seeded_datetime.year()
    assert result == 1997
    result = _seeded_datetime.year()
    assert result == 1991


def test_gmt_offset(_datetime):
    result = _datetime.gmt_offset()
    assert result in GMT_OFFSETS


def test_seeded_gmt_offset(_seeded_datetime):
    result = _seeded_datetime.gmt_offset()
    assert result == 'UTC +07:00'
    result = _seeded_datetime.gmt_offset()
    assert result == 'UTC +04:30'


def test_day_of_month(_datetime):
    result = _datetime.day_of_month()
    assert ((result >= 1) or (result <= 31))


def test_seeded_day_of_month(_seeded_datetime):
    result = _seeded_datetime.day_of_month()
    assert result == 21
    result = _seeded_datetime.day_of_month()
    assert result == 4


def test_date(dt):
    result = dt.date(start=1999, end=1999, fmt='%m/%d/%Y')

    result = datetime.datetime.strptime(result, '%m/%d/%Y')
    assert result.year == 1999  # check range was applied correctly

    date = dt.date(start=2018, end=2018)
    result_fmt = datetime.datetime.strptime(date, dt._data['formats']['date'])
    assert result_fmt.year == 2018


def test_seeded_date(_seeded_datetime):
    result = _seeded_datetime.date(start=1942, end=2042, fmt='%m/%d/%Y')
    assert result == '02/01/2023'
    result = _seeded_datetime.date()
    assert result == '04/08/2017'
    result = _seeded_datetime.date()
    assert result == '12/04/2008'


def test_time(dt):
    default = dt.time()
    default = datetime.datetime.strptime(default, dt._data['formats']['time'])

    assert isinstance(default, datetime.datetime)

    result = dt.time(fmt='%H:%M')
    result = datetime.datetime.strptime(result, '%H:%M')
    assert isinstance(result, datetime.datetime)


def test_seeded_time(_seeded_datetime):
    result = _seeded_datetime.time(fmt='%H:%M')
    assert result == '20:07'
    result = _seeded_datetime.time()
    assert result == '08:15:14'
    result = _seeded_datetime.time()
    assert result == '23:06:43'


def test_century(_datetime):
    result = _datetime.century()
    assert result is not None
    assert isinstance(result, str)


def test_seeded_century(_seeded_datetime):
    result = _seeded_datetime.century()
    assert result == 'XXI'
    result = _seeded_datetime.century()
    assert result == 'IV'


def test_day_of_week(dt):
    result = dt.day_of_week()
    assert result in dt._data['day']['name']

    result_abbr = dt.day_of_week(abbr=True)
    assert result_abbr in dt._data['day']['abbr']


def test_seeded_day_of_week(_seeded_datetime):
    result = _seeded_datetime.day_of_week(abbr=True)
    assert result == 'Sat'
    result = _seeded_datetime.day_of_week()
    assert result == 'Monday'
    result = _seeded_datetime.day_of_week()
    assert result == 'Monday'
    result = _seeded_datetime.day_of_week()
    assert result == 'Saturday'


def test_month(dt):
    result = dt.month()
    assert result is not None

    result_abbr = dt.month(abbr=True)
    assert isinstance(result_abbr, str)


def test_seeded_month(_seeded_datetime):
    result = _seeded_datetime.month(abbr=True)
    assert result == 'Nov.'
    result = _seeded_datetime.month()
    assert result == 'February'
    result = _seeded_datetime.month()
    assert result == 'January'


def test_periodicity(dt):
    result = dt.periodicity()
    assert result in dt._data['periodicity']


def test_seeded_periodicity(_seeded_datetime):
    result = _seeded_datetime.periodicity()
    assert result == 'Never'
    result = _seeded_datetime.periodicity()
    assert result == 'Once'


def test_timezone(_datetime):
    result = _datetime.timezone()

    assert result is not None
    assert isinstance(result, str)
    assert result in TIMEZONES


def test_seeded_timezone(_seeded_datetime):
    result = _seeded_datetime.timezone()
    assert result == 'Europe/Copenhagen'
    result = _seeded_datetime.timezone()
    assert result == 'America/Argentina/Buenos_Aires'


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


def test_seeded_timestamp(_seeded_datetime):
    result = _seeded_datetime.timestamp(posix=True)
    assert result == 1169626514
    result = _seeded_datetime.timestamp()
    assert result == 1164387937
    result = _seeded_datetime.timestamp()
    assert result == 1010038472


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


def test_seeded_datetime(_seeded_datetime):
    result = _seeded_datetime.datetime(humanized=True)
    assert result == 'January, 24 2007'
    result = _seeded_datetime.datetime()
    assert result == datetime.datetime.strptime(
        '2006-11-24 17:05:37', '%Y-%m-%d %H:%M:%S',
    )
    result = _seeded_datetime.datetime()
    assert result == datetime.datetime.strptime(
        '2002-01-03 06:14:32', '%Y-%m-%d %H:%M:%S',
    )


def test_week_date(_datetime):
    result = _datetime.week_date(start=2017, end=2018)
    result = result.replace('-', ' ').replace('W', '')
    year, week = result.split(' ')

    assert (int(year) >= 2017) and (int(year) <= 2018)
    assert int(week) <= 52


def test_seeded_week_date(_seeded_datetime):
    result = _seeded_datetime.week_date(start=42, end=2042)
    assert result == '1351-W8'
    result = _seeded_datetime.week_date()
    assert result == '2017-W48'
    result = _seeded_datetime.week_date()
    assert result == '2018-W16'
