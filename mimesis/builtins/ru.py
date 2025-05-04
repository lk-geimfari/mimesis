"""Specific data provider for Russia (ru)."""

from datetime import datetime

from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed

__all__ = ["RussiaSpecProvider"]


class RussiaSpecProvider(BaseDataProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.RU, seed=seed)
        self._current_year = str(datetime.now().year)

    class Meta:
        """The name of the provider."""

        name = "russia_provider"
        datafile = "builtin.json"

    def generate_sentence(self) -> str:
        """Generate sentence from the parts.

        :return: Sentence.
        """
        sentences = self._extract(["sentence"])
        sentence = [
            self.random.choice(sentences[k]) for k in ("head", "p1", "p2", "tail")
        ]
        return " ".join(sentence)

    def passport_series(self, year: int | None = None) -> str:
        """Generate random series of passport.

        :param year: Year of manufacture.
        :type year: int or None
        :return: Series.

        :Example:
            02 15.
        """
        if not year:
            year = self.random.randint(10, int(self._current_year[2:]))

        region = self.random.randint(1, 99)
        return f"{region:02d} {year}"

    def passport_number(self) -> int:
        """Generate random passport number.

        :return: Number.

        :Example:
            560430
        """
        return self.random.randint(100000, 999999)

    def series_and_number(self) -> str:
        """Generate a random passport number and series.

        :return: Series and number.

        :Example:
            57 16 805199.
        """
        series = self.passport_series()
        number = self.passport_number()
        return f"{series} {number}"

    def snils(self) -> str:
        """Generate snils with a special algorithm.

        :return: SNILS.

        :Example:
            41917492600.
        """
        numbers = []
        control_codes = []

        for i in range(0, 9):
            numbers.append(self.random.randint(0, 9))

        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)
        code = "".join(map(str, numbers))

        if control_code in (100, 101):
            _snils = code + "00"
            return _snils

        if control_code < 100:
            _snils = code + str(control_code)
            return _snils

        if control_code > 101:
            control_code = control_code % 101
            if control_code == 100:
                control_code = 0
            _snils = code + f"{control_code:02}"
            return _snils
        raise RuntimeError("Must not be reached")

    def inn(self) -> str:
        """Generate random, but valid ``INN``.

        :return: INN.
        """

        def control_sum(nums: list[int], t: str) -> int:
            digits_dict = {
                "n2": [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
                "n1": [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            }
            number = 0
            digits = digits_dict[t]

            for i, _ in enumerate(digits, start=0):
                number += nums[i] * digits[i]
            return number % 11 % 10

        numbers = []
        for x in range(0, 10):
            numbers.append(self.random.randint(1 if x == 0 else 0, 9))

        n2 = control_sum(numbers, "n2")
        numbers.append(n2)
        n1 = control_sum(numbers, "n1")
        numbers.append(n1)
        return "".join(map(str, numbers))

    def ogrn(self) -> str:
        """Generate random valid ``OGRN``.

        :return: OGRN.

        :Example:
            4715113303725.
        """
        numbers = []
        for _ in range(0, 12):
            numbers.append(self.random.randint(1 if _ == 0 else 0, 9))

        _ogrn = "".join(str(i) for i in numbers)
        check_sum = str(int(_ogrn) % 11 % 10)

        return f"{_ogrn}{check_sum}"

    def bic(self) -> str:
        """Generate random ``BIC`` (Bank ID Code).

        :return: BIC.

        :Example:
            044025575.
        """
        country_code = "04"
        code = f"{self.random.randint(1, 10):02}"
        bank_number = f"{self.random.randint(0, 99):02}"
        bank_office = f"{self.random.randint(50, 999):03}"
        bic = country_code + code + bank_number + bank_office
        return bic

    def kpp(self) -> str:
        """Generate random ``KPP``.

        :return: 'KPP'.

        :Example:
            560058652.
        """
        tax_codes: list[str] = self._extract(["tax_codes"])
        tax_code = tax_codes[self.random.randint(0, len(tax_codes) - 1)]
        reg_code = f"{self.random.randint(1, 99):02}"
        reg_number = f"{self.random.randint(1, 999):03}"
        kpp = tax_code + reg_code + reg_number
        return kpp
