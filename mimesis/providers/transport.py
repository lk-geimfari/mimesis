# -*- coding: utf-8 -*-

"""Provides data related to transports."""

from typing import Optional

from mimesis.data import (
    AIRPLANES,
    CARS,
    MANUFACTURERS,
    TRUCKS,
    VR_CODES,
    VRC_BY_LOCALES,
)
from mimesis.providers.base import BaseProvider

__all__ = ['Transport']


class Transport(BaseProvider):
    """Class for generating data related to transports."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)

    class Meta:
        """Class for metadata."""

        name = 'transport'

    def truck(self, model_mask: str = '#### @@') -> str:
        """Generate a truck model.

        :param model_mask: Mask of truck model. Here '@' is a
            placeholder of characters and '#' is a placeholder of digits.
        :return: Dummy truck model.

        :Example:
            Caledon-966O.
        """
        return '{}-{}'.format(
            self.random.choice(TRUCKS),
            self.random.custom_code(model_mask),
        )

    def manufacturer(self) -> str:
        """Get a random card manufacturer.

        :return: A car manufacturer

        :Example:
            Tesla.
        """
        return self.random.choice(MANUFACTURERS)

    def car(self) -> str:
        """Get a random vehicle.

        :return: A vehicle.

        :Example:
            Tesla Model S.
        """
        return self.random.choice(CARS)

    def airplane(self, model_mask: str = '###') -> str:
        """Generate a dummy airplane model.

        :param model_mask: Mask of truck model. Here '@' is a
            placeholder of characters and '#' is a placeholder of digits.
        :return: Airplane model.

        :Example:
            Boeing 727.
        """
        model = self.random.custom_code(mask=model_mask)
        plane = self.random.choice(AIRPLANES)
        return '{} {}'.format(plane, model)

    def vehicle_registration_code(self, locale: Optional[str] = None) -> str:
        """Get vehicle registration code of country.

        :param locale: Registration code for locale (country).
        :return: Vehicle registration code.
        """
        if locale:
            return VRC_BY_LOCALES[locale]

        return self.random.choice(VR_CODES)
