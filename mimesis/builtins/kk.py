"""Specific data provider for Kazakhstan (kk)."""
import random

from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider, Datetime
from mimesis.types import Date, MissingSeed, Seed

__all__ = ["KazakhstanSpecProvider"]


class KazakhstanSpecProvider(BaseDataProvider):
    """Class that provides special data for Kazakhstan (kk)."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.KK, seed=seed)
        self._current_year = Date.today().year

    class Meta:
        """The name of the provider."""

        name = "kazakhstan_provider"
        datafile = "builtin.json"

    def patronymic(self, gender: Gender | None = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Абайқызы.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: list[str] = self._extract(["patronymic", str(gender)])
        return self.random.choice(patronymics)

    def iin(
        self, date_of_birth: Date | None = None, gender: Gender | None = None
    ) -> str:
        """Generate random, but valid ``IIN``.

        :return: IIN.
        """

        n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        n2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]

        if date_of_birth is None:
            date_of_birth = Datetime().date(
                self._current_year - 100, self._current_year
            )
        if gender is None:
            gender = self.random.choice([Gender.MALE, Gender.FEMALE])
        century = date_of_birth.year // 100 + 1

        part_1 = date_of_birth.strftime("%y%m%d")
        part_2 = random.randint(5, 6)
        match (gender, century):
            case (Gender.MALE, 19):
                part_2 = 1
            case (Gender.FEMALE, 19):
                part_2 = 2
            case (Gender.MALE, 20):
                part_2 = 3
            case (Gender.FEMALE, 20):
                part_2 = 4
            case (Gender.MALE, _):
                part_2 = 5
            case (Gender.FEMALE, _):
                part_2 = 6
        part_3 = str(self.random.randint(1000, 9999))

        while True:
            digits = list(map(int, f"{part_1}{part_2}{part_3}"))
            control = sum(i * j for (i, j) in zip(digits, n1)) % 11
            if control == 10:
                control = sum(i * j for (i, j) in zip(digits, n2)) % 11
            if len(str(control)) == 1:
                break
            part_3 = str(self.random.randint(1000, 9999))

        return f"{part_1}{part_2}{part_3}{control}"
