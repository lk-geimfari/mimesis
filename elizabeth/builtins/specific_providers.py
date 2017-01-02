from string import ascii_uppercase
from random import randint, choice

__all__ = ['USA', 'Brazil', 'Russia']


def _custom_code(mask="@###", char='@', digit='#'):
    """
    Generate custom code using ascii uppercase and random integers.

    :param mask: Mask of code.
    :param char: Placeholder for characters.
    :param digit: Placeholder for digits.
    :return: Custom code.
    :Example::
        5673-AGFR-SFSFF-1423-4/AD.
    """
    code = ''
    for p in mask:
        if p == char:
            code += choice(ascii_uppercase)
        elif p == digit:
            code += str(randint(0, 9))
        else:
            code += p
    return code


class Brazil(object):
    """Class that provides special data for pt-br"""

    class Meta:
        name = 'brazil_provider'

    @staticmethod
    def cpf(with_mask=True):
        """
        Get a random CPF (brazilian social security code)

        :param with_mask: use CPF mask (###.###.###-##) in the return
        :returns: Random CPF
        :Example:
            001.137.297-40
        """

        def get_verifying_digit_cpf(cpf, peso):
            """
            Calculates the verifying digit for the CPF

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
        """
        Get a random cnpj (brazilian social security code)

        :param with_mask: use cnpj mask (###.###.###-##) in the return
        :returns: Random cnpj
        :Example:
            77.732.230/0001-70
        """

        def get_verifying_digit_cnpj(cnpj, peso):
            """
            Calculates the verifying digit for the cnpj
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


class USA(object):
    class Meta:
        name = 'usa_provider'

    @staticmethod
    def tracking_number(service='usps'):
        """
        Generate random tracking number for USPS, FedEx and UPS.
        :param service:
        :return:
        """
        service = service.lower()

        if service not in ('usps', 'fedex', 'ups'):
            raise ValueError('Unsupported post service')

        services = {
            'usps': (
                '#### #### #### #### ####',
                '@@ ### ### ### US'
            ),
            'fedex': (
                "#### #### ####",
                "#### #### #### ###"
            ),
            'ups': ("1Z@####@##########",)
        }
        mask = choice(services[service])
        return _custom_code(mask=mask)

    def ssn(self):
        """
        Generate a random, but valid Social Security Number.
        :return:
        """
        # ranges = {
        #     'NY': (100, 134),
        #     'NJ': (135, 138),
        #     'PA': (159, 211),
        #     'MD': (212, 220),
        #     'VA': (223, 231),
        #     'WV': (232, 236),
        #     'NC': (237, 246),
        #     'SC': (247, 251),
        #     'GA': (252, 260),
        #     'FL': (261, 267),
        #     'OH': (268, 302),
        #     'IN': (303, 317),
        #     'IL': (318, 361),
        #     'MI': (362, 386),
        #     'WI': (387, 399),
        #     'KY': (400, 407),
        #     'TN': (408, 415),
        #     'AL': (416, 424),
        #     'MS': (425, 428),
        #     'AR': (429, 432),
        #     'LA': (433, 439),
        #     'OK': (440, 448),
        #     'TX': (449, 467),
        #     'MN': (468, 477),
        #     'IA': (478, 485),
        #     'MO': (486, 500),
        #     'ND': (501, 502),
        #     'SD': (503, 504),
        #     'NE': (505, 508),
        #     'KS': (509, 515),
        #     'MT': (516, 517),
        #     'ID': (518, 519),
        #     'WY': (520,),
        #     'CO': (521, 524),
        #     'NM': (525,),
        #     'AZ': (526, 527),
        #     'UT': (528, 529),
        #     'NV': (530,),
        #     'WA': (531, 539),
        #     'OR': (540, 544),
        #     'CA': (545, 573),
        #     'AK': (574,),
        #     'HI': (575, 576),
        #     'DC': (577, 579),
        #     'VI': (580,)
        # }
        pass


class Russia(object):
    """
    Specific data for russian language (ru)
    """

    class Meta:
        name = 'russia_provider'

    @staticmethod
    def passport_series(year=None):
        """
        Generate random series of passport.

        :param year: Year of manufacture.
        :return: Series.
        """
        year = randint(10, 16) if not \
            year else year

        region = randint(1, 99)
        return '{region} {year}'.format(
            region=region, year=year)

    @staticmethod
    def passport_number():
        """
        Generate random passport number.

        :return: Number.
        """
        return _custom_code(mask='######')

    def series_and_number(self):
        """
        Generate a random passport number and series.

        :return: Series and number.
        """
        snn = '{} {}'.format(
            self.passport_series(),
            self.passport_number())
        return snn
