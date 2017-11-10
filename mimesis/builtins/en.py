from typing import Union

from mimesis.builtins.base import BaseSpecProvider


class USASpecProvider(BaseSpecProvider):
    """Class that provides special data for en"""

    class Meta:
        name = 'usa_provider'

    def tracking_number(self, service: str = 'usps') -> str:
        """Generate random tracking number for USPS, FedEx and UPS.

        :param str service: Post service.
        :return: Tracking number.
        """
        service = service.lower()

        if service not in ('usps', 'fedex', 'ups'):
            raise ValueError('Unsupported post service')

        services = {
            'usps': (
                '#### #### #### #### ####',
                '@@ ### ### ### US',
            ),
            'fedex': (
                '#### #### ####',
                '#### #### #### ###',
            ),
            'ups': (
                '1Z@####@##########',
            ),
        }
        mask = self.random.choice(services[service])  # type: ignore
        return self.code(mask=mask)

    def ssn(self) -> str:
        """Generate a random, but valid Social Security Number.

        :returns: Random SSN

        :Example:
            569-66-5801
        """
        # Valid SSNs exclude 000, 666, and 900-999 in the area group
        area = self.random.randint(1, 899)
        if area == 666:
            area = 665

        return '{:03}-{:02}-{:04}'.format(
            area,
            self.random.randint(1, 99),
            self.random.randint(1, 9999),
        )

    def personality(self, category: str = 'mbti') -> Union[str, int]:
        """Generate a type of personality.

        :param str category: Category.
        :return: Personality type.
        :rtype: str or int

        :Example:
            ISFJ.
        """
        mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                 'ISTP', 'ISFP', 'INFP', 'INTP',
                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

        if category.lower() == 'rheti':
            return self.random.randint(1, 10)

        return self.random.choice(mbtis)
