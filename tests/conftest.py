import pytest

import mimesis
from mimesis import config

locales = config.LIST_OF_LOCALES
platform = ['win32', 'linux2']


@pytest.fixture(params=locales)
def generic(request):
    return mimesis.Generic(request.param)


@pytest.fixture(params=locales)
def address(request):
    return mimesis.Address(request.param)


@pytest.fixture(params=locales)
def business(request):
    return mimesis.Business(request.param)


@pytest.fixture(params=locales)
def dt(request):
    return mimesis.Datetime(request.param)


@pytest.fixture(params=locales)
def food(request):
    return mimesis.Food(request.param)


@pytest.fixture(params=locales)
def personal(request):
    return mimesis.Personal(request.param)


@pytest.fixture(params=locales)
def science(request):
    return mimesis.Science(request.param)


@pytest.fixture(params=locales)
def text(request):
    return mimesis.Text(request.param)


@pytest.fixture(params=platform)
def path(request):
    return mimesis.Path(request.param)


@pytest.fixture(params=locales)
def transport(request):
    return mimesis.Transport(request.param)
