import csv
import json
import pickle
import re
import unicodedata
from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from mimesis.enums import Gender
from mimesis.exceptions import (
    AliasesTypeError,
    FieldArityError,
    FieldError,
    FieldNameError,
    FieldsetError,
    SchemaError,
)
from mimesis.keys import maybe, romanize
from mimesis.locales import Locale
from mimesis.random import Random
from mimesis.schema import Field, Fieldset, Schema, SchemaBuilder, SchemaContext
from mimesis.types import MissingSeed
from tests.test_providers.patterns import DATA_PROVIDER_STR_REGEX

if TYPE_CHECKING:
    from pathlib import Path


def test_str(default_field):
    assert re.match(DATA_PROVIDER_STR_REGEX, str(default_field))


@pytest.fixture(scope="module", params=list(Locale))
def localized_field(request):
    return Field(request.param)


@pytest.fixture(scope="module")
def default_field(request):
    return Field()


@pytest.fixture(scope="module", params=list(Locale))
def localized_fieldset(request):
    return Fieldset(request.param)


@pytest.fixture(scope="module")
def default_fieldset(request):
    return Fieldset()


@pytest.fixture(scope="module")
def custom_fieldset(request):
    class MyFieldSet(Fieldset):
        fieldset_iterations_kwarg = "iterations"

    return MyFieldSet()


@pytest.fixture(scope="module", params=list(Locale))
def fieldset_with_default_i(request):
    return Fieldset(request.param, i=100)


@pytest.fixture
def schema(localized_field):
    return Schema(
        schema=lambda: {
            "id": localized_field("uuid"),
            "name": localized_field("word"),
            "timestamp": localized_field("timestamp"),
            "zip_code": localized_field("postal_code"),
            "owner": {
                "email": localized_field("email", key=str.lower),
                "creator": localized_field("full_name", gender=Gender.FEMALE),
            },
        },
        iterations=10,
    )


@pytest.mark.parametrize(
    "field_name",
    [
        "uuid",
        "full_name",
        "street_name",
    ],
)
def test_field(localized_field, field_name):
    assert localized_field(field_name)


@pytest.mark.parametrize(
    "field_name",
    [
        "text title",
        "person.title",
        "person/title",
        "person:title",
    ],
)
def test_field_different_separator(localized_field, field_name):
    assert isinstance(localized_field(field_name), str)


@pytest.mark.parametrize(
    "field_name, i",
    [
        ("bank", 8),
        ("address", 4),
        ("name", 2),
    ],
)
def test_fieldset(localized_fieldset, field_name, i):
    result = localized_fieldset(field_name, i=i)
    assert isinstance(result, list) and len(result) == i


def test_field_get_random_instance(localized_field):
    assert isinstance(localized_field.get_random_instance(), Random)
    assert localized_field.get_random_instance() == localized_field._generic.random


@pytest.mark.parametrize(
    "field_name",
    [
        "bank",
        "address",
        "full_name",
    ],
)
def test_fieldset_with_default_i(localized_fieldset, field_name):
    result = localized_fieldset(field_name)
    assert isinstance(result, list)
    assert len(result) == localized_fieldset.fieldset_default_iterations


def test_custom_fieldset(custom_fieldset):
    result = custom_fieldset("name", iterations=3)
    assert isinstance(result, list) and len(result) == 3

    with pytest.raises(TypeError):
        custom_fieldset("name", i=4)


def test_fieldset_with_common_i(fieldset_with_default_i):
    result = fieldset_with_default_i("name")
    assert isinstance(result, list) and len(result) == 100

    result = fieldset_with_default_i("name", i=3)
    assert isinstance(result, list) and len(result) == 3


def test_field_with_key_function(localized_field):
    result = localized_field("person.name", key=list)
    assert isinstance(result, list) and len(result) >= 1


def test_field_with_key_function_two_parameters(localized_field):
    def key_function(value, random):
        return f"{value}_{random.randint(1, 100)}"

    result = localized_field("person.name", key=key_function)
    name, number = result.split("_")
    assert isinstance(result, str)
    assert 1 <= int(number) <= 100


@pytest.mark.parametrize(
    "locale",
    (
        Locale.RU,
        Locale.UK,
        Locale.KK,
    ),
)
def test_field_with_romanize(locale):
    localized_field = Field(locale=locale)
    result = localized_field("name", key=romanize(locale))
    assert not all(unicodedata.category(char).startswith("C") for char in result)


