from typing import Optional

from mimesis.helpers import Random


class BaseSpecProvider(object):
    def __init__(self, seed: Optional[int] = None) -> None:
        self.seed = seed
        self.random = Random()

        if seed is not None:
            self.random.seed(seed)
