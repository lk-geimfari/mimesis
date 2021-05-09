import mimesis
import pytest
from mimesis.locales import Locale

locales = list(Locale)
platform = ["win32", "linux"]


@pytest.fixture
def seed():
    return "mimesis"


@pytest.fixture(params=locales)
def generic(request):
    return mimesis.Generic(request.param)


@pytest.fixture(params=locales)
def address(request):
    return mimesis.Address(request.param)


@pytest.fixture(params=locales)
def finance(request):
    return mimesis.Finance(request.param)


@pytest.fixture(params=locales)
def dt(request):
    return mimesis.Datetime(request.param)


@pytest.fixture(params=locales)
def food(request):
    return mimesis.Food(request.param)


@pytest.fixture(params=locales)
def person(request):
    return mimesis.Person(request.param)


@pytest.fixture(params=locales)
def text(request):
    return mimesis.Text(request.param)


@pytest.fixture(params=platform)
def path(request):
    return mimesis.Path(request.param)
