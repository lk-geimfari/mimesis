# -*- coding: utf-8 -*-

import pytest

from mimesis import Development, data


@pytest.fixture
def dev():
    return Development()


def test_license(dev):
    result = dev.software_license()
    assert result in data.LICENSES


def test_version_control_system(dev):
    vcs = ['Git', 'Subversion']
    assert dev.version_control_system() in vcs


def test_version(dev):
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


def test_programming_language(dev):
    result = dev.programming_language()
    assert result in data.PROGRAMMING_LANGS


def test_database(dev):
    result = dev.database()
    assert result in data.SQL

    result = dev.database(nosql=True)
    assert result in data.NOSQL


def test_other(dev):
    result = dev.container()
    assert result in data.CONTAINER


def test_frontend(dev):
    result = dev.frontend()
    assert result in data.FRONTEND


def test_backend(dev):
    _result = dev.backend()
    assert _result in data.BACKEND


def test_os(dev):
    result = dev.os()
    assert result in data.OS


def test_boolean(dev):
    result = dev.boolean()
    assert result or (not result)
