"""Custom types and shortcuts for annotating Mimesis."""

import datetime
from typing import Any, Dict, Union

__all__ = [
    'JSON',
    'Bytes',
    'DateTime',
    'Timestamp',
    'Time',
    'Date',
    'Seed',
]

JSON = Dict[str, Any]

_StrOrInt = Union[str, int]

Bytes = bytes

DateTime = datetime.datetime

Time = datetime.time

Date = datetime.date

Timestamp = _StrOrInt

Seed = Union[int, str, bytes, bytearray]
