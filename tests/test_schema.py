from os.path import (
    abspath,
    dirname,
    join,
)

import pytest

from mimesis import config
from mimesis.exceptions import UndefinedSchema
from mimesis.schema import Schema

PATH = abspath(join(dirname(__file__), 'data_fixtures'))


@pytest.fixture(params=config.LIST_OF_LOCALES)
def schema(request):
    return Schema(request.param)


@pytest.fixture
def valid_schema():
    return dict(
        id='cryptographic.uuid',
        name='text.word',
        version='development.version',
        owner=dict(
            email='personal.email',
            token='cryptographic.token',
            creator='personal.full_name'),
        sites=[{'home_page': 'internet.home_page'}],
    )


@pytest.fixture
def invalid_schema():
    return dict(
        id='none.none',
        name='text.none',
        version='development.none',
        owner=dict(
            email='personal.none',
            token='cryptographic.none',
            creator='personal.none',
        ),
        sites=[{'home_page': 'internet.home_page'}],
    )


def test_valid_schema(schema, valid_schema):
    result = schema.load(schema=valid_schema).create(iterations=1)
    assert isinstance(result, dict)  # check type_to decorator

    result_2 = schema.load(schema=valid_schema).create(iterations=10)

    assert isinstance(result_2, list)
    assert len(result_2) == 10


def test_invalid_schema(schema, invalid_schema):
    with pytest.raises(AttributeError):
        schema.load(schema=invalid_schema).create()


def test_load_schema_by_path(schema):
    valid_path = PATH + '/schema.json'
    result = schema.load(path=valid_path)
    assert isinstance(result.schema, dict)


def test_load_invalid_schema(schema):
    invalid_json_file = PATH + '/invalid_schema.json'
    with pytest.raises(ValueError):
        schema.load(path=invalid_json_file)


def test_load_schema_by_invalid_path(schema):
    invalid_path = PATH + '/schema.j'

    with pytest.raises(FileNotFoundError):
        schema.load(path=invalid_path)


def test_undefined_schema(schema):
    with pytest.raises(UndefinedSchema):
        schema.create()
