"""Integrations with other tools that use entrypoints."""

from mimesis import random


def pytest_randomly_reseed(seed: int) -> None:
    """
    This function is called by `pytest-randomly` during `pytest` setup.

    It sets the global seed for every provider / field.
    You can still modify the seed with `.reseed()` calls if needed.
    """
    random.global_seed = seed
