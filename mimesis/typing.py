"""
Custom types and shortcuts for annotating Mimesis.
Otherwise, simply import the types you need at the top of each file.
"""

import datetime
from typing import Any, Dict, Union

__all__ = [
    'JSON',
    'Size',
    'Bytes',
    'DateTime',
    'Timestamp',
]

JSON = Union[
    Dict[Any, Any],
    Any,
]

_StrOrInt = Union[str, int]

Size = _StrOrInt

Number = _StrOrInt

Bytes = bytes

DateTime = Union[datetime.datetime, Any]

Timestamp = _StrOrInt
