# -*- coding: utf-8 -*-

import re

import pytest

from mimesis.builtins import ItalySpecProvider
from mimesis.enums import Gender


@pytest.fixture
def italy():
    return ItalySpecProvider()


def test_noun(italy):
    result = italy.fiscal_code(gender=Gender.MALE)
    assert re.fullmatch(
        r'^[A-Z]{6}\d{2}[A-EHLMPR-T][0123][0-9][A-MZ]\d{3}[A-Z]$', result)

    result = italy.fiscal_code(gender=Gender.FEMALE)
    assert re.fullmatch(
        r'^[A-Z]{6}\d{2}[A-EHLMPR-T][4567][0-9][A-MZ]\d{3}[A-Z]$', result)
