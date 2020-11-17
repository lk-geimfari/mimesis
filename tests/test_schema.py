import re

import pytest

from mimesis import locales
from mimesis.builtins import USASpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import (
    UnacceptableField,
    UndefinedField,
    UndefinedSchema,
    UnsupportedField,
)
from mimesis.schema import Field, Schema

from .test_providers import patterns


def test_str(field):
    assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(field))


@pytest.mark.parametrize(
    'locale', locales.LIST_OF_LOCALES,
)
def test_field(locale):
    filed = Field(locale)
    result = filed('full_name')
    assert result
    assert isinstance(result, str)

    with pytest.raises(UnsupportedField):
        filed('unsupported_field')

    with pytest.raises(UndefinedField):
        filed()


def test_field_with_custom_providers():
    field = Field(providers=[USASpecProvider])
    assert field('ssn')
    assert field('usa_provider.ssn')


@pytest.fixture
def field():
    return Field('en')


@pytest.fixture
def valid_schema(field):
    return lambda: {
        'id': field('uuid'),
        'name': field('word'),
        'version': field(
            'version', key=str.lower, pre_release=True,
        ),
        'timestamp': field('timestamp'),
        'mime_type': field('mime_type'),
        'zip_code': field('postal_code'),
        'owner': {
            'email': field('email', key=str.lower),
            'token': field('token_hex'),
            'creator': field(
                'full_name', gender=Gender.FEMALE,
            ),
            'billing': {
                'ethereum_address': field('ethereum_address'),
            },
        },
        'defined_cls': {
            'title': field('person.title'),
            'title2': field('text.title'),
        },
        'items': field(
            'choice', items=[
                .1, .3, .4,
                .5, .6, .7,
                .8, .9, .10,
            ]),
        'unique_items': field(
            'choice',
            items='aabbcccddd',
            length=4,
            unique=True,
        ),
    }


def test_fill(field, valid_schema):
    result = Schema(schema=valid_schema).create(iterations=2)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)


def test_none_schema():
    with pytest.raises(UndefinedSchema):
        schema = Schema(schema=None)  # type: ignore
        schema.create()


def test_schema_with_unacceptable_field(field):
    invalid_schema = (lambda: {
        'word': field('text.word.invalid'),
        'items': field(
            'choice.choice.choice', items=[
                .1, .3, .4,
                .5, .6, .7,
                .8, .9, .10,
            ]),
    })

    with pytest.raises(UnacceptableField):
        Schema(schema=invalid_schema).create()


def test_field_with_key(field):
    usual_result = field('age')
    assert isinstance(usual_result, int)

    result_on_key = field('age', key=float)
    assert isinstance(result_on_key, float)
