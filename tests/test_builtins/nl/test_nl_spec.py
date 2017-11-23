import pytest

from mimesis.builtins import NLSpecProvider


@pytest.fixture
def nl():
    return NLSpecProvider()


def test_ssn(nl):
    result = nl.bsn()
    assert result is not None
    assert len(result) == 9
    assert result.isdigit()

    test11 = result[0:1] * 9 + \
             result[1:2] * 8 + \
             result[2:3] * 7 + \
             result[3:4] * 6 + \
             result[4:5] * 5 + \
             result[5:6] * 4 + \
             result[6:7] * 3 + \
             result[7:8] * 2 + \
             result[8:9] * -1
    assert test11 % 11 == 0
