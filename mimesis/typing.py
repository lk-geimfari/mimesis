# -*- coding: utf-8 -*-

"""Custom types and shortcuts for annotating Mimesis."""

import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Union

__all__ = [
    "JSON",
    "DateTime",
    "Timestamp",
    "Time",
    "Date",
    "Seed",
    "Matrix",
]

JSON = Dict[str, Any]

DateTime = datetime.datetime

Time = datetime.time

Date = datetime.date

Timestamp = Union[str, int]

Seed = Union[int, str, bytes, bytearray]

KeywordsType = Union[List[str], Set[str]]

Matrix = Union[List[float], List[complex], List[int], List[Decimal]]
