"""Specific data provider for USA (en)."""

import typing as t

from mimesis.builtins.base import BaseSpecProvider
from mimesis.locales import Locale
from mimesis.types import Seed

__all__ = ["USASpecProvider"]


class USASpecProvider(BaseSpecProvider):
    """Class that provides special data for USA (en)."""

    def __init__(self, seed: Seed = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.EN, seed=seed)

    class Meta:
        """The name of the provider."""

        name: t.Final[str] = "usa_provider"

    def tracking_number(self, service: str = "usps") -> str:
        """Generate random tracking number.

        Supported services: USPS, FedEx and UPS.

        :param str service: Post service.
        :return: Tracking number.
        """
        service = service.lower()

        if service not in ("usps", "fedex", "ups"):
            raise ValueError("Unsupported post service")

        services = {
            "usps": (
                "#### #### #### #### ####",
                "@@ ### ### ### US",
            ),
            "fedex": (
                "#### #### ####",
                "#### #### #### ###",
            ),
            "ups": ("1Z@####@##########",),
        }
        mask = self.random.choice(services[service])
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

        return "{:03}-{:02}-{:04}".format(
            area,
            self.random.randint(1, 99),
            self.random.randint(1, 9999),
        )
