# -*- coding: utf-8 -*-

"""Specific data provider for USA (en)."""

from typing import Union, Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.builtins.enums.en import State
from mimesis.typing import Seed

__all__ = ['USASpecProvider']


class USASpecProvider(BaseSpecProvider):
    """Class which provides special data for USA (en)."""

    def __init__(self, seed: Seed = None):
        """Initialize attributes."""
        super().__init__(locale='en', seed=seed)
        self.pull(self._datafile)

    class Meta:
        """The name of the provider."""

        name = 'usa_provider'

    def tracking_number(self, service: str = 'usps') -> str:
        """Generate random tracking number.

        Supported services: USPS, FedEx and UPS.

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
        return self.random.custom_code(mask=mask)

    def ssn(self) -> str:
        """Generate a random, but valid SSN.

        :returns: SSN.

        :Example:
            569-66-5801
        """
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

        :param category: Category.
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

    def telephone(self, state: Optional[State] = None) -> str:
        """Generate a random phone number by state.

        :param state: State enum.
        :return: Phone number.

        :Example:
           1-253-427-5903
        """
        state_code = self._validate_enum(state, State)
        codes = self._data['area_codes_by_states'][state_code]
        masks = self._data['telephone_fmt']
        telephone_mask = self.random.choice(masks)
        telephone_mask = telephone_mask.format(self.random.choice(codes))
        return self.random.custom_code(mask=telephone_mask)
