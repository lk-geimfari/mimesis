# -*- coding: utf-8 -*-
import re

from elizabeth.data import LOCALE_CODES
from ._patterns import STR_REGEX


def test_str(code):
    assert re.match(STR_REGEX, str(code))


def test_custom_code(code):
    result = code.custom_code(
        mask='@###', char='@', digit='#')

    assert len(result) == 4


def test_custom_code_args(code):
    result = code.custom_code(
        mask='@@@-###-@@@').split('-')

    a, b, c = result
    assert a.isalpha()
    assert b.isdigit()
    assert c.isalpha()


def test_ean(code):
    result = code.ean(fmt='ean-8')
    assert len(result) == 8

    result = code.ean(fmt='ean-13')
    assert len(result) == 13


def test_imei(code):
    result = code.imei()
    assert len(result) <= 15


def test_pin(code):
    result = code.pin()
    assert len(result) == 4


def test_issn(code):
    result = code.issn()
    assert len(result) == 9


def test_locale_code(code):
    result = code.locale_code()
    assert result in LOCALE_CODES


def test_isbn(generic):
    result = generic.code.isbn(fmt='isbn-10')
    assert len(result) >= 10

    result = generic.code.isbn(fmt='isbn-13')
    assert len(result) >= 13
