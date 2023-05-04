"""Base specific data provider."""

from mimesis.providers import BaseDataProvider

__all__ = ["CountrySpecificProvider"]


class CountrySpecificProvider(BaseDataProvider):
    """Base class for all builtin providers.

    Having this class is necessary in order to maintain
    shared logic among all built-in providers.
    """

    class Meta:
        datafile = "builtin.json"
