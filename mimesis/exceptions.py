"""Custom exceptions which used in Mimesis."""

import typing as t

from mimesis.enums import Locale


class LocaleError(ValueError):
    """Raised when a locale isn't supported."""

    def __init__(self, locale: t.Union[Locale, str]) -> None:
        """Initialize attributes for informative output.

        :param locale: Locale.
        """
        self.locale = locale

    def __str__(self) -> str:
        return f"Invalid locale «{self.locale}»"


class SchemaError(ValueError):
    """Raised when schema is unsupported."""

    def __str__(self) -> str:
        return "Schema should a callable object."


class NonEnumerableError(TypeError):
    """Raised when object is not instance of Enum."""

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
    def __init__(self, name: t.Optional[str] = None) -> None:
        """Initialize attributes for more informative output.

        :param name: Name of the field..
        """
        self.name = name
        self.message = "A field «{}» is not supported."
        self.message_none = "Field cannot be None."

    def __str__(self) -> str:
        if self.name is None:
            return self.message_none
        return self.message.format(self.name)
