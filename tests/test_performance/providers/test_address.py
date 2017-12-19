import pytest
from profiling.tracing import TracingProfiler

from mimesis.providers import Address
from tests.conftest import PERFORMANCE_COUNTER, runner


@pytest.fixture
def _profiler():
    return TracingProfiler()


@pytest.fixture
def _instance():
    return Address()


@pytest.mark.parametrize(
    'method', [
        'street_number',
        'street_name',
        'street_suffix',
        'address',
        'state',
        'region',
        'province',
        'federal_subject',
        'postal_code',
        'country_iso_code',
        'country',
        'city',
        'latitude',
        'longitude',
        'coordinates',
        'continent',
        'calling_code',
    ],
)
def test_methods(_profiler, _instance: Address, method):
    with _profiler:
        runner(_instance.__getattribute__(method), PERFORMANCE_COUNTER)
    print('\n', method, _profiler.result())
