from typing import Any, Callable

from mimesis.random import Random

__all__ = ["maybe"]


def maybe(value: Any, probability: float = 0.5) -> Callable[[Any, Random], Any]:
    """Return a closure (a key function).

    The returned closure itself returns either **value** or
    the first argument passed to closure with a certain probability (0.5 by default).

    :param value: The value that may be returned.
    :param probability: The probability of returning **value**.
    :return: A closure that takes two arguments.
    """

    def key(result: Any, random: Random) -> Any:
        if 0 < probability <= 1:
            value_weight = 1 - probability
            (result,) = random.choices(
                population=[result, value],
                weights=[value_weight, probability],
                k=1,
            )
        return result

    return key
