# -*- coding: utf-8 -*-

"""Specific data provider for Brazil (pt-br)."""

from mimesis.builtins.base import BaseSpecProvider
from mimesis.typing import Seed

__all__ = ['BrazilSpecProvider']


class BrazilSpecProvider(BaseSpecProvider):
    """Class that provides special data for Brazil (pt-br)."""

    def __init__(self, seed: Seed = None):
        """Initialize attributes."""
        super().__init__(locale='pt-br', seed=seed)

    class Meta:
        """The name of the provider."""

        name = 'brazil_provider'

    def cpf(self, with_mask: bool = True) -> str:
        """Get a random CPF.

        :param with_mask: Use CPF mask (###.###.###-##).
        :returns: Random CPF.

        :Example:
            001.137.297-40
        """
        def get_verifying_digit_cpf(cpf, peso):
            """Calculate the verifying digit for the CPF.

            :param cpf: List of integers with the CPF.
            :param peso: Integer with the weight for the modulo 11 calculate.
            :returns: The verifying digit for the CPF.
            """
            soma = 0
            for index, digit in enumerate(cpf):
                soma += digit * (peso - index)
            resto = soma % 11
            if resto == 0 or resto == 1 or resto >= 11:
                return 0
            return 11 - resto

        cpf_without_dv = [self.random.randint(0, 9) for _ in range(9)]
        first_dv = get_verifying_digit_cpf(cpf_without_dv, 10)

        cpf_without_dv.append(first_dv)
        second_dv = get_verifying_digit_cpf(cpf_without_dv, 11)
        cpf_without_dv.append(second_dv)

        cpf = ''.join([str(i) for i in cpf_without_dv])

        if with_mask:
            return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf

    def cnpj(self, with_mask: bool = True) -> str:
        """Get a random CNPJ.

        :param with_mask: Use cnpj mask (###.###.###-##)
        :returns: Random cnpj.

        :Example:
            77.732.230/0001-70
        """
        def get_verifying_digit_cnpj(cnpj, peso):
            """Calculate the verifying digit for the CNPJ.

            :param cnpj: List of integers with the CNPJ.
            :param peso: Integer with the weight for the modulo 11 calculate.
            :returns: The verifying digit for the CNPJ.
            """
            soma = 0
            if peso == 5:
                peso_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            elif peso == 6:
                peso_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            for i, _ in enumerate(cnpj):
                soma += peso_list[i] * cnpj[i]
            resto = soma % 11
            if resto < 2:
                return 0
            return 11 - resto

        cnpj_without_dv = [self.random.randint(0, 9) for _ in range(12)]

        first_dv = get_verifying_digit_cnpj(cnpj_without_dv, 5)
        cnpj_without_dv.append(first_dv)

        second_dv = get_verifying_digit_cnpj(cnpj_without_dv, 6)
        cnpj_without_dv.append(second_dv)

        cnpj = ''.join([str(i) for i in cnpj_without_dv])

        if with_mask:
            return '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5],
                                           cnpj[5:8], cnpj[8:12], cnpj[12:])
        return cnpj
