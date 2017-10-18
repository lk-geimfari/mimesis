import pytest

from mimesis.builtins import GermanySpecProvider


@pytest.fixture
def germany():
    return GermanySpecProvider()


def test_noun(germany):
    result = germany.noun()

    assert result is not None
    assert result in germany._data['noun']

    result_plural = germany.noun(plural=True)
    assert result_plural in germany._data['plural']
