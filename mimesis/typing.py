"""Custom types and shortcuts for annotating Mimesis."""

import datetime
from typing import Any, Dict, Union

__all__ = [
    'JSON',
    'Size',
    'Bytes',
    'DateTime',
    'Timestamp',
    'Seed',
]

JSON = Union[
    Dict[Any, Any],
    Any,
]

_StrOrInt = Union[str, int]

Size = _StrOrInt

Bytes = bytes

DateTime = Union[datetime.datetime, Any]

Timestamp = _StrOrInt

Seed = Union[int, str, bytes, bytearray]
