import pytest
from profiling.tracing import TracingProfiler

from mimesis.providers import Structured
from tests.conftest import PERFORMANCE_COUNTER, runner


@pytest.fixture
def _profiler():
    return TracingProfiler()


@pytest.fixture
def _structured():
    return Structured()


@pytest.mark.parametrize(
    'method', [
        'css',
        'css_property',
        'html',
        'html_attribute_value',
        'json',
    ],
)
def test_methods(_profiler, _structured: Structured, method):
    with _profiler:
        runner(_structured.__getattribute__(method), PERFORMANCE_COUNTER)
    print('\n', method, _profiler.result())
