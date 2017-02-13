# -*- coding: utf-8 -*-

import elizabeth
import pytest

locales = [
    'en-au',
    'da',
    'de',
    'en',
    'en-gb',
    'es',
    'fa',
    'fi',
    'fr',
    'is',
    'it',
    'nl',
    'no',
    'pl',
    'pt',
    'pt-br',
    'ru',
    'sv',
    'hu',
    'ko',
    'cs',
    'jp',
    'tr'
]


@pytest.fixture(params=locales)
def generic(request):
    return elizabeth.Generic(request.param)


@pytest.fixture(params=locales)
def address(request):
    return elizabeth.Address(request.param)


@pytest.fixture(params=locales)
def business(request):
    return elizabeth.Business(request.param)


@pytest.fixture(params=locales)
def code(request):
    return elizabeth.Code(request.param)


@pytest.fixture(params=locales)
def dt(request):
    return elizabeth.Datetime(request.param)


@pytest.fixture(params=locales)
def food(request):
    return elizabeth.Food(request.param)


@pytest.fixture(params=locales)
def personal(request):
    return elizabeth.Personal(request.param)


@pytest.fixture(params=locales)
def science(request):
    return elizabeth.Science(request.param)


@pytest.fixture(params=locales)
def structured(request):
    return elizabeth.Structured(request.param)


@pytest.fixture(params=locales)
def text(request):
    return elizabeth.Text(request.param)


@pytest.fixture()
def transport():
    return elizabeth.Transport()
