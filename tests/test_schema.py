import csv
import json
import pickle
import re
import tempfile
from collections.abc import Iterator

import pytest

from mimesis.builtins.en import USASpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import FieldError, FieldsetError, SchemaError
from mimesis.locales import Locale
from mimesis.schema import BaseField, Field, Fieldset, Schema
from mimesis.types import MissingSeed
from tests.test_providers import patterns


def test_str(field):
    assert re.match(patterns.DATA_PROVIDER_STR_REGEX, str(field))


@pytest.fixture(scope="module", params=list(Locale))
def field(request):
    return Field(request.param)


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
        },
        iterations=10,
    )


@pytest.fixture
def extended_field():
    return Field(locale=Locale.EN, providers=(USASpecProvider,))


@pytest.fixture(scope="module", params=list(Locale))
def fieldset(request):
    return Fieldset(request.param)


@pytest.fixture(scope="module", params=list(Locale))
def custom_fieldset(request):
    class MyFieldSet(Fieldset):
        fieldset_iterations_kwarg = "wubba_lubba_dub_dub"

    return MyFieldSet(request.param)


@pytest.fixture(scope="module", params=list(Locale))
def fieldset_with_default_i(request):
    return Fieldset(request.param, i=100)


def test_field(field):
    assert field("uuid")
    assert field("full_name")
    assert field("street_name")


@pytest.mark.parametrize(
    "field_name",
    [
        "text title",
        "person.title",
        "person/title",
        "person:title",
    ]
)
def test_field_different_separator(field, field_name):
    assert isinstance(field(field_name), str)


@pytest.mark.parametrize(
    "field_name, i",
    [
        ("bank", 8),
        ("address", 4),
        ("name", 2),
    ],
)
def test_fieldset(fieldset, field_name, i):
    result = fieldset(field_name, i=i)
    assert isinstance(result, list) and len(result) == i


@pytest.mark.parametrize(
    "field_name",
    [
        "bank",
        "address",
        "full_name",
    ],
)
def test_fieldset_with_default_i(fieldset, field_name):
    result = fieldset(field_name)
    assert isinstance(result, list)
    assert len(result) == fieldset.fieldset_default_iterations


def test_custom_fieldset(custom_fieldset):
    result = custom_fieldset("name", wubba_lubba_dub_dub=3)
    assert isinstance(result, list) and len(result) == 3

    with pytest.raises(TypeError):
        custom_fieldset("name", i=4)


def test_fieldset_with_common_i(fieldset_with_default_i):
    result = fieldset_with_default_i("name")
    assert isinstance(result, list) and len(result) == 100

    result = fieldset_with_default_i("name", i=3)
    assert isinstance(result, list) and len(result) == 3


def test_fieldset_error(fieldset):
    with pytest.raises(FieldsetError):
        fieldset("username", key=str.upper, i=0)


def test_fieldset_field_error(fieldset):
    with pytest.raises(FieldError):
        fieldset("unsupported_field")


@pytest.mark.parametrize(
    "field_name", [
        "person.full_name.invalid",
        "invalid_field",
        "unsupported_field"
    ]
)
def test_field_error(field, field_name):
    with pytest.raises(FieldError):
        field(field_name)


def test_field_with_custom_providers(extended_field):
    assert extended_field("ssn")


def test_field_with_key_function(field):
    result = field("person.name", key=list)
    assert isinstance(result, list) and len(result) >= 1


def test_field_raises_field_error(field):
    with pytest.raises(FieldError):
        field("person.unsupported_field")

    with pytest.raises(FieldError):
        field("unsupported_field")

    with pytest.raises(FieldError):
        field()

    with pytest.raises(FieldError):
        field("person.full_name.invalid")


def test_explicit_lookup(field):
    result = field._explicit_lookup("person.surname")

    assert callable(result)
    assert isinstance(result(), str)


def test_fuzzy_lookup(field):
    result = field._fuzzy_lookup("surname")

    assert callable(result)
    assert isinstance(result(), str)


@pytest.mark.parametrize(
    "field_name",
    (
            "surname",
            "person.surname",
    ),
)
def test_lookup_method(field, field_name):
    result = field._lookup_method(field_name)

    assert callable(result)
    assert isinstance(result(), str)


@pytest.mark.parametrize(
    "field_name",
    (
            "",
            "foo",
            "foo.bar",
            "person.surname.male",
    ),
)
def test_lookup_method_field_error(field, field_name):
    with pytest.raises(FieldError):
        field._lookup_method(field_name)

    with pytest.raises(ValueError):
        field._explicit_lookup(field_name)

    with pytest.raises(FieldError):
        field._fuzzy_lookup(field_name)


@pytest.fixture(scope="module", params=list(Locale))
def test_base_field(request):
    field = BaseField(request.param)

    assert field.perform("uuid")
    assert field.perform("full_name")
    assert field.perform("street_name")


@pytest.mark.parametrize(
    "invalid_schema", [None, {"a": "uuid"}, [True, False], (1, 2, 3)]
)
def test_schema_instantiation_raises_schema_error(invalid_schema):
    with pytest.raises(SchemaError):
        Schema(schema=invalid_schema)  # type: ignore


def test_schema_instantiation_raises_value_error():
    with pytest.raises(ValueError):
        Schema(schema=lambda: {"uuid": Field()("uuid")}, iterations=0)


def test_choice_field(field):
    result = field("choice", items=["a", "b", "c", "d"], length=2)
    assert len(result) == 2


def test_schema_create(schema):
    result = schema.create()

    assert len(result) == schema.iterations
    assert isinstance(result, list)


def test_schema_iterator(schema):
    count = 0
    for item in schema:
        assert isinstance(item, dict)
        count += 1

    assert isinstance(schema, Iterator)
    assert count == schema.iterations

    with pytest.raises(StopIteration):
        schema.iterations = 0
        next(schema)


def test_schema_to_csv(schema):
    with tempfile.NamedTemporaryFile("r+") as temp_file:
        schema.to_csv(temp_file.name)
        dict_reader = csv.DictReader(temp_file)

        assert len(list(dict_reader)) == schema.iterations
        assert isinstance(dict_reader, csv.DictReader)

        for row in dict_reader:
            assert "id" in row and "timestamp" in row


def test_schema_to_json(schema):
    with tempfile.NamedTemporaryFile("r+") as temp_file:
        schema.to_json(temp_file.name, sort_keys=True, ensure_ascii=False)

        data = json.load(temp_file)
        assert len(list(data)) == schema.iterations
        assert "id" in data[0] and "id" in data[-1]


def test_schema_to_pickle(schema):
    with tempfile.NamedTemporaryFile("rb") as temp_file:
        schema.to_pickle(temp_file.name)

        data = pickle.load(temp_file)
        assert "id" in data[0] and "id" in data[-1]
        assert isinstance(data, list)
        assert len(data) == schema.iterations


@pytest.mark.parametrize(
    "seed",
    [
        1,
        3.14,
        "seed",
        MissingSeed,
    ],
)
def test_field_reseed(field, seed):
    field.reseed(seed)
    result1 = field("dsn")

    field.reseed(seed)
    result2 = field("dsn")

    assert result1 == result2
