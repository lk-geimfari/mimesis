# -*- coding: utf-8 -*-

import pytest

from mimesis import Development, data


@pytest.fixture
def dev():
    return Development()


@pytest.fixture
def _seeded_dev():
    return Development(seed=42)


def test_license(dev):
    result = dev.software_license()
    assert result in data.LICENSES


def test_seeded_license(_seeded_dev):
    result = _seeded_dev.software_license()
    assert result == 'The BSD 3-Clause License'
    result = _seeded_dev.software_license()
    assert result == 'Apache License, 2.0 (Apache-2.0)'


def test_version_control_system(dev):
    vcs = ['Git', 'Subversion']
    assert dev.version_control_system() in vcs


def test_seeded_version_control_system(_seeded_dev):
    result = _seeded_dev.version_control_system()
    assert result == 'Git'
    result = _seeded_dev.version_control_system()
    assert result == 'Git'
    result = _seeded_dev.version_control_system()
    assert result == 'Subversion'


def test_version(dev):
    result = dev.version().split('.')

    major = int(result[0])
    assert major >= 0
    assert major <= 11

    minor = int(result[1])
    assert minor >= 0
    assert minor <= 11

    micro = int(result[2])
    assert micro >= 0
    assert micro <= 11


def test_seeded_version(_seeded_dev):
    result = _seeded_dev.version()
    assert result == '10.1.0'
    result = _seeded_dev.version()
    assert result == '11.4.3'


def test_programming_language(dev):
    result = dev.programming_language()
    assert result in data.PROGRAMMING_LANGS


def test_seeded_programming_language(_seeded_dev):
    result = _seeded_dev.programming_language()
    assert result == 'OCaml'
    for _ in range(3):
        result = _seeded_dev.programming_language()
    assert result == 'Python'


def test_database(dev):
    result = dev.database()
    assert result in data.SQL

    result = dev.database(nosql=True)
    assert result in data.NOSQL


def test_seeded_database(_seeded_dev):
    result = _seeded_dev.database(nosql=True)
    assert result == 'Apache Cassandra'
    result = _seeded_dev.database()
    assert result == 'MariaDB'
    result = _seeded_dev.database()
    assert result == 'PostgreSQL'


def test_container(dev):
    result = dev.container()
    assert result in data.CONTAINER


def test_seeded_container(_seeded_dev):
    result = _seeded_dev.container()
    assert result == 'Kubernetes'
    result = _seeded_dev.container()
    assert result == 'Docker'


def test_frontend(dev):
    result = dev.frontend()
    assert result in data.FRONTEND


def test_seeded_frontend(_seeded_dev):
    result = _seeded_dev.frontend()
    assert result == 'TypeScript/CSS/HTML'
    result = _seeded_dev.frontend()
    assert result == 'JS/HTML/CSS/Canvas/SVG'


def test_backend(dev):
    _result = dev.backend()
    assert _result in data.BACKEND


def test_seeded_backend(_seeded_dev):
    result = _seeded_dev.backend()
    assert result == 'Erlang/ChicagoBoss'
    result = _seeded_dev.backend()
    assert result == 'Java'


def test_os(dev):
    result = dev.os()
    assert result in data.OS


def test_seeded_os(_seeded_dev):
    result = _seeded_dev.os()
    assert result == 'elementaryOS'
    result = _seeded_dev.os()
    assert result == 'Fedora'
