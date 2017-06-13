# -*- coding: utf-8 -*-

import re

from ._patterns import STR_REGEX


def test_str(medicine):
    assert re.match(STR_REGEX, str(medicine))


def test_prescription_drug(generic):
    result = generic.medicine.prescription_drug()
    assert result in generic.medicine._data['prescription_drug']
