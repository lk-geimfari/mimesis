from random import randint, choice

from elizabeth.core import Code
from elizabeth.exceptions import JSONKeyError
from elizabeth.utils import pull

# TODO: Rename provider to *SpecificProvider, where * is locale code.
__all__ = [
    'USA',
    'Brazil',
    'Russia'
]

# Internal
_custom_code = Code.custom_code


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
    """Class that provides special data for en"""

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

    @staticmethod
    def ssn():
        """
        Generate a random, but valid Social Security Number.

        :returns: Random SSN
        :Example:
            569-66-5801
        """
        # Valid SSNs exclude 000, 666, and 900-999 in the area group
        area = randint(1, 899)
        if area == 666:
            area = 665

        return '{:03}-{:02}-{:04}'.format(
            area, randint(1, 99), randint(1, 9999))

    @staticmethod
    def personality(category='mbti'):
        """
        Generate a type of personality.

        :param category: Category.
        :return: Personality type.
        :Example:
            ISFJ.
        """
        mbtis = ("ISFJ", "ISTJ", "INFJ", "INTJ",
                 "ISTP", "ISFP", "INFP", "INTP",
                 "ESTP", "ESFP", "ENFP", "ENTP",
                 "ESTJ", "ESFJ", "ENFJ", "ENTJ")

        if category.lower() == 'rheti':
            return randint(1, 10)

        return choice(mbtis)


class Russia(object):
    """Specific data for russian language (ru)"""

    class Meta:
        name = 'russia_provider'

    @staticmethod
    def patronymic(gender='female'):
        """
        Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.
        :Example:
            Алексеевна.
        """
        gender = gender.lower()

        try:
            patronymic = pull('personal.json', 'ru')['patronymic']
            return choice(patronymic[gender])
        except:
            raise JSONKeyError(
                'Not exist key. Please use one of ["female", "male"]')

    @staticmethod
    def passport_series(year=None):
        """
        Generate random series of passport.

        :param year: Year of manufacture.
        :return: Series.
        :Example:
            02 15.
        """
        year = randint(10, 16) if not \
            year else year

        region = randint(1, 99)
        return '{:02d} {}'.format(region, year)

    @staticmethod
    def passport_number():
        """
        Generate random passport number.

        :return: Number.
        :Example:
            560430
        """
        return _custom_code(mask='######')

    def series_and_number(self):
        """
        Generate a random passport number and series.

        :return: Series and number.
        :Example:
            57 16 805199.
        """
        return '%s %s' % (
            self.passport_series(),
            self.passport_number()
        )
