"""
This module contains knowledge about the types we use.

Policy
~~~~~~

If any of the following statements is true, move the type to this file:

- if a type is used in multiple files
- if a type is complex enough it has to be documented
- if a type is very important for the public API

"""

import datetime
from collections.abc import Callable
from decimal import Decimal
from typing import Any, Final


__all__ = [
    "JSON",
    "CallableSchema",
    "Date",
    "DateTime",
    "Key",
    "KeyFunc",
    "Keywords",
    "Matrix",
    "MissingSeed",
    "Number",
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

CallableSchema = Callable[[], JSON | None]

# One-arg keys, or two-arg keys that also receive Random.
KeyFunc = Callable[[Any], Any] | Callable[[Any, Any], Any]
Key = KeyFunc | None
