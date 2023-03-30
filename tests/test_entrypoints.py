"""Ensure that integrations work as planned."""

from mimesis import random
from mimesis.types import MissingSeed


def test_pytest_randomly(pytestconfig):
    try:
        randomly_seed = pytestconfig.getoption("randomly_seed")
    except ValueError:
        # Uninstall `pytest-randomly` to trigger this error.
        randomly_seed = MissingSeed

    assert random.global_seed == randomly_seed
