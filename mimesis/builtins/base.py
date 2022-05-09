"""Base specific data provider."""
import typing as t

from mimesis.providers import BaseDataProvider

__all__ = ["BaseSpecProvider"]


class BaseSpecProvider(BaseDataProvider):
    """Base provider for specific data providers."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes of superclass."""
        super().__init__(*args, **kwargs)
        self._datafile = "builtin.json"
