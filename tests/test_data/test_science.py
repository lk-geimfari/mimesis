# -*- coding: utf-8 -*-

import re

from elizabeth.data.int import MATH_FORMULAS
from ._patterns import STR_REGEX


def test_str(science):
    assert re.match(STR_REGEX, str(science))


def test_math_formula(science):
    result = science.math_formula()
    assert result in MATH_FORMULAS


def test_scientific_article(generic):
    result = generic.science.scientific_article()
    assert result in generic.science._data['article']


def test_currency(generic):
    result = generic.science.currency()
    assert result in generic.science._data['currency']


def test_prescription_drug(generic):
    result = generic.science.prescription_drug()
    assert result in generic.science._data['prescription_drug']


def test_chemical_element(generic):
    # Because: https://travis-ci.org/lk-geimfari/elizabeth/jobs/196565835
    if generic.locale != 'fa':
        result = generic.science.chemical_element(name_only=True)
        assert len(result) >= 1

        result = generic.science.chemical_element(name_only=False)
        assert isinstance(result, dict)
