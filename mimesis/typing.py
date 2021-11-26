# -*- coding: utf-8 -*-

"""Custom types and shortcuts for annotating Mimesis."""

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
