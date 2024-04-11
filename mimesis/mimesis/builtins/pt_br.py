"""Specific data provider for Brazil (pt-br)."""

from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed

__all__ = ["BrazilSpecProvider"]


class BrazilSpecProvider(BaseDataProvider):
    """Class that provides special data for Brazil (pt-br)."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.PT_BR, seed=seed)

    class Meta:
        name = "brazil_provider"
        datafile = None

    @staticmethod
    def __get_verifying_digit_cpf(cpf: list[int], weight: int) -> int:
        """Calculate the verifying digit for the CPF.

        :param cpf: List of integers with the CPF.
        :param weight: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CPF.
        """
        total = 0

        for index, digit in enumerate(cpf):
            total += digit * (weight - index)

        remainder = total % 11

        if remainder == 0 or remainder == 1 or remainder >= 11:
            return 0

        return 11 - remainder

    def cpf(self, with_mask: bool = True) -> str:
        """Get a random CPF.

        :param with_mask: Use CPF mask (###.###.###-##).
        :returns: Random CPF.

        :Example:
            001.137.297-40
        """

        cpf_without_dv = [self.random.randint(0, 9) for _ in range(9)]
        first_dv = self.__get_verifying_digit_cpf(cpf_without_dv, 10)

        cpf_without_dv.append(first_dv)
        second_dv = self.__get_verifying_digit_cpf(cpf_without_dv, 11)
        cpf_without_dv.append(second_dv)

        cpf = "".join(str(i) for i in cpf_without_dv)

        if with_mask:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf

    @staticmethod
    def __get_verifying_digit_cnpj(cnpj: list[int], weight: int) -> int:
        """Calculate the verifying digit for the CNPJ.

        :param cnpj: List of integers with the CNPJ.
        :param weight: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CNPJ.
        """
        total = 0
        weights_dict = {
            5: [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
            6: [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
        }
        weights = weights_dict[weight]

        for i, _ in enumerate(cnpj):
            total += weights[i] * cnpj[i]

        remainder = total % 11
        return 0 if (remainder < 2) else (11 - remainder)

    def cnpj(self, with_mask: bool = True) -> str:
        """Get a random CNPJ.

        :param with_mask: Use cnpj mask (###.###.###-##)
        :returns: Random cnpj.

        :Example:
            77.732.230/0001-70
        """

        cnpj_without_dv = [self.random.randint(0, 9) for _ in range(12)]

        first_dv = self.__get_verifying_digit_cnpj(cnpj_without_dv, 5)
        cnpj_without_dv.append(first_dv)

        second_dv = self.__get_verifying_digit_cnpj(cnpj_without_dv, 6)
        cnpj_without_dv.append(second_dv)

        cnpj = "".join(str(i) for i in cnpj_without_dv)

        if with_mask:
            return "{}.{}.{}/{}-{}".format(
                cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]
            )
        return cnpj
