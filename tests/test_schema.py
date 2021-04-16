import re

import pytest
from mimesis import locales
from mimesis.enums import Gender
from mimesis.exceptions import (
    UnacceptableField,
    UndefinedFieldName,
    UnsupportedField,
)
from mimesis.schema import Field, Schema

from .test_providers import patterns


def test_str(field):
    assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(field))


@pytest.mark.parametrize(
    'locale',
    locales.LIST_OF_LOCALES,
)
def test_field(locale):
    field = Field(locale)
    full_name = field('full_name')
    assert full_name
    assert isinstance(full_name, str)

    uppercase_uuid = field('uuid', key=str.upper)
    assert uppercase_uuid.isupper()

    with pytest.raises(UnsupportedField):
        field('person.unsupported_field')

    with pytest.raises(UnsupportedField):
        field('unsupported_field')

    with pytest.raises(UnacceptableField):
        field('person.full_name.invalid')

    with pytest.raises(UndefinedFieldName):
        field()


@pytest.fixture
def schema(field):
    return Schema(
        schema=lambda: {
            'id': field('uuid'),
            'name': field('word'),
            'version': field(
                'version',
                key=str.lower,
                pre_release=True,
            ),
            'timestamp': field('timestamp'),
            'mime_type': field('mime_type'),
            'zip_code': field('postal_code'),
            'owner': {
                'email': field('email', key=str.lower),
                'token': field('token_hex'),
                'creator': field('full_name', gender=Gender.FEMALE),
            },
            'defined_cls': {
                'title': field('person.title'),
                'title2': field('text.title'),
            },
            'items': field(
                'choice',
                items=[
                    0.1,
                    0.2,
                    0.3,
                    0.4,
                ],
            ),
        }
    )


#
# def test_schema_create(schema):
#     result = schema.create(5)
#
#     first, *mid, last = result
#
#     assert first['timestamp'] != last['timestamp']
#     assert first['owner']['creator'] != last['owner']['creator']
#     assert isinstance(result, list)
#     assert len(result) == 5
#
#     assert schema.create(0) == []
#
