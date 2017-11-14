import pytest

from mimesis import config
from mimesis.schema import Field
from mimesis.exceptions import UndefinedSchema


@pytest.mark.parametrize(
    'locale', config.LIST_OF_LOCALES,
)
def test_field(locale):
    filed = Field(locale)
    result = filed('username', template='l.d')
    assert result.split('.')[1].isdigit()

    with pytest.raises(ValueError):
        filed('unsupported_field')
        filed('')


@pytest.fixture
def valid():
    _ = Field('en')
    return lambda: {
        'id': _('uuid'),
        'name': _('word'),
        'version': _('version'),
        'owner': {
            'email': _('email'),
            'token': _('token'),
            'creator': _('full_name', gender='female'),
        },
    }


@pytest.fixture
def _():
    return Field('en')


def test_fill(_, valid):
    result = _.fill(schema=valid, iterations=2)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

    with pytest.raises(UndefinedSchema):
        _.fill(schema=lambda: {})
