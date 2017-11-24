import pytest

from mimesis.builtins import NetherlandsSpecProvider


@pytest.fixture
def nl():
    return NetherlandsSpecProvider()


def test_ssn(nl):
    result = nl.bsn()
    assert result is not None
    assert len(result) == 9
    assert result.isdigit()

    # elaborate way to validate
    test11 = int(result[0:1]) * 9 + \
        int(result[1:2]) * 8 + \
        int(result[2:3]) * 7 + \
        int(result[3:4]) * 6 + \
        int(result[4:5]) * 5 + \
        int(result[5:6]) * 4 + \
        int(result[6:7]) * 3 + \
        int(result[7:8]) * 2 + \
        int(result[8:9]) * -1
    assert test11 % 11 == 0
