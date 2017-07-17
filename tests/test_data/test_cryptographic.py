import re

import pytest

from mimesis.exceptions import UnsupportedAlgorithm

from ._patterns import UUID_REGEX


def test_uuid(crypto):
    assert re.match(UUID_REGEX, crypto.uuid())


def test_hash(crypto):
    assert len(crypto.hash(algorithm='md5')) == 32
    assert len(crypto.hash(algorithm='sha1')) == 40
    assert len(crypto.hash(algorithm='sha224')) == 56
    assert len(crypto.hash(algorithm='sha256')) == 64
    assert len(crypto.hash(algorithm='sha384')) == 96
    assert len(crypto.hash(algorithm='sha512')) == 128

    with pytest.raises(UnsupportedAlgorithm):
        crypto.hash(algorithm='mimesis')


def test_bytes(crypto):
    assert crypto.bytes(entropy=64) is not None
    assert isinstance(crypto.bytes(entropy=64), bytes)


def test_token(crypto):
    # Each byte converted to two hex digits.
    assert len(crypto.token(entropy=16)) == 32
    assert isinstance(crypto.token(), str)
