import pytest

from mimesis.schema import Schema


@pytest.fixture
def schema():
    return Schema()


def test_valid_schema(schema):
    valid_schema = {
        'id': 'cryptographic.uuid',
        'name': 'text.word',
        'version': 'development.version',
        'owner': {
            'email': 'personal.email',
            'token': 'cryptographic.token',
            'creator': 'personal.full_name',
        },
    }

    result = schema.load(schema=valid_schema).create(iterations=1)
    assert isinstance(result, dict)  # check type_to decorator

    result_2 = schema.load(schema=valid_schema).create(iterations=10)

    assert isinstance(result_2, list)
    assert len(result_2) == 10


def test_invalid_schema(schema):
    invalid_schema = {
        'id': 'none.none',
        'name': 'text.none',
        'version': 'development.none',
        'owner': {
            'email': 'personal.none',
            'token': 'cryptographic.none',
            'creator': 'personal.none',
        },
    }

    with pytest.raises(AttributeError):
        schema.load(schema=invalid_schema).create()
