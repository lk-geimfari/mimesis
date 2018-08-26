"""Specific data provider for Poland (pl)."""

from calendar import isleap
from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.typing import DateTime

__all__ = ['PolandSpecProvider']


class PolandSpecProvider(BaseSpecProvider):
    """Class that provides special data for Poland (pl)."""

    class Meta:
        """The name of the provider."""

        name = 'poland_provider'

    def nip(self) -> str:
        """Generate random valid 10-digit NIP.

        :return: valid 10-digit NIP
        """
        nip_digits = list(map(int, str(self.random.randint(101, 998))))
        for _ in range(6):
            nip_digits.append(self.random.randint(0, 9))
        args = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        sum_v = sum(map(lambda x: x[0] * x[1], zip(args, nip_digits)))
        checksum_digit = sum_v % 11
        while checksum_digit > 9:
            checksum_digit = 0
        nip_digits.append(checksum_digit)
        return ''.join(str(d) for d in nip_digits)

    def pesel(self, birth_date: Optional[DateTime]=None,
              gender: Optional[Gender]=None) -> str:
        """Generate random 11-digit PESEL.

        :param birth_date: initial birth date (optional)
        :param gender: gender of person
        :return: valid 11-digit PESEL
        """
        if not birth_date:
            year = self.random.randint(1800, 2299) % 100
            month = self.random.randint(1, 12)
            if month in (4, 6, 9, 10):
                day = self.random.randint(1, 30)
            elif month == 2:
                if isleap(year):
                    day = self.random.randint(1, 29)
                else:
                    day = self.random.randint(1, 28)
            else:
                day = self.random.randint(1, 31)
        else:
            year = birth_date.date().year
            month = birth_date.date().month
        pesel_digits = list(map(int, '{:02d}'.format(year)))
        if 1800 <= year <= 1899:
            month += 80
        elif 1900 <= year <= 1999:
            pass
        elif 2000 <= year <= 2099:
            month += 20
        elif 2100 <= year <= 2199:
            month += 40
        elif 2200 <= year <= 2299:
            month += 60
        pesel_digits += list(map(int, '{:02d}'.format(month)))
        pesel_digits += list(map(int, '{:02d}'.format(day)))
        series_number = self.random.randint(0, 999)
        pesel_digits += list(map(int, '{:03d}'.format(series_number)))
        if gender == Gender.MALE:
            gender_digit = self.random.choice((1, 3, 5, 7, 9))
        elif gender == Gender.FEMALE:
            gender_digit = self.random.choice((0, 2, 4, 6, 8))
        else:
            gender_digit = self.random.choice(range(10))
        pesel_digits += list(map(int, str(gender_digit)))
        args = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
        sum_v = sum(map(lambda x: x[0] * x[1], zip(args, pesel_digits)))
        checksum_digit = sum_v % 10
        pesel_digits.append(checksum_digit)
        return ''.join(str(d) for d in pesel_digits)

    def regon(self) -> str:
        """Generate random valid 9-digit REGON.

        :return: valid 9-digit REGON
        """
        args = (8, 9, 2, 3, 4, 5, 6, 7)
        regon_digits = [self.random.randint(0, 9) for x in range(8)]
        sum_v = sum(map(lambda x: x[0] * x[1], zip(args, regon_digits)))
        checksum_digit = sum_v % 11
        if checksum_digit > 9:
            checksum_digit = 0
        regon_digits.append(checksum_digit)
        return ''.join(str(d) for d in regon_digits)
