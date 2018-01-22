import pytest

from mimesis.enums import Gender
from mimesis.schema import Field, Schema


@pytest.fixture
def _description():
    _ = Field('en')
    return lambda: {
        'id': _('uuid'),
        'name': _('text.word'),
        'version': _('version', pre_release=True),
        'timestamp': _('timestamp', posix=False),
        'owner': {
            'email': _('email', key=str.lower),
            'token': _('token'),
            'creator': _('personal.full_name', gender=Gender.FEMALE),
        },
    }


def test_schema(benchmark, _description):
    schema = Schema(schema=_description)
    result = benchmark(schema.create, 100)
    assert result
