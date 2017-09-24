import pytest

from mimesis.helpers import Random


@pytest.fixture
def random():
    return Random()


def test_randints(random):
    result = random.randints()

    # Length of default list is 3
    assert len(result) == 3

    result_custom = random.randints(25, 1, 1)

    assert len(result_custom) == 25
    # All elements in result_custom equals to 1.
    assert result_custom[0] == 1 and result_custom[-1] == 1


@pytest.mark.parametrize(
    'n', (8, 16, 32, 64),
)
def test_urandom(random, n):
    result = random.urandom(n)

    assert len(result) == n
    assert isinstance(result, bytes)
