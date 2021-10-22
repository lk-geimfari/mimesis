import re
import warnings
from collections.abc import Iterator

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import FieldError, SchemaError
from mimesis.locales import Locale
from mimesis.schema import BaseField, Field, Schema
from tests.test_providers import patterns


def test_str(field):
    assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(field))


@pytest.fixture
def default_field():
    return Field(locale=Locale.EN)


@pytest.fixture(scope="module", params=list(Locale))
def field(request):
    return Field(request.param)


@pytest.fixture
def modified_field():
    return Field(locale=Locale.EN, providers=(USASpecProvider,))


def test_field(field):
    assert field("uuid")
    assert field("full_name")
    assert field("street_name")


def test_field_with_custom_providers(default_field, modified_field):
    with pytest.raises(FieldError):
        default_field("ssn")

    assert modified_field("ssn")


def test_field_with_key_function(field):
    result = field("person.name", key=list)
    assert isinstance(result, list) and len(result) >= 1


def test_field_raises_field_error(default_field):
    with pytest.raises(FieldError):
        default_field("person.unsupported_field")

    with pytest.raises(FieldError):
        default_field("unsupported_field")

    with pytest.raises(FieldError):
        default_field()

    with pytest.raises(FieldError):
        default_field("person.full_name.invalid")


@pytest.fixture(scope="module", params=list(Locale))
def test_base_field(request):
    field = BaseField(request.param)

    assert field.perform("uuid")
    assert field.perform("full_name")
    assert field.perform("street_name")


@pytest.fixture
def schema(field):
    return Schema(
        schema=lambda: {
            "id": field("uuid"),
            "name": field("word"),
            "timestamp": field("timestamp"),
            "zip_code": field("postal_code"),
            "owner": {
                "email": field("email", key=str.lower),
                "creator": field("full_name", gender=Gender.FEMALE),
            },
            "defined_cls": {
                "title": field("person.title"),
                "title2": field("text.title"),
            },
        }
    )


@pytest.mark.parametrize(
    "invalid_schema", [None, {"a": "uuid"}, [True, False], (1, 2, 3)]
)
def test_schema_raises_schema_error(invalid_schema):
    with pytest.raises(SchemaError):
        Schema(schema=invalid_schema)  # type: ignore


def test_schema_create(schema):
    result = schema.create(5)

    assert len(result) == 5
    assert isinstance(result, list)

    first, *mid, last = result

    assert first["timestamp"] != last["timestamp"]
    assert first["owner"]["creator"] != last["owner"]["creator"]

    with pytest.raises(ValueError):
        schema.create(0)


def test_schema_iterator(schema):
    result = schema.iterator(5)

    assert len(list(result)) == 5
    assert isinstance(result, Iterator)

    result = schema.iterator(1)
    assert len(list(result)) == 1

    with pytest.raises(ValueError):
        next(schema.iterator(0))


def test_schema_loop(schema):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        infinite = schema.loop()

        result_1 = next(infinite)
        result_2 = next(infinite)

        assert result_1["timestamp"] != result_2["timestamp"]
        assert result_1["owner"]["creator"] != result_2["owner"]["creator"]
