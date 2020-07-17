# -*- coding: utf-8 -*-

"""Provider of data related to date and time."""

from calendar import monthrange, timegm
from datetime import date, datetime, time, timedelta
from typing import List, Optional, Union

from mimesis.compat import pytz
from mimesis.data import GMT_OFFSETS, ROMAN_NUMS, TIMEZONES
from mimesis.providers.base import BaseDataProvider
from mimesis.typing import Date, DateTime, Time

__all__ = ['Datetime']


class Datetime(BaseDataProvider):
    """Class for generating data related to the date and time."""

    # See: https://git.io/Jf15A
    CURRENT_YEAR = datetime.now().year

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self._datafile = 'datetime.json'
        self._pull(self._datafile)

    class Meta:
        """Class for metadata."""

        name = 'datetime'

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

    def week_date(self, start: int = 2017, end: int = CURRENT_YEAR) -> str:
        """Get week number with year.

        :param start: From start.
        :param end: To end.
        :return: Week number.
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
        """
        key = 'abbr' if abbr else 'name'
        days = self._data['day'].get(key)
        return self.random.choice(days)

    def month(self, abbr: bool = False) -> str:
        """Get a random month.

        :param abbr: Abbreviated month name.
        :return: Month name.
        """
        key = 'abbr' if abbr else 'name'
        months = self._data['month'].get(key)
        return self.random.choice(months)

    def year(self, minimum: int = 1990, maximum: int = CURRENT_YEAR) -> int:
        """Generate a random year.

        :param minimum: Minimum value.
        :param maximum: Maximum value.
        :return: Year.
        """
        return self.random.randint(minimum, maximum)

    def century(self) -> str:
        """Get a random century.

        :return: Century.
        """
        return self.random.choice(ROMAN_NUMS)

    def periodicity(self) -> str:
        """Get a random periodicity string.

        :return: Periodicity.
        """
        periodicity = self._data['periodicity']
        return self.random.choice(periodicity)

    def date(self, start: int = 2000, end: int = CURRENT_YEAR) -> Date:
        """Generate random date object.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :return: Formatted date.
        """
        year = self.random.randint(start, end)
        month = self.random.randint(1, 12)
        day = self.random.randint(1, monthrange(year, month)[1])
        date_object = date(year, month, day)
        return date_object

    def formatted_date(self, fmt: str = '', **kwargs) -> str:
        """Generate random date as string.

        :param fmt: The format of date, if None then use standard
            accepted in the current locale.
        :param kwargs: Keyword arguments for :meth:`~Datetime.date()`
        :return: Formatted date.
        """
        date_obj = self.date(**kwargs)

        if not fmt:
            fmt = self._data['formats'].get('date')

        return date_obj.strftime(fmt)

    def time(self) -> Time:
        """Generate a random time object.

        :return: ``datetime.time`` object.
        """
        random_time = time(
            self.random.randint(0, 23),
            self.random.randint(0, 59),
            self.random.randint(0, 59),
            self.random.randint(0, 999999),
        )
        return random_time

    def formatted_time(self, fmt: str = '') -> str:
        """Generate string formatted time.

        :param fmt: The format of time, if None then use standard
            accepted in the current locale.
        :return: String formatted time.
        """
        time_obj = self.time()

        if not fmt:
            fmt = self._data['formats'].get('time')
        return time_obj.strftime(fmt)

    def day_of_month(self) -> int:
        """Generate a random day of month, from 1 to 31.

        :return: Random value from 1 to 31.
        """
        return self.random.randint(1, 31)

    def timezone(self) -> str:
        """Get a random timezone.

        :return: Timezone.
        """
        return self.random.choice(TIMEZONES)

    def gmt_offset(self) -> str:
        """Get a random GMT offset value.

        :return: GMT Offset.
        """
        return self.random.choice(GMT_OFFSETS)

    def datetime(self, start: int = 2000, end: int = CURRENT_YEAR,
                 timezone: Optional[str] = None) -> DateTime:
        """Generate random datetime.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :param timezone: Set custom timezone (pytz required).
        :return: Datetime
        """
        datetime_obj = datetime.combine(
            date=self.date(start, end),
            time=self.time(),
        )
        if timezone:
            if not pytz:
                raise ImportError('Timezones are supported only with pytz')
            tz = pytz.timezone(timezone)
            datetime_obj = tz.localize(datetime_obj)

        return datetime_obj

    def formatted_datetime(self, fmt: str = '', **kwargs) -> str:
        """Generate datetime string in human readable format.

        :param fmt: Custom format (default is format for current locale)
        :param kwargs: Keyword arguments for :meth:`~Datetime.datetime()`
        :return: Formatted datetime string.
        """
        dt_obj = self.datetime(**kwargs)

        if not fmt:
            date_fmt = self._data['formats'].get('date')
            time_fmt = self._data['formats'].get('time')
            fmt = '{} {}'.format(date_fmt, time_fmt)

        return dt_obj.strftime(fmt)

    def timestamp(self, posix: bool = True, **kwargs) -> Union[str, int]:
        """Generate random timestamp.

        :param posix: POSIX time.
        :param kwargs: Kwargs for :meth:`~Datetime.datetime()`.
        :return: Timestamp.
        """
        stamp = self.datetime(**kwargs)

        if posix:
            return timegm(stamp.utctimetuple())

        return stamp.strftime('%Y-%m-%dT%H:%M:%SZ')
