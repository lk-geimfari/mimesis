import re
import uuid

import pytest

from mimesis import Cryptographic
from mimesis.enums import Algorithm
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestCryptographic:
    @pytest.fixture
    def crypto(self):
        return Cryptographic()

    def test_str(self, crypto):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(crypto))

    def test_uuid_object(self, crypto):
        assert isinstance(crypto.uuid_object(), uuid.UUID)

    def test_uuid(self, crypto):
        uuid_result = crypto.uuid()
        assert isinstance(uuid_result, str)
        assert re.match(patterns.UUID_REGEX, uuid_result)

    @pytest.mark.parametrize(
        "algorithm, length",
        [
            (Algorithm.MD5, 32),
            (Algorithm.SHA1, 40),
            (Algorithm.SHA224, 56),
            (Algorithm.SHA256, 64),
            (Algorithm.SHA384, 96),
            (Algorithm.SHA512, 128),
            (Algorithm.BLAKE2S, 64),
            (Algorithm.BLAKE2B, 128),
        ],
    )
    def test_hash(self, crypto, algorithm, length):
        result = crypto.hash(algorithm=algorithm)
        assert len(result) == length

    def test_hash_non_enum(self, crypto):
        with pytest.raises(NonEnumerableError):
            crypto.hash(algorithm="nil")

    @pytest.mark.parametrize("entropy", [32, 64, 128])
    def test_token_bytes(self, crypto, entropy):
        result = crypto.token_bytes(entropy=entropy)
        assert len(result) == entropy
        assert isinstance(result, bytes)

    @pytest.mark.parametrize("entropy", [32, 64, 128])
    def test_token_hex(self, crypto, entropy):
        result = crypto.token_hex(entropy=entropy)
        # Each byte converted to two hex digits.
        assert len(result) == entropy * 2
        assert isinstance(result, str)

    @pytest.mark.parametrize("entropy", [32, 64, 128])
    def test_token_urlsafe(self, crypto, entropy):
        result = crypto.token_urlsafe(entropy=entropy)
        assert len(result) > entropy
        assert isinstance(result, str)

    def test_mnemonic_phrase(self, crypto):
        result = crypto.mnemonic_phrase()
        assert isinstance(result, str)
        phrase_len = len(result.split(" "))
        assert phrase_len == 12 or phrase_len == 24


class TestSeededCryptographic:
    @pytest.fixture
    def c1(self, seed):
        return Cryptographic(seed=seed)

    @pytest.fixture
    def c2(self, seed):
        return Cryptographic(seed=seed)

    def test_hash(self, c1, c2):
        assert c1.hash() == c2.hash()
        assert c1.hash(algorithm=Algorithm.SHA512) == c2.hash(
            algorithm=Algorithm.SHA512
        )

    def test_mnemonic_phrase(self, c1, c2):
        assert c1.mnemonic_phrase() == c2.mnemonic_phrase()
