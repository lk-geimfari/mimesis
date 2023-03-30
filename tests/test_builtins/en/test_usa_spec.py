import re

import pytest

from mimesis.builtins import USASpecProvider


@pytest.fixture
def usa():
    return USASpecProvider()


@pytest.mark.parametrize(
    "service, length",
    [
        ("usps", 24),
        ("fedex", 18),
        ("ups", 18),
    ],
)
def test_usps_tracking_number(usa, service, length):
    result = usa.tracking_number(service=service)
    assert result is not None
    assert len(result) <= length

    with pytest.raises(ValueError):
        usa.tracking_number(service="x")


def test_ssn(usa, mocker):
    result = usa.ssn()
    assert result is not None
    assert "666" != result[:3]
    assert re.match(r"^\d{3}-\d{2}-\d{4}$", result)
    assert result.replace("-", "").isdigit()
    assert len(result.replace("-", "")) == 9

    mocker.patch.object(usa.random, "randint", return_value=666)
    result = usa.ssn()
    assert "665" == result[:3]
