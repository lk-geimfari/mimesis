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
from typing import Any, Callable, Dict, List, Set, Tuple, Union

__all__ = [
    "Date",
    "DateTime",
    "JSON",
    "Matrix",
    "Seed",
    "Time",
    "Timestamp",
    "Keywords",
    "SchemaType",
]

JSON = Dict[str, Any]

DateTime = datetime.datetime

Time = datetime.time

Date = datetime.date

Timestamp = Union[str, int]

Seed = Union[None, int, float, str, bytes, bytearray]

Keywords = Union[List[str], Set[str], Tuple[str, ...]]

Matrix = Union[
    List[int],
    List[float],
    List[complex],
    List[Decimal],
]

SchemaType = Callable[[], JSON]
