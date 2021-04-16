# -*- coding: utf-8 -*-

"""Specific data provider for Denmark (da)."""

from typing import Optional

from mimesis import locales
from mimesis.builtins.base import BaseSpecProvider
from mimesis.typing import Seed

__all__ = ["DenmarkSpecProvider"]


class DenmarkSpecProvider(BaseSpecProvider):
    """Class that provides special data for Denmark (da)."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=locales.DE, seed=seed)

    class Meta:
        """The name of the provider."""

        name = "denmark_provider"

    def cpr(self) -> str:
        """Generate a random CPR number (Central Person Registry).

        :return: CPR number.

        :Example:
            0105865167
        """
        day = "{:02d}".format(self.random.randint(1, 31))
        month = "{:02d}".format(self.random.randint(1, 12))
        year = "{:02d}".format(self.random.randint(0, 99))
        serial_number = "{:04d}".format(self.random.randint(0, 9999))

        cpr_nr = "{}{}{}{}".format(day, month, year, serial_number)

        return cpr_nr
