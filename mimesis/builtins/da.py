# -*- coding: utf-8 -*-

"""Specific data provider for Denmark (da)."""

from typing import Optional

from mimesis.builtins.base import BaseSpecProvider
from mimesis.locales import Locale
from mimesis.typing import Seed

__all__ = ["DenmarkSpecProvider"]


class DenmarkSpecProvider(BaseSpecProvider):
    """Class that provides special data for Denmark (da)."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.DE, seed=seed)

    class Meta:
        """The name of the provider."""

        name = "denmark_provider"

    def cpr(self) -> str:
        """Generate a random CPR number (Central Person Registry).

        :return: CPR number.

        :Example:
            0105865167
        """
        cpr_nr = "{:02d}{:02d}{:02d}{:04d}".format(
            self.random.randint(1, 31),
            self.random.randint(1, 12),
            self.random.randint(0, 99),
            self.random.randint(0, 9999),
        )
        return cpr_nr
