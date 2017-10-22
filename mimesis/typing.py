"""
This module is included built in and custom types for type hinting.
This is internal module and you shouldn't use it if you don't know
why you should.
"""

from typing import Any, Dict, List, Union, Mapping

__all__ = [
    'Any',
    'Dict',
    'Gender',
    'Generic',
    'JSON',
    'List',
    'Mapping',
    'Union',
]

Generic = Union[str, int, float, bool, None]

JSON = Union[
    Generic,
    Dict[str, Any],
    List[Any],
]

# Gender can be represented as integer (0, 1, 2, 9) like in ISO/IEC 5218
# and as string: ('0', '1', '2', '9', 'female', 'male', 'f', 'm')
Gender = Union[str, int]
