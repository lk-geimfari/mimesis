import re

import pytest

from mimesis import Development, data
from mimesis.enums import DSNType

from . import patterns


class TestDevelopment:
    @pytest.fixture
    def dev(self):
        return Development()

    def test_str(self, dev):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(dev))

    def test_license(self, dev):
        result = dev.software_license()
        assert result in data.LICENSES

    def test_system_quality_attribute(self, dev):
        result = dev.system_quality_attribute()
        assert result in data.SYSTEM_QUALITY_ATTRIBUTES

    def test_ility(self, dev):
        result = dev.ility()
        assert result in data.SYSTEM_QUALITY_ATTRIBUTES

    def test_version(self, dev):
        result = dev.version().split(".")
        result = [int(i) for i in result]

        assert len(result) == 3

        major = result[0]
        assert (major >= 0) and (major <= 11)

        minor = result[1]
        assert (minor >= 0) and (minor <= 11)

        patch = result[2]
        assert (patch >= 0) and (patch <= 11)

        pre_release = dev.version(pre_release=True)
        assert len(pre_release.split(".")) == 4

        # Use calendar versioning
        calver = dev.version(calver=True)
        y, *_ = calver.split(".")
        assert (int(y) >= 2016) and (int(y) <= dev._now.year)

        # Use calendar versioning with pre_release
        calver_pre_release = dev.version(calver=True, pre_release=True)
        y, *_ = calver_pre_release.split(".")
        assert len(calver_pre_release.split(".")) == 4
        assert (int(y) >= 2016) and (int(y) <= dev._now.year)

    def test_programming_language(self, dev):
        result = dev.programming_language()
        assert result in data.PROGRAMMING_LANGS

    def test_os(self, dev):
        result = dev.os()
        assert result in data.OS

    def test_boolean(self, dev):
        result = dev.boolean()
        assert result or (not result)

    @pytest.mark.parametrize(
        "dsn_type",
        [
            DSNType.POSTGRES,
            DSNType.MYSQL,
            DSNType.MONGODB,
            DSNType.REDIS,
            DSNType.COUCHBASE,
            DSNType.MEMCACHED,
            DSNType.RABBITMQ,
        ],
    )
    def test_dsn(self, dev, dsn_type):
        scheme, port = dsn_type.value
        assert dev.dsn(dsn_type=dsn_type).endswith(f":{port}")
        assert dev.dsn(dsn_type=dsn_type).startswith(f"{scheme}://")


class TestSeededDevelopment:
    @pytest.fixture
    def dv1(self, seed):
        return Development(seed=seed)

    @pytest.fixture
    def dv2(self, seed):
        return Development(seed=seed)

    def test_software_license(self, dv1, dv2):
        assert dv1.software_license() == dv2.software_license()

    def test_version(self, dv1, dv2):
        assert dv1.version() == dv2.version()
        assert dv1.version(calver=True, pre_release=True) == dv2.version(
            calver=True, pre_release=True
        )

    def test_programming_language(self, dv1, dv2):
        assert dv1.programming_language() == dv2.programming_language()

    def test_os(self, dv1, dv2):
        assert dv1.os() == dv2.os()

    def test_boolean(self, dv1, dv2):
        assert dv1.boolean() == dv2.boolean()

    def test_dsn(self, dv1, dv2):
        assert dv1.dsn() == dv2.dsn()

    def test_system_quality_attribute(self, dv1, dv2):
        assert dv1.system_quality_attribute() == dv2.system_quality_attribute()

    def test_ility(self, dv1, dv2):
        assert dv1.ility() == dv2.ility()
