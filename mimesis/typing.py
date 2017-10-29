"""
This module is included built in and custom types for type hinting.
This is internal module and you shouldn't use it if you don't know
why you should.
"""
import datetime
from typing import (Any, Callable, Dict, Iterable, List,
                    Union, Mapping, MutableSequence, Tuple)

__all__ = [
    'Any',
    'Array',
    'Dict',
    'Gender',
    'JSON',
    'List',
    'Mapping',
    'Size',
    'Union',
    'Callable',
    'Iterable',
    'Tuple',
    'MutableSequence',
]

JSON = Union[
    Dict[str, Any],
    Any,
]

StrOrInt = Union[str, int]

# Gender can be int and str.
Gender = StrOrInt

Size = StrOrInt

Number = StrOrInt

# Array (instance of array.array)
Array = Union[
    # array.ArrayType can contain float and integer.
    MutableSequence[float],
    MutableSequence[int],
    List[Union[int, float]],
]

# Bytes type
Bytes = bytes

# Datetime
DateTime = Union[datetime.datetime, str]
