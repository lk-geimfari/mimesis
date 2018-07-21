from random import Random
from typing import Any, Optional, Sequence, Union

from mimesis.typing import Seed

__all__ = ['Choice']


class Choice(object):
    """An object which provides randomly choosing elements."""

    def __init__(self, seed: Optional[Seed] = None) -> None:
        """Initialize choice object.

        :param seed: Seed for random.
        """
        self.random = Random()

        if seed is not None:
            self.random.seed = seed  # type: ignore

    def __call__(self, items: Optional[Sequence] = None, number: int = 1,
                 unique: bool = False) -> Union[Sequence[Any], Any]:
        """Override standard call.

        It takes a sequence of elements and randomly returns **number**
        of elements from the passed sequence.

        :param items: Sequence of elements.
        :param number: Number of elements to return
        :param unique: Only unique elements.
        :return: New sequence of elements randomly selected from **items**.
        """
        if items:
            if number > 1:
                data = []  # type: ignore
                for _ in range(number):
                    item = self.random.choice(items)
                    if unique:
                        if item not in data:
                            data.append(item)
                    else:
                        data.append(item)
                return data

            return self.random.choice(items)
        return items
