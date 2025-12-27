import base64
import json
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

    def test_jwt_default(self, crypto):
        result = crypto.jwt()
        assert isinstance(result, str)

        # JWT should have 3 parts separated by dots
        parts = result.split(".")
        assert len(parts) == 3

        # Decode and verify header
        header_json = base64.urlsafe_b64decode(parts[0] + "==")
        header = json.loads(header_json)
        assert header["alg"] == "HS256"
        assert header["typ"] == "JWT"

        # Decode and verify payload has expected fields
        payload_json = base64.urlsafe_b64decode(parts[1] + "==")
        payload = json.loads(payload_json)
        assert "sub" in payload
        assert "name" in payload
        assert "iat" in payload
        assert "exp" in payload
        assert payload["name"] == "Test User"

    @pytest.mark.parametrize(
        "algorithm",
        [
            "HS256",
            "HS384",
            "HS512",
            "RS256",
            "RS384",
            "RS512",
            "ES256",
            "ES384",
            "ES512",
        ],
    )
    def test_jwt_with_algorithm(self, crypto, algorithm):
        result = crypto.jwt(algorithm=algorithm)
        assert isinstance(result, str)

        parts = result.split(".")
        assert len(parts) == 3

        # Verify algorithm in header
        header_json = base64.urlsafe_b64decode(parts[0] + "==")
        header = json.loads(header_json)
        assert header["alg"] == algorithm

    @pytest.mark.parametrize(
        "payload",
        [
            {"user_id": 123, "role": "admin"},
            {"sub": "user@example.com", "permissions": ["read", "write"]},
            {"custom_field": "value", "nested": {"key": "value"}},
            {"empty": None, "bool": True, "number": 42},
        ],
    )
    def test_jwt_with_custom_payload(self, crypto, payload):
        result = crypto.jwt(payload=payload)
        assert isinstance(result, str)

        parts = result.split(".")
        assert len(parts) == 3

        payload_json = base64.urlsafe_b64decode(parts[1] + "==")
        decoded_payload = json.loads(payload_json)
        assert decoded_payload == payload

    def test_jwt_structure(self, crypto):
        result = crypto.jwt()

        # Should be base64url encoded
        parts = result.split(".")
        for part in parts[:2]:
            assert all(c.isalnum() or c in "-_" for c in part)

    @pytest.mark.parametrize(
        "prefix, length, fmt, expected_min_length",
        [
            ("", 32, "hex", 32),
            ("sk_", 32, "hex", 35),
            ("pk_", 32, "hex", 35),
            ("api_", 32, "hex", 36),
            ("", 64, "hex", 64),
            ("test_", 16, "hex", 21),
            ("", 32, "base64", 32),
            ("sk_", 32, "base64", 35),
            ("pk_", 48, "base64", 51),
        ],
    )
    def test_api_key(self, crypto, prefix, length, fmt, expected_min_length):
        result = crypto.api_key(prefix=prefix, length=length, fmt=fmt)
        assert isinstance(result, str)

        if prefix:
            assert result.startswith(prefix)

        assert len(result) >= expected_min_length

        key_part = result[len(prefix):] if prefix else result
        if fmt == "hex":
            assert all(c in "0123456789abcdef" for c in key_part)
        elif fmt == "base64":
            assert all(c.isalnum() or c in "-_" for c in key_part)

    def test_api_key_default(self, crypto):
        result = crypto.api_key()
        assert isinstance(result, str)
        assert len(result) == 32
        assert all(c in "0123456789abcdef" for c in result)

    def test_api_key_invalid_format(self, crypto):
        with pytest.raises(ValueError, match="Unknown format"):
            crypto.api_key(fmt="invalid")

    @pytest.mark.parametrize(
        "algorithm, expected_length, expected_colons",
        [
            ("sha256", 95, 31),  # 32 bytes = 64 hex chars + 31 colons = 95 total
            ("sha1", 59, 19),    # 20 bytes = 40 hex chars + 19 colons = 59 total
        ],
    )
    def test_certificate_fingerprint(self, crypto, algorithm, expected_length, expected_colons):
        result = crypto.certificate_fingerprint(algorithm=algorithm)
        assert isinstance(result, str)
        assert len(result) == expected_length

        # Check format: colon-separated hex pairs
        parts = result.split(":")
        assert len(parts) == expected_colons + 1

        # Each part should be 2 uppercase hex characters
        for part in parts:
            assert len(part) == 2
            assert all(c in "0123456789ABCDEF" for c in part)

    def test_certificate_fingerprint_default(self, crypto):
        result = crypto.certificate_fingerprint()
        assert isinstance(result, str)
        assert len(result) == 95  # 32 bytes * 2 hex chars + 31 colons
        assert result.count(":") == 31

    def test_certificate_fingerprint_invalid_algorithm(self, crypto):
        with pytest.raises(ValueError, match="Unknown algorithm"):
            crypto.certificate_fingerprint(algorithm="invalid")

    def test_certificate_fingerprint_format(self, crypto):
        result = crypto.certificate_fingerprint()
        pattern = r"^([0-9A-F]{2}:)*[0-9A-F]{2}$"
        assert re.match(pattern, result)


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

    def test_jwt(self, c1, c2):
        assert c1.jwt() == c2.jwt()
        assert c1.jwt(algorithm="RS256") == c2.jwt(algorithm="RS256")

    def test_jwt_with_payload(self, c1, c2):
        payload = {"user_id": 123, "role": "admin"}
        assert c1.jwt(payload=payload) == c2.jwt(payload=payload)

    def test_api_key(self, c1, c2):
        assert c1.api_key() == c2.api_key()
        assert c1.api_key(prefix="sk_") == c2.api_key(prefix="sk_")
        assert c1.api_key(length=64, fmt="base64") == c2.api_key(length=64, fmt="base64")

    def test_certificate_fingerprint(self, c1, c2):
        assert c1.certificate_fingerprint() == c2.certificate_fingerprint()
        assert c1.certificate_fingerprint(algorithm="sha1") == c2.certificate_fingerprint(algorithm="sha1")
