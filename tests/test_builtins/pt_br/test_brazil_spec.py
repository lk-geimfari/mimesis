import re

import pytest

from mimesis.builtins import BrazilSpecProvider


@pytest.fixture
def pt_br():
    return BrazilSpecProvider()


def test_cpf(pt_br):
    # test if the cpf has 14 digits with the mask
    cpf_with_mask = pt_br.cpf()
    assert len(cpf_with_mask) == 14

    # test the mask
    non_numeric_digits = re.sub('\d', '', cpf_with_mask)
    assert '..-' == non_numeric_digits == non_numeric_digits
    assert len(re.sub('\D', '', cpf_with_mask)) == 11

    # test for the cpf without mask
    cpf_without_mask = pt_br.cpf(False)
    assert len(cpf_without_mask) == 11
    non_numeric_digits = re.sub('\d', '', cpf_without_mask)
    assert '' == non_numeric_digits


def test_cnpj(pt_br):
    # test if the cnpj has 18 digits with the mask
    cnpj_with_mask = pt_br.cnpj()
    assert len(cnpj_with_mask) == 18

    # test the mask
    non_numeric_digits = re.sub('\d', '', cnpj_with_mask)
    assert '../-' == non_numeric_digits == non_numeric_digits
    assert len(re.sub('\D', '', cnpj_with_mask)) == 14

    # test for the cnpj without mask
    cnpj_without_mask = pt_br.cnpj(False)
    assert len(cnpj_without_mask) == 14
    non_numeric_digits = re.sub('\d', '', cnpj_without_mask)
    assert '' == non_numeric_digits
