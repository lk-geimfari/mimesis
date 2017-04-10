import pytest
import re

from elizabeth.builtins.en import USASpecProvider


@pytest.fixture
def usa():
    return USASpecProvider()


def test_usps_tracking_number(usa):
    result = usa.tracking_number(service='usps')
    assert result is not None
    assert len(result) == 24 or len(result) == 17

    result_1 = usa.tracking_number(service='fedex')
    assert result_1 is not None
    assert len(result_1) == 14 or len(result_1) == 18

    result_2 = usa.tracking_number(service='ups')
    assert result_2 is not None
    assert len(result_2) == 18

    with pytest.raises(ValueError):
        usa.tracking_number(service='x')


def test_personality(usa):
    result = usa.personality(category='rheti')
    assert int(result) <= 9 or int(result) >= 1

    result_1 = usa.personality(category='mbti')
    assert isinstance(result_1, str)
    assert len(result_1) == 4
    assert result_1.isupper()


def test_ssn(usa):
    result = usa.ssn()
    assert result is not None
    # todo fix so this actually checks that 666 prefix can never be returned
    assert '666' != result[:3]
    assert re.match('^\d{3}-\d{2}-\d{4}$', result)

    assert result.replace('-', '').isdigit()
    assert len(result.replace('-', '')) == 9
