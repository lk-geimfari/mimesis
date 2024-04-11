import pytest

from mimesis.builtins import DenmarkSpecProvider


@pytest.fixture
def denmark():
    return DenmarkSpecProvider()


@pytest.mark.parametrize(
    "cpr_nr_no_checksum,checksum",
    [
        # Randomly generated CPR numbers and expected checksums
        ("060170000", 10),  # 00 is an invalid serial_number here
        ("260310579", 9),
        ("060558958", 8),
        ("210609428", 7),
        ("171208281", 6),
        ("130208400", 5),
        ("020678688", 4),
        ("050302471", 3),
        ("030670890", 2),
        ("100309468", 1),
        ("250814378", 0),
    ],
)
def test_calculate_checksum(denmark, cpr_nr_no_checksum, checksum):
    assert denmark._calculate_checksum(cpr_nr_no_checksum) == checksum


def test_cpr(denmark):
    cpr_number = denmark.cpr()
    assert cpr_number is not None
    assert len(cpr_number) == 10


@pytest.mark.parametrize(
    "year, expected_values",
    [
        ("1234", TypeError),
        (-1, ValueError),
        (1857, ValueError),
        (1858, [5, 6, 7, 8]),
        (1888, [5, 6, 7, 8]),
        (1900, [0, 1, 2, 3]),
        (1921, [0, 1, 2, 3]),
        (1937, [4, 9]),
        (1942, [4, 9]),
        (1999, [4, 9]),
        (2000, [4, 5, 6, 7, 8, 9]),
        (2021, [4, 5, 6, 7, 8, 9]),
        (2037, ValueError),
        (2222, ValueError),
    ],
)
def test_calculate_century_selector(denmark, year, expected_values):
    if isinstance(expected_values, list):
        assert denmark._calculate_century_selector(year) in expected_values
    else:
        with pytest.raises(expected_values):
            denmark._calculate_century_selector(year)
