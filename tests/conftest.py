import pytest

import mimesis
from mimesis import config

locales = config.LIST_OF_LOCALES
platform = ['win32', 'linux']

#
# @pytest.fixture(autouse=True)
# def add_providers(doctest_namespace):
#     seed = 0xFF
#     doctest_namespace['address'] = mimesis.Address('en', seed=seed)
#     doctest_namespace['business'] = mimesis.Business('en', seed=seed)
#     doctest_namespace['dt'] = mimesis.Datetime('en', seed=seed)
#     doctest_namespace['food'] = mimesis.Food('en', seed=seed)
#     doctest_namespace['person'] = mimesis.Person('en', seed=seed)
#     doctest_namespace['science'] = mimesis.Science('en', seed=seed)
#     doctest_namespace['text'] = mimesis.Text('en', seed=seed)
#     doctest_namespace['path'] = mimesis.Path('en', seed=seed)
#     doctest_namespace['transport'] = mimesis.Transport('en', seed=seed)
#     doctest_namespace['sizes'] = mimesis.ClothingSize(seed=seed)
#     doctest_namespace['code'] = mimesis.Code('en', seed=seed)
#     doctest_namespace['file'] = mimesis.File(seed=seed)
#     doctest_namespace['development'] = mimesis.Development(seed=seed)
#     doctest_namespace['games'] = mimesis.Games(seed=seed)
#     doctest_namespace['hardware'] = mimesis.Hardware(seed=seed)
#     doctest_namespace['internet'] = mimesis.Internet(seed=seed)
#     doctest_namespace['numbers'] = mimesis.Numbers(seed=seed)
#     doctest_namespace['payment'] = mimesis.Payment(seed=seed)
#     doctest_namespace['structure'] = mimesis.Structure(seed=seed)
#     doctest_namespace['units'] = mimesis.UnitSystem(seed=seed)
#     doctest_namespace['cryptographic'] = mimesis.Cryptographic(seed=seed)


@pytest.fixture
def seed():
    return 'mimesis'


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
def person(request):
    return mimesis.Person(request.param)


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