@pytest.mark.parametrize(
    "locale",
    (
        Locale.RU,
        Locale.UK,
        Locale.KK,
    ),
)
def test_fieldset_with_romanize(locale):
    localized_fieldset = Fieldset(locale=locale, i=5)
    romanized_results = localized_fieldset("name", key=romanize(locale))
    for result in romanized_results:
        assert not all(unicodedata.category(char).startswith("C") for char in result)


def test_field_with_maybe(default_field):
    result = default_field("person.name", key=maybe("foo", probability=1))
    assert result == "foo"

    result = default_field("person.name", key=maybe("foo", probability=0))
    assert result != "foo"


def test_fieldset_error(default_fieldset):
    with pytest.raises(FieldsetError):
        default_fieldset("username", key=str.upper, i=0)


def test_fieldset_field_error(default_fieldset):
    with pytest.raises(FieldError):
        default_fieldset("unsupported_field")


@pytest.mark.parametrize(
    "field_name", ["person.full_name.invalid", "invalid_field", "unsupported_field"]
)
def test_field_error(localized_field, field_name):
    with pytest.raises(FieldError):
        localized_field(field_name)


def test_field_raises_field_error(default_field):
    with pytest.raises(FieldError):
        default_field("person.unsupported_field")

    with pytest.raises(FieldError):
        default_field("unsupported_field")

    with pytest.raises(FieldError):
        default_field()

    with pytest.raises(FieldError):
        default_field("person.full_name.invalid")


def test_explicit_lookup(localized_field):
    result = localized_field._explicit_lookup("person.surname")

    assert callable(result)
    assert isinstance(result(), str)


def test_fuzzy_lookup(localized_field):
    result = localized_field._fuzzy_lookup("surname")

    assert callable(result)
    assert isinstance(result(), str)


@pytest.mark.parametrize(
    "field_name",
    [
        "",
        "foo",
        "foo.bar",
        "person.surname.male",
    ],
)
def test_lookup_method_field_error(localized_field, field_name):
    with pytest.raises(FieldError):
        localized_field._lookup_method(field_name)

    with pytest.raises(ValueError):
        localized_field._explicit_lookup(field_name)

    with pytest.raises(FieldError):
        localized_field._fuzzy_lookup(field_name)


@pytest.mark.parametrize(
    "invalid_schema", [None, {"a": "uuid"}, [True, False], (1, 2, 3)]
)
def test_schema_instantiation_raises_schema_error(invalid_schema):
    with pytest.raises(SchemaError):
        Schema(schema=invalid_schema)  # type: ignore


def test_schema_instantiation_raises_value_error():
    with pytest.raises(ValueError):
        Schema(schema=lambda: {"uuid": Field()("uuid")}, iterations=0)


def test_choice_field(localized_field):
    result = localized_field("choice", items=["a", "b", "c", "d"], length=2)
    assert len(result) == 2


def test_schema_create(schema):
    result = schema.create()

    assert len(result) == schema.iterations
    assert isinstance(result, list)


def _assert_schema_iteration(schema, iterable):
    count = 0
    for item in iterable:
        assert isinstance(item, dict)
        count += 1

    assert isinstance(schema, Iterator)
    assert count == schema.iterations

    with pytest.raises(StopIteration):
        schema.iterations = 0
        next(schema)


def test_schema_iterator(schema):
    _assert_schema_iteration(schema, schema.iterator())


def test_schema_iterator_protocol(schema):
    _assert_schema_iteration(schema, schema)


def test_schema_to_csv(tmp_path: "Path", schema: Schema):
    file = tmp_path / "test.csv"
    schema.to_csv(str(file))

    dict_reader = csv.DictReader(file.read_text("UTF-8").splitlines())

    assert len(list(dict_reader)) == schema.iterations
    assert isinstance(dict_reader, csv.DictReader)

    for row in dict_reader:
        assert "id" in row and "timestamp" in row


def test_schema_to_json(tmp_path: "Path", schema: Schema):
    file = tmp_path / "test.json"
    schema.to_json(str(file), sort_keys=True, ensure_ascii=False)

    data = json.loads(file.read_text("UTF-8"))
    assert len(list(data)) == schema.iterations
    assert "id" in data[0] and "id" in data[-1]


