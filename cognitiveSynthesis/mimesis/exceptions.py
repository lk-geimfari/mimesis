"""Custom exceptions which are used in Mimesis."""

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
    """Raised when a schema is unsupported."""

    def __str__(self) -> str:
        return (
            "The schema must be a callable object that returns a dict."
            "See https://mimesis.name/en/master/schema.html for more details."
        )


class NonEnumerableError(TypeError):
    """Raised when an object is not an instance of Enum."""

    message = "You should use one item of: «{}» of the object mimesis.enums.{}"

    def __init__(self, enum_obj: t.Any) -> None:
        """Initialize attributes for informative output.

        :param enum_obj: Enum object.
        """
        if enum_obj:
            self.name = enum_obj
            self.items = ", ".join(map(str, enum_obj))
        else:
            self.items = ""

    def __str__(self) -> str:
        return self.message.format(self.items, self.name.__name__)


class FieldError(ValueError):
    """Raised when field is not found."""

    def __init__(self, name: str | None = None) -> None:
        """Initialize attributes for more informative output.

        :param name: Name of the field.
        """
        self.name = name
        self.message = "Field «{}» is not supported."
        self.message_none = "The field cannot have the value None."

    def __str__(self) -> str:
        if self.name is None:
            return self.message_none
        return self.message.format(self.name)


class FieldsetError(ValueError):
    """Raised when a resulting fieldset is empty."""

    def __str__(self) -> str:
        return "The «iterations» parameter should be greater than 1."


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
    """Raised when registering field handler has incompatible arity."""

    def __str__(self) -> str:
        return "The custom handler must accept at least two arguments: 'random' and '**kwargs'"


class AliasesTypeError(TypeError):
    """Raised when the aliases attribute is set to a format other than a flat dictionary."""

    def __str__(self) -> str:
        return (
            "The 'aliases' attribute needs to be a non-nested dictionary where "
            "keys are the aliases and values are the corresponding field names."
        )
