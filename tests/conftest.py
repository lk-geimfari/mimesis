import os

import pytest

import mimesis
from mimesis.locales import Locale

platform = ["win32", "linux", "darwin"]


def get_locales():
    if os.getenv("MIMESIS_TESTS_ONLY_EN"):
        return [Locale.EN]
    return Locale.values()


@pytest.fixture(params=get_locales())
def localized_field(request):
    return mimesis.Field(request.param)


@pytest.fixture(params=get_locales())
def localized_fieldset(request):
    return mimesis.Fieldset(request.param)


@pytest.fixture(params=get_locales())
def fieldset_with_default_i(request):
    return mimesis.Fieldset(request.param, i=100)


@pytest.fixture
def seed():
    return "mimesis"


@pytest.fixture(params=get_locales())
def generic(request):
    return mimesis.Generic(request.param)


@pytest.fixture(params=get_locales())
def address(request):
    return mimesis.Address(request.param)


@pytest.fixture(params=get_locales())
def finance(request):
    return mimesis.Finance(request.param)


@pytest.fixture(params=get_locales())
def dt(request):
    return mimesis.Datetime(request.param)


@pytest.fixture(params=get_locales())
def food(request):
    return mimesis.Food(request.param)


@pytest.fixture(params=get_locales())
def person(request):
    return mimesis.Person(request.param)


@pytest.fixture(params=get_locales())
def text(request):
    return mimesis.Text(request.param)


@pytest.fixture(params=platform)
def path(request):
    return mimesis.Path(request.param)
