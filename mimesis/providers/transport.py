"""Provides data related to transports."""

import typing as t

from mimesis.data import (
    AIRPLANES,
    CARS,
    MANUFACTURERS,
    TRUCKS,
    VR_CODES,
    VRC_BY_LOCALES,
)
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider

__all__ = ["Transport"]


class Transport(BaseProvider):
    """Class for generating data related to transports."""

    class Meta:
        """Class for metadata."""

        name: t.Final[str] = "transport"

    def truck(self, model_mask: str = "#### @@") -> str:
        """Generate a truck model.

        :param model_mask: Mask of truck model. Here '@' is a
            placeholder of characters and '#' is a placeholder of digits.
        :return: Dummy truck model.

        :Example:
            Caledon-966O.
        """
        model = self.random.custom_code(model_mask)
        truck = self.random.choice(TRUCKS)
        return f"{truck}-{model}"

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

    def airplane(self, model_mask: str = "###") -> str:
        """Generate a dummy airplane model.

        :param model_mask: Mask of truck model. Here '@' is a
            placeholder of characters and '#' is a placeholder of digits.
        :return: Airplane model.

        :Example:
            Boeing 727.
        """
        model = self.random.custom_code(mask=model_mask)
        plane = self.random.choice(AIRPLANES)
        return f"{plane} {model}"

    def vehicle_registration_code(self, locale: t.Optional[Locale] = None) -> str:
        """Get vehicle registration code of country.

        :param locale: Registration code for locale (country).
        :return: Vehicle registration code.
        """
        if locale:
            return VRC_BY_LOCALES[locale.value]

        return self.random.choice(VR_CODES)
