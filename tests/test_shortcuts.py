# -*- coding: utf-8 -*-

import pytest

from mimesis import shortcuts


@pytest.mark.parametrize(
    'number, check_sum', [
        ('5563455651', '2'),
        ('7992739871', '3'),
        ('5161675549', '5'),
    ],
)
def test_luhn_checksum(number, check_sum):
    assert shortcuts.luhn_checksum(number) == check_sum
