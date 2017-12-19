import pytest
from profiling.tracing import TracingProfiler

from mimesis.providers import Cryptographic
from tests.conftest import PERFORMANCE_COUNTER, runner


@pytest.fixture
def _profiler():
    return TracingProfiler()


@pytest.fixture
def _cryptographic():
    return Cryptographic()


@pytest.mark.parametrize(
    'method', [
        'uuid',
        'hash',
        'bytes',
        'token',
        'salt',
        'mnemonic_code',
    ],
)
def test_methods(_profiler, _cryptographic: Cryptographic, method):
    with _profiler:
        runner(_cryptographic.__getattribute__(method), PERFORMANCE_COUNTER)
    print('\n', method, _profiler.result())
