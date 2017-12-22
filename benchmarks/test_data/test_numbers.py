import pytest

from mimesis.providers import Numbers as Provider


@pytest.fixture
def _tested_provider():
    return Provider()


@pytest.mark.benchmark(
    group='providers.' + Provider.__name__,
)
@pytest.mark.parametrize(
    'method', (
        m for m in sorted(Provider.__dict__)
        if not m.startswith('_')
    ),
)
def test_method(benchmark, method, _tested_provider):
    result = benchmark(_tested_provider.__getattribute__(method))
    assert result
