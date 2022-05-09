"""Specific data provider for Poland (pl)."""

import typing as t

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import Datetime
from mimesis.types import DateTime, Seed

__all__ = ["PolandSpecProvider"]


class PolandSpecProvider(BaseSpecProvider):
    """Class that provides special data for Poland (pl)."""

    def __init__(self, seed: Seed = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.PL, seed=seed)

    class Meta:
        """The name of the provider."""

        name: t.Final[str] = "poland_provider"

    def nip(self) -> str:
        """Generate random valid 10-digit NIP.

        :return: Valid 10-digit NIP
        """
        nip_digits = [int(d) for d in str(self.random.randint(101, 998))]
        nip_digits += [self.random.randint(0, 9) for _ in range(6)]
        nip_coefficients = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        sum_v = sum(nc * nd for nc, nd in zip(nip_coefficients, nip_digits))

        checksum_digit = sum_v % 11
        if checksum_digit > 9:
            return self.nip()
        nip_digits.append(checksum_digit)
        return "".join(map(str, nip_digits))

    def pesel(
        self, birth_date: t.Optional[DateTime] = None, gender: t.Optional[Gender] = None
    ) -> str:
        """Generate random 11-digit PESEL.

        :param birth_date: Initial birth date (optional)
        :param gender: Gender of person
        :return: Valid 11-digit PESEL
        """
        date_object = birth_date
        if not date_object:
            date_object = Datetime().datetime(1940, 2018)

        date = date_object.date()
        year = date.year % 100
        month = date.month
        day = date.day

        if 1800 <= year <= 1899:
            month += 80
        elif 2000 <= year <= 2099:
            month += 20
        elif 2100 <= year <= 2199:
            month += 40
        elif 2200 <= year <= 2299:
            month += 60

        series_number = self.random.randint(0, 999)

        pesel_digits = list(
            map(int, f"{year:02d}{month:02d}{day:02d}{series_number:03d}")
        )

        if gender == Gender.MALE:
            gender_digit = self.random.choice((1, 3, 5, 7, 9))
        elif gender == Gender.FEMALE:
            gender_digit = self.random.choice((0, 2, 4, 6, 8))
        else:
            gender_digit = self.random.choice(range(10))

        pesel_digits.append(gender_digit)
        pesel_coeffs = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
        sum_v = sum(nc * nd for nc, nd in zip(pesel_coeffs, pesel_digits))
        checksum_digit = sum_v % 10
        pesel_digits.append(checksum_digit)
        return "".join(map(str, pesel_digits))

    def regon(self) -> str:
        """Generate random valid 9-digit REGON.

        :return: Valid 9-digit REGON
        """
        regon_coeffs = (8, 9, 2, 3, 4, 5, 6, 7)
        regon_digits = [self.random.randint(0, 9) for _ in range(8)]
        sum_v = sum(nc * nd for nc, nd in zip(regon_coeffs, regon_digits))
        checksum_digit = sum_v % 11
        if checksum_digit > 9:
            checksum_digit = 0
        regon_digits.append(checksum_digit)
        return "".join(map(str, regon_digits))
