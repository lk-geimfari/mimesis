from random import choice, randint

from elizabeth.core import Code

# Internal
_custom_code = Code.custom_code


class USASpecProvider(object):
    """Class that provides special data for en"""

    class Meta:
        name = 'usa_provider'

    @staticmethod
    def tracking_number(service='usps'):
        """Generate random tracking number for USPS, FedEx and UPS.
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
        """Generate a random, but valid Social Security Number.

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
        """Generate a type of personality.

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
