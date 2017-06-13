import elizabeth
import pytest

locales = [
    "cs",
    "da",
    "de",
    "de-at",
    "de-ch",
    "en",
    "en-au",
    "en-ca",
    "en-gb",
    "es",
    "es-mx",
    "fa",
    "fi",
    "fr",
    "hu",
    "is",
    "it",
    "ja",
    "ko",
    "nl",
    "nl-be",
    "no",
    "pl",
    "pt",
    "pt-br",
    "ru",
    "sv",
    "tr",
    "uk",
    "zh"
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
def medicine(request):
    return elizabeth.Medicine(request.param)


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
