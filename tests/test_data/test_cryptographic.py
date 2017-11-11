import re

import pytest

from mimesis.exceptions import UnsupportedAlgorithm

from ._patterns import UUID_REGEX


def test_uuid(crypto):
    assert re.match(UUID_REGEX, crypto.uuid())


@pytest.mark.parametrize(
    'algorithm, length', [
        ('md5', 32),
        ('sha1', 40),
        ('sha224', 56),
        ('sha256', 64),
        ('sha384', 96),
        ('sha512', 128),
    ],
)
def test_hash(crypto, algorithm, length):
    result = crypto.hash(algorithm=algorithm)
    assert len(result) == length

    with pytest.raises(UnsupportedAlgorithm):
        crypto.hash(algorithm='mimesis')


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
