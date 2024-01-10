"""
This module contains knowledge about the types we use.

Policy
~~~~~~

If any of the following statements is true, move the type to this file:

- if type is used in multiple files
- if type is complex enough it has to be documented
- if type is very important for the public API

"""

import datetime
from decimal import Decimal
from typing import Any, Callable, Final

__all__ = [
    "CallableSchema",
    "Date",
    "DateTime",
    "JSON",
    "Key",
    "Keywords",
    "Matrix",
    "MissingSeed",
    "Seed",
    "Time",
    "Timestamp",
]

JSON = dict[str, Any]

DateTime = datetime.datetime

Time = datetime.time

Date = datetime.date

Timestamp = str | int


class _MissingSeed:
    """We use this type as a placeholder for cases when seed is not set."""


MissingSeed: Final = _MissingSeed()

Seed = None | int | float | str | bytes | bytearray | _MissingSeed

Keywords = list[str] | set[str] | tuple[str, ...]

Number = int | float | complex | Decimal

Matrix = list[list[Number]]

CallableSchema = Callable[[], JSON]

Key = Callable[[Any], Any] | None
