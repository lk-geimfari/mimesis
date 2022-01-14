"""Base specific data provider."""
from typing import Any

from mimesis.providers import BaseDataProvider

__all__ = ["BaseSpecProvider"]


class BaseSpecProvider(BaseDataProvider):
    """Base provider for specific data providers."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes of superclass."""
        super().__init__(*args, **kwargs)
        self._datafile = "builtin.json"
