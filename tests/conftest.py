import pytest

import mimesis
from mimesis.locales import Locale

platform = ["win32", "linux", "darwin"]


@pytest.fixture
def seed():
    return "mimesis"


@pytest.fixture(params=Locale.values())
def generic(request):
    return mimesis.Generic(request.param)


@pytest.fixture(params=Locale.values())
def address(request):
    return mimesis.Address(request.param)


@pytest.fixture(params=Locale.values())
def finance(request):
    return mimesis.Finance(request.param)


@pytest.fixture(params=Locale.values())
def dt(request):
    return mimesis.Datetime(request.param)


@pytest.fixture(params=Locale.values())
def food(request):
    return mimesis.Food(request.param)


@pytest.fixture(params=Locale.values())
def person(request):
    return mimesis.Person(request.param)


@pytest.fixture(params=Locale.values())
def text(request):
    return mimesis.Text(request.param)


@pytest.fixture(params=platform)
def path(request):
    return mimesis.Path(request.param)
