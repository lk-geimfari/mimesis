from typing import Dict, List, Union, Mapping, Any

__all__ = ['Any', 'Dict', 'List', 'Union',
           'Mapping', 'Gender', 'JSON', 'Generic']

Generic = Union[str, int, float, bool, None]

JSON = Union[
    Generic,
    Dict[str, Any],
    List[Any],
]

# Gender can be represented as integer (0, 1, 2, 9) like in ISO/IEC 5218
# and as string: ('0', '1', '2', '9', 'female', 'male', 'f', 'm')
Gender = Union[str, int]
