import re
import uuid

import pytest

from mimesis import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestCryptographic(object):

    @pytest.fixture
    def crypto(self):
        return Cryptographic()

    def test_str(self, crypto):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(crypto))

    @pytest.mark.parametrize(
        'as_object', [
            True,
            False,
        ],
    )
    def test_uuid(self, crypto, as_object):
        uuid_result = crypto.uuid(as_object=as_object)
        if as_object:
            assert isinstance(uuid_result, uuid.UUID)
        else:
            assert re.match(patterns.UUID_REGEX, crypto.uuid(as_object))

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
    def test_hash(self, crypto, algorithm, length):
        result = crypto.hash(algorithm=algorithm)
        assert len(result) == length

    def test_hash_non_enum(self, crypto):
        with pytest.raises(NonEnumerableError):
            crypto.hash(algorithm='nil')

    @pytest.mark.parametrize('entropy', [32, 64, 128])
    def test_token_bytes(self, crypto, entropy):
        result = crypto.token_bytes(entropy=entropy)
        assert len(result) == entropy
        assert isinstance(result, bytes)

    @pytest.mark.parametrize('entropy', [32, 64, 128])
    def test_token_hex(self, crypto, entropy):
        result = crypto.token_hex(entropy=entropy)
        # Each byte converted to two hex digits.
        assert len(result) == entropy * 2
        assert isinstance(result, str)

    @pytest.mark.parametrize('entropy', [32, 64, 128])
    def test_token_urlsafe(self, crypto, entropy):
        result = crypto.token_urlsafe(entropy=entropy)
        assert len(result) > entropy
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        'length, separator', [
            (8, None),
            (16, ' - '),
            (16, '_'),
        ],
    )
    def test_mnemonic_phrase(self, crypto, length, separator):
        if not separator:
            separator = ' '

        result = crypto.mnemonic_phrase(length=length, separator=separator)
        assert isinstance(result, str)
        assert len(result.split(separator)) == length
        assert separator in result


class TestSeededCryptographic(object):

    @pytest.fixture
    def c1(self, seed):
        return Cryptographic(seed=seed)

    @pytest.fixture
    def c2(self, seed):
        return Cryptographic(seed=seed)

    def test_uuid(self, c1, c2):
        assert c1.uuid() != c2.uuid()

    def test_hash(self, c1, c2):
        assert c1.hash() != c2.hash()
        assert c1.hash(algorithm=Algorithm.SHA512) != \
               c2.hash(algorithm=Algorithm.SHA512)

    def test_mnemonic_phrase(self, c1, c2):
        assert c1.mnemonic_phrase() == c2.mnemonic_phrase()
        assert c1.mnemonic_phrase(length=16, separator=' | ') == \
               c2.mnemonic_phrase(length=16, separator=' | ')
