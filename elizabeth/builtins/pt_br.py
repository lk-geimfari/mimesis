from random import randint


class BrazilSpecProvider(object):
    """Class that provides special data for pt-br"""

    class Meta:
        name = 'brazil_provider'

    @staticmethod
    def cpf(with_mask=True):
        """Get a random CPF (brazilian social security code)

        :param with_mask: use CPF mask (###.###.###-##) in the return
        :returns: Random CPF
        :Example:
            001.137.297-40
        """

        def get_verifying_digit_cpf(cpf, peso):
            """Calculates the verifying digit for the CPF

            :param cpf: ist of integers with the CPF
            :param peso: Integer with the weight for the modulo 11 calculate
            :returns: the verifying digit for the CPF
            """
            soma = 0
            for index, digit in enumerate(cpf):
                soma += digit * (peso - index)
            resto = soma % 11
            if resto == 0 or resto == 1 or resto >= 11:
                return 0
            return 11 - resto

        cpf_without_dv = [randint(0, 9) for _ in range(9)]
        first_dv = get_verifying_digit_cpf(cpf_without_dv, 10)

        cpf_without_dv.append(first_dv)
        second_dv = get_verifying_digit_cpf(cpf_without_dv, 11)
        cpf_without_dv.append(second_dv)

        cpf = ''.join([str(i) for i in cpf_without_dv])

        if with_mask:
            return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf

    @staticmethod
    def cnpj(with_mask=True):
        """Get a random cnpj (brazilian social security code)

        :param with_mask: use cnpj mask (###.###.###-##) in the return
        :returns: Random cnpj
        :Example:
            77.732.230/0001-70
        """

        def get_verifying_digit_cnpj(cnpj, peso):
            """Calculates the verifying digit for the cnpj
            :param cnpj: list of integers with the cnpj
            :param peso: integer with the weigth for the modulo 11 calcule
            :returns: the verifying digit for the cnpj
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

        cnpj_without_dv = [randint(0, 9) for _ in range(12)]

        first_dv = get_verifying_digit_cnpj(cnpj_without_dv, 5)
        cnpj_without_dv.append(first_dv)

        second_dv = get_verifying_digit_cnpj(cnpj_without_dv, 6)
        cnpj_without_dv.append(second_dv)

        cnpj = ''.join([str(i) for i in cnpj_without_dv])

        if with_mask:
            return cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + \
                   cnpj[8:12] + '-' + cnpj[12:]
        return cnpj
