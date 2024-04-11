import datetime
import re

import pytest

from mimesis import Development, datasets

from . import patterns


class TestDevelopment:
    @pytest.fixture
    def dev(self):
        return Development()

    def test_str(self, dev):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(dev))

    def test_license(self, dev):
        result = dev.software_license()
        assert result in datasets.LICENSES

    def test_system_quality_attribute(self, dev):
        result = dev.system_quality_attribute()
        assert result in datasets.SYSTEM_QUALITY_ATTRIBUTES

    def test_ility(self, dev):
        result = dev.ility()
        assert result in datasets.SYSTEM_QUALITY_ATTRIBUTES

    def test_version(self, dev):
        result = dev.version().split(".")
        result = [int(i) for i in result]

        assert len(result) == 3

        for part in result:
            assert (part >= 0) and (part <= 100)

    def test_calver(self, dev):
        calver = dev.calver()
        year = calver.split(".")[0]
        assert (int(year) >= 2016) and (int(year) <= datetime.datetime.now().year)

    def test_stage(self, dev):
        assert dev.stage() in datasets.STAGES

    def test_programming_language(self, dev):
        result = dev.programming_language()
        assert result in datasets.PROGRAMMING_LANGS

    def test_os(self, dev):
        result = dev.os()
        assert result in datasets.OS

    def test_boolean(self, dev):
        result = dev.boolean()
        assert result or (not result)


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

    def test_calver(self, dv1, dv2):
        assert dv1.calver() == dv2.calver()

    def test_stage(self, dv1, dv2):
        assert dv1.stage() == dv2.stage()

    def test_programming_language(self, dv1, dv2):
        assert dv1.programming_language() == dv2.programming_language()

    def test_os(self, dv1, dv2):
        assert dv1.os() == dv2.os()

    def test_boolean(self, dv1, dv2):
        assert dv1.boolean() == dv2.boolean()

    def test_system_quality_attribute(self, dv1, dv2):
        assert dv1.system_quality_attribute() == dv2.system_quality_attribute()

    def test_ility(self, dv1, dv2):
        assert dv1.ility() == dv2.ility()
