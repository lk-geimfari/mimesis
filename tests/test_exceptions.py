"""Tests for exception message formatting."""

from mimesis.enums import Gender
from mimesis.exceptions import (
    AliasesTypeError,
    FieldArityError,
    FieldError,
    FieldNameError,
    FieldsetError,
    LocaleError,
    NonEnumerableError,
    SchemaError,
)


def test_locale_error_str():
    assert "en" in str(LocaleError("en"))


def test_schema_error_str():
    assert "callable" in str(SchemaError())


def test_non_enumerable_error_str():
    assert "Expected a member" in str(NonEnumerableError(None))
    assert "Gender" in str(NonEnumerableError(Gender))


def test_field_error_str():
    assert "required" in str(FieldError())
    assert "email" in str(FieldError("email"))


def test_fieldset_error_str():
    assert "«i»" in str(FieldsetError())


def test_field_name_error_str():
    assert "bad-name" in str(FieldNameError("bad-name"))


def test_field_arity_error_str():
    assert "random" in str(FieldArityError())


def test_aliases_type_error_str():
    assert "aliases" in str(AliasesTypeError())
