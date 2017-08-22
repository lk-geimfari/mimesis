import datetime
from calendar import monthrange

from mimesis.data import GMT_OFFSETS, ROMAN_NUMS, TIMEZONES
from mimesis.providers import BaseProvider
from mimesis.utils import pull


class Datetime(BaseProvider):
    """Class for generate the fake data that you can use for
    working with date and time."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('datetime.json', self.locale)

    def day_of_week(self, abbr=False):
        """Get a random day of week.

        :param abbr: Abbreviated name of the day.
        :return: Name of day of the week.
        :Example:
            Wednesday (Wed. when abbr=True).
        """
        key = 'abbr' if abbr else 'name'
        days = self.data['day'][key]
        return self.random.choice(days)

    def month(self, abbr=False):
        """Get a random month.

        :param abbr: if True then will be returned abbreviated month name.
        :return: Month name.
        :Example:
            January (Jan. when abbr=True).
        """
        key = 'abbr' if abbr else 'name'
        months = self.data['month'][key]
        return self.random.choice(months)

    def year(self, minimum=1990, maximum=2050):
        """Generate a random year.

        :param minimum: Minimum value.
        :param maximum: Maximum value
        :return: Year.
        :Example:
            2023.
        """
        return self.random.randint(int(minimum), int(maximum))

    def century(self):
        """Get a random value from list of centuries (roman format).

        :return: Century.
        :Example:
            XXI
        """
        return self.random.choice(ROMAN_NUMS)

    def periodicity(self):
        """Get a random periodicity string.

        :return: Periodicity.
        :Example:
            Never.
        """
        periodicity = self.data['periodicity']
        return self.random.choice(periodicity)

    def date(self, start=2000, end=2035, fmt=None):
        """Generate a string representing of random date formatted for
        the locale or as specified.

        :param start: Minimum value of year.
        :param end: Maximum value of year.
        :param fmt: Format string for date.
        :return: Formatted date.
        :Example:
            08/16/88 (en)
        """
        if not fmt:
            fmt = self.data['formats']['date']

        year = self.random.randint(start, end)
        month = self.random.randint(1, 12)
        d = datetime.date(
            year, month, self.random.randint(1, monthrange(year, month)[1]))
        return d.strftime(fmt)

    def time(self, fmt=None):
        """Generate a random time formatted for the locale or as specified.

        :return: Time.
        :Example:
            21:30:00 (en)
        """
        if not fmt:
            fmt = self.data['formats']['time']

        t = datetime.time(
            self.random.randint(0, 23),
            self.random.randint(0, 59),
            self.random.randint(0, 59),
            self.random.randint(0, 999999),
        )
        return t.strftime(fmt)

    def day_of_month(self):
        """Generate a random day of month, from 1 to 31.

        :return: Random value from 1 to 31.
        :Example:
            23
        """
        return self.random.randint(1, 31)

    def timezone(self):
        """Get a random timezone

        :return: Timezone.
        :Example:
            Europe/Paris
        """
        return self.random.choice(TIMEZONES)

    def gmt_offset(self):
        """Get a random GMT offset value.

        :return: GMT Offset.
        :Example:
            'UTC +03:00'
        """
        return self.random.choice(GMT_OFFSETS)
