import re

import pytest

from mimesis import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError

from ._patterns import UUID_REGEX


@pytest.fixture
def crypto():
    return Cryptographic()


@pytest.fixture
def _seeded_crypto():
    return Cryptographic(seed=42)


def test_uuid(crypto):
    assert re.match(UUID_REGEX, crypto.uuid())


def test_seeded_uuid(_seeded_crypto):
    result = _seeded_crypto.uuid()
    assert result == 'bdd640fb-0667-1ad1-1c80-317fa3b1799d'
    result = _seeded_crypto.uuid()
    assert result == '23b8c1e9-3924-56de-3eb1-3b9046685257'


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


# TODO: https://github.com/lk-geimfari/mimesis/issues/325#issuecomment-352364359
def skip_test_seeded_hash(_seeded_crypto):
    result = _seeded_crypto.hash(algorithm=Algorithm.SHA512)
    assert result == '6f7ffaf8fe3e6c87855a3463e4cf218c7093f1cbc523e6f55b8298' \
                     '72cc428e1c3e3280a70c6fbb01352247e7663f018bf515e465716f' \
                     '616bbb63f24b6bdee9df'
    result = _seeded_crypto.hash()
    assert result == '093663e794b058987a9f8bbbdb978bc92659a510a5357923205dec93'
    result = _seeded_crypto.hash()
    assert result == '47a130c4a09e97e54deac6dd40e86b58'


def test_hash_non_enum(crypto):
    with pytest.raises(NonEnumerableError):
        crypto.hash(algorithm='nil')


def test_bytes(crypto):
    result = crypto.bytes(entropy=64)
    assert result is not None
    assert isinstance(result, bytes)


def test_seeded_bytes(_seeded_crypto):
    result = _seeded_crypto.bytes(entropy=16)
    assert result == b'\xa3\x1c\x06\xbdF>9#\xbc\x1a\xad\xbd\xe4\x8b\x16\x97'
    result = _seeded_crypto.bytes()
    assert result == b'l\x08\x07\x177;\x81\x9a\x06\x8f2\xb7\xa6\xb3\x8bk8r' \
                     b'\x96G\xcf\xde\x01\xc2\xce(\xb2lWG\'7'
    result = _seeded_crypto.bytes()
    assert result == b'\xf5\xc3V\x1a\x17a\x18[\xd8X\x9aC\xce\x0b\xbau\x89' \
                     b'\x1f\xf9\xec`\x14\x8dK\xd4\xa0\x9e\xe2\xdc\\\x931'


def test_token(crypto):
    result = crypto.token(entropy=16)

    # Each byte converted to two hex digits.
    assert len(result) == 32
    assert isinstance(result, str)


def test_seeded_token(_seeded_crypto):
    result = _seeded_crypto.token(entropy=16)
    assert result == 'a31c06bd463e3923bc1aadbde48b1697'
    result = _seeded_crypto.token()
    assert result == '6c080717373b819a068f32b7a6b38b6b' \
                     '38729647cfde01c2ce28b26c57472737'
    result = _seeded_crypto.token()
    assert result == 'f5c3561a1761185bd8589a43ce0bba75' \
                     '891ff9ec60148d4bd4a09ee2dc5c9331'


def test_salt(crypto):
    result = crypto.salt()

    assert result is not None
    assert len(result) == 32


def test_seeded_salt(_seeded_crypto):
    result = _seeded_crypto.salt()
    assert result == 'bdd640fb06674ad19c80317fa3b1799d'
    result = _seeded_crypto.salt()
    assert result == '23b8c1e9392446debeb13b9046685257'


@pytest.mark.parametrize(
    'length', [
        8,
        16,
    ],
)
def test_mnemonic_code(crypto, length):
    result = crypto.mnemonic_code(length=length)
    assert isinstance(result, str)
    result = result.split(' ')
    assert len(result) == length


def test_seeded_mnemonic_code(_seeded_crypto):
    result = _seeded_crypto.mnemonic_code(length=6)
    assert result == 'limousines profiles protect captain agricultural ready'
    result = _seeded_crypto.mnemonic_code()
    assert result == 'tired wise delivered moon lbs summit highlights key ' \
                     'bike photo won diameter'
    result = _seeded_crypto.mnemonic_code()
    assert result == 'lack sponsored soap moderate us wright junior ' \
                     'collaboration virgin twin concept determination'
