"""Provides a random choice from items in a sequence."""
import typing as t

from mimesis.providers.base import BaseProvider

__all__ = ["Choice"]


class Choice(BaseProvider):
    """Class for generating a random choice from items in a sequence."""

    class Meta:
        name = "choice"

    def choice(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Choice random item form sequence.

        See https://github.com/lk-geimfari/mimesis/issues/619

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: Sequence or uncontained element randomly chosen from items.
        """
        return self.__call__(*args, **kwargs)

    def __call__(
        self,
        items: t.Sequence[t.Any] | None,
        length: int = 0,
        unique: bool = False,
    ) -> t.Sequence[t.Any] | t.Any:
        """Generates a randomly chosen sequence or bare element from a sequence.

        Provide elements randomly chosen from the elements in a sequence
        **items**, where when **length** is specified the random choices are
        contained in a sequence of the same type of length **length**,
        otherwise a single uncontained element is chosen. If **unique** is set
        to True, constrain a returned sequence to contain only unique elements.

        :param items: Non-empty sequence (list, tuple or string) of elements.
        :param length: Length of the sequence (number of elements) to provide.
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

        if not isinstance(items, t.Sequence):
            raise TypeError("**items** must be non-empty sequence.")

        if not items:
            raise ValueError("**items** must be a non-empty sequence.")

        if length < 0:
            raise ValueError("**length** should be a positive integer.")

        if length == 0:
            return self.random.choice(items)

        if unique and len(set(items)) < length:
            raise ValueError(
                "There are not enough unique elements in "
                "**items** to provide the specified **number**."
            )
        if unique:
            data: list[str] = self.random.sample(list(set(items)), k=length)
        else:
            data = self.random.choices(items, k=length)

        if isinstance(items, list):
            return data
        elif isinstance(items, tuple):
            return tuple(data)
        return "".join(data)