def test_schema_to_pickle(tmp_path: "Path", schema: Schema):
    file = tmp_path / "test.pkl"
    schema.to_pickle(str(file))

    data = pickle.loads(file.read_bytes())
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
def test_field_reseed(localized_field, seed):
    localized_field.reseed(seed)
    result1 = localized_field("dsn")

    localized_field.reseed(seed)
    result2 = localized_field("dsn")

    assert result1 == result2


def my_field_handler(random, a="b", c="d", **kwargs):
    return random.choice([a, c])


class MyFieldHandler:
    def __call__(self, random, a="b", c="d", **kwargs):
        return random.choice([a, c])


@pytest.mark.parametrize(
    "field_name, handler",
    [
        ("wow", MyFieldHandler()),
        ("wow", my_field_handler),
        ("wow", lambda rnd, a="a", c="d", **kwargs: rnd.choice([a, c])),
    ],
)
def test_register_handler(default_field, default_fieldset, field_name, handler):
    default_field.register_handler(field_name, handler)
    default_fieldset.register_handler(field_name, handler)

    res_1 = default_field(field_name, key=str.upper)
    res_2 = default_field(field_name, key=str.lower, a="a", c="c", d="e")

    assert res_1.isupper() and res_2.islower()

    default_field.unregister_handler(field_name)

    with pytest.raises(FieldError):
        default_field(field_name)


def test_field_handle_decorator(default_field):
    @default_field.handle("my_field")
    def my_field(random, **kwargs):
        return random.choice(["a", "b"])

    assert default_field("my_field") in ["a", "b"]

    default_field.unregister_handler("my_field")

    with pytest.raises(FieldError):
        default_field("my_field")


def test_fieldset_handle_decorator(default_fieldset):
    @default_fieldset.handle()
    def my_field(random, **kwargs):
        return random.choice(["a", "b"])

    assert len(default_fieldset("my_field")) == 10

    default_fieldset.unregister_handler("my_field")

    with pytest.raises(FieldError):
        default_fieldset("my_field")


def test_register_handler_callable_with_wrong_arity(default_field):
    def wrong_arity(**kwargs):
        return "error"

    with pytest.raises(FieldArityError):
        default_field.register_handler("invalid_field", wrong_arity)


def test_register_handler_non_callable(default_field):
    with pytest.raises(TypeError):
        default_field.register_handler("a", "a")

    with pytest.raises(TypeError):
        default_field.register_handler(b"sd", my_field_handler)


@pytest.mark.parametrize(
    "invalid_field_name",
    [
        "a.b",
        "a b",
        "a-b",
        "a/b",
        "a\\b",
        "1a",
    ],
)
def test_register_handler_with_invalid_name(default_field, invalid_field_name):
    with pytest.raises(FieldNameError):
        default_field.register_handler(invalid_field_name, my_field_handler)


def test_register_handlers(default_field):
    _kwargs = {"a": "a", "b": "b"}
    default_field.register_handlers(
        fields=[
            ("a", lambda rnd, **kwargs: kwargs),
            ("b", lambda rnd, **kwargs: kwargs),
            ("c", lambda rnd, lol="lol", **kwargs: kwargs),
        ]
    )

    result = default_field("a", **_kwargs)
    assert result["a"] == _kwargs["a"] and result["b"] == _kwargs["b"]


def test_unregister_handler(default_field):
    # Make sure that there are no handlers.
    default_field.unregister_all_handlers()
    # Register fields first
    default_field.register_handler("my_field", my_field_handler)
    # Make sure that registration is done.
    assert len(default_field._handlers.keys()) > 0
    # Extract field handler by its name
    registered_field = default_field._handlers["my_field"]
    # Make sure that handlers are the same
    assert registered_field == my_field_handler
    # Unregister field
    default_field.unregister_handler("my_field")
    with pytest.raises(FieldError):
        default_field("my_field")


