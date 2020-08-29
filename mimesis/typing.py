# -*- coding: utf-8 -*-

"""Custom types and shortcuts for annotating Mimesis."""

import datetime
from typing import Any, Callable, Dict, Union

__all__ = [
    'JSON',
    'DateTime',
    'Timestamp',
    'Time',
    'Date',
    'SchemaType',
    'Seed',
]

JSON = Dict[str, Any]

DateTime = datetime.datetime

Time = datetime.time

Date = datetime.date

Timestamp = Union[str, int]

Seed = Union[int, str, bytes, bytearray]

SchemaType = Callable[[], JSON]
