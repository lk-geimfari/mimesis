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
