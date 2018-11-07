"""Provides a random choice from items in a sequence."""

from typing import Any, Optional, Sequence, Union

from mimesis.providers.base import BaseProvider

__all__ = ['Choice']


class Choice(BaseProvider):
    """Class for generating a random choice from items in a sequence."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def __call__(self, items: Optional[Sequence[Any]], length: int = 0,
                 unique: bool = False) -> Union[Sequence[Any], Any]:
        """Generate a randomly-chosen sequence or bare element from a sequence.

        Provide elements randomly chosen from the elements in a sequence
        **items**, where when **length** is specified the random choices are
        contained in a sequence of the same type of length **length**,
        otherwise a single uncontained element is chosen. If **unique** is set
        to True, constrain a returned sequence to contain only unique elements.

        :param items: Non-empty sequence (list, tuple or string) of elements.
        :param length: Length of sequence (number of elements) to provide.
        :param unique: If True, ensures provided elements are unique.
        :return: Sequence or uncontained element randomly chosen from items.
        :raises TypeError: For non-sequence items or non-integer length.
        :raises ValueError: If negative length or insufficient unique elements.

        >>> from mimesis import Choice
        >>> choice = Choice()

        >>> choice(items=['a', 'b', 'c'])
        'c'
        >>> choice(items=['a', 'b', 'c'], length=1)
        ['a']
        >>> choice(items='abc', length=2)
        'ba'
        >>> choice(items=('a', 'b', 'c'), length=5)
        ('c', 'a', 'a', 'b', 'c')
        >>> choice(items='aabbbccccddddd', length=4, unique=True)
        'cdba'
        """
        # Ensure valid type and value for inputs
        if not (isinstance(items, (list, tuple, str)) and
                isinstance(length, int)):
            raise TypeError('List, tuple or string **items** and integer '
                            '**number** required.')
        # Technically allow length=0 input, but apply as default for 'not set'
        elif len(items) == 0 or length < 0:
            raise ValueError('**Items** must be a non-empty sequence and '
                             '**number** should be a positive integer.')

        if length == 0:  # else hereafter number >= 1 from constraints above
            return self.random.choice(items)

        # Process result as list then convert back to original type if non-list
        data = []  # type: ignore
        if unique and len(set(items)) < length:  # avoid an infinite while loop
            raise ValueError('There are not enough unique elements in '
                             '**items** to provide the specified **number**.')
        while len(data) < length:
            item = self.random.choice(items)
            if (unique and item not in data) or not unique:
                data.append(item)
        if isinstance(items, list):
            return data
        elif isinstance(items, tuple):
            return tuple(data)
        else:
            return ''.join(data)
