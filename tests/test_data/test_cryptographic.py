import re

import pytest

from mimesis import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError

from ._patterns import UUID_REGEX


@pytest.fixture
def crypto():
    return Cryptographic()


def test_uuid(crypto):
    assert re.match(UUID_REGEX, crypto.uuid())


@pytest.mark.parametrize(
    'algorithm, length', [
        (Algorithm.MD5, 32),
        (Algorithm.SHA1, 40),
        (Algorithm.SHA224, 56),
        (Algorithm.SHA256, 64),
        (Algorithm.SHA384, 96),
        (Algorithm.SHA512, 128),
    ],
)
def test_hash(crypto, algorithm, length):
    result = crypto.hash(algorithm=algorithm)
    assert len(result) == length


def test_hash_non_enum(crypto):
    with pytest.raises(NonEnumerableError):
        crypto.hash(algorithm='nil')


def test_bytes(crypto):
    result = crypto.bytes(entropy=64)
    assert result is not None
    assert isinstance(result, bytes)


def test_token(crypto):
    result = crypto.token(entropy=16)

    # Each byte converted to two hex digits.
    assert len(result) == 32
    assert isinstance(result, str)


def test_salt(crypto):
    result = crypto.salt()

    assert result is not None
    assert len(result) == 32


@pytest.mark.parametrize(
    'length', [
        8,
        16,
    ],
)
def test_mnemonic_code(crypto, length):
    result = crypto.mnemonic_phrase(length=length)
    assert isinstance(result, str)
    result = result.split(' ')
    assert len(result) == length
