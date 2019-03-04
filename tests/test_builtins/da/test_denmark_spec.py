import pytest

from mimesis.builtins import DenmarkSpecProvider


@pytest.fixture
def denmark():
    return DenmarkSpecProvider()


def test_cpr(denmark):
    cpr_number = denmark.cpr()
    assert cpr_number is not None
    assert len(cpr_number) == 10
