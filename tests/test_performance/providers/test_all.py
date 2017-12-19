import types

import pytest
from profiling.tracing import TracingProfiler

from mimesis import providers
from tests.conftest import PERFORMANCE_COUNTER, runner


def _get_methods(cls):
    methods = []
    for attr in [x for x in dir(cls) if not x.startswith('_')]:
        attr_method = cls.__getattribute__(attr)
        if isinstance(attr_method, types.MethodType):
            methods.append(attr_method)
    return methods


@pytest.fixture
def _profiler():
    return TracingProfiler()


def _providers():
    yield providers.Address()
    yield providers.Business()
    yield providers.ClothingSizes()
    yield providers.Code()
    yield providers.Cryptographic()
    yield providers.Datetime()
    yield providers.Development()
    yield providers.File()
    yield providers.Food()
    yield providers.Games()
    yield providers.Hardware()
    yield providers.Internet()
    yield providers.Numbers()
    yield providers.Path()
    yield providers.Payment()
    yield providers.Personal()
    yield providers.Science()
    yield providers.Structured()
    yield providers.Text()
    yield providers.Transport()
    yield providers.UnitSystem()


def test_perfomance(_profiler: TracingProfiler):
    print('\n')
    for provider in _providers():
        provider_methods = _get_methods(provider)
        with _profiler:
            for method in provider_methods:
                runner(method, PERFORMANCE_COUNTER)
        print('{:16}: {}'.format(
            type(provider).__name__,
            _profiler.result()),
        )
