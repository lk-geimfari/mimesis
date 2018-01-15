# -*- coding: utf-8 -*-

import pytest

from mimesis import Development, data


class TestDevelopment(object):
    @pytest.fixture
    def dev(self):
        return Development()

    def test_license(self, dev):
        result = dev.software_license()
        assert result in data.LICENSES

    def test_version_control_system(self, dev):
        vcs = ['Git', 'Subversion']
        assert dev.version_control_system() in vcs

    def test_version(self, dev):
        result = dev.version().split('.')

        result = [int(i) for i in result]

        assert len(result) == 3

        major = result[0]
        assert (major >= 0) and (major <= 11)

        minor = result[1]
        assert (minor >= 0) and (minor <= 11)

        patch = result[2]
        assert (patch >= 0) and (patch <= 11)

        pre_release = dev.version(pre_release=True)
        assert len(pre_release.split('.')) == 4

        # Use calendar versioning
        calver = dev.version(calver=True)
        y, *_ = calver.split('.')
        assert (int(y) >= 2016) and (int(y) <= 2018)

    def test_programming_language(self, dev):
        result = dev.programming_language()
        assert result in data.PROGRAMMING_LANGS

    def test_database(self, dev):
        result = dev.database()
        assert result in data.SQL

        result = dev.database(nosql=True)
        assert result in data.NOSQL

    def test_other(self, dev):
        result = dev.container()
        assert result in data.CONTAINER

    def test_frontend(self, dev):
        result = dev.frontend()
        assert result in data.FRONTEND

    def test_backend(self, dev):
        _result = dev.backend()
        assert _result in data.BACKEND

    def test_os(self, dev):
        result = dev.os()
        assert result in data.OS

    def test_boolean(self, dev):
        result = dev.boolean()
        assert result or (not result)


class TestSeededDevelopment(object):
    TIMES = 5

    @pytest.fixture
    def _developments(self, seed):
        return Development(seed=seed), Development(seed=seed)

    def test_software_license(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.software_license() == d2.software_license()

    def test_version_control_system(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.version_control_system() == d2.version_control_system()

    def test_version(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.version() == d2.version()
            assert d1.version(calver=True, pre_release=True) == \
                d2.version(calver=True, pre_release=True)

    def test_programming_language(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.programming_language() == d2.programming_language()

    def test_database(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.database() == d2.database()
            assert d1.database(nosql=True) == d2.database(nosql=True)

    def test_container(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.container() == d2.container()

    def test_frontend(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.frontend() == d2.frontend()

    def test_backend(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.backend() == d2.backend()

    def test_os(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.os() == d2.os()

    def test_boolean(self, _developments):
        d1, d2 = _developments
        for _ in range(self.TIMES):
            assert d1.boolean() == d2.boolean()
