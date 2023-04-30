from mimesis.keys import maybe
from mimesis.random import random


def test_maybe():
    key = maybe(None, probability=1)
    assert key("foo", random) is None

    key = maybe(None, probability=0.0)
    assert key("foo", random) is not None
