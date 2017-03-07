# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.providers import Development
from elizabeth.core.intd import (
    FRONTEND,
    PROGRAMMING_LANGS,
    OS,
    CONTAINER,
    LICENSES,
    NOSQL,
    BACKEND,
    SQL
)


@pytest.fixture
def dev():
    return Development()


def test_license(dev):
    result = dev.software_license()
    assert result in LICENSES


def test_version_control_system(dev):
    vcs = ["Git", "Subversion"]
    assert dev.version_control_system() in vcs


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


def test_programming_language(dev):
    result = dev.programming_language()
    assert result in PROGRAMMING_LANGS


def test_database(dev):
    result = dev.database()
    assert result in SQL

    _result = dev.database(nosql=True)
    assert _result in NOSQL


def test_other(dev):
    result = dev.container()
    assert result in CONTAINER


def test_frontend(dev):
    result = dev.frontend()
    assert result in FRONTEND


def test_backend(dev):
    _result = dev.backend()
    assert _result in BACKEND


def test_os(dev):
    result = dev.os()
    assert result in OS


def test_stackoverflow_question(dev):
    url = dev.stackoverflow_question()
    post_id = int(url.split('/')[-1])
    assert post_id >= 1000000
    assert post_id <= 9999999
