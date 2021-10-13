# -*- coding: utf-8 -*-

"""Provides a sequence of random choices from items in a sequence."""
import collections.abc
from typing import Any, Final, List, Optional, Sequence, Union

from mimesis.providers.base import BaseProvider

__all__ = ["Choices"]


class Choices(BaseProvider):
    """Class for generating a random sequence from items in a sequence."""

    class Meta:
        """Class for metadata."""

        name: Final[str] = "choices"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def __call__(
        self,
        items: Optional[Sequence[Any]],
        weights: Optional[Sequence[float]] = None,
        length: int = 1,
        unique: bool = False,
    ) -> Union[Sequence[Any], Any]:
        """Generate a randomly-chosen sequence from a sequence.

        Provide elements randomly chosen from the elements in a sequence
        **items**, where selections are made accoding to the relative weights and
        when **length** is specified the random choices are
        contained in a sequence of the same type of length **length**.
        If **unique** is set to True, constrain a returned sequence to contain
        only unique elements.

        :param items: Non-empty sequence (list, tuple or string) of elements.
        :param weights: Non-empty sequence (list or tuple) of floats.
        :param length: Length of sequence (number of elements) to provide.
        :param unique: If True, ensures provided elements are unique.
        :return: Sequence or uncontained element randomly chosen from items.
        :raises TypeError: For non-sequence items or non-integer length.
        :raises ValueError: If negative length or insufficient unique elements.

        >>> from mimesis import Choices
        >>> choices = Choices()
        >>> choices(items=['a', 'b', 'c'])
        ['c']
        >>> choices(items=['a', 'b', 'c'], length=1)
        ['a']
        >>> choices(items='abc', length=2)
        'ba'
        >>> choices(items=('a', 'b', 'c'), length=5)
        ('c', 'a', 'a', 'b', 'c')
        >>> choices(items='aabbbccccddddd', length=4, unique=True)
        'cdba'
        >>> choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [8, 3, 9, 2, 10, 1, 8, 3, 9, 2], length=5)
        [2, 8, 5, 7, 5]
        >>> choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [8, 3, 9, 2, 10, 1, 8, 3, 9, 2], length=5, unique=True)
        [5, 9, 7, 3, 1]
        """

        if not isinstance(items, collections.abc.Sequence):
            raise TypeError("**items** must be non-empty sequence.")

        if not items:
            raise ValueError("**items** must be a non-empty sequence.")

        if length < 0:
            raise ValueError("**length** should be a positive integer.")

        data: List[str] = []
        if unique and len(set(items)) < length:  # avoid an infinite while loop
            raise ValueError(
                "There are not enough unique elements in "
                "**items** to provide the specified **number**."
            )
        if unique:
            while len(data) < length:
                (item,) = self.random.choices(items, weights, k=1)
                if unique and item not in data:
                    data.append(item)
        else:
            data = self.random.choices(items, weights, k=length)

        if isinstance(items, list):
            return data
        elif isinstance(items, tuple):
            return tuple(data)
        return "".join(data)
