import pytest

from mimesis.builtins import RussiaSpecProvider
from mimesis.exceptions import JSONKeyError


@pytest.fixture
def russia():
    return RussiaSpecProvider()


def test_passport_series(russia):
    result = russia.passport_series()
    assert result is not None
    result = result.split(' ')
    assert isinstance(result, list)

    result = russia.passport_series(year=10)
    region, year = result.split(' ')
    assert int(year) == 10
    assert region is not None


def test_passport_number(russia):
    result = russia.passport_number()
    assert isinstance(result, int)
    assert (result <= 999999) and (
        result >= 100000)


def test_series_and_number(russia):
    result = russia.series_and_number()
    assert result is not None


def test_patronymic(russia):
    patronymic = russia.patronymic

    assert isinstance(patronymic(gender='female'), str)
    assert len(patronymic(gender='female')) >= 4

    assert isinstance(patronymic(gender='male'), str)
    assert len(patronymic(gender='male')) >= 4

    with pytest.raises(JSONKeyError):
        patronymic(gender='nil')


def test_generate_sentence(russia):
    result = russia.generate_sentence()
    assert len(result) >= 20
    assert isinstance(result, str)


def test_snils(russia):
    result = russia.snils()
    number = result.replace('-', '')
    assert len(number) == 11
