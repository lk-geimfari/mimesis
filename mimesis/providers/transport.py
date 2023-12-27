"""Provides data related to transports."""

from mimesis.data import (
    AIRPLANES,
    AUTO_MANUFACTURERS,
    CARS,
    VR_CODES,
    VRC_BY_LOCALES,
)
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider

__all__ = ["Transport"]


class Transport(BaseProvider):
    """Class for generating data related to transports."""

    class Meta:
        name = "transport"

    def manufacturer(self) -> str:
        """Get a random car manufacturer.

        :return: A car manufacturer

        :Example:
            Tesla.
        """
        return self.random.choice(AUTO_MANUFACTURERS)

    def car(self) -> str:
        """Get a random vehicle.

        :return: A vehicle.

        :Example:
            Tesla Model S.
        """
        return self.random.choice(CARS)

    def airplane(self) -> str:
        """Generate a dummy airplane model.

        :return: Airplane model.

        :Example:
            Boeing 727.
        """
        return self.random.choice(AIRPLANES)

    def vehicle_registration_code(self, locale: Locale | None = None) -> str:
        """Get vehicle registration code of country.

        :param locale: Registration code for locale (country).
        :return: Vehicle registration code.
        """
        if locale:
            return VRC_BY_LOCALES[locale.value]

        return self.random.choice(VR_CODES)
