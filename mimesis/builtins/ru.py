# -*- coding: utf-8 -*-

"""Specific data provider for Russia (ru)."""

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.typing import Seed

__all__ = ['RussiaSpecProvider']


class RussiaSpecProvider(BaseSpecProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, seed: Seed = None):
        """Initialize attributes."""
        super().__init__(locale='ru', seed=seed)
        self._pull(self._datafile)

    class Meta:
        """The name of the provider."""

        name = 'russia_provider'

    def generate_sentence(self) -> str:
        """Generate sentence from the parts.

        :return: Sentence.
        """
        sentences = self._data['sentence']
        sentence = [
            self.random.choice(sentences[k]) for k
            in ('head', 'p1', 'p2', 'tail')
        ]
        return '{0} {1} {2} {3}'.format(*sentence)

    def patronymic(self, gender: Gender = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Алексеевна.
        """
        gender = self._validate_enum(gender, Gender)
        patronymics = self._data['patronymic'][gender]
        return self.random.choice(patronymics)

    def passport_series(self, year: int = None) -> str:
        """Generate random series of passport.

        :param year: Year of manufacture.
        :type year: int or None
        :return: Series.

        :Example:
            02 15.
        """
        if not year:
            year = self.random.randint(10, 18)

        region = self.random.randint(1, 99)
        return '{:02d} {}'.format(region, year)

    def passport_number(self) -> int:
        """Generate random passport number.

        :return: Number.

        :Example:
            560430
        """
        return self.random.randint(
            100000, 999999)

    def series_and_number(self) -> str:
        """Generate a random passport number and series.

        :return: Series and number.

        :Example:
            57 16 805199.
        """
        return '{}{}'.format(
            self.passport_series(),
            self.passport_number(),
        )

    def snils(self) -> str:
        """Generate snils with special algorithm.

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
        code = ''.join(str(number) for number in numbers)

        if control_code in (100, 101):
            snils = code + '00'
            return snils

        if control_code < 100:
            snils = code + str(control_code)
            return snils

        if control_code > 101:
            control_code = control_code % 101
            if control_code == 100:
                control_code = 0
            snils = code + '{:02}'.format(control_code)
            return snils

    def inn(self) -> str:
        """Generate random, but valid ``INN``.

        :return: INN.
        """
        def control_sum(nums: list, t: str) -> int:
            digits_dict = {
                'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
                'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            }
            number = 0
            digits = digits_dict[t]

            for i, _ in enumerate(digits, start=0):
                number += nums[i] * digits[i]
            return number % 11 % 10

        numbers = []
        for x in range(0, 10):
            numbers.append(self.random.randint(1 if x == 0 else 0, 9))

        n2 = control_sum(numbers, 'n2')
        numbers.append(n2)
        n1 = control_sum(numbers, 'n1')
        numbers.append(n1)
        return ''.join([str(x) for x in numbers])

    def ogrn(self) -> str:
        """Generate random valid ``OGRN``.

        :return: OGRN.

        :Example:
            4715113303725.
        """
        numbers = []
        for _ in range(0, 12):
            numbers.append(self.random.randint(1 if _ == 0 else 0, 9))

        ogrn = ''.join([str(x) for x in numbers])
        check_sum = str(int(ogrn) % 11 % 10)

        return '{}{}'.format(ogrn, check_sum)

    def bic(self) -> str:
        """Generate random ``BIC`` (Bank ID Code).

        :return: BIC.

        :Example:
            044025575.
        """
        country_code = '04'
        code = '{:02}'.format(self.random.randint(1, 10))
        bank_number = '{:02}'.format(self.random.randint(0, 99))
        bank_office = '{:03}'.format(self.random.randint(50, 999))
        bic = country_code + code + bank_number + bank_office
        return bic

    def kpp(self) -> str:
        """Generate random ``KPP``.

        :return: 'KPP'.

        :Example:
            560058652.
        """
        tax_codes = [
            '7700', '7800', '5000', '0100',
            '0200', '0300', '0500', '0600',
            '0700', '0800', '0900', '1000',
            '1100', '1200', '1300', '1400',
            '1500', '1600', '1700', '1800',
            '1900', '2000', '2100', '2200',
            '2300', '2400', '2500', '2600',
            '2700', '2800', '2900', '3000',
            '3100', '3200', '3300', '3400',
            '3500', '3600', '3700', '3800',
            '3900', '4000', '4100', '4900',
            '5100', '5200', '5300', '5400',
            '5500', '5600', '5700', '5800',
            '5900', '6000', '6100', '6200',
            '6300', '6400', '6500', '6600',
            '6700', '6800', '6900', '7000',
            '7100', '7200', '7300', '7400',
            '7500', '7600', '7900', '8600',
            '8700', '8900', '9100', '9200',
            '9800', '9900', '9901', '9951',
            '9952', '9953', '9954', '9955',
            '9956', '9957', '9958', '9959',
            '9961', '9962', '9965', '9966',
            '9971', '9972', '9973', '9974',
            '9975', '9976', '9977', '9979',
            '9998',
        ]

        tax_code = tax_codes[self.random.randint(0, len(tax_codes) - 1)]
        reg_code = '{:02}'.format(self.random.randint(1, 99))
        reg_number = '{:03}'.format(self.random.randint(1, 999))
        kpp = tax_code + reg_code + reg_number
        return kpp
