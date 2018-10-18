"""Provider of data related to date and time."""

from calendar import monthrange, timegm
from datetime import date, datetime, time, timedelta
from typing import List, Optional, Union

from mimesis.compat import pytz
from mimesis.data import GMT_OFFSETS, ROMAN_NUMS, TIMEZONES
from mimesis.providers.base import BaseDataProvider
from mimesis.typing import DateTime, Timestamp
from mimesis.utils import pull

__all__ = ['Datetime']


class Datetime(BaseDataProvider):
    """Class for generating data related to the date and time."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._data = pull('datetime.json', self.locale)

    @staticmethod
    def bulk_create_datetimes(date_start: DateTime,
                              date_end: DateTime, **kwargs) -> List[DateTime]:
        """Bulk create datetime objects.

        This method creates list of datetime objects from
        ``date_start`` to ``date_end``.

        You can use the following keyword arguments:

        * ``days``
        * ``hours``
        * ``minutes``
        * ``seconds``
        * ``microseconds``

        See datetime module documentation for more:
        https://docs.python.org/3.7/library/datetime.html#timedelta-objects


        :param date_start: Begin of the range.
        :param date_end: End of the range.
        :param kwargs: Keyword arguments for datetime.timedelta
        :return: List of datetime objects
        :raises: ValueError: When ``date_start``/``date_end`` not passed and
            when ``date_start`` larger than ``date_end``.

        :Example:

        >>> dt = Datetime()
        >>> now = datetime.now()
        >>> week_ago = datetime.now() - timedelta(days=9)
        >>> datetimes = dt.bulk_create_datetimes(week_ago, now, days=1)
        >>> isinstance(datetimes, list)
        True
        """
        dt_objects = []

        if not date_start and not date_end:
            raise ValueError('You must pass date_start and date_end')

        if date_end < date_start:
            raise ValueError('date_start can not be larger than date_end')

        while date_start <= date_end:
            date_start += timedelta(**kwargs)
            dt_objects.append(date_start)

        return dt_objects

    def week_date(self, start: int = 2017, end: int = 2018) -> str:
        """Get week number with year.

        :param start: From start.
        :param end: To end.
        :return: Week number.

        :Example:

        >>> dt = Datetime()
        >>> week_date = dt.week_date(2018, 2018)
        >>> '2018' in week_date
        True
        """
        year = self.year(start, end)
        week = self.random.randint(1, 52)
        return '{year}-W{week}'.format(
            year=year,
            week=week,
        )

    def day_of_week(self, abbr: bool = False) -> str:
        """Get a random day of week.

        :param abbr: Abbreviated day name.
        :return: Day of the week.

        :Example:

        >>> dt = Datetime()
        >>> day_of_week = dt.day_of_week()
        >>> day_of_week in dt._data['day']['name']
        True
         >>> day_of_week = dt.day_of_week(abbr=True)
        >>> day_of_week in dt._data['day']['abbr']
        True
        """
        key = 'abbr' if abbr else 'name'
        days = self._data['day'].get(key)
        return self.random.choice(days)

    def month(self, abbr: bool = False) -> str:
        """Get a random month.

        :param abbr: Abbreviated month name.
        :return: Month name.

        :Example:
            January
        """
        key = 'abbr' if abbr else 'name'
        months = self._data['month'].get(key)
        return self.random.choice(months)

    def year(self, minimum: int = 1990, maximum: int = 2050) -> int:
        """Generate a random year.

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Year.

        :Example:

        >>> dt = Datetime()
        >>> year = dt.year(2015, 2019)
        >>> 2015 <= year <= 2019
        True
        """
        return self.random.randint(minimum, maximum)

    def century(self) -> str:
        """Get a random century.

        :return: Century.

        :Example:

        >>> dt = Datetime()
        >>> century = dt.century()
        >>> century in ROMAN_NUMS
        True
        """
        return self.random.choice(ROMAN_NUMS)

    def periodicity(self) -> str:
        """Get a random periodicity string.

        :return: Periodicity.

        :Example:

        >>> dt = Datetime()
        >>> periodicity = dt.periodicity()
        >>> periodicity in dt._data['periodicity']
        True
        """
        periodicity = self._data['periodicity']
        return self.random.choice(periodicity)

    def date(self, start: int = 2000,
             end: int = 2035, fmt: str = '', as_string: bool = False) -> Union[date, str]:
        """Generate a string representing of random date.

        Date can be automatically formatted for the current
        locale or specified.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :param fmt: Format string for date.
        :param as_string: Boolean if return as string.
        :return: Formatted date.

        :Example:

        >>> dt = Datetime()
        >>> date = dt.date()
        >>> isinstance(date, datetime.date)
        True

        >>> dt = Datetime()
        >>> date = dt.date(as_string=True)
        >>> isinstance(date, str)
        True

        """
        if not fmt:
            fmt = self._data['formats'].get('date')

        year = self.random.randint(start, end)
        month = self.random.randint(1, 12)
        d = date(year, month, self.random.randint(
            1, monthrange(year, month)[1]))
        if as_string:
            return d.strftime(fmt)
        return d

    def time(self, fmt: str = '', as_string: bool = False) -> Union[time, str]:
        """Generate a random time.

        Time can be automatically formatted for the current
        locale or specified.

        :param fmt: Format of time.
        :param as_string: Boolean if return as string.
        :return: Time.

        :Example:

        >>> dt = Datetime()
        >>> _time = dt.time()
        >>> isinstance(_time, datetime.time)
        True

        >>> dt = Datetime()
        >>> _time = dt.time(as_string=True)
        >>> isinstance(_time, str)
        True

        """
        if not fmt:
            fmt = self._data['formats'].get('time')

        t = time(
            self.random.randint(0, 23),
            self.random.randint(0, 59),
            self.random.randint(0, 59),
            self.random.randint(0, 999999),
        )
        if as_string:
            return t.strftime(fmt)
        return t

    def day_of_month(self) -> int:
        """Generate a random day of month, from 1 to 31.

        :return: Random value from 1 to 31.

        :Example:

        >>> dt = Datetime()
        >>> day = dt.day_of_month()
        >>> 1 <= day <= 31
        True
        """
        return self.random.randint(1, 31)

    def timezone(self) -> str:
        """Get a random timezone.

        :return: Timezone.

        :Example:

        >>> dt = Datetime()
        >>> timezone = dt.timezone()
        >>> timezone in TIMEZONES
        True
        """
        return self.random.choice(TIMEZONES)

    def gmt_offset(self) -> str:
        """Get a random GMT offset value.

        :return: GMT Offset.

        :Example:

        >>> dt = Datetime()
        >>> gmt_offset = dt.gmt_offset()
        >>> gmt_offset in GMT_OFFSETS
        True
        """
        return self.random.choice(GMT_OFFSETS)

    def datetime(self, humanized: bool = False,
                 timezone: Optional[str] = None, **kwargs) -> DateTime:
        """Generate random datetime.

        :param timezone: Set custom timezone (pytz required)
        :param humanized: Readable representation.
        :param kwargs: Keyword arguments (start, end).
        :return: Datetime.
        :rtype: datetime.datetime

        :Example:

        >>> dt = Datetime()
        >>> datetime_obj = dt.datetime()
        >>> isinstance(datetime_obj, datetime)
        True
        """
        fmt = '%Y-%m-%d %H:%M:%S'
        dt_str = '{date} {time}'.format(
            date=self.date(fmt='%Y-%m-%d', **kwargs),
            time=self.time(),
        )

        dt = datetime.strptime(dt_str, fmt)

        if timezone:
            if not pytz:
                raise ImportError('Timezones are supported only with pytz')
            tz = pytz.timezone(timezone)
            dt = tz.localize(dt)

        if humanized:
            return dt.strftime('%B, %d %Y')

        return dt

    def timestamp(self, posix: bool = True, **kwargs) -> Timestamp:
        """Generate random timestamp.

        :param posix: POSIX time.
        :param kwargs: Keyword arguments (start, end).
        :return: Timestamp.
        :rtype: str or int

        :Example:

        >>> dt = Datetime()
        >>> timestamp = dt.timestamp(posix=True)
        >>> isinstance(timestamp, int)
        True
        >>> timestamp = dt.timestamp(posix=False)
        >>> isinstance(timestamp, str)
        True
        """
        stamp = self.datetime(**kwargs)

        if posix:
            return timegm(stamp.utctimetuple())

        return stamp.strftime('%Y-%m-%dT%H:%M:%SZ')