def test_unregister_handlers(default_field):
    default_field.unregister_all_handlers()
    fields = [
        ("a", lambda rnd, **kwargs: kwargs),
        ("b", lambda rnd, **kwargs: kwargs),
        ("c", lambda rnd, **kwargs: kwargs),
    ]

    # Register fields first
    default_field.register_handlers(fields=fields)
    assert len(default_field._handlers.keys()) == 3

    # Unregister all field with given names.
    default_field.unregister_handlers(["a", "b", "c", "d", "e"])
    assert len(default_field._handlers.keys()) == 0

    # Register fields again and unregister all of them at once
    default_field.register_handlers(fields=fields)
    default_field.unregister_all_handlers()
    assert len(default_field._handlers.keys()) == 0


def test_unregister_all_handlers(default_field):
    fields = [
        ("a", lambda rnd, **kwargs: kwargs),
        ("b", lambda rnd, **kwargs: kwargs),
        ("c", lambda rnd, **kwargs: kwargs),
    ]

    # Register fields first
    default_field.register_handlers(fields=fields)
    assert len(default_field._handlers.keys()) == 3

    # Unregister all fields
    default_field.unregister_all_handlers()
    assert len(default_field._handlers.keys()) == 0


def test_field_aliasing(default_field):
    default_field.aliases = {
        "🇺🇸": "country_code",
    }
    assert default_field("🇺🇸")

    with pytest.raises(FieldError):
        default_field.aliases.clear()
        default_field("🇺🇸")


@pytest.mark.parametrize(
    "aliases",
    [
        {"🇺🇸": tuple},
        {"hey": 22},
        {12: "email"},
        {b"hey": "email"},
        None,
        [],
        tuple(),
    ],
)
def test_field_invalid_aliases(default_field, aliases):
    default_field.aliases = aliases
    with pytest.raises(AliasesTypeError):
        default_field("email")

    default_field.aliases = aliases

    with pytest.raises(AliasesTypeError):
        default_field._validate_aliases()


def test_schema_map():
    field = Field(Locale.EN, seed=0xFF)

    data = (
        Schema(
            lambda: {"value": field("integer_number", start=1, end=10)}, iterations=3
        )
        .map(lambda item: {**item, "doubled": item["value"] * 2})
        .create()
    )

    assert len(data) == 3
    for item in data:
        assert "value" in item
        assert "doubled" in item
        assert item["doubled"] == item["value"] * 2


def test_schema_map_with_context():
    field = Field(Locale.EN, seed=0xFF)

    data = (
        Schema(lambda: {"name": field("name")}, iterations=3)
        .map(lambda item, ctx: {**item, "index": ctx.index, "iteration": ctx.iteration})
        .create()
    )

    assert len(data) == 3
    for i, item in enumerate(data):
        assert item["index"] == i
        assert item["iteration"] == i + 1


def test_schema_chaining():
    field = Field(Locale.EN, seed=0xFF)

    data = (
        Schema(
            lambda: {"value": field("integer_number", start=1, end=20)}, iterations=3
        )
        .map(lambda item: {**item, "doubled": item["value"] * 2})
        .create()
    )

    assert len(data) == 3


def test_schema_with_context():
    field = Field(Locale.EN, seed=0xFF)

    data = (
        Schema(lambda: {"name": field("name")}, iterations=2)
        .with_context(company="Acme Inc", version="v2")
        .map(lambda item, ctx: {**item, "company": ctx.custom["company"]})
        .create()
    )

    assert len(data) == 2
    for item in data:
        assert item["company"] == "Acme Inc"


def test_relational_schema():
    field = Field(Locale.EN, seed=0xFF)
    builder = SchemaBuilder(seed=field.seed)
    builder.define(
        "users",
        Schema(
            lambda: {
                "id": field("increment"),
                "name": field("name"),
            }
        ),
    )
    builder.define(
        "posts",
        Schema(
            lambda: {
                "id": field("increment"),
                "title": field("sentence"),
            }
        ).map(
            lambda item, ctx: {
                **item,
                "user_id": ctx.pick_from("users", "id"),
            }
        ),
    )

    data = builder.create(users=3, posts=5)

    assert len(data["users"]) == 3
    assert len(data["posts"]) == 5

    for post in data["posts"]:
        assert "user_id" in post
        assert post["user_id"] in [u["id"] for u in data["users"]]


def test_schema_context():
    ctx = SchemaContext(index=5, seed=0xFF, custom={"test": "value"})

    assert ctx.index == 5
    assert ctx.iteration == 6
    assert ctx.custom["test"] == "value"
