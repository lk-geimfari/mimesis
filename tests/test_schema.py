import re

import pytest

from mimesis import config
from mimesis.builtins import USASpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import (UndefinedField, UndefinedSchema,
                                UnsupportedField)
from mimesis.schema import Field, Schema

from .test_providers import patterns


def test_str(field):
    assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(field))


@pytest.mark.parametrize(
    'locale', config.LIST_OF_LOCALES,
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
        'version': field('version', key=str.lower, pre_release=True),
        'timestamp': field('timestamp'),
        'mime_type': field('mime_type'),
        'zip_code': field('postal_code'),
        'owner': {
            'email': field('email', key=str.lower),
            'token': field('token'),
            'creator': field('full_name', gender=Gender.FEMALE),
            'billing': {
                'ethereum_address': field('ethereum_address'),
            },
        },
        'defined_cls': {
            'title': field('person.title'),
            'title2': field('text.title'),
        },
    }


def test_fill(field, valid_schema):
    result = Schema(schema=valid_schema).create(iterations=2)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

    with pytest.raises(UndefinedSchema):
        Schema(schema=None).create()  # type: ignore


def test_field_with_key(field):
    usual_result = field('age')
    assert isinstance(usual_result, int)

    result_on_key = field('age', key=lambda v: float(v))
    assert isinstance(result_on_key, float)
