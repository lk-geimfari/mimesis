"""Custom exceptions used by Mimesis."""

import typing as t

from mimesis.enums import Locale


class LocaleError(ValueError):
    """Raised when a locale isn't supported."""

    def __init__(self, locale: Locale | str) -> None:
        """Initialize attributes for informative output.

        :param locale: Locale.
        """
        self.locale = locale

    def __str__(self) -> str:
        return f"Invalid locale «{self.locale}»"


class SchemaError(ValueError):
    """Raised when a schema is invalid."""

    def __str__(self) -> str:
        return (
            "The schema must be a callable object that returns a dict. "
            "See https://mimesis.name/en/master/schema.html for more details."
        )


class NonEnumerableError(TypeError):
    """Raised when an object is not a member of the expected Enum."""

    def __init__(self, enum_obj: t.Any) -> None:
        """Initialize attributes for informative output.

        :param enum_obj: Enum object.
        """
        if enum_obj:
            self.name = enum_obj
            self.items = ", ".join(map(str, enum_obj))
        else:
            self.name = None
            self.items = ""

    def __str__(self) -> str:
        if not self.name:
            return "Expected a member of an Enum."
        return (
            f"Argument must be a member of mimesis.enums.{self.name.__name__}: "
            f"«{self.items}»"
        )


class FieldError(ValueError):
    """Raised when a field is missing or invalid."""

    def __init__(self, name: str | None = None) -> None:
        """Initialize attributes for more informative output.

        :param name: Name of the field.
        """
        self.name = name

    def __str__(self) -> str:
        if self.name is None:
            return "A field name is required."
        return f"Field «{self.name}» is not supported."


class FieldsetError(ValueError):
    """Raised when the fieldset iteration count is invalid."""

    def __str__(self) -> str:
        return "The «i» parameter must be at least 1."


class FieldNameError(ValueError):
    """Raised when a field name is invalid."""

    def __init__(self, name: str | None = None) -> None:
        """Initialize attributes for more informative output.

        :param name: Name of the field.
        """
        self.name = name

    def __str__(self) -> str:
        return f"The field name «{self.name}» is not a valid Python identifier."


class FieldArityError(ValueError):
    """Raised when a registered field handler has incompatible arity."""

    def __str__(self) -> str:
        return (
            "The custom handler must accept at least two arguments: "
            "'random' and '**kwargs'"
        )


class AliasesTypeError(TypeError):
    """Raised when aliases is not a flat dictionary."""

    def __str__(self) -> str:
        return (
            "The 'aliases' attribute must be a non-nested dictionary where "
            "keys are aliases and values are the corresponding field names."
        )
