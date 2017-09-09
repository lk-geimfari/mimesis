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
    assert len(crypto.hash(algorithm=algorithm)) == length

    with pytest.raises(UnsupportedAlgorithm):
        crypto.hash(algorithm='mimesis')


def test_bytes(crypto):
    assert crypto.bytes(entropy=64) is not None
    assert isinstance(crypto.bytes(entropy=64), bytes)


def test_token(crypto):
    # Each byte converted to two hex digits.
    assert len(crypto.token(entropy=16)) == 32
    assert isinstance(crypto.token(), str)
